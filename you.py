import pytube

# Get the YouTube video URL from the user
url = input("Enter the YouTube video URL: ")

# Create a Pytube YouTube object from the video URL
yt = pytube.YouTube(url)

# Get the available video streams and their resolutions
video_streams = yt.streams.filter(type="video").all()
print("Available video streams:")
for i, stream in enumerate(video_streams):
    print(f"{i+1}. Resolution: {stream.resolution}, FPS: {stream.fps}, Type: {stream.mime_type}")

# Ask the user to choose the video quality
while True:
    choice = int(input("Enter the number of the stream you want to download: "))
    if 1 <= choice <= len(video_streams):
        break
    print("Invalid choice. Please enter a number between 1 and", len(video_streams))

# Download the selected video stream
video_streams[choice-1].download()
print("Video downloaded successfully.")
