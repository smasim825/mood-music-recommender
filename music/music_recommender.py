from googleapiclient.discovery import build
import random
import os

def recommend_music(emotion):
    api_key = os.getenv("YOUTUBE_API_KEY")
    youtube = build("youtube", "v3", developerKey=api_key)

    emotion_map = {
        "happy": ["happy songs", "party music", "uplifting pop"],
        "sad": ["sad songs", "emotional music", "breakup songs"],
        "angry": ["rock music", "metal music", "rage songs"],
        "fear": ["dark ambient music", "suspense music"],
        "calm": ["calm music", "relaxing instrumental", "meditation music"],
        "romantic": ["love songs", "romantic hits"],
        "neutral": ["chill music", "lofi beats"]
    }

    query = random.choice(emotion_map.get(emotion, ["chill music"]))

    request = youtube.search().list(
        part="snippet",
        q=query,
        type="video",
        videoCategoryId="10",
        maxResults=10
    )

    response = request.execute()

    items = response["items"]
    random.shuffle(items)

    songs = []
    for item in items[:5]:
        title = item["snippet"]["title"]
        channel = item["snippet"]["channelTitle"]
        songs.append(f"{title} - {channel}")

    return songs
