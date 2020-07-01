# android-framer
Add frames and titles to your Google Play screenshots. Inspired by [fastlane frameit](https://docs.fastlane.tools/actions/frameit/)


![framer](https://user-images.githubusercontent.com/1595227/62423493-ac7bff80-b6c9-11e9-83ff-dc921afc3c47.png)

## Prerequsities
* Python 3.6
* [ImageMagick](https://imagemagick.org/)

## Usage
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
  "background": "background.png",
  "data": {
    "1": [
      "title1_1",
      "title1_2"
    ],
    "2": [
      "title2_1"
    ]
  },
  "font": "font.ttf",
  "fontsize":"108",
  "xposition":156,
  "yposition":780,
  "resize":100,
  "output": "output"
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

## Folder Structure
```
.
├── font.ttf
├── framer.json
├── strings.json
├── images
│   ├── en-US
│   │   ├── 1.png
│   │   └── 2.png
│   └── tr-TR
│       ├── 1.png
│       └── 2.png
└── output
    ├── en-US
    │   ├── 1_out.png
    │   └── 2_out.png
    └── tr-TR
        ├── 1_out.png
        └── 2_out.png
```

## Running
`python3 framer.py`
