# coding=utf-8

import json,os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

labelsFile = "framer.json"
stringsFile = "strings.json"
folder = "images"

labels = json.loads(open(labelsFile).read())
titles = json.loads(open(stringsFile).read())
bg = labels["background"]
font = labels["font"]
data = labels["data"]


def cmd(command):
	return os.popen(command).read()

def __main__():
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
				resized = resize(imgFolder, file, ext)
				framed = frame(imgFolder, resized, ext)
				if (data.has_key(file)):
					titleKeys = data[file]
					title1 = ""
					title2 = ""
					if (titles.has_key(lang)):
						if (len(titleKeys) > 0 and titles[lang].has_key(titleKeys[0])):
							title1 = titles[lang][titleKeys[0]]
						if (len(titleKeys) > 1 and titles[lang].has_key(titleKeys[1])):
							title2 = titles[lang][titleKeys[1]]
						label(framed, title1, title2)

def resize(imgFolder, file, ext):
	ratio = 74.4
	img = imgFolder + file  + ext
	out = imgFolder + file + '_' + ext
	cmd('convert ' + img + ' -resize %' + str(ratio) + ' ' + out)
	return file + "_"

def frame(imgFolder, file, ext):
	img = imgFolder + file + ext
	out = imgFolder + file + 'framed' + ext
	cmd('convert ' + bg +' ' + img +' -geometry +243+583 -composite ' + out)
	return out

def label(img, title1, title2):
	out = img.replace('_framed', '_out')
	command = "convert " + img +" -font " + font + " -gravity North -fill white -pointsize 108 -draw \"text 0,100 '" + title1 +"'\"  -draw \"text 0,220 '" + title2 + "'\" " + out
	cmd(command)
	cmd("rm " + img)
	cmd("rm " + img.replace("_framed", "_"))

__main__()
