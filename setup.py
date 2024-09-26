from setuptools import setup, find_packages

from firebase_browserstack import __version__

setup(
    name='firebase_browserstack',
    version=__version__,
    author='ahmadachmed',
    author_email='ahmadilham000@gmail.com',
    description='Firebase app distribution integrated with Browserstack',
    packages= find_packages(),
    install_requires=[
        'google-api-python-client',
        'requests'
    ]
)