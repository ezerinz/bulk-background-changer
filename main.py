from rembg import remove
from configparser import ConfigParser
import PIL.Image as img
import os, glob, io

config = ConfigParser()
config.read("config.cfg")
input_path = 'input'
output_path = 'hasil'

if not os.path.exists(input_path):
    os.mkdir(input_path)

if not os.path.exists(output_path):
    os.mkdir(output_path)

for all in glob.glob('input/*'):
    filename = os.path.basename(all).rsplit('.', 1)[0]
    input = img.open(all)
    b = io.BytesIO()
    nobg = remove(input)
    nobg.save(b, format="png")
    rembg = img.open(b)
    output = img.new("RGBA", input.size, config.get('config', 'bgcolor'))
    output.paste(rembg, mask=rembg)
    output.convert("RGB").save("hasil/"+filename+".png")

