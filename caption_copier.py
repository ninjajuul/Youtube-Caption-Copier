from youtube_transcript_api import YouTubeTranscriptApi
import re


def get_video_id(url):
    """Extract YouTube video ID from a URL."""
    patterns = [
        r"youtube\.com/watch\?v=([^&]+)",
        r"youtu\.be/([^?&]+)",
        r"youtube\.com/shorts/([^?&]+)"
    ]

    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)

    return None


def get_captions(video_id):
    """Get captions from YouTube video."""
    try:
        api = YouTubeTranscriptApi()

        transcript = api.fetch(video_id)

        text = []
        for line in transcript:
            text.append(line.text)

        return " ".join(text)

    except Exception as e:
        return f"Error getting captions: {e}"


def main():
    print("=== YouTube Caption Copier ===")
    
    url = input("Paste YouTube URL: ")

    video_id = get_video_id(url)

    if not video_id:
        print("Invalid YouTube URL.")
        return

    print("\nFetching captions...\n")

    captions = get_captions(video_id)

    print("=" * 60)
    print(captions)
    print("=" * 60)

    print("\nDone! You can now select and copy the text above.")


if __name__ == "__main__":
    main()