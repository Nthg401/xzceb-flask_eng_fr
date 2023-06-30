""" 
The file is used to translate the text from english formate to French and viceversa
"""

import json
import os

from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """_summary_
     It is use to translate the english text to french

    Args:
        englishText (string): _description_

    Returns:
        _type_: _description_ string
    """
    #write the code here
    french_text = MyMemoryTranslator(source="en-US",target="fr-FR").translate(text=english_text)
    print(french_text)
    return french_text

def french_to_english(french_text):
    """_summary_
    this method is used to convert french to english

    Args:
        frenchText (string): _description_

    Returns:
        _type_: string
    """
    #write the code here
    english_text = MyMemoryTranslator(source="fr-FR",target="en-US").translate(text=french_text)
    print(english_text)
    return english_text


