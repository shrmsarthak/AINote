from os import path 
from pydub import AudioSegment

def chnge_format(src,dst):  # for example src-> "tedx.mp3":dst-> "tedx.wav" 
    sound = AudioSegment.from_mp3(src) 
    return sound.export(dst, format="wav")