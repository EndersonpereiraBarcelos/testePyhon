from translate import Translator

options = Translator(from_lang = "pt-br", to_lang = "english")
inputString = "testando o tradutor"
translate = options.translater(inputString)
print(translate)