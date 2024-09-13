import speech_recognition as sr #sr modulr for speech recog-->
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import threading

from pyfirmata import Arduino,SERVO
from time import sleep

from tkinter import *
root =Tk()

port='COM5'
board=Arduino(port)
lf=6
lt=7 
rf=8
rt=9
board.digital[lf].mode=SERVO
board.digital[lt].mode=SERVO
board.digital[rf].mode=SERVO
board.digital[rt].mode=SERVO

led1=board.get_pin("d:4:o")
led1.write(1) 

#path1= "C:\\Users\\HP\\OneDrive\\Desktop\\miniproject\\images\\normal_2.jpeg"

def rotateServo(pin,angle):
    board.digital[pin].write(angle)    

rotateServo(rf,90)
rotateServo(rt,90)
rotateServo(lf,90)
rotateServo(lt,90)

r=sr.Recognizer()
text_speech=pyttsx3.init()

engine = pyttsx3.init()


rate = engine.getProperty('rate')   # getting details of current speaking rate
engine.setProperty('rate',180)     # setting up new voice rate


voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[0].id)



def talk(text):
    engine.say(text)
    engine.runAndWait()

talk("Initiating all systems")

def dance():
    for i in range(0,180):
        rotateServo(lf,i)
        sleep(0.0025)
    for i in range(180,0,-1):
        rotateServo(lf,i)   
        sleep(0.0025)  
    rotateServo(lf,90)       
    for i in range(0,180):
        rotateServo(rf,i)
        sleep(0.0025)
    for i in range(180,0,-1):
        rotateServo(rf,i)   
        sleep(0.0025)  
    rotateServo(rf,90)                 

def dance1():
    x=0
    while(x<10):
        for i in range(0,60):
            rotateServo(lf,i)
            rotateServo(rf,i)
            sleep(0.0025)
        for i in range(60,0,-1):
            rotateServo(lf,i)
            rotateServo(rf,i)
            sleep(0.0025)
        for i in range(0,120):
            rotateServo(lf,i)
            rotateServo(rf,i)
            sleep(0.0025)
        for i in range(120,0,-1):
            rotateServo(lf,i)
            rotateServo(rf,i)
            sleep(0.0025)    
        x+=1    


def hi():
    talk("hi ")
    rotateServo(lf,10)
    sleep(1)
    rotateServo(rf,60)
    rotateServo(lt,90)
    rotateServo(rt,90)
    rotateServo(lt,0)
    j=0
    while(j<2):
        rotateServo(lf,180)
        sleep(0.5)
        rotateServo(lf,0)
        sleep(0.5)
        j+=1
    talk("nice to meet you")    


def searchGoogle(query):
    import wikipedia as googleScrap
    query = query.replace("google","")
    talk("This is what I found on google")
    try:
        pywhatkit.search(query)
        result = googleScrap.summary(query,1)
        talk(result)

    except:
        talk("No speakable output available")

info="my name is friday .I am an AI robot assistant. I can do many thing like searching the internet ,play songs,say jokes and many more all on your command. I can even control your aplliacnce just by saying simple commands.I was created by Shiva manish,vishal and tanish. "
def take_command():  
    with sr.Microphone() as source:
        print("Talk")
        rotateServo(rf,90)
        rotateServo(rt,90)
        rotateServo(lf,90)
        rotateServo(lt,90)
        talk("hi, how may i help you")
        r.adjust_for_ambient_noise(source)
        audio_text=r.listen(source)
        talk('I am processing your command')
        print("Wait!!!")
        try:
            txt=r.recognize_google(audio_text)
            txt=txt.lower()
            txt=txt.replace('friday','')
            print(txt)
        except:
            txt=""
            print("i dont know that")    
    return(txt)        

def run_friday():
    print("in run friday")
    command=take_command()
    if 'play'in command:
        song=command.replace('play','')
        talk('playing'+song)
        pywhatkit.playonyt(song)
        sleep(5)
        dance1()
        exit()
    elif'google'in command:
        searchGoogle(command)    
    elif'turn on'in command:
        led1.write(0)     
    elif'turn off'in command:
        led1.write(1)     
    elif 'time'in command:
        time=datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('current time is'+time)
    elif 'about you'in command:
        talk(info)    
    elif'say'in command:
        say=command.replace('say','')    
        talk(say)

    elif'search'in command:
        search=command.replace('search','')    
        wiki_info=wikipedia.summary(search,1)
        talk(wiki_info)
    elif'joke'in command:
        joke=pyjokes.get_joke()
        print(joke)
        talk(joke)
    elif 'dance'in command:
        dance()
    else:
        talk("I dont know that")   
        run()  
print("out off while")

def run():
    rotateServo(rf,90)
    rotateServo(rt,90)
    rotateServo(lf,90)
    rotateServo(lt,90)
    
    with sr.Microphone() as source:
        print("listening......")
        r.adjust_for_ambient_noise(source)
        t=r.listen(source)
        t=r.recognize_google(t)
        t=t.lower()
        print(t)
        if'friday'in t:
            run_friday()
        if'hai'or 'hi'in t :
            hi()   
        if'sleep'in t:
            for i in range(90,0,-1):
                rotateServo(rf,i)
                sleep(0.005)
            for i in range(90,180):
                rotateServo(lf,i) 
                sleep(0.005)   
            exit()
        else:
            run()    
    sleep(1)
        
for i in range(0,90):
    rotateServo(lf,i)
    sleep(0.005)
for i in range(180,90,-1):
    rotateServo(rf,i) 
    sleep(0.005)  
def stop():
    exit()
talk("All systems are online")
while(True):
    root.title("friday")
    root.configure(bg="#141414")
    root.geometry("400x400")
    button1=Button(root,text="stop",height=2,width=15,command=threading.Thread(target=stop).start).place(x=250,y=320)
    button2=Button(root,text="run",height=2,width=15,command=threading.Thread(target=run).start).place(x=50,y=320)
   # img1= ImageTk.PhotoImage(Image.open(path1))
    from PIL import ImageTk ,Image
    img1 = ImageTk.PhotoImage(Image.open("C:\\Users\\HP\\OneDrive\\Desktop\\miniproject\\images\\normal_2.jpeg") )

    panel = Label(root, image = img1)
    panel.pack(side = "bottom", expand = "yes")
    root.mainloop()  
'''
while(True):
    for i in range(0,90):
        rotateServo(lf,i)
        sleep(0.005)
    for i in range(180,90,-1):
        rotateServo(rf,i) 
        sleep(0.005)  
'''