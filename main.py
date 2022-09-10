
from gtts import gTTS


filename = str(input("Enter the file name which do you want to save audio in:\n"))
mytext = str(input("Enter the text:\n"))


language = 'en'

myobj = gTTS(text=mytext, lang=language, slow=False)


myobj.save(filename)

