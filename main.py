import pyttsx3

book = open(r"damacharla id.txt")
book_text = book.readlines()
engine = pyttsx3.init()
for i in book_text:
    engine.say(i)
    engine.setProperty("rate", 100)
    engine.runAndWait()
