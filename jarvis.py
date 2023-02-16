from gtts import gTTS
import random
import time
import playsound
import os
from time import sleep
import speech_recognition as sr
import pyautogui

def listen_command():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print("Скажіть команду: ")
		audio = r.listen(source)
	try:
		our_speech = r.recognize_google(audio, language="ru")
		print("Ви: "+our_speech)
		return our_speech
	except sr.UnknownValueError:
		return "error"
	except sr.RequestError:
		return "error"

def do_this_command(message):
	message = message.lower()
	if "джарвис" in message:
		say_message("слухаю")
	elif "открыть текстовый документ" in message:
		os.startfile("C:/Users/User/Desktop/Склад/Jarvis/textdoc.txt")
	elif "пока" in message:
		say_message("бувай")
		exit()
	else:
		print("error")

def say_message(message):
	voice = gTTS(message, lang="ru")
	file_voice_name = "_audio_"+str(time.time())+"_"+str(random.randint(0,100000))+".mp3"
	voice.save(file_voice_name)
	playsound.playsound(file_voice_name)
	print("Jarvis: "+message)
	os.remove(file_voice_name)


if __name__ == "__main__":
	while True:
		command = listen_command()
		do_this_command(command)