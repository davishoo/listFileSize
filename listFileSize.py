#! python3
# list the file size of designated folder, and then create a log file at D:\Temp

import os
#import os.path          #old  code,  guess it can be deleted
#import glob               #old  code,  guess it can be deleted

SUFFIXES = ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB']

def approximate_size(size):
    '''Convert a file size to human-readable form.

    Keyword arguments:
    size -- file size in bytes
  
    Returns: string

    '''
    if size < 0:
        raise ValueError('number must be non-negative')

    multiple = 1024.0 
    for suffix in SUFFIXES:
        size /= multiple
        if size < multiple:
            return '{0:.1f} {1}'.format(size, suffix)   # :1f means 'keep 1 dicimal place'; 0 stands for size, 1 for suffix

print('Example: D:\\file\\python\\AutomatePDF')
rootDir = input('Please input director path: ')
count = 0
fileDict = {}
sortfileDict = {}
for parent, dirnames, filenames in os.walk(rootDir):
    #print('Folder: %s' % dirName)
    for filename in filenames:
        name = os.path.join(parent,filename)
        try:
            filesize = os.path.getsize(name)
        except (OSError):
            filesize = 0                  # If exception happens, filesize = 0
        fileDict[name] = filesize
        count += 1
        print(count)
        
sortfileDict = sorted(fileDict.items(), key=lambda fileDict:fileDict[1], reverse = True)
'''
fileDict.iteritems()........ transform fileDict to iter so that it can be sorted
key=lambda fileDict:fileDict[1].......sort the items according to file size

'''
os.chdir('D:\Temp')
fList = open('filelist.txt','w', encoding='utf-8')
for i in range(len(sortfileDict)):
    #print sortfileDict[i][0], "\t", sortfileDict[i][1]
    fileList = "{1} \t {0} \n".format(sortfileDict[i][0], approximate_size(sortfileDict[i][1]))
    fList.write(fileList)

fList.close()

print('DONE! Result file "filelist.txt" has been saved at D:\Temp')



