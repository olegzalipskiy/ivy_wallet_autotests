# Open source pet-project
### ***Before starting work with this framework make sure that you have python > 3.8 version and pip installed.***

## **Dependencies**

<ol>
<li>Docker</li>
<li>Appium</li>
<li>Android studio</li>
<li>Repo with testing app - https://github.com/Ivy-Apps/ivy-wallet</li>>
</ol>
To install all packages run the following command from the project folder:

```
pip3 install -r requirements.txt
```


## **Launching**

For launch all tests you should execute command
```pytest``` in terminal in the root of the project

For debug, you should to create `.env` file in folder ``resourcers`` with relative info:

```
APP={ABSOLUTE_PATH_TO_APK_FILE}
ENVIRONMENT_URL="http://0.0.0.0:4723"
AUTOMATION_NAME=UIAutomator2
OS_NAME=Android
PLATFORM_VERSION={ANDROID_VERSION}
DEVICE_NAME={ANDROID_DEVICE_NAME}
PLATFORM_NAME=Android
BASE_URL=""
LOCAL=True
```

After this you should manually launch Appium and Android Emulator.
