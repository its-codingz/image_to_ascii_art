import pywhatkit as pywkt

path = input("Enter Image name(with extension): ")

topath = "Output File"

pywkt.image_to_ascii_art(path,topath)
