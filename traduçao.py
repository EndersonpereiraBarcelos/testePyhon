#Sem eros

from translate import Translator

options = Translator(from_lang = "pt-br", to_lang = "english")
inputString = "testando o tradutor"
#inputString = "Ola mundo"
translate = options.translate(inputString)
print(translate)