from ctypes.wintypes import MSG
from re import X
import keyboard
from numpy.core.fromnumeric import take
from pyttsx3 import engine
import pyttsx3
import pyautogui
import speech_recognition as sr
import datetime
from bs4 import BeautifulSoup
from playsound import playsound
from googletrans import Translator
from time import ctime
from wikipedia import *
import webbrowser
from audioop import *
from gtts import gTTS
import pywhatkit
from pywikihow import search_wikihow
import os
import cv2
import winsound
import PyPDF2
from tkinter import *
from tkinter.filedialog import *
from pytube import YouTube
from PIL import ImageGrab
import numpy as np
from win32api import GetSystemMetrics


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
cam=cv2.VideoCapture(0)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def  wishMe():
    hour= int(datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<16:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("How may I help you")
  
def takeCommand():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        speak("Processing your Requirements,sir!")
        query=r.recognize_google(audio,language='en-in')
        
    except Exception as e:
        speak("Sir please say again...")
        return "None"
    


def TaskExe(): 
    pyautogui.press('esc')
    speak("Verification Succesful")
    speak("Welcome back, Sir")
    wishMe() 
   

    
    def TakeHindi():
        r= sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)
    
        try:
            print("Recognizing...")
            query=r.recognize_google(audio,language='hi')
            
        except sr.UnknownValueError:
            speak("Sir please say again...")
            return "None"
        return query
    def Trans():
        speak("Tell me the line sir!")
        line = TakeHindi()
        translate = Translator()
        result = translate.translate(line)
        Text = result.text
        speak("Sir,The translation For This Line Is" + Text)
        print("The translation For This Line Is: " + Text)
    def Temp():
        search= takeCommand()
        url = f"https://www.google.com/search?q={search}"
        search=search.replace("Find","")
        search=search.replace("the temprature","")
        search=search.replace("in","")
        r = requests.get(url)
        data = BeautifulSoup(r.text,"html.parser")
        temprature = data.find("div", class_ ="BNeawe").text
        speak("The Temprature in {search} is {temrature} celsius")
    def Reader():
        speak("Tell Me The Name of Book,Sir!")
        name = takeCommand()

        if 'india' in name:
            book= askopenfilename()
            pdfReader = PyPDF2.PdfFileReader(book)
            pages = pdfReader.getNumPages()
            speak(f"Total number of pages are {pages}")
            speak("From which page should I start reading sir?")
            numPage=int(input("Enter the page number sir: "))
            page=pdfReader.getPage(numPage)
            text = page.extarctText()
            speak("In which language should I Read?")
            lang=takeCommand()
            if 'hindi' in lang:
                transl=Translator()
                textHin = transl.translate(text,'hi')
                textm = textHin.text
                speech = gTTS(text = textm)
                try:
                    speech.save('book.mp3')
                    playsound('book.mp3')
                except:
                    playsound('book.mp3')
            
            else:
                speak(text)
        if 'europe' in name:
            book= askopenfilename()
            pdfReader = PyPDF2.PdfFileReader(book)
            pages = pdfReader.getNumPages()
            speak(f"Total number of pages are {pages}")
            speak("Sir please enter the page from where I should start reading.")
            numPage=int(input("Enter the page number sir: "))
            page=pdfReader.getPage(numPage)
            text = page.extarctText()
            speak("In which language should I Read?")
            lang=takeCommand()
            if 'hindi' in lang:
                transl=Translator()
                textHin = transl.translate(text,'hi')
                textm = textHin.text
                speech = gTTS(text = textm)
                try:
                    speech.save('book.mp3')
                    playsound('book.mp3')
                except:
                    playsound('book.mp3')
            
            else:
                speak(text)
    def SpeedTest():
        import speedtest
        speak("Cheking speed..,Sir!")
        speed=speedtest.Speedtest()
        downloading=speed.download()
        correctDown = int(downloading/800000)
        uploading = speed.upload()
        correctUpload= int(uploading/800000)
        if 'uploading' in query:
            speak("Sir,The uploading speed is {correctUpload} mbp s")
        elif 'downloading' in query:
            speak("Sir,The downloading speed is {correctDown} mbp s")
        else:
            speak("Sir,The Downloading speed is {correctDown} mbp s and Uploading speed is {correctUpload} mbp s")
                  
    while True:
            query=takeCommand().lower()
             
            if 'jarvis' in query:
                query=query.replace("jarvis","")
            elif 'yourself' in query:
                speak('My name is Jarvis,sir!, I am Your Personal AI assistant.')
            elif 'open wiki' in query:
                webbrowser.open("wikipedia.com")
            elif 'Tell me about' in query:
                speak('Searching Wikipedia...Please Wait!')
                query= query.replace("wikipedia","")
                results= wikipedia.summary(query, sentences=4)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            elif 'google search' in query:
                import wikipedia as googleScrap
                query =query.replace("google search","")
                query=query.replace("jarvis","")
                query =query.replace("google","")
                speak("This is what I found on web,sir!")
                pywhatkit.search(query)
                try:
                    pywhatkit.search(query)
                    result= googleScrap.summary(query,3)
                    speak(result)
                except:
                    speak("No Data Found,Sir!")
            elif 'find my location' in query:
                speak('Ok sir, Wait a second!')
                webbrowser.open("https://www.google.com/search?q=check+my+location&rlz=1C1VDKB_enIN958IN958&oq=check+my+lo&aqs=chrome.3.69i57j0l9.9033j0j7&sourceid=chrome&ie=UTF-8")
            elif 'video downloader' in query:
                root = Tk()
                root.geometry('500x300')
                root.resizable(0,0)
                root.title("Youtube Video Downloader")
                speak("Enter the URL Here,Sir!")

                Label(root,text="Youtube Video Downloader",font='arial 15 bold').pack()
                link = StringVar()
                Label(root,text="Paste your Youtube URL Here ",font='arial 15 bold').place(x=160,y=60)
                Entry(root,width = 70,textvariable= link).place(x=32,y=90)

                def VideoDownloader():
                    url=YouTube(str(link.get()))
                    video=url.streams.first()
                    video.download("C:\\Users\\Bhawesh\\Desktop\\Pyhton Project\\jarvis\\youtube video downloader")
                    Label(root,text="Downloaded",font='arial 15').place(x=180,y=210)

                Button(root,text= "Download",font = 'arial 15 bold',bg='navy blue',padx= 2,command= VideoDownloader).place(x=180,y=150)

                root.mainloop()
                speak("Video downloaded,Sir!")
            elif 'location' in query:
                query=query.replace('Find location of','')
                speak("Finding the location" + query)
                url= 'https://google.nl/maps/place/' + query + '/&amp;'
            
                webbrowser.get().open(url)
            elif 'open youtube' in query:
                    webbrowser.open("youtube.com")
            elif 'youtube' in query:
                speak("What's your command,sir ?")
                command = takeCommand()
                
                if 'pause' in command:
                    keyboard.press('space bar')
                elif 'restart' in command:
                    keyboard.press('0')
                elif 'mute' in command:
                    keyboard.press('m')
                elif 'skip' in command:
                    keyboard.press('l')
                elif 'back' in command:
                    keyboard.press('j')  
                elif 'fullscreen' in command:
                    keyboard.press('f')
                elif 'film mode' in command:
                    keyboard.press('t')
                elif 'increase volume' in command:
                    keyboard.press('up')
                elif 'decrease volume' in command:
                    keyboard.press('down')
                speak("Done sir!")  
            elif 'website' in query:
                speak("Ok sir, Wait a second!")
                query= query.replace("website","")
                query=query.replace("jarvis","")
                query=query.replace(" ","")
                web1=query.replace("open","")
                web2= 'https://www.'+ web1 + '.com'
                webbrowser.open(web2)
                speak("Website Opened,Sir!")
            elif 'close' in query:
                speak('sir,please wait a second!')
                speak("Sir, which program should I close?")
                if 'youtube' in query:
                    os.system("TASKKILL /f /im chrome.exe")
                elif 'chrome' in query:
                    os.system("TASKKILL /f /im chrome.exe")
                elif 'whatsapp' in query:
                    os.system("TASKKILL /f /im WhatsApp.exe")
                elif 'vs code' in query:
                    os.system("TASKKILL /f /im Code.exe")
                speak("All the requested programs are closed,sir!")
            elif 'open google' in query:
                webbrowser.open("google.com")
            elif 'open stack overflow' in query:
                webbrowser.open("stackoverflow.com")
            elif 'open lecture notes' in query:
                webbrowser.open("lecturenotes.in")
            elif 'open whatsapp' in query:
                mk= "C:\\Users\\Bhawesh\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
                os.startfile(mk)
            elif 'open vs code' in query:
                ph= "C:\\Users\\Bhawesh\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(ph)
            elif 'play some song' in query:
                speak("Which song should I play Sir!")
                song=query.replace('play','')
                speak("Playing song" + song)
                pywhatkit.playonyt(song)
            elif 'play' in query:
                song=query.replace('play','')
                speak("Playing song" + song)
                pywhatkit.playonyt(song)
            elif 'time' in query:
                time = query.replace('Tell me the','')
                speak(ctime())
                print(ctime())
            elif 'capture video' in query:
                while cam.isOpened():
                    ret, frame1=cam.read()
                    ret, frame2=cam.read()
                    diff= cv2.absdiff(frame1, frame2)
                    gray =cv2.cvtColor(diff, cv2.COLOR_RGB2GRAY)
                    blur= cv2.GaussianBlur(gray, (5,5), 0)
                    _, thresh=cv2.threshold(blur,20,255, cv2.THRESH_BINARY)
                    dilated= cv2.dilate(thresh, None, iterations=3)
                    contours ,_=cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
                    for c in contours:
                        if cv2.contourArea(c) <5000:
                            continue
                        x,y,w,h = cv2.boundingRect(c)
                        cv2.rectangle(frame1, (x,y), (x+w,y+h),(0,255,0),2)
                        winsound.PlaySound('alert.wav',winsound.SND_ASYNC)
                    if cv2.waitKey(10)== ord('q'):
                        break
                cv2.imshow('Jarvis cam', frame1) 
            elif 'audio book' in query:
                Reader()
                if cv2.waitKey(10)== ord('q'):
                    break
            elif 'screen capture' in query:
                width=GetSystemMetrics(0)
                height=GetSystemMetrics(1)
                time_stamp=datetime.datetime.now().strftime('%Y-%m-%D-%H-%M-%S')
                file_name = (f'{time_stamp}.mp4')            
                fourcc=cv2.VideoWriter_fourcc('m','p','4','v')
                captured_video=cv2.VideoWriter(file_name, fourcc,20.0,(width,height))
                webcam=cv2.VideoCapture(0)
                while True:
                    img=ImageGrab.grab(bbox=(0,0,width,height))
                    img_np=np.array(img)
                    img_final=cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
                    _, frame=webcam.read()
                    fr_height ,fr_width,_=frame.shape
                    img_final[0:fr_height,0:fr_width,:]= frame[0: fr_height,0:fr_width,:]
                    cv2.imshow('Image Capture', img_final)
                    captured_video.write(img_final)
                    if cv2.waitKey(10) == ord('q'):
                        break
            elif 'message' in query:
                speak("Sir, Please Enter the name, to send message")
                while Drive:
                    Drive = True
                    name = input("Sir,Enter the Name:  ")
                    speak(f"What's the message for {name},sir")
                    MSG=takeCommand()
                    MSG=MSG.replace("send","")
                    from automatewhatsapp import WhatsappMsg
                    WhatsappMsg(name,MSG)
                    speak("Do you want to send another message?")
                    query= takeCommand()
                    if 'yes' in query:
                        Drive = True
                    else:
                        Drive = False
            elif 'call' in query:
                speak("Sir, Please Enter the name, to Whom You want to call ")
                name=input("Sir, Enter the Name:  ")
                from automatewhatsapp import WhatsappCall
                WhatsappCall(name)
                speak("Do you want to send another call?")
                query= takeCommand()
            elif 'video call' in query:

                name=query.replace("whatsapp video call","")
                name=name.replace("Make","")
                name=name.replace("to","")
                Name=str(name)
                from automatewhatsapp import WhatsappVideoCall
                WhatsappVideoCall(Name)
            elif 'chat' in query:

                speak("Whose chat do you want ,sir ?")
                Name=takeCommand()
                from automatewhatsapp import WhatsappChat
                WhatsappChat(Name)
            elif 'repeat my words' in query:
                speak("Sure,sir!")
                jj=takeCommand()
                speak(f"Sir,you said: {jj}")
            elif 'chrome' in query:
                from Autocommand import ChromeAuto
            elif 'alarm' in query:
                speak("Enter the time,sir!")
                time=input(" Enter The Time: ")
                while True:
                    alarm= datetime.now()
                    now = alarm.strftime("%H:%M:%S")
                    if now == time:
                        speak("It's Time to Wake Up,Sir!")
                        playsound('alarm.mp3')
                        speak("Alarm closed,sir!")
                    elif now>time:
                        break
            elif 'screenshot' in query:
                speak('What should be the file name,sir!')
                path=takeCommand()
                path1name= path + ".png"
                path1 = "C:\\Users\\Bhawesh\Desktop\\Pyhton Project\\jarvis\\screenshot\\" + path1name
                kk=pyautogui.screenshot()
                kk.save(path1)
                os.startfile("C:\\Users\\Bhawesh\Desktop\\Pyhton Project\\jarvis\\screenshot")
                speak("Sir,screenshot is captured.")
            elif 'translator' in query:
                Trans()
            elif 'remember that' in query:
                rememberMsg= query.replace("remember that","")
                rememberMsg= query.replace("jarvis","")
                speak(f"You tell Me to Remind You About : " + rememberMsg)
                remember = open('data.txt','w')
                remember.write(rememberMsg)
                remember.close()           
            elif 'what do you remember' in query:
                remember=open('data.txt','r')
                speak("You Told me to remember that: " + remember.read()) 
            elif "downloading speed" in query:
                SpeedTest()
            elif "uploading speed" in query:
                SpeedTest()
            elif "Internet speed" in query:
                SpeedTest()
            elif 'temprature' in query:
                Temp()
            elif 'how to' in query:
                speak("Getting data from Internet !")
                op=query.replace('jarvis','')
                max_result = 1
                how_to_func = search_wikihow(op,max_result)
                assert len(how_to_func) ==1
                how_to_func[0].print()
                speak(how_to_func[0].summary)
            elif 'you need a break' in query:
                speak('Ok sir, you can call me anytime!')
                speak('Just say wake up jarvis!')
                exit()
            elif 'shut down' in query:
                speak("Sir,Can You Enter The number of programs Opened")
                n = int(input("Enter the number of programs Opened Sir:"))
                i=0
                speak("Ok Sir, Wait a second!")
                for i in range (0,n):
                    keyboard.press_and_release("alt + F4")
                    if i==n:
                        os.system('shutdown /s /t 1')
            elif 'restart' in query:
                speak("Sir,Can You Tell me The number of programs Opened")
                ku= takeCommand()
                jm=0
                print(ku)
                speak("Ok Sir, Wait a second!")
                for i in range (0,n):
                    keyboard.press_and_release("alt + F4")
                    if i==n:
                        os.system('shutdown /r /t 1')
            if 'quit' in query:
                speak('Thankyou,For your time. Let me know if you need my help sir!')
                exit()
if __name__ == "__main__":
    speak('Recognizing, please wait!')    
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('trainer/trainer.yml')   
    cascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascadePath) 

    font = cv2.FONT_HERSHEY_SIMPLEX 


    id = 1 

    name = ['','Bhawesh']


    cam = cv2.VideoCapture(0, cv2.CAP_DSHOW) 
    cam.set(3, 640) 
    cam.set(4, 480) 

    minW = 0.1*cam.get(3)
    minH = 0.1*cam.get(4)
    while True:

        ret, img =cam.read()

        converted_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) 

        faces = faceCascade.detectMultiScale( 
                converted_image,
                scaleFactor = 1.2,
                minNeighbors = 5,
                minSize = (int(minW), int(minH))
            )

        for(x,y,w,h) in faces:

                cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)

                id, accuracy = recognizer.predict(converted_image[y:y+h,x:x+w]) 

                if (accuracy < 100):
                    id = name[id]
                    accuracy = "  {0}%".format(round(100 - accuracy))
                    TaskExe()
                else:
                    id = "unknown"
                    accuracy = "  {0}%".format(round(100 - accuracy))
                    print("Verification Failed!!")
                    
                cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
                cv2.putText(img, str(accuracy), (x+5,y+h-5), font, 1, (255,255,0), 1)  
            
        cv2.imshow('camera',img) 

        k = cv2.waitKey(10)&0xff 
        if k == 'q':
                break
        cam.release()
        cv2.destroyAllWindows()
