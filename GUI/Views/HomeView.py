# Imports

import tkinter as tk
import cv2
from PIL import Image, ImageTk
import face_recognition
import numpy as np
import threading


class HomeView(tk.Frame):
    """This class is used to create the home page of the application. It also includes a Camera frame that does image
    detection."""

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # Gets encodings and names from the controller, These encodings are made from the facial detection library
        self.image_encodings, self.known_names = self.controller.return_image_encodings()

        # TODO Could we make it look a bit better? Maybe add more widgets?
        self.camera_label = tk.Label(self, bd=10, relief='raised')
        self.camera_label.pack()

        # Gets default Camera to use

        self.cap = cv2.VideoCapture(0)
        self.stop_event = threading.Event()

        self.update_camera()

    def update_camera(self):

        # Success code, and the actual frame
        ret, frame = self.cap.read()

        if ret:
            # Perform facial detection on the frame in a separate thread. This will make it way faster

            # TODO: Will using GPU make it even more faster?
            threading.Thread(target=self.process_frame, args=(frame,)).start()

        # Schedule the next update of the camera, this will prevent it from having low FPS
        if not self.stop_event.is_set():
            self.camera_label.after(10, self.update_camera)

    def process_frame(self, frame):

        try:

            # Resizing and BGR --> RGB
            imgS_resize = cv2.resize(frame, (0, 0), None, 0.25, 0.25)
            imgS_BGR = cv2.cvtColor(imgS_resize, cv2.COLOR_BGR2RGB)

            # Finds the actual facial locations in the camera, and converts them to encodings as well
            facesCurFrame = face_recognition.face_locations(imgS_BGR)
            encodesCurFrame = face_recognition.face_encodings(imgS_BGR, facesCurFrame)

            for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
                matches = face_recognition.compare_faces(self.image_encodings, encodeFace)

                # How distant is it from the faces stored in the directory?
                faceDis = face_recognition.face_distance(self.image_encodings, encodeFace)
                # Argmin forces it to make the choice of the lowest distance, which is what it most closely resembles
                matchIndex = np.argmin(faceDis)

                # If the face matches, and the distance is less than 0.47, then it will display the name, 0.47 is an
                # arbitrary number
                if matches[matchIndex] and faceDis[matchIndex] < 0.47:
                    # Github Copilot suggested what is below, and it seems to work well
                    name = self.known_names[matchIndex].upper()
                    y1, x2, y2, x1 = faceLoc
                    x1, y1, x2, y2 = x1 * 4, y1 * 4, x2 * 4, y2 * 4
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 0), 2)
                    cv2.rectangle(frame, (x1, y2 - 35), (x2, y2), (0, 0, 0), cv2.FILLED)
                    cv2.putText(frame, name, (x1 + 6, y2 - 6), 4, 1, (255, 255, 255), 2)

            # Convert the frame to RGB format, as we want to display it in tkinter
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Resize the frame with desired dimensions
            resized_frame = cv2.resize(rgb_frame, (700, 600))

            # Convert the frame to a format that tkinter can display
            photo = ImageTk.PhotoImage(image=Image.fromarray(resized_frame))

            # Update the label with the new frame
            self.camera_label.configure(image=photo)
            self.camera_label.image = photo
        except ValueError:
            # This will occur if encodings have not been completed before the app starts
            # This does not happen in our program, but it is good to have it here as we continue to develop the app
            pass

    def stop(self):
        # This will stop the camera
        self.stop_event.set()

    # IMPORTANT
    # Look at the documentation on x and y systems, REMEMBER to put [ (frame, ] at the start
