from ocr.ocr_extraction import extract_text_from_image
from sentiment.analyze_sentiment import get_emotion
from music.music_recommender import recommend_music

def main():
    image_path = input("Enter path to image: ")


    text = extract_text_from_image(image_path)
    print("\nExtracted Text:")
    print(text)
    print()


    emotion = get_emotion(text)
    print(f"Detected Emotion: {emotion}\n")


    songs = recommend_music(emotion)
    print("Recommended Songs:")
    for song in songs:
        print(f"- {song}")

if __name__ == "__main__":
    main()
