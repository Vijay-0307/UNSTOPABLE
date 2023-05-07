from googleapiclient.discovery import build

# Authenticate to YouTube
api_key = "AIzaSyBPHs1Pq49RrKiW1BIFl2uJHYrwa7cpeyY"

# Create YouTube service
youtube = build('youtube', 'v3', developerKey=api_key)

# Define keyword
keyword = "நூல்கள்"

# Search videos with keyword
search_response = youtube.search().list(
    part="snippet",
    q=keyword,
    type="video",
    maxResults=10
).execute()

for item in search_response["items"]:
    video_title = item["snippet"]["title"]
    video_id = item["id"]["videoId"]
    channel_title = item["snippet"]["channelTitle"]
    published_at = item["snippet"]["publishedAt"]
    print("Video Title:", video_title)
    print("Video ID:", video_id)
    print("Channel Title:", channel_title)
    print("Published At:", published_at)
    print("---")
