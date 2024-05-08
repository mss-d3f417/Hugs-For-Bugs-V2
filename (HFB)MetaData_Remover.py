# Made By D3F417 - With Purple Heart
# Kidi Don't Copy This Code ! 
# GitHub : https://github.com/mss-d3f417
# Site : https://d3f417.info

import argparse
from PIL import Image



def clear_all_metadata(imgname):
  
    
    img = Image.open(imgname)
    
    
    data = list(img.getdata())
    
    
    img_without_metadata = Image.new(img.mode, img.size)
    img_without_metadata.putdata(data)
    
    
    img_without_metadata.save(imgname)
    
    print(f"HFB : Metadata Kirit successfully Paked from '{imgname}'.")


parser = argparse.ArgumentParser(description="Remove metadata from an aks file.")
parser.add_argument("img", help="Image file from which to remove metadata")


args = parser.parse_args()


if args.img:
    clear_all_metadata(args.img)