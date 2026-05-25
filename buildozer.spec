[app]
# (str) Title of your application
title = Tasky App

# (str) Package name
package.name = taskyapp

# (str) Package domain (needed for android packaging)
package.domain = org.MauroGRF

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning (method 1)
version = 0.1

# (list) Application requirements
# CAUTION: If you use KivyMD, add it here like: python3,kivy,kivymd
requirements = python3,kivy

# (str) Supported platforms (android is the default)
target = android

# (int) Android API to use
android.api = 33

# (int) Minimum API required
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (bool) Use private storage for data
android.private_storage = True

# (str) Format used for packaging (apk or aab)
android.archs = armeabi-v7a, arm64-v8a

[buildozer]
# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
