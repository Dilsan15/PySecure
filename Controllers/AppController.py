from GUI import GUIWindow
from Models import ImageModel


class AppController():
    def __init__(self):
        self.current_page = None
        self.image_model = ImageModel()
        self.WindowView = GUIWindow(self)
        self.change_view("HomeView")
        self.WindowView.mainloop()

    def return_image_encodings(self):
        return self.image_model.encode_images()

    def return_images_dict(self):
        return self.image_model.get_images_pair()

    def change_view(self, frame_id, *args):
        self.current_page = frame_id
        self.WindowView.change_view(frame_id)
