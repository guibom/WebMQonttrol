# Copyright (c) 2014, Guilherme Ramos <longinus@gmail.com>
# https://github.com/guibom/WebMQonttrol
# Released under the MIT license. See LICENSE file for details.
import eg

eg.RegisterPlugin(
	name = "EGMQonttrol",
	author = "Guilherme Ramos",
	version = "0.0.1",
	kind = "other",
	canMultiLoad = False,
	url = "https://github.com/guibom/WebMQonttrol",
	description = "Plugin used to interface with WebMQonttrol webpage."
)

import json
from os import walk
from os.path import splitext, join
from threading import Event, Thread

class EGMQonttrol(eg.PluginBase):

	def __init__(self):
		self.started = False;
		self.AddAction(SendFileList)

	def __start__(self):
		self.started = True;

	def __stop__(self):		
		self.started = False;

class SendFileList(eg.ActionBase):
	name = "Get File List"
	description = "Get JSON list of files from path"

	def __call__(self):
		try:
			path = eg.event.payload[2:]  #Used to remove first part of the payload

			if (path):			
				for (_, dirList, fileList) in walk(path):
					break
				
				self.plugin.TriggerEvent("FileListCreated", json.dumps({'root':path, 'files':fileList, 'folders':dirList}))
		except:
			pass

		
# broker = '192.168.0.175'
# path = 'C:/Users/Longinus/Downloads'
# MQTT = mosquitto.Mosquitto("EVMQonttrol")
# MQTT.connect(broker)
# for (_, dirList, fileList) in walk(path):	
# 	break
# MQTT.publish("home/htpc/listfiles/result", json.dumps({'root':path, 'files':fileList, 'folders':dirList}))
# OLD Code that sent the file extension too. Proved to be faster to quickly figure it out in javascript
# filesObj = []
# for currentFile in fileList:
# 	filesObj.append({'name':currentFile, 'type':splitext(join(path, currentFile))[1]})
# MQTT.publish("home/htpc/listfiles/result", json.dumps({'root':path, 'files':filesObj, 'folders':dirList}))