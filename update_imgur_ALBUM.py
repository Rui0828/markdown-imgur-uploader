import re
import requests
import os
from dotenv import load_dotenv
import configparser

def upload_image_to_imgur(image_url, album_id, access_token):
    """
    Upload an image to Imgur.

    :param image_url: The URL of the image to upload
    :param album_id: Your Imgur album ID
    :param access_token: Your Imgur access token
    :return: The URL of the uploaded image
    """
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    data = {
        "image": image_url,
        "album": album_id,
        "type": "URL"
    }
    response = requests.post("https://api.imgur.com/3/image", headers=headers, data=data)

    if response.status_code == 200:
        return response.json()["data"]["link"]
    else:
        raise Exception(f"Failed to upload image: {response.json()}")

def update_markdown_with_imgur_links(markdown_text, album_id, access_token):
    """
    Find all Imgur and hackmd.io image links in the Markdown and replace them with new Imgur links.

    :param markdown_text: The content of the Markdown file
    :param album_id: Your Imgur album ID
    :param access_token: Your Imgur access token
    :return: Updated Markdown content
    """
    # Match image URLs in the Markdown content
    img_pattern = re.compile(r"!\[.*?\]\((https?://(?:i\.imgur\.com|hackmd\.io)/.+?)\)")

    def replace_image(match):
        old_url = match.group(1)
        new_url = upload_image_to_imgur(old_url, album_id, access_token)
        print(f"Updated image: {old_url} -> {new_url}")
        return match.group(0).replace(old_url, new_url)

    # Replace all matches with updated URLs
    updated_markdown = re.sub(img_pattern, replace_image, markdown_text)
    return updated_markdown

def main():
    # Load environment variables
    load_dotenv()
    album_id = os.getenv("ALBUM_ID")
    access_token = os.getenv("ACCESS_TOKEN")

    if not all([album_id, access_token]):
        raise EnvironmentError("Missing one or more required environment variables: ALBUM_ID, ACCESS_TOKEN")

    # Load configuration from config.ini
    config = configparser.ConfigParser()
    config.read("config.ini")

    if "Paths" not in config or "note_path" not in config["Paths"]:
        raise ValueError("Missing 'note_path' in config.ini under [Paths] section.")

    markdown_file = config["Paths"]["note_path"]

    # Load your Markdown file
    with open(markdown_file, "r", encoding="utf-8") as file:
        markdown_content = file.read()

    # Update the Markdown with new Imgur links
    updated_content = update_markdown_with_imgur_links(markdown_content, album_id, access_token)

    # Overwrite the original Markdown file
    with open(markdown_file, "w", encoding="utf-8") as file:
        file.write(updated_content)

    print(f"Updated Markdown content saved to {markdown_file}!")

if __name__ == "__main__":
    main()
