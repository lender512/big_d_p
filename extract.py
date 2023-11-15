import os
import whisper
from tqdm import tqdm

# Define the folder where the wav files are located
root_folder = "content"
exit_folder = "output"

# Set up Whisper client
print("Loading whisper model...")
model = whisper.load_model("small")
print("Whisper model complete.")

# Get the number of wav files in the root folder and its sub-folders
print("Getting number of files to transcribe...")
num_files = sum(1 for dirpath, dirnames, filenames in os.walk(root_folder) for filename in filenames if filename.endswith(".wav"))
print("Number of files: ", num_files)

options = whisper.DecodingOptions(language="Spanish")

# Transcribe the wav files and display a progress bar
with tqdm(total=num_files, desc="Transcribing Files") as pbar:
    for dirpath, dirnames, filenames in os.walk(root_folder):
        for filename in filenames:
            print(filename)
            if filename.endswith(".mp3"):
                filepath = os.path.join(dirpath, filename)
                result = model.transcribe(filepath, language="es", fp16=False, verbose=True)
                transcription = result['text']
                # Write transcription to text file
                filename_no_ext = os.path.splitext(filename)[0]
                with open(os.path.join(exit_folder, filename_no_ext + '.txt'), 'w') as f:
                    f.write(transcription)
                pbar.update(1)