import piexif 
import piexif.helper
import base64
from PIL import Image

filename = 'HACK3D_Challenge.jpg'
extracted_img = 'extract1.jpg' 

img = Image.open(filename)
exif_dict = piexif.load(img.info['exif'])
#loads all exif data

user_comment = piexif.helper.UserComment.load(exif_dict["Exif"][piexif.ExifIFD.UserComment])
#extracts the user comment(edited exif data) from the given picture.
#print(user_comment)

with open(extracted_img,'wb') as imageFile: imageFile.write(base64.b64decode(user_comment.encode('utf-8')))
#writes the user-commented exif data into an image file(extracted_img)
