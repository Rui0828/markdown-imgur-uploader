import os
import re
import requests
from dotenv import load_dotenv
import configparser

# Load environment variables
load_dotenv()
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

# Load configuration
config = configparser.ConfigParser()
config.read("config.ini")
note_path = config.get("Paths", "note_path")

# Imgur upload function
def upload_to_imgur(image_url):
    headers = {"Authorization": f"Client-ID {CLIENT_ID}"}
    response = requests.post("https://api.imgur.com/3/image", headers=headers, data={"image": image_url})

    if response.status_code == 200:
        return response.json()["data"]["link"]
    else:
        print(f"Failed to upload image: {image_url}")
        print(response.json())
        return None

# Read the markdown note
with open(note_path, "r", encoding="utf-8") as file:
    note_content = file.read()

# Find all image URLs from imgur and hackmd.io
image_pattern = re.compile(r"!\[.*?\]\((https?://(?:i\.imgur\.com|hackmd\.io)/.+?)\)")
updated_content = note_content

for match in image_pattern.finditer(note_content):
    original_url = match.group(1)
    new_url = upload_to_imgur(original_url)

    if new_url:
        updated_content = updated_content.replace(original_url, new_url)
        print(f"Updated: {original_url} -> {new_url}")

# Write the updated content back to the markdown note
with open(note_path, "w", encoding="utf-8") as file:
    file.write(updated_content)

print("All images updated successfully.")
