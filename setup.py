import setuptools

setuptools.setup(
    name='firebase_browserstack',
    version='0.0.1',
    author='ahmadachmed',
    author_email='ahmadilham000@gmail.com',
    description='Firebase app distribution integrated with Browserstack',
    packages= ['firebase_browserstack'],
    install_requires=[
        'google-api-python-client',
        'requests'
    ]
)