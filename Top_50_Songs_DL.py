from bs4 import BeautifulSoup
import requests
import urllib.request, urllib.parse, urllib.error
import webbrowser
import time

# What happens if the artists name has %20 in it??


def download_song(art_name, song_name):
	art_name = art_name.replace("%20", "+")
	song_name = art_name + "+" + song_name.replace(" ", "+")
	url = "http://mp3g.lu/search.php?q=" + song_name
	soup = BeautifulSoup(requests.get(url).text, "html.parser")
	for link in soup.findAll('a', {'class':'button2'}):
		href = link.get("href")
		print(href)
		webbrowser.open_new_tab(href)
		time.sleep(5) #to delay the time between request...
		break

def artist_download(artist_name):
	artist_name = artist_name.replace(" ", "%20")
	url = "http://www.top50songs.org/artist.php?artist=" + artist_name
	soup = BeautifulSoup(requests.get(url).text, "html.parser")
	for link in soup.findAll('a'):
		href = link.get("href")
		if(href != None and "/song-info/" in href):
			download_song(artist_name, link.get("title"))


choice = input("Enter the name of the artist you'd like to get songs from: ")
artist_download(choice)