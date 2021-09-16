import speech_recognition as sr
import datetime
import webbrowser
import time
r= sr.Recognizer()

def record(ask=False):
    with sr.Microphone()as source:
        if ask:
            print(ask)
        audio = r.listen(source)
        voice = ""
        try:
            voice= r.recognize_google(audio , language="tr-TR")
        except sr.UnknownValueError:
            print("Anlayamadım")
        except sr.RequestError:
            print("Sistemde Arıza Var")
        return voice

def response(voice):
    now = datetime.datetime.now()
    if "nasılsın" in voice:
        print("iyiyim sen nasılsın")
    if "saat kaç" in voice:
        print ("Saat:" +now.strftime("%H:%M:%S"))
    if "Tarih ne" in voice:
        print ("Bugün günlerden:" + now.strftime("%Y-%m-%d"))
    if "arama yap" in voice:
        search =record("ne aramak istersin?")
        url= "https://www.google.com/search?q="+search
        webbrowser.get().open(url)
        print(search + " için bulduklarım")

print("nasıl yardımcı olabilirim")
time.sleep(1)

while(1):
    voice=record()
    print (voice)
    response(voice)