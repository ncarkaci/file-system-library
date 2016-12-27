#!/usr/bin/env python
#
# File uitility library. The library has useful functions on running file system.
# Each function has different aim.
#
# Author: Necmettin Çarkacı
# E-mail: necmettin [ . ] carkaci [ @ ] gmail [ . ] com
#
#Usage : 


import os, sys, time, random
import hashlib
from collections import OrderedDict # for sort dict 

'''
# Collect all files from given directory and return their paths list
# 
# param directory : <string> directory name
# param extensionList : <string> file extension, using for file type filter. Default value is []
# param reverse : <boolean> Default value is False
#
# return <list> paths of files
#
'''
def getFilePaths(directory, extensionList=[], reverse=False):

	file_paths = []

	for root, directories, files in os.walk(directory):
		for filename in files:
			if (len(extensionList) > 0) : # get speified extension files
				extension = os.path.splitext(filename)[1]

				if ((extension.lower() in extensionList) or (extension.upper() in extensionList)) :	
					if(not reverse):		
						filepath = os.path.join(root, filename)
						file_paths.append(filepath) 
						#print (filepath)
				elif (reverse):
					filepath = os.path.join(root, filename)
					file_paths.append(filepath)
 
			else :	# get all files			
					filepath = os.path.join(root, filename)
					file_paths.append(filepath) 
					#print (filepath)

	print ("Number of file found : "+ str(len(file_paths)))
	return file_paths


'''
# Get list of files and return a dictionary group as file size.
# 
# param listOfFile : <list> list of file path
#
# return <dict> (<key><value>) : key : size, value : filename
#
'''
def groupFilesAsSize(listOfFile):
	
	fileGroupDict = {} # <key><value> --> <size> [list of file names]

	for filename in listOfFile:
		size = os.path.getsize(filename)
		
		if size in fileGroupDict.keys(): # or if fileGroupDict.get(size, []):
			fileGroupDict[size].append(filename)
		else :
			fileGroupDict[size] = [] # create list for value of key
			fileGroupDict[size].append(filename)
	
	#print (fileGroupDict)
	print ("Number of group : "+ str(len(fileGroupDict)))	
	return 	fileGroupDict

'''
# Get list of files and return a dictionary group as file type.
# It check file type as extension
#
# param listOfFile : <list> list of file path
#
# return <dict> (<key><value>) : key : type, value : filename
#
# Todo : make file type cheking as file header information
'''
def groupFilesAsExtension(listOfFile):
	
	fileGroupDict = {} # <key><value> --> <size> [list of file names]

	for filename in listOfFile:
		extension = os.path.splitext(filename)[1]
		
		if extension in fileGroupDict.keys(): # or if fileGroupDict.get(size, []):
			fileGroupDict[extension].append(filename)
		else :
			fileGroupDict[extension] = [] # create list for value of key
			fileGroupDict[extension].append(filename)
	
	#print (fileGroupDict)
	print ("Number of group : "+ str(len(fileGroupDict)))	
	return 	fileGroupDict


'''
# Get file group dictionary return non-unique groups in dictionary
# Non-unique group in dictionary means it key has multiple value
#
# param fileGroupDict : <dict> (<key><value>) file group
#
# return <dict> (<key><value>) : non-unique groups in dictionary
#
'''
def filterUniqueGroupFromDict(fileGroupDict):

	uniqueFileSizeDict = {}

	for size in fileGroupDict:
		listOfFile = fileGroupDict[size]
		if (len(listOfFile) > 1):
			uniqueFileSizeDict[size] = listOfFile

	#print (uniqueFileSizeDict)
	print ("Number of group after filtering : "+ str(len(uniqueFileSizeDict)))
	return uniqueFileSizeDict


'''
# Calculate md5 hash value for given file and return the value
# if fast hash enabled, it calculate fast hashing.
# Fast hashing meaning it get specific part of the file header and calculate hash for this part.
# Fast hashing part size can give as parameter 
#
# param filename : <string> file path
# param fastHash : <boolean> Specific part of the file header hashing. This enabled for big file hashing process. Default value is False
# param buf : <integer> Fast hashing size. Default value is 1024*1024 = 1 megabyte
#
# return <string> : hash value of file
#
'''
def getFileHash(filename, fastHash=False, buf=(1024*1024)):

	hasher = hashlib.md5()
	with open(filename, 'rb') as file:
		
		if (fastHash) :
		    chunk = file.read(buf)
		    while len(chunk) > 0:
		        hasher.update(chunk)
		        chunk = file.read(buf)
		else :
			content = file.read()
			hasher.update(content)

	#print(hasher.hexdigest())
	
	return hasher.hexdigest()


'''
# Move list of the files into different directory
# If the same name file exists, it add random prefix into filename
#
# param listOfFile : <string list> list of file path
# param destinationDir : <string> Destination directory name
#
# return void
#
'''
def moveFiles(listOfFile, destinationDir):

	for filename in listOfFile:
		path, name 	= os.path.split(filename)
		prefix_num 	= random.randrange(1,99999999)

		if not os.path.exists(destinationDir):
			os.makdirs(destinationDir)

		destinationFilename = os.getcwd()+os.sep+destinationDir+os.sep+str(prefix_num)+"_"
		os.rename(filename,destinationFilename+name)

'''
# Print dictionary which its key has multiple values and print this
#
# param extensionDict : <dict> (<string><string list>) dictionary
#
# return void
#
'''
def printDict(extensionDict):
	
	sortedExtDict = OrderedDict(sorted(extensionDict.items(), key=lambda t: len(t[1])))
	print ('Key : '+str(len(sortedExtDict))+'\n'+'Values : ')

	for key in sortedExtDict.keys():
		print (key+' : '+str(len(sortedExtDict[key])))
	

'''
# Collect deeply all files from directory and calculate md5 hash values of the files, 
# And rename the files with their hash values
#
# param directory : <string> directory name
#
# return void
#
'''
def renameFileWithHashValue(directory):

	listOfFiles = getFilePaths(directory)	

	for sourceFilename in listOfFiles:
		hashValue = getFileHash(sourceFilename)
		path, name = os.path.split(sourceFilename)
		ext = name.split('.')[-1]
		destinationFilename = path+os.sep+hashValue+'.'+ext
		os.rename(sourceFilename,destinationFilename)	
			
if __name__ == '__main__':
	
	directory = sys.argv[1]

	start = time.time()
	print("Start time : "+str(time.clock()))

	# listOfFile = getFilePaths(directory, extensionList, reverse)
	# print ('Files collected. The files are grouping as size ... ')	
	# moveFiles(listOfFile, 'videos')
	
	# groupFile = groupFilesAsExtension(listOfFile)
	# printDict(groupFile)

	renameFileWithHashValue(directory)

	end = time.time()
	print ('End time : '+str(time.clock()))
	print('Running time : '+str(end - start))

