# Parses translation commands and returns help text, language lists, or translated messages.
import googletrans
import LangCodes
from googletrans import Translator
from LangCodes import CodeDict

tl = Translator()


def translate(msg: str) -> str:
    msg = msg.lower()

    if (msg == "/thelp"):
      return("""Type '/t [ENGLISH] - [LANGUAGE]'
if language not specified, will auto-translate to english!
Type '/tlangs' to see all current available languages!""")
    
    if(msg == "/tlangs"):
      lang_str = "Afrikaans"
      for value in CodeDict.values():
        if(value != "afrikaans"):
          lang_str += " , " + value.capitalize()
      return("The available languages are:\n"+lang_str+".")


    #TODO - Parse user message
    