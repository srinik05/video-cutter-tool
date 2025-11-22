# video-cutter-tool

✂️ Video Cutter Tool (Python + FFmpeg)

A simple, fast, and flexible video clip extractor built using Python and FFmpeg.
This script lets you generate multiple clips from any video by providing time ranges in HH:MM:SS format.

🚀 Features

Extract multiple clips from a single video
Define unlimited (start, end) time ranges
Super-fast cutting using -c copy (no re-encoding)
Output clips saved automatically
Fully customizable

🛠 Technologies Used
Python 3
FFmpeg (for cutting video)
os module (script execution)

📦 Installation
1️⃣ Install Python
https://www.python.org/downloads/

2️⃣ Install FFmpeg
Download FFmpeg:
https://ffmpeg.org/download.html

Windows Steps:
Download FFmpeg ZIP
Extract it
Add the bin/ folder to System PATH

Verify using:
ffmpeg -version
▶ Running the Script
Run this command in your terminal:
python cut_videos.py

🧠 How It Works (Execution Flow)
You specify:
Input video file
List of (start_time, end_time) clip ranges
Output folder name
Script loops through each time range
For each clip, an FFmpeg command is generated:

ffmpeg -i input.mp4 -ss <start> -to <end> -c copy output_clip.mp4


Each clip is saved inside:

output_clips/
   ├── clip_1.mp4
   ├── clip_2.mp4
   ├── clip_3.mp4

📂 Project Structure
video-cutter/
│
├── cut_videos.py        # Script to extract clips
├── input.mp4            # Your video file (you provide)
├── output_clips/        # Automatically created
└── README.md

📝 Configuration Inside Script
Example clip configuration:
clips = [
    ("00:00:00", "00:03:43"),
    ("00:02:15", "00:02:25"),
    ("00:02:50", "00:03:54")
]


You can add unlimited clips.

🧪 Example FFmpeg Command Used
ffmpeg -i "input.mp4" -ss 00:00:00 -to 00:03:43 -c copy "output_clips/clip_1.mp4"


-c copy → no re-encoding (very fast)
-ss → start time
-to → end time

⚠ Important Notes
input.mp4 must be placed in the same folder as the script (or use a full path).
Time format must be HH:MM:SS.
FFmpeg must be installed and added to PATH.
Output folder is created automatically if not present.