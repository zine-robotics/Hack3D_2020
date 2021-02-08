import piexif 
import piexif.helper
import base64
from PIL import Image

filename = 'HACK3D_Challenge.jpg'
extracted_img = 'extract1.jpg' 

img = Image.open(filename)
exif_dict = piexif.load(img.info['exif'])

user_comment = piexif.helper.UserComment.load(exif_dict["Exif"][piexif.ExifIFD.UserComment])
#print(user_comment)

with open(extracted_img,'wb') as imageFile: imageFile.write(base64.b64decode(user_comment.encode('utf-8')))

