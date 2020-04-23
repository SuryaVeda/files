#!/bin/bash
function print_my_input() {
  echo 'Your input: ' $1
}
function firefox(){
   python fun.py firefox
}
function whatsapp() {
  python fun.py whatsapp
}
function youtube_mp3() {
  youtube-dl --extract-audio --audio-format mp3 $1
}

function youtube_video() {
  youtube-dl $1
}
function porn() {
  python fun.py porn
}

function doctor() {
  python fun.py doctor
}

function starwars() {
  python fun.py starwars
}

function music() {
  python fun.py music
}

function poirot() {
  python fun.py poirot
}
function mp3 () {
  youtube-dl -o "%(title)s.%(ext)s" --extract-audio --audio-format mp3 $1 
}

function mp3fav () {
  python3 fun.py mp3fav $1 $2
}

function video () {
  python3 fun.py video $1 $2
}
function mp4 () {
  youtube-dl -f 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best' --write-auto-sub -o "%(title)s.%(ext)s" $1
}

function organize () {
  python3 clean.py organize $1
}

function house () {
 python3 /Users/suryaveda/fun.py house
}
function bootcamp () {
 bless -mount /Volumes/BOOTCAMP -setBoot -nextonly
 shutdown -r now
}
function m3u8 () {
  python3 fun.py m3u8 $1 $2
}

export PATH="$PATH:/Users/suryaveda/.dat/releases/dat-13.13.1-macos-x64"
