# Imgur Uploader for Markdown Notes

**Read this in other languages: [[English](README.md) | [繁體中文](README_zh.md)]**

When uploading notes from HackMD or local Markdown files to GitHub, image links can often break, making the images inaccessible. This script solves that problem by uploading images to Imgur and replacing the links in your Markdown file.

## Prerequisites

1. **Set Up Environment Variables**
   - Create a `.env` file in the project directory.
   - Add the following keys:
     ```env
     # Without album
     CLIENT_ID=your_client_id
     CLIENT_SECRET=your_client_secret

     # With album
     ALBUM_ID=your_album_id
     ACCESS_TOKEN=your_access_token
     ```

2. **Configure the Path to Your Note**
   - Create or update a `config.ini` file in the project directory.
   - Add the following configuration:
     ```ini
     [Paths]
     note_path=path_to_your_markdown_file.md
     ```

## Usage

1. **Change HackMD Note Permissions** (if applicable)
   - Temporarily set the HackMD note's "Read" permission to "Everyone" so the script can access the images. You can change it back to "Private" after running the script.

2. **Run the Script**
   - If you are uploading to an album, use:
     ```bash
     python update_imgur_ALBUM.py
     ```
   - If you are uploading without an album, use:
     ```bash
     python update_imgur_wo_album.py
     ```

3. **Update Permissions** (optional)
   - If you changed the HackMD note's "Read" permission in step 1, revert it to "Private".

4. **Push the Updated Note to GitHub**
   - Commit and push the updated Markdown file to your GitHub repository.

## Notes

- The script will automatically find and replace all image links hosted on `i.imgur.com` or `hackmd.io` with new Imgur links.
- Ensure that your `.env` file contains valid credentials for Imgur and that your access token has sufficient permissions to upload images.

## Example Configurations

### Example `.env`
```env
CLIENT_ID=abc123
CLIENT_SECRET=xyz789
ALBUM_ID=your_album_id
ACCESS_TOKEN=your_access_token
```

### Example `config.ini`
```ini
[Paths]
note_path=/path/to/your/note.md
```

## Troubleshooting

- **Missing Environment Variables:** Ensure all required variables are set in `.env`.
- **Incorrect Note Path:** Verify the `note_path` in `config.ini` points to the correct Markdown file.
- **Imgur Upload Errors:** Check your Imgur credentials and ensure your access token is valid.

With this script, you can easily upload images to Imgur, ensuring your Markdown notes remain intact on GitHub without the need to keep HackMD notes publicly accessible, thereby maintaining privacy.
