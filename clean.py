from __future__ import unicode_literals
import os, sys
from os.path import join 

x = [sys.argv[2]]
def organize(x):
    count = 0
    for i in x:
        for file in os.listdir(i):
            if file.endswith('.torrent'):
                filename = "" + file
                count += 1
                currentPath = i + '/' + filename
                print('current path:', currentPath)
                destinationPath = i + '/torrentFiles'
                print('destination Path:', destinationPath)
                newPath = destinationPath + '/' +filename
                print('New Path', newPath)
                if os.path.exists(destinationPath):
                    os.rename(currentPath, newPath)
                else:
                    os.mkdir(destinationPath)
                    os.rename(currentPath, newPath)
                    print ('Files:', count)
            elif file.endswith('.jpg') or file.endswith('.png') or file.endswith('jpeg') or file.endswith('gif'):
                filename = "" + file
                count += 1
                currentPath = i + '/' + filename
                destinationPath = i + '/pics'
                newPath = destinationPath + '/' +filename
                if os.path.exists(destinationPath):
                    os.rename(currentPath, newPath)
                else:
                    os.mkdir(destinationPath)
                    os.rename(currentPath, newPath)
                    print ('Files:', count)
            elif file.endswith('.pdf'):
                filename = "" + file
                count += 1
                currentPath = i + '/' + filename
                print('current path:', currentPath)
                destinationPath = i + '/extraPdfs'
                print('destination Path:', destinationPath)
                newPath = destinationPath + '/' +filename
                print('New Path', newPath)
                if os.path.exists(destinationPath):
                    os.rename(currentPath, newPath)
                else:
                    os.mkdir(destinationPath)
                    os.rename(currentPath, newPath)
                    print ('Files:', count)


            elif file.endswith('.mp3') or file.endswith('.m4a'):
                filename = "" + file
                count += 1
                currentPath = i + '/' + filename
                destinationPath = i + '/music'
                newPath = destinationPath + '/' +filename
                if os.path.exists(destinationPath):
                    os.rename(currentPath, newPath)
                else:
                    os.mkdir(destinationPath)
                    os.rename(currentPath, newPath)
            elif file.endswith('.mp4') or file.endswith('.mkv') or file.endswith('.webm') or file.endswith('.avi'):
                filename = "" + file
                currentPath = i + '/' + filename
                if os.path.getsize(currentPath) >= 750410312:
                    destinationPath = i + '/movies'
                    newPath = destinationPath + '/' +filename
                    if os.path.exists(destinationPath):
                        os.rename(currentPath, newPath)
                    else:
                        os.mkdir(destinationPath)
                        os.rename(currentPath, newPath)
                else:
                    destinationPath = i +'/videos'
                    newPath = destinationPath + '/' + filename
                    if os.path.exists(destinationPath):
                        os.rename(currentPath, newPath)
                    else:
                        os.mkdir(destinationPath)
                        os.rename(currentPath, newPath)
            elif file.endswith('.srt'):
                filename = "" + file
                count += 1
                currentPath = i + '/' + filename
                destinationPath = i + '/srt'
                newPath = destinationPath + '/' +filename
                if os.path.exists(destinationPath):
                    os.rename(currentPath, newPath)
                else:
                    os.mkdir(destinationPath)
                    os.rename(currentPath, newPath)
            elif file.endswith('.zip') or file.endswith('.rar'):
                filename = "" + file
                count += 1
                currentPath = i + '/' + filename
                destinationPath = i + '/compressedFiles'
                newPath = destinationPath + '/' +filename
                if os.path.exists(destinationPath):
                    os.rename(currentPath, newPath)
                else:
                    os.mkdir(destinationPath)
                    os.rename(currentPath, newPath)
            elif file.endswith('.html') or file.endswith('.py') or file.endswith('.css') or file.endswith('.json'):
                filename = "" + file
                count += 1
                currentPath = i + '/' + filename
                destinationPath = i + '/developer'
                newPath = destinationPath + '/' +filename
                if os.path.exists(destinationPath):
                    os.rename(currentPath, newPath)
                else:
                    os.mkdir(destinationPath)
                    os.rename(currentPath, newPath)
            elif file.endswith('.pptx') or file.endswith('.key'):
                filename = "" + file
                count += 1
                currentPath = i + '/' + filename
                destinationPath = i + '/powerpoint'
                newPath = destinationPath + '/' +filename
                if os.path.exists(destinationPath):
                    os.rename(currentPath, newPath)
                else:
                    os.mkdir(destinationPath)
                    os.rename(currentPath, newPath)
            elif file.endswith('.dmg') or file.endswith('.app') or file.endswith('.pkg') or file.endswith('.xip'):
                filename = "" + file
                count += 1
                currentPath = i + '/' + filename
                destinationPath = i + '/apps'
                newPath = destinationPath + '/' +filename
                if os.path.exists(destinationPath):
                    os.rename(currentPath, newPath)
                else:
                    os.mkdir(destinationPath)
                    os.rename(currentPath, newPath)
            else:
                print( file + ' extension not supported')
 
if __name__ == '__main__':
    globals()[sys.argv[1]]([sys.argv[2]])