import base64
import json
import os
from google.oauth2 import service_account
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/cloud-platform']

SERVICE_ACCOUNT = "sa.json"

BS_USERNAME = os.getenv("BS_USERNAME")
BS_PASSWORD = os.getenv("BS_PASSWORD")

def get_firebase_apk_url(app_id, firebase_project_number):
    sa = os.getenv('FIREBASE_SERVICE_ACCOUNT')
    sa = base64.b64decode(sa).decode("utf-8")
    sa = json.loads(sa)
    with open(SERVICE_ACCOUNT, 'w') as json_file:
        json.dump(sa, json_file)

    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT, scopes=SCOPES
    )
    
    service = build('firebaseappdistribution', 'v1', credentials=credentials)

    request = service.projects().apps().releases().list(parent=f'projects/{firebase_project_number}/apps/{app_id}')
    response = request.execute()

    # Mendapatkan URL APK dari branch yang diambil
    branch = os.getenv('BRANCH_APK', 'master')
    download_url = None
    for release in response.get('releases', []):
        if 'releaseNotes' in release and branch in release['releaseNotes']['text']:
            download_url = release['binaryDownloadUri']
            break

    if download_url:
        os.remove(SERVICE_ACCOUNT)
        print(f"{download_url},")
        return download_url
    else:
        print(f"No APK found in Firebase for branch: {branch},")