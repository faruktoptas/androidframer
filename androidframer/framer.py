#!/usr/bin/env python3
# coding: utf-8
import os
import json
import logging
import time

class Framer:
	#Logging functionality
	if not os.path.isdir("./logs"):
		os.mkdir("./logs")
	logging.basicConfig(filename="./logs/log.txt",level=logging.INFO)

	def __init__(self, config, strings, images):
		#Supplies folders and files
		self.configFile = config
		self.stringsFile = strings
		self.folder = images
		#Read
		self.config = json.loads(open(self.configFile).read())
		self.titles = json.loads(open(self.stringsFile, encoding='utf-8').read())
		#Config file
		self.bg = self.config["background"]
		self.font = self.config["font"]
		self.data = self.config["data"]
		self.resizeRatio = self.config["resize"]
		self.fontSize = self.config["fontsize"]
		self.xPos = str(self.config["xposition"])
		self.yPos = str(self.config["yposition"])
		self.output = self.config["output"]

	def start(self):
		'''Runs main Framer program'''
		#Logging
		start_time = time.time()
		logging.info("Starting androidframer at {0}".format(time.asctime()))
		folder = self.folder
		output = self.output
		try:
		    os.listdir(output)
		except FileNotFoundError:
		    os.mkdir(output)
		    logging.warning("{0} not found, so has been created.".format(output))
		files = os.listdir(folder)
		langFolders = []
		for f in files:
			if os.path.isdir(os.path.join(folder, f)):
				langFolders.append(f)

		for lang in langFolders:
			outFolder = os.path.join(output, lang)
			imgFolder = os.path.join(folder, lang)
			try:
			    os.listdir(outFolder)
			except FileNotFoundError:
				os.mkdir(outFolder)
				logging.debug("Created folder {0}".format(outFolder))
			for f in os.listdir(os.path.join(folder, lang)):
				img = os.path.join(imgFolder, f)
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
							tempOut = self.label(framed, title1, title2)
							out = tempOut.replace(imgFolder, outFolder)
							os.rename(tempOut, out)
		logging.info("Finished running in {}s".format(round(time.time()-start_time,2)))

	def cmd(self, command):
		'''Opens pipe and reads command from system'''
		return os.popen(command).read()

	def resize(self, imgFolder, file, ext):
		"""
		Resize image.

		Takes file in imgFolder and resizes it.

		Parameters
		----------
		imgFolder : string
			Address of folder with image
		file : string
			Name of image file
		ext : string
			Extension of image file

		Returns
		-------
		string
			file with an appended underscore
		"""
		img = os.path.join(imgFolder, (file + ext))
		out = os.path.join(imgFolder, (file + '_' + ext))
		command = f"magick {img} -resize {str(100)}% {out}"
		self.cmd(command)
		return file + "_"

	def frame(self, imgFolder, file, ext):
		'''Put the file.ext in a frame'''
		img = os.path.join(imgFolder, (file + ext))
		out = os.path.join(imgFolder, (file + 'framed' + ext))
		command = f"magick composite -compose atop -geometry +{self.xPos}+{self.yPos} {img} {self.bg} {out}"
		self.cmd(command)
		return out

	def label(self, img, title1, title2):
		'''Label img with title1 and title2'''
		out = img.replace('_framed', '_out')
		command = f"magick {img} -font {self.font} -gravity North -fill white -pointsize {self.fontSize} -draw \"text 0,190 '{title1}'\" -draw \"text 0,220 '{title2}'\" {out}"
		self.cmd(command)
		try:
			os.remove(img)
		except:
			print("")
		try:
			os.remove(img.replace('_framed', '_'))
		except:
			print("")
		return out