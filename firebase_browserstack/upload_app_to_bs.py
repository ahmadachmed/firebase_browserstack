import os
import sys
import requests
from firebase_browserstack.get_apk_url import get_firebase_apk_url


UPLOAD_URL = "https://api-cloud.browserstack.com/app-automate/upload"
USERNAME = os.getenv("BS_USERNAME")
PASSWORD = os.getenv("BS_PASSWORD")

def uploadApp_firebase(firebase_project_number, android_uat_app_id, android_dev_app_id, ios_uat_app_id, ios_dev_app_id):
    env = os.getenv('ENV').upper()
    device = os.getenv('DEVICE').upper()

    if device == 'IOS' and env == 'DEV':
        app_id = ios_dev_app_id
    elif device == 'IOS' and env == 'UAT':
        app_id = ios_uat_app_id
    elif device == 'ANDROID' and env == 'DEV':
        app_id = android_dev_app_id
    elif device == 'ANDROID' and env == 'UAT':
        app_id = android_uat_app_id

    firebase_apk_url = get_firebase_apk_url(app_id, firebase_project_number)
    if firebase_apk_url:
        url = UPLOAD_URL
        if  device == 'IOS':
            payload = {'ios_keychain_support': 'true', 'url': firebase_apk_url}
        else:
            payload = {'url': firebase_apk_url}
        try:
            resp = requests.post(url, auth=(USERNAME,PASSWORD), data=payload)
            if resp.status_code == 200:
                bs_app_id = resp.json()["app_url"]
                return bs_app_id
            else:
                print("Error:", resp.json())
                return None

        except Exception as e:
            print("Error occurred:", e)
            return None
    else:
        print("Failed to get APK URL")
        return None

if __name__ == "__main__":
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        print(uploadApp_firebase(arg))