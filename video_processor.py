import re
import requests
from bs4 import BeautifulSoup
from youtube_transcript_api import YouTubeTranscriptApi
import os

def extract_video_identifier(url):
    pattern = re.compile(r"(?:v=|\/)([0-9A-Za-z_-]{11}).*")
    match = pattern.search(url)
    if match:
        return match.group(1)
    raise ValueError("Invalid YouTube URL format")

def fetch_transcript(video_id):
    try:
        transcript_data = YouTubeTranscriptApi.get_transcript(video_id)
        return " ".join([entry['text'] for entry in transcript_data])
    except Exception as e:
        raise Exception(f"Failed to fetch transcript: {str(e)}")

def retrieve_metadata(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        metadata = {
            'title': soup.find('meta', property='og:title')['content'],
            'channel': soup.find('link', itemprop='name')['content'],
            'views': soup.find('meta', itemprop='interactionCount')['content'],
            'upload_date': soup.find('meta', itemprop='datePublished')['content']
        }
        
        return metadata
    except Exception as e:
        raise Exception(f"Failed to retrieve metadata: {str(e)}")

def get_thumbnail(video_id):
    thumbnail_url = f"https://img.youtube.com/vi/{video_id}/0.jpg"
    thumbnail_path = f"thumbnails/{video_id}.jpg"
    
    if not os.path.exists("thumbnails"):
        os.makedirs("thumbnails")
    
    response = requests.get(thumbnail_url)
    with open(thumbnail_path, 'wb') as file:
        file.write(response.content)
    
    return thumbnail_path
