import pywhatkit
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound


def text_to_speech(texts):
    print(texts)
    language = "en"
    sound = gTTS(text=texts, lang=language, slow=False)

    # save and play sound from created directory
    sound.save("/Users/mac/PycharmProjects/AI_Project/sounds/sound.mp3")
    playsound("/Users/mac/PycharmProjects/AI_Project/sounds/sound.mp3")


# text_to_speech("hello")


def get_audio():
    while True:
        record = sr.Recognizer()
        with sr.Microphone() as source:
            print("I'm listening")
            playsound("/Users/mac/PycharmProjects/AI_Project/sounds/activate_project.wav")
            speech = record.listen(source)

        voice_text = record.recognize_google(speech)
        print("\tYou said: ", voice_text)

        if "siri" in voice_text.lower():
            text_to_speech("\tHi there. How may I be of service today?")
            playsound("/Users/mac/PycharmProjects/AI_Project/sounds/activate_project.wav")
            voice_text = get_audio()

        return voice_text


text = get_audio()
# get_audio()


while text is None:
    text_to_speech("please repeat yourself")
    text = get_audio()
if text is not None and "youtube" in text.lower():
    text_to_speech("Okay let me look it up on youtube")
    pywhatkit.playonyt(text)

else:
    text_to_speech("Okay let me make a quick search")
    pywhatkit.search(text)
