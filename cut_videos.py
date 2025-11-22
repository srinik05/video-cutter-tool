import os

# ----------- CONFIGURE HERE -------------
input_video = "input.mp4"

# Give time ranges in HH:MM:SS format
# Add as many as you want
clips = [
    ("00:00:00", "00:03:43"),  # Clip 1: 1:00 → 2:30
    ("00:02:15", "00:02:25"),  # Clip 2: 5:00 → 6:15
    ("00:02:50", "00:03:54")   # Clip 3: 10:40 → 12:00
]

output_folder = "output_clips"
# ----------------------------------------

# Create output folder if not exists
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Loop through each clip and cut
for index, (start, end) in enumerate(clips, start=1):
    output_file = f"{output_folder}/clip_{index}.mp4"
    
    cmd = f'ffmpeg -i "{input_video}" -ss {start} -to {end} -c copy "{output_file}"'

    print(f"\nProcessing Clip {index}: {start} → {end}")
    print(cmd)
    os.system(cmd)

print("\nAll clips created successfully! 🎉")
