# adb-thermal-monitor
non rooted google pixel and other android devices thermal zones temperature monitor.
adb shellを使用した非rootのGoogle Pixel向けのサーマルゾーンの温度を表示する簡易モニター

## How to use
使い方
```sh
python3 dumptz.py
```
Updates every 2 seconds.
2秒間隔で更新されます
## 概要
```sh
adb shell dumpsys thermalservice
```
を実行した際に出力される結果から"Current temperatures from HAL:"のサーマルゾーン名とその温度を見やすく出力しています

Android 13のPixel 7とPixel 4でSoC内の温度が表示されることを確認しております
