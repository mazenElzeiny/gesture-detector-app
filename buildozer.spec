[app]
title = Gesture Detector
package.name = gesturedetector
package.domain = org.mazen
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy==2.2.1,pyjnius
orientation = portrait
fullscreen = 0
android.permissions = BLUETOOTH,BLUETOOTH_ADMIN,BLUETOOTH_CONNECT,BLUETOOTH_SCAN,ACCESS_FINE_LOCATION
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
