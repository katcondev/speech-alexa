import speech_recognition as sr

# mic_list = sr.Microphone.list_microphone_names()

# for i, microphone_name in enumerate(mic_list):
#     if "Microphone" in microphone_name:
#         print(f"Microphone with name '{microphone_name}' has index {i}")


r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something")
    audio = r.listen(source)
    voice_data = r.recognize_google(audio)
    print(voice_data)
