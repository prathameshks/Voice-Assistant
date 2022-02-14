import speech_recognition as s_r
import pyttsx3
import math
import webbrowser
import os
import wolframalpha
import wikipedia
import tkinter as tk
root=tk.Tk()
color="white"

root.geometry("70x70+1280+650")
root.config(bg=color)
root.columnconfigure(0,weight=1)
root.rowconfigure(0,weight=1)
root.overrideredirect(1)
root.attributes("-topmost",True)
sor,term=0,None
open_fns=["open_youtube","open_chrome","open_python","open_control_panel","open_Command_Prompt","open_File_Explorer","open_this_pc","open_Windows_Administrative_Tools","open_Windows_PowerShell","open_Magnifier","open_Narrator","open_On_Screen_Keyboard","open_Notepad","open_Internet_Explorer","open_my_sql","open_Access","open_Acrobat_Reader","open_Adobe_Photoshop","open_BlueStacks","open_Excel","open_Firefox","open_Google_Chrome","open_Microsoft_Edge","open_Notepad_plus_plus","open_Outlook","open_PowerPoint","open_Publisher","open_Skype_for_Business","open_Sublime_Text","open_Word","open_Excel_2013","open_OneNote_2013","open_Outlook_2013","open_PowerPoint_2013","open_Publisher_2013","open_SkyDrive_Pro_2013","open_Word_2013","open_pycharm","open_teams","open_microsoft_teams"]
main_fns=["sorry","end"]
# def startalways():
# 	try:
# 		r = s_r.Recognizer()
# 		my_mic = s_r.Microphone(device_index=1)
# 		with my_mic as source:
# 			r.adjust_for_ambient_noise(source)
# 			audio = r.listen(source)
# 			goten=r.recognize_google(audio)
# 			return goten
# 	except:
# 		pass
def speak(textmain):
	try:
		vf=open("voice.txt","r")
		voice=int(vf.read(1))
		vf.close()
		if voice not in(0,1):
			1/0
	except:
		vf=open("voice.txt","w")
		vf.write('1')
		voice=1
		vf.close()
	vp=voice
	engine = pyttsx3.init() # object creation
	engine.setProperty('rate', 150)	 # setting up new voice rate
	engine.setProperty('volume',3.0)	# setting up volume level  between 0 and 1
	voices = engine.getProperty('voices')
	engine.setProperty('voice', voices[vp].id)   #changing index, changes voices. o for male, 1 for female
	print(textmain)
	# updatetextcomp(str(textmain))	
	try:
		engine.say(textmain)
		# engine.save_to_file('Hello World', 'test.mp3')
		engine.runAndWait()
		engine.stop()
		return True
	except:
		engine.say("Something went wrong.")
		engine.runAndWait()
		engine.stop()
		return False

def listen():
	r = s_r.Recognizer()
	# #print(s_r.Microphone())
	my_mic = s_r.Microphone(device_index=1) #my device index is 1, you have to put your device index
	with my_mic as source:
		r.adjust_for_ambient_noise(source, duration=2) #reduce noiseadjust_for_ambient_noise(source, duration=1)
		print("listening")
		# updatetextcomp(str('listening'))
		audio = r.listen(source) #take voice input from the microphone
	try: 
		goten=r.recognize_google(audio, language='en-in') #to #print voice into text
		print("\t\t\t\t"+goten)
		# updatetextclient(str(goten))
		return goten
	except:
		return "sorry"

def match(listened,mainfns=main_fns,openfns=open_fns):
	global term
	global listenedw
	greets=["greet","hi","good morning","good night","how are you","i am fine","whats up","good day","good evening"]
	listenedw=listened.lower()
	words=listenedw.split(" ")
	if listenedw in ["close","quit","exit","stop","stop listening"]:
		return "end"
	elif listenedw in greets:
		# greet
		greetresp=["Hello","hi","good morning,have a good day","ok good night, sweet dreams","I am fine, tell about you","ok, what can i do for you?","everything cool","same to you","good evening"]
		global greeting
		greeting=greetresp[greets.index(listenedw)]
		return "greet"
	elif listenedw in ["change voice","change your voice"]:
		return 'changev'
	elif words[0].lower() in ["information","search","find"]:
		global wikidata
		wikidata=str(listenedw[int(len(words[0])+1):])
		return 'searchwiki'
	elif words[0].lower() in ["open"]:
		bestfn="False"
		for fn in openfns:
			i=fn.lower()
			fnwords=i.split("_")
			matches=0
			for j in words:
				if j in fnwords:
					matches+=1
			if matches>=math.ceil(len(words)):
				bestfn=fn
		if bestfn=="False":
			global term
			term=str(listenedw[5:])
			return "webopen"
		else:
			return bestfn
	else:
		bestfn="False"
		for fn in mainfns:
			i=fn.lower()
			fnwords=i.split("_")
			matches=0
			for j in words:
				if j in fnwords:
					matches+=1
			if matches>=math.ceil(len(words)):
				bestfn=fn
		if bestfn=="False":
			return "tell"
		else:
			return bestfn

def end():
	speak("ok good bye")
	exit()
def greet():
	speak(greeting)
def searchwiki():
	speak('Searching Wikipedia...')
	results = wikipedia.summary(wikidata, sentences=2 )
	speak("According to Wikipedia")
	speak(results)
def search(question):
	app_id = '6LJUGL-QGQXA75X53'
	client = wolframalpha.Client(app_id)
	res = client.query(question)
	if res['@success']=='true':
		pod0=res['pod'][0]['subpod']['plaintext']
		if (question.lower()).startswith("tell"):
			data="ok\n"
		else:
			data=str(pod0+"\n")
		pod1=res['pod'][1]
		if (('definition' in pod1['@title'].lower()) or ('result' in  pod1['@title'].lower()) or (pod1.get('@primary','false') == 'true')):
			result = pod1['subpod']['plaintext']
			data+=str(result)
		return data
	else:
		data=str("can't get information.")
		# sorry()
		return data
def tell():
	speak("ok finding that on web")
	data=search(listenedw)
	speak(data)
	
def changev():
	try:
		vf=open("voice.txt","r")
		voice = int(vf.read(1))
		vf.close()
		if voice not in(0,1):
			1/0
	except:
		vf=open("voice.txt","w")
		vf.write('1')
		voice=1
		vf.close()

	vf=open("voice.txt","w")
	if voice==1:
		vf.write('0')
		speak("voice changed to male.")
	elif voice==0:
		vf.write("1")
		speak("voice changed to female.")
	vf.close()
def sorry():
	global sor
	sor+=1
	if sor>3:
		exit()
	speak("Sorry i didn't get that.")
def webopen():
	speak(f"ok serching web for {term}")
	chromedir= 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
	url = "https://www.google.com.tr/search?q={}".format(term)
	webbrowser.get(chromedir).open_new(url) 
	
def open_youtube():
	speak("ok opening youtube on chrome")
	chromedir= 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
	webbrowser.get(chromedir).open_new("http://youtube.com") 
	
def open_chrome():
	speak("ok opening chrome")
	os.startfile(r'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe')

def open_pycharm():
	speak("ok opening Pycharm")
	os.startfile(r'D:\New folder\PyCharm Community Edition 2019.2.2\bin\pycharm64.exe')

def open_teams():
	speak("ok opening microsoft teams")
	os.startfile(r'C:\Users\ADMIN\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Microsoft Teams.lnk')

def open_microsoft_teams():
	speak("ok opening microsoft teams")
	os.startfile(r'C:\Users\ADMIN\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Microsoft Teams.lnk')

def open_python():
	speak("ok opening python IDLE")
	os.startfile(r'C:\Users\ADMIN\AppData\Local\Programs\Python\Python38\Lib\idlelib\idle.pyw')
	
def open_control_panel():
	speak("ok opening Control Panel")
	os.startfile(r'C:\Users\ADMIN\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\System Tools\Control Panel.lnk')
	
def open_Command_Prompt():
	speak("ok opening Command Prompt")
	os.startfile(r'C:\Users\ADMIN\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\System Tools\Command Prompt.lnk')
	
def open_File_Explorer():
	speak("ok opening File Explorer")
	os.startfile(r'C:\Users\ADMIN\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\System Tools\File Explorer.lnk')
	
def open_this_pc():
	speak("ok opening This PC")
	os.startfile(r'C:\Users\ADMIN\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\System Tools\File Explorer.lnk')
	
def open_Windows_Administrative_Tools():
	speak("ok opening Windows Administrative Tools")
	os.startfile(r'C:\Users\ADMIN\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\System Tools\Windows Administrative Tools.lnk')
	
def open_Windows_PowerShell():
	speak("ok opening Windows PowerShell")
	os.startfile(r'C:\Users\ADMIN\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Windows PowerShell\Windows PowerShell.lnk')
	
def open_Magnifier():
	speak("ok starting Magnifier")
	os.startfile(r'C:\Users\ADMIN\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Accessibility\Magnifier.lnk')
	
def open_Narrator():
	speak("ok starting Narrator")
	os.startfile(r'C:\Users\ADMIN\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Accessibility\Narrator.lnk')
	
def open_On_Screen_Keyboard():
	speak("ok starting On Screen Keyboard")
	os.startfile(r'C:\Users\ADMIN\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Accessibility\On-Screen Keyboard.lnk')
	
def open_Notepad():
	speak("ok opening Notepad")
	os.startfile(r'C:\Users\ADMIN\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Accessories\Notepad.lnk')
	
def open_Internet_Explorer():
	speak("ok opening Internet Explorer")
	os.startfile(r'C:\Users\ADMIN\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Accessories\Internet Explorer.lnk')
	
def open_my_sql():
	speak("ok opening my sql")
	os.startfile(r'C:\Users\ADMIN\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\MySQL\MySQL Server 5.5\MySQL 5.5 Command Line Client.lnk')
	
def open_Access():
	speak("ok opening Access")
	os.startfile(r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Access.lnk')
	
def open_Acrobat_Reader():
	speak("ok opening Acrobat Reader DC")
	os.startfile(r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Acrobat Reader DC.lnk')
	
def open_Adobe_Photoshop():
	speak("ok opening Adobe Photoshop")
	os.startfile(r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Adobe Photoshop 7.0.lnk')
	
def open_BlueStacks():
	speak("ok opening BlueStacks")
	os.startfile(r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\BlueStacks.lnk')
	
def open_Excel():
	speak("ok opening Excel")
	os.startfile(r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Excel.lnk')
	
def open_Firefox():
	speak("ok opening Firefox")
	os.startfile(r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Firefox.lnk')
	
def open_Google_Chrome():
	speak("ok opening Google Chrome")
	os.startfile(r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Google Chrome.lnk')
	
def open_Microsoft_Edge():
	speak("ok opening Microsoft Edge")
	os.startfile(r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Edge.lnk')
	
def open_Notepad_plus_plus():
	speak("ok opening Notepad++")
	os.startfile(r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Notepad++.lnk')
	
def open_Outlook():
	speak("ok opening Outlook")
	os.startfile(r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Outlook.lnk')
	
def open_PowerPoint():
	speak("ok opening PowerPoint")
	os.startfile(r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\PowerPoint.lnk')
	
def open_Publisher():
	speak("ok opening Publisher")
	os.startfile(r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Publisher.lnk')
	
def open_Skype_for_Business():
	speak("ok opening Skype for Business")
	os.startfile(r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Skype for Business.lnk')
	
def open_Sublime_Text():
	speak("ok opening Sublime Text")
	os.startfile(r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Sublime Text 3.lnk')
	
def open_Word():
	speak("ok opening Word")
	os.startfile(r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Word.lnk')

def open_Excel_2013():
	speak("ok opening Excel 2013")
	os.startfile(r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2013\Excel 2013.lnk')
def open_OneNote_2013():
	speak("ok opening OneNote 2013")
	os.startfile(r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2013\OneNote 2013.lnk')
def open_Outlook_2013():
	speak("ok opening Outlook 2013")
	os.startfile(r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2013\Outlook 2013.lnk')
def open_PowerPoint_2013():
	speak("ok opening PowerPoint 2013")
	os.startfile(r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2013\PowerPoint 2013.lnk')
def open_Publisher_2013():
	speak("ok opening Publisher 2013")
	os.startfile(r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2013\Publisher 2013.lnk')
def open_SkyDrive_Pro_2013():
	speak("ok opening SkyDrive Pro 2013")
	os.startfile(r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2013\SkyDrive Pro 2013.lnk')
def open_word_2013():
	speak("ok opening Word 2013")
	os.startfile(r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2013\Word 2013.lnk')

#last
def run(function):
	exec(str(function+"()"))
def start():
	data=listen()
	fnte=match(data)
	run(fnte)
def exitall():
	root.destroy()
	exit()
# def minmize():
# 	root.withdraw()
tk.Button(root,text="\n\nStart\n",command=start,bg="black",fg="white").grid(row=0,rowspan=2,column=0,padx=0,pady=0,sticky="nsew")
tk.Button(root,text="X",command=exitall,bg="red",fg="white").grid(row=0,column=0,padx=0,pady=0,sticky="ne")
# tk.Button(root,text="_",command=minmize,bg="red",fg="white").grid(row=0,column=0,padx=20,pady=0,sticky="ne")

root.mainloop()