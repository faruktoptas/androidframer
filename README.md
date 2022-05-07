# android-framer ![Python Build Action](https://github.com/faruktoptas/androidframer/workflows/Python%20Build/badge.svg)

Add frames and titles to your Google Play screenshots. Inspired by [fastlane frameit](https://docs.fastlane.tools/actions/frameit/)


![framer](https://user-images.githubusercontent.com/1595227/87590805-141b3700-c6f0-11ea-945d-dc0ea79167a1.jpg)

## Prerequsities
* Python 3.6
* [ImageMagick](https://imagemagick.org/)

## Install
```pip3 install androidframer==0.1```

```python
from androidframer import Framer

Framer("resources/framer.json", "resources/strings.json", "resources/images").start()
```
or clone this repo and then run the script below:

`python3 sample.py`

## Configure
### Edit framer.json file

* background: Background frame. More frames can be found on [Facebook Design](https://facebook.design/devices).
* font: Title font
* fontsize: Title font size
* resize: Resize ratio of the source image
* xposition: X position of source image to background image
* yposition: Y position of source image to background image 
* data: Title keys ("1" for 1.png) Currently supports 1 or 2 lines
* output: Directory to place output files
```json
{
  "background": "resources/background.png",
  "data": {
    "1": [
      "title1_1",
      "title1_2"
    ],
    "2": [
      "title2_1"
    ]
  },
  "font": "resources/font.ttf",
  "fontsize":"108",
  "xposition":156,
  "yposition":780,
  "resize":100,
  "output": "resources/output"
}
```
### Edit strings.json file
For each language set strings for title keys specified in framer.json
```json
{
  "en-US": {
    "title1_1": "Follow popular news",
    "title1_2": "feeds",
    "title2_1": "News summary"
  },
  "tr-TR": {
    "title1_1": "Popüler haber sitelerini",
    "title1_2": "takip edin",
    "title2_1": "Haber özeti"
  }
}
```
### ImageMagick commands
```bash
magick input.png -resize 50% out.png
magick composite -compose atop -geometry +x+y 1.png 2.png out.png
magick input.png -gravity North -font font.ttf -fill white -pointsize 150 -draw 'text 0,100 "some text"' out.png
```