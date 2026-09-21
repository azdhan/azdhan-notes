# Auto-transcription trigger for audio attachments (>5 min)
# Runs on-device Whisper when file arrives; outputs transcript to long notes folder.
import os, subprocess

def transcribe_audio(file_path: str) -> str:
    # Placeholder: call whisper CLI / python-whisper on device
    result = subprocess.run(["whisper", file_path, "--language", "en", "--output_dir", "A:/Azdhanvibing/azdhan-notes/content/azent-notes-tg/long notes by azent"], capture_output=True, text=True)
    return result.stdout
