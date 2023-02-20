import pyaudioconvert as pac
from pprint import pprint
from utils import chnge_format
import pyaudioconvert as pac
from transformers import pipeline
from nemo.collections.nlp.models import PunctuationCapitalizationModel
from summarizer import Summarizer

# change format from mp3 to wav
src = "missiles.mp3"
dst = "missiles.wav"
chnge_format(src,dst)
#convert 44000hz audio to 16000hz
pac.convert_wav_to_16bit_mono('missiles.wav', 'missiles.wav')

# https://huggingface.co/models?pipeline_tag=automatic-speech-recognition
pipe = pipeline(model="facebook/wav2vec2-base-960h")

output = pipe("missiles.wav", chunk_length_s=10)

print(output["text"])

# to get the list of pre-trained models
PunctuationCapitalizationModel.list_available_models()
# Download and load the pre-trained BERT-based model
model = PunctuationCapitalizationModel.from_pretrained("punctuation_en_bert")

summary = model.add_punctuation_capitalization([output['text'].lower()])

model = Summarizer()
summary = " ".join(summary)
result = model(summary, min_length=60)
full = ''.join(result)

import textwrap
from fpdf import FPDF

def text_to_pdf(text, filename):
    a4_width_mm = 210
    pt_to_mm = 0.35
    fontsize_pt = 10
    fontsize_mm = fontsize_pt * pt_to_mm
    margin_bottom_mm = 10
    character_width_mm = 7 * pt_to_mm
    width_text = a4_width_mm / character_width_mm

    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.set_auto_page_break(True, margin=margin_bottom_mm)
    pdf.add_page()
    pdf.set_font(family='Courier', size=fontsize_pt)
    splitted = text.split('\n')

    for line in splitted:
        lines = textwrap.wrap(line, width_text)

        if len(lines) == 0:
            pdf.ln()

        for wrap in lines:
            pdf.cell(0, fontsize_mm, wrap, ln=1)

    pdf.output(filename, 'F')
