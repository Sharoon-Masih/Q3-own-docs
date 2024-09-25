import speech_recognition as sr # 'as' keyword is use for aliasing mtlb kay now i dont have to call 'speech_recognition' everytime, i can do it just by calling 'sr'
import webbrowser 
import pyttsx3
import musiclib # its our module
import requests

recognizer = sr.Recognizer(); 
engine = pyttsx3.init()

def speak(text:str):
    engine.say(text); 
    engine.runAndWait(); # yeh iss lia lgya hai kiu kay jab .say() ka method execute ho rha hai toh .runAndWait() method usko stop for saying and then terminate hoga.

def process(command):
    if 'google' in command.lower():
        webbrowser.open('https://www.google.com'); # yeh jo web browser module hai yeh python ma use hi issliya hota hai takay python program say webbrowser ko manipulate kia jaye.  
    elif 'facebook' in command.lower():
        webbrowser.open('https://facebook.com')
    elif 'youtube' in command.lower():
        webbrowser.open('https://youtube.com')
    elif 'instagram' in command.lower():
        webbrowser.open('https://instagram.com')
    elif 'jessica' in command.lower():
        speak('Jessica is a lazy girl')
    elif 'danish' in command.lower():
        speak('danish is a monkey guy')
    elif 'jane' in command.lower():
        speak('jane is a gorgeous and intelligent girl.')
    elif 'akhtar' in command.lower():
        speak('akhtar is a hilter women.')
    elif command.lower().startswith('play'):
        song = command.split(' ')[1]
        print(song)
        link = musiclib.music[song]
        webbrowser.open(link)
    elif 'news' in command.lower():
        response = requests.get(f'https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=36e10a1aba834f6b8a0be4e4fc486976')

        if response.status_code == 200:
            data = response.json(); 
            articles = data.get('articles',[])
            speak('top ten news are here')
            for i in range(10):
                speak(articles[i]['title']) # yaha pehla may article
            
    else:
        speak('Sorry, I cant do that')

if __name__ == '__main__':
    speak('initializing jarvis...')
    r = sr.Recognizer() # yeh wala method basically jitni be speech ko recognize krnay ka liya functionalities hain unko activate krdega.
    status = True
    while status:
        print('recognizing...') # yeh just for as a indicator use kia hai kay user ko pta chlay kay speech recognize ho rhi hai.
        
        # recognize speech using google
        try:
            with sr.Microphone() as source: # then phr sr,Microphone() ka through humara jo system ka microphone hai wo active hojayega or then ohr yeh mic ka through voice ko catchup krkay jo 'source' variable hai usme return krta hai.
                print("listening...") # yeh indicate krta hai kay mic listen kr rha hai.
                audio = r.listen(source,timeout=2,phrase_time_limit=1) # ab wo jo mic return krega wo hum Recoginizer().listen() method ko pass kreinga or wo proper fine krka audio return krega.

                # isme jo 'timeout' wala parameter hai uska mtlb hai kay jo be timeout ma time specify krein gay utnay time ka liya srf wait krega then it will move on.
                # phrase_time_limit iss parameter ka mtlb hai kay jitna be time isme set kreinga jarvis srf utnay time tk sunay ga then wo stop krdey ga jasa humna 1 second set kia hai toh its mean kay wo srf 1 second tk sunaga han then jab hum stop hoka phr say bolega toh it will listen.

                word = r.recognize_google(audio) # then phr wo jo audio return krega wo further humna agay jo recoginizer provider use kr rhay hain usko pass kia like here we are using 'google' recognizer we can also use azure or etc. ab yeh jo recognizer hai yeh 'audio' ko accept krka string ma convert krkay return krega.
                # or then phr jo string return hogi uski base pa further functionality perform hogi.
               

                # if user will say switch off so program will terminate.
                if ('switch off' == word.lower()):
                    status = False

                if('jarvis' in word.lower()): # 'in'  keyword ka iss lia use kia hai bcuz agr hum word == 'jarvis' krdeta toh wo phr srf tabhi detect krta jab user srf 'jarvis' bolta but hum chahtay hain kay user agr 'hey jarvis' ya kuch be related to jarvis speak kray toh wo response kray iss lia hum yeh check kr rhay hain kay string may agr jarvis exist krta hai toh phr wo response kray. 
                    speak('yeah'); 
                    print('Jarvis Active..')
                with sr.Microphone() as MicOutput:
                    audioCommand = r.listen(MicOutput)
                    command = r.recognize_google(audioCommand)
                    print(command)
                    process(command)
        except Exception as e:
            print(f"jarvis error; {e}")
