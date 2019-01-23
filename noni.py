from chatterbot import ChatBot , preprocessors #method to train the bot
from chatterbot.trainers import ListTrainer #import chatbot
import os #allow us to work with folders
import sys
import pyttsx3
from pyttsx3 import * #speech engine
import speech_handler as spnd




bot = ChatBot("Noni") #creat the name
bot.set_trainer(ListTrainer) #set the trainer

Noni = pyttsx3.init()#initializing engine

sound = Noni.getProperty("voices")
Noni.setProperty("voice",sound[1].id)
Noni.setProperty("rate",150)
Noni.setProperty("volume",5)

for _file in os.listdir("files"): #open files inside the folder
    chats = open("files/"+ _file,'r').readlines()#read lines and place in chat

bot.train(chats)#train the chats


name = input("Noni : Hello i am Noni, what is your name?\n")
Noni.say("nice name"+str(name))

while True:
    request = input(name + ':-')
    response = bot.get_response(request)
    Noni.say(response)
    print("Noni:",response, "\n")#print the response or replies to use
    if request=="shut down":
        sys.exit()
    else:
        Noni.runAndWait()
    


    
