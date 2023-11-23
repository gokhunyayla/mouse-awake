from setuptools import setup

APP = ['app.py']
DATA_FILES = ['cursor.png']
OPTIONS = {
    'iconfile': 'cursor.icns',
    'plist': {
        'CFBundleShortVersionString': '1.0.0',
        'LSUIElement': True,
    },
    'packages': ['rumps'],
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)