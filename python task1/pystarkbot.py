import pyttsx3
import os
import datetime

engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 180)


print("************LUCIFER**************")
print()

pyttsx3.speak("Hello Akash")
print()
print("WELCOME TO MY INTELLECTUAL PROGRAM".center(135))
engine.runAndWait()
pyttsx3.speak("I am your virtual assistant Lucifer")
pyttsx3.speak("How can I help you out?")



def bye():
    print("BYE")
    pyttsx3.speak("Bye")
    print("SEE YOU SOON :-)")
    pyttsx3.speak("See you soon")

def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        pyttsx3.speak("Have A Great Day Sir")
        print("Have A Great Day Sir")
    elif hour>=12 and hour<18:
        pyttsx3.speak("Have A Great Day Sir")
        print("Have A Great Day Sir")
    else:
        pyttsx3.speak("Have A Great Day Sir")
        print("Have A Great Day Sir")

print("What can I do for you : "  , end='')
print("""
    A: PLAY GAMES
    M: Listen Music
    C : WANT TO CHANGE THE SETTINGS OF PC
    G : ACCESS MY GITHUB

    Q : QUIT
    """)

while True:
    print("\t\t\t Please Enter Your Choice : " , end='')
    choice = input()

    if ("what is the time" in choice or "show me the time" in choice):
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        print(strTime)
        pyttsx3.speak(f"the current time is {strTime}")
        
        

    elif ("date" in choice):
        pyttsx3.speak("Showing todays date sir")
        os.system("date")

    elif ("what is ur name?" in choice or "tell me about yourself" in choice):
        pyttsx3.speak("My name is Lucifer  I am your personal assistant sir  & will always be there to help you")


    if choice == 'A' or choice == 'a':
        pyttsx3.speak("You Don't Have any Games in the system")
        want = input()
        if ("games" in want or "explore" in want):
            pyttsx3.speak("Microsoft Store will be opening in a while")
            os.system("start ms-windows-store:")
    elif choice == 'M' or choice == 'm':
        pyttsx3.speak("Opening your music")
        os.system("spotify")     
    elif choice == 'C' or choice == 'c':
        pyttsx3.speak("Sure Opening Control Panel for you")
        os.system('control panel')  
    elif choice == 'G' or choice == 'g':
        pyttsx3.speak("Opening your github sir")
        os.system('chrome https://github.com/')      
    elif ("linkedin" in choice):
        pyttsx3.speak("Opening your linkedin sir")
        os.system('chrome https://linkedin.com/')      
    elif ("want to stream online videos" in choice):
        pyttsx3.speak("Opening Youtube sir")
        os.system('chrome https://www.youtube.com/')  
    elif ("Open Amazon Web Services" in choice):
        pyttsx3.speak("Opening AWS cloud sir")
        os.system('chrome https://aws.amazon.com/')  
    elif ("want to use Google" in choice) or ("Cloud Services" in choice):
        pyttsx3.speak("Opening Google cloud Platform sir")
        os.system('chrome https://cloud.google.com/')  
    elif ("explore some new webseries for me" in choice):
        pyttsx3.speak("Opening Netflix sir")
        os.system('chrome https://www.netflix.com/in/')  
    elif ("gmail" in choice):
        pyttsx3.speak("Opening Gmail sir")
        os.system('chrome www.gmail.com')   
    elif ("twitter" in choice):
        pyttsx3.speak("Opening Tweet sir")
        os.system('chrome www.twitter.com')
    elif ("paint" in  choice) or ("drawing" in choice):
        pyttsx3.speak("Running paint for you")
        os.system("mspaint") 
    elif ("run" in choice)  or ("chrome" in choice):
        pyttsx3.speak("Sure Opening Chrome for you")
        os.system("chrome")          
    elif  ("notepad" in choice) or ("editor" in choice):
        pyttsx3.speak("Opening notepad for you")
        os.system("notepad")
    elif ("want to" in choice) or ("access my VMs" in choice):
        pyttsx3.speak('Opening virtualbox for you')
        os.system("VirtualBox")  
    elif ("facebook" in choice):
        pyttsx3.speak("Opening Facebook") 
        os.system('chrome www.facebook.com') 
    elif ("shopping" in choice) or ("online" in choice):
        pyttsx3.speak("Opening Amazon Sir")
        os.system('chrome www.amazon.in')
    elif ("connect" in choice) or ("I want to connect" in choice) or ("to remote server" in choice):
        pyttsx3.speak("Opening putty sir")
        os.system('putty')     
    elif ("teamviewer" in choice):
        pyttsx3.speak("opening teamviewer sir")
        os.system('teamviewer')            
    
    elif ("How is the weather these days lucifer?" in choice):
        pyttsx3.speak("The weather is cloudy these days sir")
        pyttsx3.speak("And the temperature is around 29 degree celsius")
    elif ("tell me the current scenario of COVID-19" in choice):
        print("""Active Cases :  676,900
              Discharge/Cured Cases : 1,919,842
              Deaths :  50,921
        """) 
        print("This is the current report of COVID-19 August 2020")         
        pyttsx3.speak("This is the current report of COVID-19 August 2020")      
    elif choice == 'Q' or choice == 'q':
        pyttsx3.speak("Exiting your programs")
        break
  
wishMe()
        
bye()

    
