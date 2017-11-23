
#https://github.com/mps-youtube/pafy/blob/master/README.rst
import pafy
import os

playlist_url = []

new_list = []

x_list=[]



f = open('nicha_songs.txt', 'r')

for line in f:
	playlist_url.append(line.strip('https://youtu.be/'))




for i in playlist_url:
	new_list.append(i.rstrip('\n'))




for y in new_list:
	if y.strip():
		x_list.append(y)



for i in x_list:

	video = pafy.new(i)

	bestaudio = video.getbestaudio()

	bestaudio.download()





