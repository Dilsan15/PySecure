# Imports

import os
import cv2
import face_recognition


class ImageModel:
    """Not really a Data model (as far as I know) but serves a similar function"""

    def __init__(self):

        # Image storing variables, one for the actual image, one for the pic name, and one for the encoded versions

        self.images = []
        self.pic_names = []
        self.encode_list = []
        self.dir_list = os.listdir(r"Models/Images")

    def encode_images(self):

        for pic in self.dir_list:
            curImg = cv2.imread(f'Models/Images/{pic}')
            self.images.append(curImg)
            self.pic_names.append(os.path.splitext(pic)[0])

        # Encode the images and store them in the encode_list variable
        for img in self.images:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            encode = face_recognition.face_encodings(img)[0]
            self.encode_list.append(encode)

        return self.encode_list, self.pic_names

    def get_images_pair(self):
        # Return a dictionary of the images and their names, needed for presenting the images in the ManageView
        return {k: v for k, v in zip(self.pic_names, self.images)}



# 1. Me in the stored images directory (It should draw a square around my face)




# 2. Me not in the stored images Directory (it won't detect me, but i can still detect others like Damien)
# I jus deleted my image off of the stored images directory

# no detection right now ... until i reupload my image and restart the prj
