# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os, sys
import subprocess
from sys import argv
import youtube_dl
from ffmpy import FFmpeg


def organize(y):
    count = 0
    x = [y]
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
            elif file.endswith('.jpg') or file.endswith('.png') or file.endswith('jpeg'):
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
            elif file.endswith('.dmg') or file.endswith('.app'):
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
                print('hello')
def video(*args):
    outtmpl = sys.argv[3] +'' + '.%(ext)s'    
    ydl_opts = {
    'format': 'bestvideo+bestaudio/best',
    'outtmpl': outtmpl,

    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        os.chdir('/Users/suryaveda/downloads/')
        ydl.download([sys.argv[2]])

    organize("/Users/suryaveda/downloads/")

def m3u8(*args):
	os.chdir('/Users/suryaveda/downloads/')
	url = sys.argv[2] + ''
	name = sys.argv[3] + '.mp4'
	f = FFmpeg( inputs={url : None}, outputs={ name :'-c copy -bsf:a aac_adtstoasc'})
	f.run()
	organize("/Users/suryaveda/downloads/")


def mp3():
    outtmpl = sys.argv[3] +'' + '.%(ext)s'
    ydl_opts2 = {
        'format': 'bestaudio/best',
        'outtmpl': outtmpl,
        'postprocessors': [
            {'key': 'FFmpegExtractAudio','preferredcodec': 'mp3',
             'preferredquality': '192',
            },
            {'key': 'FFmpegMetadata'},
        ],
               }
    with youtube_dl.YoutubeDL(ydl_opts2) as ydl:
        os.chdir('/Users/suryaveda/Downloads/')
        ydl.download([sys.argv[2]])
    organize("/Users/suryaveda/downloads/")

def mp3fav():
    outtmpl = sys.argv[3] +'' + '.%(ext)s'
    ydl_opts2 = {
        'format': 'bestaudio/best',
        'outtmpl': outtmpl,
        'postprocessors': [
            {'key': 'FFmpegExtractAudio','preferredcodec': 'mp3',
             'preferredquality': '192',
            },
            {'key': 'FFmpegMetadata'},
        ],
               }
    with youtube_dl.YoutubeDL(ydl_opts2) as ydl:
        os.chdir('/Users/suryaveda/Downloads/')
        ydl.download([sys.argv[2]])
        os.chdir('/Users/suryaveda/Desktop/fav/')
        ydl.download([sys.argv[2]])
    organize("/Users/suryaveda/downloads/")


def music(*args):
	os.system("open /Users/suryaveda/Downloads/music")

def doctor(*args):
	os.system("open /Volumes/sk/Backups.backupdb/'addepalli’s MacBook Pro'/2017-12-21-172313/'Macintosh HD'/Users/suryaveda/Downloads/shows/'HOUSE M D S 1-8'/'Doctor Who'")

def starwars(*args):
    os.system("open /Users/suryaveda/Downloads/movies/'star wars'")

def house(*args):
    os.system("open /Volumes/sk/Backups.backupdb/'addepalli’s MacBook Pro'/2017-12-21-172313/'Macintosh HD'/Users/suryaveda/Downloads/shows/'HOUSE M D S 1-8'")

def firefox():
	os.system("open /Applications/Firefox.app ")

def whatsapp():
	os.system("open /Applications/WhatsApp.app ")

def porn(*args):
	os.system("open /Applications/VLC.app /volumes/sk/'Scrubs - season 1.en'")

def unpacker(*args):
    folders = os.listdir(sys.argv[2])
    print (folders)
    for x in folders:
        folder_path = os.path.join(sys.argv[2], x)
        if os.path.isdir(folder_path):
            files = os.listdir(folder_path)
            print(files)
            for file in files:
                new_path = os.path.join(sys.argv[2], file)
                old_path = os.path.join(folder_path, file)
                os.rename(old_path, new_path)
            os.rmdir(folder_path)

        else:
            print ('not a folder')

    print("Done!")

def poirot(*args):
	os.system("open /Applications/VLC.app /volumes/sk/poirot")

def the(*args):
    folders = os.listdir(sys.argv[2])
    newlist = []
    words = ['The', 'the']
    for file in folders:
        old_path = os.path.join(sys.argv[2], file)
        if os.path.isdir(old_path):
            searchWord = file.split()
            word2 = file.split('.')
            word3 = file.split('_')
            for word in words:
                if word == searchWord[0] or word == word2[0] or word == word3[0]:
                    newlist.append(file)
                    print(newlist)
                    old_path = os.path.join(sys.argv[2], file)
                    path = os.path.join(sys.argv[2], 'Ths')
                    new_path = path + '/' + file
                    if os.path.exists(path):
                        os.rename(old_path, new_path)
                    else:
                        os.mkdir(path)
                        os.rename(old_path, new_path)




if __name__ == '__main__':
	try:
		globals()[sys.argv[1]]([sys.argv[2]])
	except:
		globals()[sys.argv[1]]()

		

