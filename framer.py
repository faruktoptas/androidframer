# coding=utf-8

import json,os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

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
			if(os.path.isdir(folder + "/" + f)):
				langFolders.append(f)

		for lang in langFolders:
			for f in os.listdir(folder + "/" + lang ):
				imgFolder = folder + "/" + lang + "/"
				img = imgFolder + f
				file = f[:f.rfind(".")]
				ext = f[f.rfind("."):]
				if (len(file) > 0 and unicode(file).isnumeric()):
					resized = self.resize(imgFolder, file, ext)
					framed = self.frame(imgFolder, resized, ext)
					if (self.data.has_key(file)):
						titleKeys = self.data[file]
						title1 = ""
						title2 = ""
						if (self.titles.has_key(lang)):
							if (len(titleKeys) > 0 and self.titles[lang].has_key(titleKeys[0])):
								title1 = self.titles[lang][titleKeys[0]]
							if (len(titleKeys) > 1 and self.titles[lang].has_key(titleKeys[1])):
								title2 = self.titles[lang][titleKeys[1]]
							self.label(framed, title1, title2)
	


	def cmd(self, command):
		return os.popen(command).read()

	def resize(self, imgFolder, file, ext):
		img = imgFolder + file  + ext
		out = imgFolder + file + '_' + ext
		self.cmd('convert ' + img + ' -resize %' + str(self.resizeRatio) + ' ' + out)
		return file + "_"

	def frame(self, imgFolder, file, ext):
		img = imgFolder + file + ext
		out = imgFolder + file + 'framed' + ext
		self.cmd('convert ' + self.bg +' ' + img +' -geometry +' + self.xPos + '+' + self.yPos +' -composite ' + out)
		return out

	def label(self, img, title1, title2):
		out = img.replace('_framed', '_out')
		command = "convert " + img +" -font " + self.font + " -gravity North -fill white -pointsize " + self.fontSize + " -draw \"text 0,100 '" + title1 +"'\"  -draw \"text 0,220 '" + title2 + "'\" " + out
		self.cmd(command)
		self.cmd("rm " + img)
		self.cmd("rm " + img.replace("_framed", "_"))

Framer().start()
