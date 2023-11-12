# audioBook

# importing necessary library for our project
import pyttsx3
import PyPDF2

# Open Pdf and read pdf
# NOTE Change oop.pdf to your Pdf Before You run it.
book = open("oop.pdf", "rb")
pdfReader = PyPDF2.PdfReader(book)

# initialize speaking library
speaker = pyttsx3.init()
page = pdfReader.pages[7]
text = page.extract_text()
speaker.say(text)
speaker.runAndWait()
