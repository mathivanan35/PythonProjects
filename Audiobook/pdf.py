import pyttsx3
import PyPDF2

book = open(r'C:\Users\Public\Sample\Audiobook\pdf_file\Qus.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
speaker = pyttsx3.init()
for i in range(pages):
    page = pdfReader.getPage(i)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()
