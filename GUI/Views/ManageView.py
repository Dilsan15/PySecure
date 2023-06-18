import os
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import cv2
from tkinter import filedialog


class ManageView(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Getting image data from the controller
        self.controller = controller
        self.images_dict = controller.return_images_dict()
        self.save_dir = r"Models\Images"

        # Make a canvas to display the images in
        self.frame_canvas = tk.Frame(self)
        self.frame_canvas.pack(fill=tk.BOTH, expand=True)
        self.canvas = tk.Canvas(self.frame_canvas, borderwidth=2)
        self.scrollbar = ttk.Scrollbar(self.frame_canvas, orient='vertical', command=self.canvas.yview)

        # Helps handle they're dynamically changing number of images?
        self.frame = tk.Frame(self.canvas)
        self.frame.bind("<Configure>", self.on_frame_configure)

        self.create_image_labels()
        self.display_images()

        # Create a window within the canvas and associate it with the frame
        self.canvas.create_window((0, 0), window=self.frame, anchor="nw")

        # Configure the canvas to use the scrollbar for vertical scrolling
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # Pack the canvas to the left, fill both directions, and expand to fill available space
        self.canvas.pack(side="left", fill='both', expand=True)
        self.scrollbar.pack(side="right", fill="y")

        # Create a frame and pack it to the parent widget
        self.frame_button = tk.Frame(self)
        self.frame_button.pack()

        upload_button = tk.Button(self.frame_button, text="Upload New", command=self.upload_dialog)
        upload_button.pack(side='top', pady=10)

        # make the upload button look nicer, gives user a warninbg as well

        tk.Label(self.frame_button, text="You will have to restart the application to see changes!").pack(side='top',
                                                                                                          pady=10)
        upload_button.config(
            width=20,
            height=2,
            bg="#00008B",
            fg="#FFD700",
            highlightthickness=0,
            bd=0,
            activebackground="#FFFFFF",
            activeforeground="#000000",
            relief=tk.FLAT,
        )

    def create_image_labels(self):

        for i, (name, image) in enumerate(self.images_dict.items()):
            frame = tk.Frame(self.frame, bd=10, relief="groove")
            frame.grid(row=i // 3, column=i % 3, padx=10, pady=5)

            # Convert the OpenCV image to PIL Image
            image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            pil_image = Image.fromarray(image_rgb)
            resized_image = pil_image.resize((225, 200))

            photo = ImageTk.PhotoImage(resized_image)
            label = tk.Label(frame, bd=0, image=photo)
            label.image = photo
            label.pack()

            # Create label for the person's name
            name_label = tk.Label(frame, text=name)
            name_label.pack(fill=tk.BOTH)

            # Create delete button for removing the picture
            delete_button = tk.Button(frame, text="Delete", fg="white", bg="red",
                                      command=lambda idx=name: self.delete_image(idx))
            delete_button.pack(fill=tk.BOTH)

    def upload_dialog(self):
        file_path = filedialog.askopenfilename(initialdir="/", title="Select file")
        if file_path:
            # Load the selected image
            image = cv2.imread(file_path)

            # Save the uploaded image to the directory
            os.makedirs(self.save_dir, exist_ok=True)
            file_name = os.path.splitext(os.path.basename(file_path))[0]
            save_path = os.path.join(self.save_dir, f"{file_name}.jpg")
            cv2.imwrite(save_path, image)

            # Append the uploaded image and its name to the self.images_dict dictionary
            self.images_dict[file_name] = image

            # Display the updated images
            self.display_images()

    # TODO: Duplicate code? can we make this a function later?
    def display_images(self):
        # Clear the existing labels
        for child in self.frame.winfo_children():
            child.destroy()

        # Display each image and its associated name in a label
        for i, (name, image) in enumerate(self.images_dict.items()):
            # Create a frame to hold the label and the button
            frame = tk.Frame(self.frame, bd=10, relief="groove")
            frame.grid(row=i // 3, column=i % 3, padx=10, pady=5)

            # Convert the OpenCV image to PIL Image, necessary step since tkinter only accepts PIL images (not the
            # OpenCV format)
            image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            pil_image = Image.fromarray(image_rgb)
            resized_image = pil_image.resize((225, 200))

            # Create a label with the image
            photoS = ImageTk.PhotoImage(resized_image)
            label = tk.Label(frame, bd=0, image=photoS)
            label.image = photoS
            label.pack()

            # Create label for the person's name
            name_label = tk.Label(frame, text=name)
            name_label.pack(fill=tk.BOTH)

            # Create delete button for removing the picture
            delete_button = tk.Button(frame, text="Delete", fg="white", bg="red",
                                      command=lambda idx=name: self.delete_image(idx))
            delete_button.pack(fill=tk.BOTH)

        # Scroll bar config?
        self.canvas.update_idletasks()
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def delete_image(self, name):
        if name in self.images_dict:
            # Delete the selected image and its associated name
            del self.images_dict[name]

            # Delete the image file from the directory
            image_path = os.path.join(self.save_dir, f"{name}.jpg")
            if os.path.exists(image_path):
                os.remove(image_path)

            self.display_images()

    def on_frame_configure(self, event):
        # Second positional argument is useless but raises an error if not included
        self.canvas.configure(scrollregion=self.canvas.bbox('all'))
