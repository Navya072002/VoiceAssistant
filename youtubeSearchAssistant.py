import speech_recognition as sr
import webbrowser as wb

r1= sr.Recognizer()
r2= sr.Recognizer()
r3= sr.Recognizer()

mic= sr.Microphone()

with mic as source:
    print('[search youtube]')
    print('speak now')
    r3.adjust_for_ambient_noise(source)
    audio= r3.listen(source)
    transcript = r3.recognize_google(audio)
    print(transcript)

if 'hello' in transcript:
    r2= sr.Recognizer()
    url= 'https://www.youtube.com/results?search_query='
    with sr.Microphone() as source:
        print('search your query')
        r2.adjust_for_ambient_noise(source)
        audio= r2.listen(source)

        try:
            get= r2.recognize_google(audio)
            print(get)
            wb.get().open_new(url+get)
        except sr.UnknownValueError:
            print('error')
        except sr.RequestError as e:
            print('failed'.format(e))