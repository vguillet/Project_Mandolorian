
##################################################################################################################
"""

"""

# Built-in/Generic Imports

# Libs
import speech_recognition as sr
import pyttsx3
from gtts import gTTS
import playsound

# Own modules

__version__ = '1.1.1'
__author__ = 'Victor Guillet'
__date__ = '10/09/2019'

##################################################################################################################


class Kortex:
    def __init__(self, gender="male", language="en"):
        gender_ref_voice = {"male": "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0",
                            "female": "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"}
        self.gender_ref = gender_ref_voice[gender]

        self.language = language

        # --> Define initialisation message
        # self.speak("Korrtex version 1 online. Ready to receive instructions!")

    def speak(self, text):
        # --> Use gTTS for speech synthesis
        tts = gTTS(text=text, lang=self.language)
        filename = 'voice.mp3'
        tts.save(filename)
        playsound.playsound(filename)

        # --> Use pyttsx3 for speech synthesis
        # engine = pyttsx3.init()
        # engine.setProperty('voice', self.gender_ref)
        # engine.say(text)
        # engine.runAndWait()

    def get_audio(self):
        """
        Fetch audio from microphone
        :return: Audio converted to text
        """
        r = sr.Recognizer()

        with sr.Microphone() as source:
            # --> Initiating ambient noise sample for filtering
            r.adjust_for_ambient_noise(source, duration=0.5)

            # --> Recording voice input
            print("Listening...")
            audio = r.listen(source)
            print("Processing voice")
            said = ""

            # --> Attempting to convert audio to text
            try:
                said = r.recognize_google(audio)
                print(said, "")
            except Exception as e:
                print("Exception: " + str(e))
        return said


if __name__ == "__main__":
    kortex = Kortex()
    kortex.get_audio()


LANGUAGES={
    'af':'Afrikaans',
    'sq':'Albanian',
    'ar':'Arabic',
    'hy':'Armenian',
    'bn':'Bengali',
    'ca':'Catalan',
    'zh-cn':'Chinese (Mandarin/China)',
    'zh-tw':'Chinese (Mandarin/Taiwan)',
    'zh-yue':'Chinese (Cantonese)',
    'hr':'Croatian',
    'cs':'Czech',
    'da':'Danish',
    'nl':'Dutch',
    'en':'English',
    'en-au':'English (Australia)',
    'en-uk':'English (United Kingdom)',
    'en-us':'English (United States)',
    'eo':'Esperanto',
    'fi':'Finnish',
    'fr':'French',
    'de':'German',
    'el':'Greek',
    'hi':'Hindi',
    'hu':'Hungarian',
    'is':'Icelandic',
    'id':'Indonesian',
    'it':'Italian',
    'ja':'Japanese',
    'ko':'Korean',
    'la':'Latin',
    'lv':'Latvian',
    'mk':'Macedonian',
    'no':'Norwegian',
    'pl':'Polish',
    'pt':'Portuguese',
    'pt-br':'Portuguese (Brazil)',
    'ro':'Romanian',
    'ru':'Russian',
    'sr':'Serbian',
    'sk':'Slovak',
    'es':'Spanish',
    'es-es':'Spanish (Spain)',
    'es-us':'Spanish (United States)',
    'sw':'Swahili',
    'sv':'Swedish',
    'ta':'Tamil',
    'th':'Thai',
    'tr':'Turkish',
    'vi':'Vietnamese',
    'cy':'Welsh'
}