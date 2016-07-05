#!/usr/bin/env python
def get_desired_capabilities():
  desired_caps = {
    "platformName": "Android",
    "platformVersion": "5.0",
    "deviceName": "MQC",
    "udid": "APU0215C05005731",
    "appPackage": "com.cheyaoshi.merchant",
    "appWaitPackage": "com.cheyaoshi.merchant",
    "app": "/Users/pzk/test/a0009999_carkey_1.2.1.apk",
    "newCommandTimeout": 30,
    "automationName": "Appium",
    "unicodeKeyboard": True,
    "resetKeyBoard": True
  }

  return desired_caps

def get_uri():
  return "http://localhost:4723/wd/hub"
