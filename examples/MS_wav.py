import azure.cognitiveservices.speech as speechsdk

def from_file():
    speech_config = speechsdk.SpeechConfig(subscription="bc7241a0e4fe4399b447ad7e4a8cb5df", region="eastasia")
    #设置目标语言
    speech_config.speech_recognition_language="zh-CN"
    audio_config = speechsdk.AudioConfig(filename="1.wav")
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

    result = speech_recognizer.recognize_once_async().get()
    print(result.text)

from_file()