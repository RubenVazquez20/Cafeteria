import re

drink = input("Dame una palabra: ")

def detector_espacios(drink):
    
    return re.findall(r'\d\s+\d', drink)
    
detector_espacios(drink)