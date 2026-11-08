[app]

title = Hello Android
package.name = helloapp
package.domain = org.example

source.dir = .
source.include_exts = py,kv,png,jpg,atlas
version = 0.1

requirements = python3,kivy
orientation = portrait
fullscreen = 0

android.api = 35
android.minapi = 24
android.build_tools_version = 35.0.0
android.accept_sdk_license = True

p4a.branch = v2024.01.21

[buildozer]
log_level = 2
warn_on_root = 1
