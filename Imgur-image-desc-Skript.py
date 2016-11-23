from bs4 import BeautifulSoup
import urllib
import os
import sys
import requests
import shutil



dir = os.path.dirname(os.path.abspath(__file__))
quoradir = dir +"\\ImgurText"

if not os.path.exists(quoradir):
        os.makedirs(quoradir)




main_url = "http://imgur.com/gallery/M0MKz"
print "Page: " + str(main_url)
r = requests.get(main_url)
	
	
#main_url_opener = urllib.urlopen(main_url)
#main_url_response = main_url_opener.read()

data = r.text


supa = BeautifulSoup(data, "html.parser")
a=1

for hit in supa.findAll("div", { "class" : "post-title-container" }):
	ahit = hit.text.encode('utf-8').decode	('ascii', 'ignore')
	text_file = open("ImgurText\\imgur-post.txt", 'a')
	text_file.write("%s\n" % (ahit))
	text_file.close()

for hit in supa.findAll("div", { "class" : "post-image-meta" }):
	ahit = hit.text.encode('utf-8').decode	('ascii', 'ignore')
	text_file = open("ImgurText\\imgur-post.txt", 'a')
	text_file.write("%d. %s\n" % (a,ahit))
	text_file.close()
	a += 1

   