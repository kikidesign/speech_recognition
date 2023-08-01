#!/usr/bin/env python3

import speech_recognition as sr

# obtain path to "english.wav" in the same folder as this script
from os import path
# AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "chinese.flac")
# AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "french.aiff")
AUDIO_FILE =  "english.wav"

# use the audio file as the audio source
r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source)  # read the entire audio file

# recognize speech using Microsoft Azure Speech
AZURE_SPEECH_KEY = "bc7241a0e4fe4399b447ad7e4a8cb5df"  # Microsoft Speech API keys 32-character lowercase hexadecimal strings
try:
    print("Microsoft Azure Speech thinks you said " + r.recognize_azure(audio, key=AZURE_SPEECH_KEY))
except sr.UnknownValueError:
    print("Microsoft Azure Speech could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Microsoft Azure Speech service; {0}".format(e))


