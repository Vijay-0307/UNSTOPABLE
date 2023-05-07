from datetime import datetime
from instagram_private_api import Client

# Provide your Instagram username and password
username = "_.v.s_"
password = "MV!j@ySury@2004"

# Create an instance of the Instagram Private API client
api = Client(username, password)

# Define your keyword
keyword = "kohli"

# Get the feed for the specified tag
results = api.feed_tag(keyword, rank_token=Client.generate_uuid(), count=10)

# Process the results
for item in results.get("items", []):
    # Extract relevant information from each item
    username = item.get("user", {}).get("username")
    timestamp = item.get("taken_at")

    # Convert the timestamp to a datetime object
    post_time = datetime.fromtimestamp(timestamp)

    # Print the extracted information
    print("Username:", username)
    print("Post Time:", post_time)
    print("---")
