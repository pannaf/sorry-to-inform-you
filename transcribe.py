import whisper


def main():
    model = whisper.load_model("base")
    result = model.transcribe("ariana.mp3")
    print(result["text"])


if __name__ == "__main__":
    main()
