# YouTube Caption Copier

A simple Python script that fetches captions (transcripts) from YouTube videos. Just paste a YouTube URL, and the script retrieves the available captions and prints the full transcript directly in your terminal, making it easy to copy and use anywhere.

## Features

* Fetch captions from YouTube videos.
* Supports:

  * Standard YouTube URLs
  * `youtu.be` short links
  * YouTube Shorts
* Displays the complete transcript in the terminal.
* Simple and lightweight.
* Easy to modify or integrate into other projects.

## Requirements

* Python 3.10 or newer
* `youtube-transcript-api`

## Installation

Clone this repository:

```bash
git clone https://github.com/ninjajuul/Youtube-Caption-Copier
cd youtube-caption-copier
```

Create a virtual environment (recommended):

### Linux/macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

### Windows

```cmd
python -m venv venv
venv\Scripts\activate
```

Install the required package:

```bash
pip install youtube-transcript-api
```

## Usage

Run the script:

```bash
python caption_copier.py
```

When prompted, paste a YouTube URL:

```
Paste YouTube URL:
```

Example:

```
Paste YouTube URL:
https://www.youtube.com/watch?v=dQw4w9WgXcQ
```

The script will fetch the transcript and print it directly in the terminal.

## Supported URLs

* `https://www.youtube.com/watch?v=VIDEO_ID`
* `https://youtu.be/VIDEO_ID`
* `https://www.youtube.com/shorts/VIDEO_ID`

## Example Output

```
============================================================
Hello everyone and welcome back...
Today we're going to...
...
============================================================
```

Simply select the text in your terminal and copy it.

## Limitations

* The video must have captions available.
* Some videos disable transcript access.
* Private, deleted, age-restricted, or region-restricted videos may not work.
* If no captions are available, the script will display an error message.

## Possible Improvements

* Automatically copy the transcript to your clipboard.
* Save transcripts as `.txt` files.
* Export to Markdown or PDF.
* Download captions in multiple languages.
* Batch process multiple YouTube URLs.
* Add a graphical user interface (GUI).

## Disclaimer

This project only retrieves publicly available YouTube transcripts. It does not generate captions or bypass any YouTube restrictions. Please respect copyright laws and YouTube's Terms of Service when using downloaded transcripts.

## License

This project is open source. Feel free to modify, improve, and share it.
