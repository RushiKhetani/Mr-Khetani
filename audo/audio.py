import pyttsx3
import pdfplumber
import PyPDF2

engine = pyttsx3.init()
engine.setProperty("rate", 17)
engine.say('welcom back sir now we started the reading book again')
engine.runAndWait()
file = 'kali.pdf'

pdfobj = open(file ,'rb')

pdfReader= PyPDF2.PdfFileReader(pdfobj)

pages = pdfReader.numPages

with pdfplumber.open(file) as pdf:
    for  i in range (0,pages):
        page = pdf.pages[i]
        text = page.extract_text()
        print(text)
        speaker = pyttsx3.init()
        speaker.say(text)
        speaker.runAndWait()
