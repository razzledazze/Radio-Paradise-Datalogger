from lxml import html
import requests
import webbrowser
import time
import csv

def getArtistSong(url): #Takes the url of the internet radio station and gives the currently playing song and artist
    page = requests.get(url)
    tree = html.fromstring(page.content)

    artistAndSong = tree.xpath('//p[@class="lead"]//text()')[1]
    artistAndSong = artistAndSong.split(' - ')

    artist = artistAndSong[0]
    song = artistAndSong[1]

    return artist,song

def getLogSongs():
    logSongs = []
    with open('paradiseLog.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            logSongs.append([row[0],row[1]])
    return logSongs

def writeLogSongs(logSongs):
    with open('paradiseLog.csv', 'w', newline='') as file:
        writer = csv.writer(file, delimiter=',')
        for song in logSongs:
            writer.writerow([song[0],song[1]])

url = 'https://www.internet-radio.com/station/radioparadise/' #enter any internet radio station url and this app will work with it

while True:
    artist,song = getArtistSong(url) #scrapes the artist and song titles from the internet radio website

    print("New song added: "+song+" by "+artist+".")

    logSongs = getLogSongs()
    logSongs.append([song,artist])
    writeLogSongs(logSongs)
    
    artistSame = True
    while artistSame == True: #until the artist changes, this will loop, once it changes the normal process will happen again
        newArtist,newSong = getArtistSong(url)
        if artist != newArtist:
            artistSame = False
