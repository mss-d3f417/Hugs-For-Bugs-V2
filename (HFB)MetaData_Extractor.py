# Made By D3F417 - With Purple Heart
# Kidi Don't Copy This Code ! 
# GitHub : https://github.com/mss-d3f417
# Site : https://d3f417.info

from PIL import Image
from PIL.ExifTags import TAGS


imagename = input("HFB > Masir File Aks Kirito Bede: ")

try:
    image = Image.open(imagename)
except FileNotFoundError:
    print("HFB > File Kirit not found. Please make Motmaeen the file Address is Dorost.")
    sys.exit(1)

info_dict = {
    "Filename": image.filename,
    "Image Size": image.size,
    "Image Height": image.height,
    "Image Width": image.width,
    "Image Format": image.format,
    "Image Mode": image.mode,
    "Image is Animated": getattr(image, "is_animated", False),
    "Frames in Image": getattr(image, "n_frames", 1)
}

for label, value in info_dict.items():
    print(f"{label:25}: {value}")

exifdata = image.getexif()

for tag_id in exifdata:
    tag = TAGS.get(tag_id, tag_id)
    data = exifdata.get(tag_id)
    
    if isinstance(data, bytes):
        data = data.decode()
    print(f"{tag:25}: {data}")
