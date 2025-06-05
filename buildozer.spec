[app]
# Name of your application
title = Krdoku
# Jméno aplikace

# Package name (must be lowercase, no spaces, no special characters)
package.name = krdoku
 # Jméno package pro android (funguje to jak linux aplikace jsou jednotlivé packages)

# Your domain (reverse domain style, e.g., com.example)
package.domain = org.test
 # Doména aplikace pro moje účely tam je defaultní

# Directory containing your application code
source.dir = .
# Kde je main.py

# File extensions to include in the APK
source.include_exts = py,png,jpg,tflite,mp3,kv,atlas,txt,dm
 # Jaké všechny soubory tam můžou být

# Python modules your app depends on
requirements = python3,kivy==2.3.1,numpy,pillow,opencv_extras,opencv,filetype,android,jnius,plyer
 # Všechny knihovny a jejich verze

# Application version
version = 1.0
 # Verze aplikace

# Screen orientation
orientation = portrait
# Orientace aplikace 

# Make the app fullscreen
fullscreen = 0s
 # Bool na to jestli se má aplikace fullscreenovat

# Permissions (add more if needed)
android.permissions = CAMERA, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE
# Jaké všechny oprávnění aplikace k systému má

# App icon and splash screen
icon.filename = %(source.dir)s/icon.png
presplash.filename = %(source.dir)s/splash.png
 # Kde je ikonka a loading screen

# Scale the splash screen
android.presplash_scale = 1
# Scaling loading screenu

p4a.bootstrap = sdl2
# Front end bootstrap 

android.ndk_api = 26
 # Verze androidu pro které je podpora
android.minapi = 26
android.api = 31



android.add_libs_arm64_v8a = %(source.dir)s/sdk/native/libs/arm64-v8a/libopencv_java4.so
 # Knihovny, které jsou stažené ze souborů
android.add_libs_armeabi_v7a = %(source.dir)s/sdk/native/libs/armeabi-v7a/libopencv_java4.so

android.repositories = 
    "mavenCentral()"
    "google()"


android.gradle_dependencies = org.tensorflow:tensorflow-lite:2.15.0, org.tensorflow:tensorflow-lite-support:0.2.0
 # Knihovny z jiných sources



[buildozer]
# Logging level
log_level = 2
 # úroveň logování při buildu

# Target Android API level
android.api = 31
 



# Packaging format (APK nebo AAB)
android.packaging_format = apk

# Additional Android architecture targets
 
android.archs = arm64-v8a, armeabi-v7a # podporované architektury procesoru
