import PyPDF2
import sys
from gtts import gTTS
import pyttsx3
from IPython.display import Audio
# Function to extract text from a PDF
def extract_text_from_pdf(file_path):
    with open(file_path, 'rb') as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
    return text

# Get the name of the uploaded file
pdf_file_name = sys.argv[1]

# Extract text from the PDF
pdf_text = extract_text_from_pdf(pdf_file_name)

# Display the first 500 characters of extracted text
# Clean the extracted text by replacing newline characters
cleaned_text = pdf_text.replace('\n', ' ')

# Print a preview of the cleaned text
print("Cleaned Text:\n", cleaned_text[:10000])
print("Extracted Text:\n", pdf_text[:10000])

# Install gTTS for text-to-speech

text_to_convert = cleaned_text
tts = gTTS(text_to_convert, lang='en')
print("Text has been converted to speech")
# Save the converted speech to an audio file
audio_file_name = "audiobook.wav"
tts.save(audio_file_name)

print(f"Audio file has been saved as: {audio_file_name}")

# Play the audio in Colab
Audio(audio_file_name)