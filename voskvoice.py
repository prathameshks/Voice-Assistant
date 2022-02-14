import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import sys
# from google import auth
from tkinter import *

Faizan_root = Tk()
Faizan_root.geometry("300x400")
Faizan_root.title("JARVIS AI by Faizan Jallani")

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
	engine.say(audio)
	engine.runAndWait()

def wishMe():
	hour = int(datetime.datetime.now().hour)
	if hour>=0 and hour<12:
		speak("Good Morning!")
	elif hour>=12 and hour<18:
		speak("Good Afternoon!")
	else:
		speak("Good Evening!")

	speak("I am JARVIS. How may I help you Sir?")



def takeCommand():
	r = sr.Recognizer()
	with sr.Microphone () as source:
		print("Listening...")
		r.pause_threshold = 1
		r.adjust_for_ambient_noise(source, duration=1)
		audio = r.listen(source)

	try:
		print("Recognizing...")
		query = r.recognize_google(audio, language='en-in')
		print(f"User said: {query}\n")

	except Exception as e:
		# print(e)
		speak("Say that again please...")
		return"None"
	return query


if __name__ == '__main__':
	wishMe()
	while True:
		query = takeCommand().lower()
		# Logic for executing tasks based on query.
		if 'wikipedia' in query:
			speak('Searching Wikipedia...')
			query = query.replace("wikipedia", "")
			results = wikipedia.summary(query, sentences=2 )
			speak("According to Wikipedia")
			print(results)
			speak(results)

		elif 'open youtube' in query:
			webbrowser.open("https://www.youtube.com/", new=2)
			speak("Enjoy")

		elif 'open google' in query:
			webbrowser.open("https://www.google.com/", new=2)

		elif 'open stack overflow' in query:
			webbrowser.open("https://stackoverflow.com/", new=2)

		elif 'play music' in query:
			music_dir = 'F:\\songs\\Favorite'
			songs = os.listdir(music_dir)
			print(songs)
			os.startfile(os.path.join(music_dir, songs[0]))

		elif 'the time' in query:
			strTime = datetime.datetime.now().strftime("%H:%M:%S")
			speak(f"Sir, the time is {strTime}")

		elif 'open code' in query:
			codePath = "C:\\Users\\Faizan\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
			os.startfile(codePath)

		elif 'open facebook' in query:
			webbrowser.open("https://www.facebook.com/", new=2)

		elif 'instagram' in query:
			webbrowser.open("https://www.instagram.com/faizangujjar01/", new=2)
			speak("Have a look sir")

		elif 'are you there' in query:
			stMsgs = ['At you service, Sir']
			speak(stMsgs)

		elif 'what is' in query:
			speak('Searching Wikipedia...')
			query = query.replace("wikipedia", "")
			results = wikipedia.summary(query, sentences=2)
			speak("According to Wikipedia")
			print(results)
			speak(results)

		elif 'search for' in query:
			speak('Searching Wikipedia...')
			query = query.replace("wikipedia", "")
			results = wikipedia.summary(query, sentences=2)
			speak("According to Wikipedia")
			print(results)
			speak(results)



		elif 'shutdown the PC' in query:
			choice = input("Please confirm to shutdown the pc (y or n)")
			if choice == 'n':
				exit()
			else:
				os.system("shutdown /s /t 1")

		elif 'exit' in query:
			sys.exit(speak("Ok sir, Take Care."))


Faizan_root.mainloop()  



"""canvas = tk.Canvas(container)
scrollbar = tk.Scrollbar(container, orient="vertical", command=canvas.yview)
scrollable_frame = tk.Frame(canvas)

scrollable_frame.bind("<Configure>",lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

canvas.create_window((0, 0), window=scrollable_frame, anchor="center")

canvas.configure(yscrollcommand=scrollbar.set)

for i in range(50):
	if i/2==0:
		tk.Label(scrollable_frame, text="Sample scrolling label"+str(i)).grid(row=i,column=0,sticky="w")
	else:
		tk.Label(scrollable_frame, text="Sample scrolling label"+str(i)).grid(row=i,column=1,sticky="e")

container.pack()
canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")
"""




# # import os
# # listp=os.listdir(r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2013")
# path="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office 2013\\"
# l=['Excel 2013.lnk', 'OneNote 2013.lnk', 'Outlook 2013.lnk', 'PowerPoint 2013.lnk', 'Publisher 2013.lnk', 'SkyDrive Pro 2013.lnk', 'Word 2013.lnk']
# for i in l:
# 	a=str(i[0:-4]).replace(" ", "_")
# 	b=str(i[0:-4])
# 	c=path+i
# 	# print(f"def open_{a}():\n\tspeak(\"ok opening {b}\")\n\tos.startfile(r'{c}')")
# 	print(f"\"open_{a}\",",end="")

# text0=""
# text1=""
# text2=""
# text3=""
# ctext1=""
# ctext2=""
# ctext3=""
# ctext4=""
# ctext5=""
# root.columnconfigure(0,weight=1)
# root.columnconfigure(1,weight=1)
# root.rowconfigure(0,weight=1)
# root.rowconfigure(1,weight=1)
# root.rowconfigure(2,weight=1)
# root.rowconfigure(3,weight=1)
# root.rowconfigure(4,weight=1)
# root.rowconfigure(5,weight=1)
# root.rowconfigure(6,weight=1)
# root.rowconfigure(7,weight=1)
# root.rowconfigure(8,weight=1)

# client1=tk.Label(root,text=text3,bg=color,wraplength=175)
# client1.grid(row=1,column=1,sticky="nsew")
# client2=tk.Label(root,text=text2,bg=color,wraplength=175)
# client2.grid(row=3,column=1,sticky="nsew")
# client3=tk.Label(root,text=text1,bg=color,wraplength=175)
# client3.grid(row=5,column=1,sticky="nsew")
# client4=tk.Label(root,text=text0,bg=color,wraplength=175)
# client4.grid(row=7,column=1,sticky="nsew")


# comp1=tk.Label(root,text=ctext5,bg=color,wraplength=175)
# comp1.grid(row=0,column=0,sticky="nsew")
# comp2=tk.Label(root,text=ctext4,bg=color,wraplength=175)
# comp2.grid(row=2,column=0,sticky="nsew")
# comp3=tk.Label(root,text=ctext3,bg=color,wraplength=175)
# comp3.grid(row=4,column=0,sticky="nsew")
# comp4=tk.Label(root,text=ctext2,bg=color,wraplength=175)
# comp4.grid(row=6,column=0,sticky="nsew")
# comp5=tk.Label(root,text=ctext1,bg=color,wraplength=175)
# comp5.grid(row=8,column=0,sticky="nsew")

# def updatetextclient(new):
# 	global text0
# 	global text1
# 	global text2
# 	global text3
# 	text3=text2
# 	text2=text1
# 	text1=text0
# 	text0=new
# 	client1.config(text=text3)
# 	client2.config(text=text2)
# 	client3.config(text=text1)
# 	client4.config(text=text0)
# def updatetextcomp(cnew):
# 	global ctext1
# 	global ctext2
# 	global ctext3
# 	global ctext4
# 	global ctext5
# 	ctext5=ctext4
# 	ctext4=ctext3
# 	ctext3=ctext2
# 	ctext2=ctext1
# 	ctext1=cnew
# 	comp1.config(text=ctext5)
# 	comp2.config(text=ctext4)
# 	comp3.config(text=ctext3)
# 	comp4.config(text=ctext2)
# 	comp5.config(text=ctext1)
