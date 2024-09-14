import os
import logging
from lyrics_transcriber import LyricsTranscriber

# Set up
audio_file = "audios/sss.mp3"
output_dir = "./output"
log_level = logging.DEBUG 
transcription_model = "medium"
render_video = True
video_resolution = "720p"


os.makedirs(output_dir, exist_ok=True)

try:
    # Create instancw
    transcriber = LyricsTranscriber(
        audio_filepath=audio_file,
        output_dir=output_dir,
        log_level=log_level,
        transcription_model=transcription_model,
        render_video=render_video,
        video_resolution=video_resolution
    )

    result_metadata = transcriber.generate()

    print("Transcription completed. Results:")
    for key, value in result_metadata.items():
        print(f"{key}: {value}")

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")