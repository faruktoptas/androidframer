#!/usr/local/bin/python
# coding: utf-8
import os
import json
from pathlib import Path # for easier multiplatform file pathing

class Framer:
	configFile = "framer.json"
	stringsFile = "strings.json"
	folder = "images"

	def __init__(self):
		self.config = json.loads(open(self.configFile).read())
		self.titles = json.loads(open(self.stringsFile).read())
		self.bg = self.config["background"]
		self.font = self.config["font"]
		self.data = self.config["data"]
		self.resizeRatio = self.config["resize"]
		self.fontSize = self.config["fontsize"]
		self.xPos = str(self.config["xposition"])
		self.yPos = str(self.config["yposition"])

	def start(self):
		folder = self.folder
		files = os.listdir(folder)
		langFolders = []
		for f in files:
			if(os.path.isdir(f"{folder}/{f}")):
				langFolders.append(f)

		for lang in langFolders:
			imgFolder = Path(f"{folder}/{lang}/") # support multiple os file paths, moved outside of nested for loop
			for f in os.listdir(f"{folder}/{lang}"):
								
				img = imgFolder / f
				file = f[:f.rfind(".")]
				ext = f[f.rfind("."):]
				if (len(file) > 0 and file.isnumeric()):
					resized = self.resize(imgFolder, file, ext)
					framed = self.frame(imgFolder, resized, ext)
					if (file in self.data.keys()):
						titleKeys = self.data[file]
						title1 = ""
						title2 = ""
						if (lang in self.titles.keys()):
							if (len(titleKeys) > 0
							and titleKeys[0] in self.titles[lang].keys()):
								title1 = self.titles[lang][titleKeys[0]]
							if (len(titleKeys) > 1
							and titleKeys[1] in self.titles[lang].keys()):
								title2 = self.titles[lang][titleKeys[1]]
							self.label(framed, title1, title2)



	def cmd(self, command):
		return os.popen(command).read()

	def resize(self, imgFolder, file, ext):
		img = imgFolder / (file + ext)
		out = imgFolder / (file + '_' + ext)
		command = f"convert {img} -resize %{str(self.resizeRatio)} {out}"
		#command = f"magick {img} -resize {str(self.resizeRatio)}% {out}" # 'convert' is a legacy util, replaced in ImageMagick 7 with 'magick'
		self.cmd(command)
		return file + "_"

	def frame(self, imgFolder, file, ext):
		img = imgFolder / (file + ext)
		out = imgFolder / (file + 'framed' + ext)
		command = f"convert {self.bg} {img} -geometry +{self.xPos}+{self.yPos} -composite {out}"
		#command = f"magick {self.bg} {img} -geometry +{self.xPos}+{self.yPos} -composite {out}"
		self.cmd(command)
		return out

	def label(self, img, title1, title2):
		out = Path(str(img).replace('_framed', '_out'))
		command = f"convert {img} -font {self.font} -gravity North -fill white -pointsize {self.fontSize} -draw \"text 0,100 '{title1}'\" -draw \"text 0,220 '{title2}'\" {out}"
		#command = f"magick {img} -font {self.font} -gravity North -fill white -pointsize {self.fontSize} -draw \"text 0,100 '{title1}'\" -draw \"text 0,220 '{title2}'\" {out}"
		self.cmd(command)
		os.remove(img)
		os.remove(Path(str(img).replace('_framed', '_')))

if __name__== '__main__':
	Framer().start()
