from rembg import remove
from configparser import ConfigParser
import PIL.Image as img
import os, glob, io

config = ConfigParser()
config.read("config.cfg")
input_path = 'input'
output_path = 'hasil'
background_color = config.get('config', 'bgcolor')

if not os.path.exists(input_path):
    os.mkdir(input_path)

if not os.path.exists(output_path):
    os.mkdir(output_path)

for all in glob.glob(input_path+"/*"):
    filename = os.path.basename(all).rsplit('.', 1)[0]
    input = img.open(all)
    b = io.BytesIO()
    nobg = remove(input)
    nobg.save(b, format="png")
    rembg = img.open(b).convert("RGBA")
    output = img.new("RGBA", input.size, background_color)
    output.paste(rembg, mask=rembg)
    output.convert("RGB").save(output_path+"/"+filename+".png")

