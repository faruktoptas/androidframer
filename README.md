# android-framer (Still being developed)
Add frames and titles to your Google Play screenshots. 


### From
![2](https://user-images.githubusercontent.com/1595227/62410434-f099d200-b5ed-11e9-8cbb-e7be21d50266.png)
### To
![2_out](https://user-images.githubusercontent.com/1595227/62410433-f099d200-b5ed-11e9-8955-06c841757fe6.png)

## Prerequsities
* [ImageMagick](https://imagemagick.org/)

## Usage
### Edit framer.json file

* background: Background frame
* font: Title font
* data: title keys ("1" for 1.png)
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
  "font": "font.ttf"
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
+-- framer.json
+-- strings.json
+-- font.ttf
+-- images
|   +-- en-US
|       +-- 1.png
|       +-- 2.png
|   +-- tr-TR
|       +-- 1.png
|       +-- 2.png
```

## Running
`python framer.py`
