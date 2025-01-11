import pyaudio
import wave
import subprocess
import time

# تنظیمات ضبط صدا
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
CHUNK = 1024
RECORD_SECONDS = 10
OUTPUT_FILE = "temp_audio.wma"

def record_audio(filename):
    audio = pyaudio.PyAudio()
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)
    
    print("Recording...")
    frames = []
    
    for _ in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
    
    print("Recording stopped.")
    stream.stop_stream()
    stream.close()
    audio.terminate()
    
    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(audio.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))

def transcribe_with_terminal(filename):
    print("Transcribing audio...")
    try:
        # اجرای دستور whisper در ترمینال
        result = subprocess.run(
            ["whisper", filename, "--model", "medium"],
            capture_output=True,
            text=True
        )
        # گرفتن خروجی متن از ترمینال
        return result.stdout
    except Exception as e:
        print(f"Error during transcription: {e}")
        return ""

if __name__ == "__main__":
    try:
        while True:
            record_audio(OUTPUT_FILE)
            transcription = transcribe_with_terminal(OUTPUT_FILE)
            print(f"Transcription:\n{transcription}")
            print("\nListening again in 2 seconds...\n")
            time.sleep(2)  # فاصله برای تکرار ضبط
    except KeyboardInterrupt:
        print("Process terminated by user.")


