# use: pip install pyttsx3 PyPDF2
import pyttsx3
import PyPDF2

texto = " "
# abre o pdf
book = open('DocumentoDesejado.pdf', 'rb')
# define um leitor pro pdf
pdfReader = PyPDF2.PdfFileReader(book)
# numero de paginas
pages = pdfReader.numPages
# inicia o leitor
speaker = pyttsx3.init()
# define a voz que vai ler (zero é a linguagem principal do windows)
voices = speaker.getProperty('voices')
speaker.setProperty('voice', voices[0].id)
speaker.setProperty('rate', 188)
speaker.setProperty('volume', 1.0)

for num in range(pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()
    texto.join(text)

speaker.save_to_file(texto, 'NomeDoAudio.mp3')
speaker.runAndWait()
