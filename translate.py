import googletrans
from googletrans import Translator
import json

translator = Translator()

# Tanslates the input to English using googletrans which uses google translate API
def transToEng(strng,langcode):
    dict={
            "00":"en",
            "01":"",
            "02": 'bn',
            "05": "gu",
            "06": 'hi',
            "07": 'kn',
            "11":"ml",
            "12":"",
            "13": "mr",
            "15": "or",
            "16": 'pa',
            "20": 'ta',
            "21": 'te',
            "22": 'ur'
        }
    
    try:
        if langcode=='00':
            res={
                "street": strng[0],
                "landmark": strng[1],
                "locality": strng[2],
                "vtc": strng[3],
                "district": strng[4],
                "state": strng[5]
            }
            return res
        
        for i in range(0,6):
            if strng[i] != "":
                strng[i]=translator.translate(strng[i], src=dict[langcode] ,dest='en').text

        res={
            "street": strng[0],
            "landmark": strng[1],
            "locality": strng[2],
            "vtc": strng[3],
            "district": strng[4],
            "state": strng[5]
        }
    except:
        return "ERROR"
    
    
    return res
