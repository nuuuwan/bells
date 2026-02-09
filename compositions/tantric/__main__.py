import os

from pydub import AudioSegment

# Get the path to the temple bell audio file
MEDIA_DIR = os.path.join("common_media")
BELL_PATH = os.path.join(MEDIA_DIR, "temple-bell.mp3")

# Load the temple bell sound
bell = AudioSegment.from_mp3(BELL_PATH)

# Crop bell to 5 seconds
bell = bell[:5000]  # Take only the first 5000 ms (5 seconds)

# Create loud and soft versions
loud_bell = bell + 0  # Original volume
soft_bell = bell - 12  # Reduce volume by 12 dB (softer)

# Build the composition
composition = AudioSegment.empty()

# 10 cycles of: loud bell → 5s silence → soft bell → 5s silence
for i in range(10):
    composition += loud_bell
    composition += soft_bell

# End with loud bell ringing three times
for i in range(3):
    composition += loud_bell

# Export the final composition
output_path = os.path.join("compositions", "tantric", "composition.mp3")
composition.export(output_path, format="mp3")

print(f"Composition created successfully!")
print(f"Output saved to: {output_path}")
print(f"Total duration: {len(composition) / 1000:.1f} seconds")

# Optionally play the composition
# Uncomment the line below to play it automatically
# play(composition)
