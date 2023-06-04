import cv2
import requests
import pytesseract
from PIL import Image
from bs4 import BeautifulSoup

# Function to extract text from an image using OCR
def extract_text_from_image(image_path):
    image = Image.open(image_path)
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    text = pytesseract.image_to_string(image)
    return text.strip()

# Function to search for lyrics using Shazam API
def search_lyrics_with_shazam_api(title, artist):
    url = "https://shazam.p.rapidapi.com/search"
    querystring = {"term": title + " " + artist}
    headers = {
        "X-RapidAPI-Host": "shazam.p.rapidapi.com",
        "X-RapidAPI-Key": "YOUR_API_KEY"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    data = response.json()
    hits = data.get('tracks', {}).get('hits', [])
    if hits:
        lyrics_url = hits[0]['track'].get('url', '')
        return lyrics_url
    else:
        return None

# Function to scrape lyrics from a website
def scrape_lyrics(lyrics_url):
    response = requests.get(lyrics_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    lyrics = soup.find("div", class_="lyrics").get_text()
    return lyrics.strip()

# Function to extract text from a muted video using OCR
def extract_text_from_video(video_path):
    video_capture = cv2.VideoCapture(video_path)
    text = ""
    while video_capture.isOpened():
        ret, frame = video_capture.read()
        if not ret:
            break
        # Apply OCR to extract text from the frame
        # Use pytesseract or any other OCR library of your choice
        frame_text = pytesseract.image_to_string(frame)
        text += frame_text.strip() + " "
    video_capture.release()
    return text.strip()

# Function to search for lyrics using Shazam API with video information
def search_lyrics_with_shazam_api_video(title, artist):
    url = "https://shazam.p.rapidapi.com/search"
    querystring = {"term": title + " " + artist + " music video"}
    headers = {
        "X-RapidAPI-Host": "shazam.p.rapidapi.com",
        "X-RapidAPI-Key": "YOUR_API_KEY"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    data = response.json()
    hits = data.get('tracks', {}).get('hits', [])
    if hits:
        lyrics_url = hits[0]['track'].get('url', '')
        return lyrics_url
    else:
        return None

# Function to scrape lyrics from a website (for video)
def scrape_lyrics_video(lyrics_url):
    # Add code to scrape lyrics from the video website
    pass

# Example usage for image
image_path = r'C:\Users\clint\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Python 3.11\Song.jpeg'
title = extract_text_from_image(image_path)
artist = "Unknown Artist"  # Assuming artist is not available in the image
lyrics_url = search_lyrics_with_shazam_api(title, artist)
print(title)
if lyrics_url:
    lyrics = scrape_lyrics(lyrics_url)
    print("Title:", title)
    print("Artist:", artist)
    print("Lyrics:", lyrics)
else:
    print("No lyrics found.")

# Example usage for video
video_path = r'C:\path\to\muted_video.mp4'
title_video = extract_text_from_video(video_path)
artist_video = "Unknown Artist"  # Assuming artist is not available in the video
lyrics_url_video = search_lyrics_with_shazam_api_video(title_video, artist_video)
print(title_video)
if lyrics_url_video:
    lyrics_video = scrape_lyrics_video(lyrics_url_video)
    print("Title (Video):", title_video)
    print("Artist (Video):", artist_video)
    print("Lyrics (Video):", lyrics_video)
else:
    print("No lyrics found for the video.")