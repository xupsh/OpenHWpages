from PIL import Image
import glob
import os

files =  glob.glob(r'C:\Users\xushi\XilinxOpenHW\doc\webpage_structure.assets\*')
OUTPUT_PATH = r'C:\Users\xushi\XilinxOpenHW\doc\resized'


for  file in files:
    file_name = os.path.basename(file)
    image = Image.open(file)
    image = image.resize([1920, 1500])
    save_name = os.path.join(OUTPUT_PATH, file_name)
    image.save(save_name)

# RGB (481, 321) JPEG