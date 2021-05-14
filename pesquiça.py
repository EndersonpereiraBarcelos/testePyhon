import wikipedia
from translate import Translator

search = "Instagram"
options = Translator(from_lang = "pt-br", to_lang = "english")
result = wikipedia.summary(search)
print(result)