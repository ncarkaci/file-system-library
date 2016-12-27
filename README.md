# File System Library

The script include multiple function related with file system operation. I write this because i don't want reuse same function again and again.

## Functions and operation
### Function List
* getFilePaths(directory, extensionList=[], reverse=False)
* groupFilesAsSize(listOfFile)
* groupFilesAsExtension(listOfFile)
* filterUniqueGroupFromDict(fileGroupDict)
* getFileHash(filename, fastHash=False, buf=(1024*1024))
* moveFiles(listOfFile, destinationDir)
* printDict(extensionDict)
* renameFileWithHashValue(directory)

### Function Details

#### getFilePaths(directory, extensionList=[], reverse=False)

Collect all files from given directory and return their paths list
 
param directory : <string> directory name
param extensionList : <string> file extension, using for file type filter. Default value is []
param reverse : <boolean> Default value is False

return <list> paths of files


#### groupFilesAsSize(listOfFile)
Get list of files and return a dictionary group as file size.
 
param listOfFile : <list> list of file path

return <dict> (<key><value>) : key : size, value : filename

#### groupFilesAsExtension(listOfFile)
Get list of files and return a dictionary group as file type. It check file type as extension

param listOfFile : <list> list of file path

return <dict> (<key><value>) : key : type, value : filename

Todo : make file type cheking as file header information

#### filterUniqueGroupFromDict(fileGroupDict)

Get file group dictionary return non-unique groups in dictionary. Non-unique group in dictionary means it key has multiple value

param fileGroupDict : <dict> (<key><value>) file group

return <dict> (<key><value>) : non-unique groups in dictionary

#### getFileHash(filename, fastHash=False, buf=(1024*1024))
Calculate md5 hash value for given file and return the value. if fast hash enabled, it calculate fast hashing. Fast hashing meaning it get specific part of the file header and calculate hash for this part. Fast hashing part size can give as parameter 

param filename : <string> file path
param fastHash : <boolean> Specific part of the file header hashing. This enabled for big file hashing process. Default value is False
param buf : <integer> Fast hashing size. Default value is 1024*1024 = 1 megabyte

return <string> : hash value of file

#### moveFiles(listOfFile, destinationDir)
Move list of the files into different directory. If the same name file exists, it add random prefix into filename

param listOfFile : <string list> list of file path
param destinationDir : <string> Destination directory name

return void

Todo : Check destionation directory not exists, create it

#### printDict(extensionDict)
Print dictionary which its key has multiple values and print this

param extensionDict : <dict> (<string><string list>) dictionary

return void

#### renameFileWithHashValue(directory)
Collect deeply all files from directory and calculate md5 hash values of the files, and rename the files with their hash values

param directory : <string> directory name

return void


