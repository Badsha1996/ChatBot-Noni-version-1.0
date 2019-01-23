import pyttsx3

Noni = pyttsx3.init()

sound = Noni.getProperty("voices")
Noni.setProperty("voice",sound[1].id)
Noni.setProperty("rate",150)
Noni.setProperty("volume",5)

Noni.say("hello i am a chatbot called noni version 1.0")
Noni.say("pogram start loading")

Noni.runAndWait()



