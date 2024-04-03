import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import cv2
import os
import numpy as np
import matplotlib.pyplot as plt

# Function to authenticate user
def authenticate():
    email = email_entry.get()
    age = age_entry.get()
    category = category_var.get()

    # Your authentication logic here
    if email == "" or age == "":
        messagebox.showerror("Error", "Please enter both email and age.")
        return
    
    try:
        age = int(age)
    except ValueError:
        messagebox.showerror("Error", "Invalid age. Please enter a valid number.")
        return
    
    # Your authentication logic here
    # if authenticated:
    #     messagebox.showinfo("Success", "Authentication successful!")
    # else:
    #     messagebox.showerror("Error", "Authentication failed.")

# Function to perform image enhancement
def enhance():
    choice = enhancement_var.get()

    # Placeholder logic for image enhancement
    image_path =f"{os.getcwd()}\\Week3\\Project\\img\\"
    image = cv2.imread(image_path)

    if choice == 1:
        # Translate the image
        M_translate = np.float32([[1, 0, 50], [0, 1, 50]])  # Translation matrix
        translated_image = cv2.warpAffine(image, M_translate, (image.shape[1], image.shape[0]))
        display(translated_image)
        
    elif choice == 2:
        # Reflect the image
        reflected_image = cv2.flip(image, 1)
        display(reflected_image)
        
    elif choice == 3:
        # Rotate the image
        rows, cols, _ = image.shape
        M_rotate = cv2.getRotationMatrix2D((cols / 2, rows / 2), 45, 1)  # Rotation matrix
        rotated_image = cv2.warpAffine(image, M_rotate, (cols, rows))
        display(rotated_image)
        
    elif choice == 4:
        # Crop the image
        cropped_image = image[50:image.shape[0] - 50, 50:image.shape[1] - 50]
        display(cropped_image)
        
    elif choice == 5:
        # Shear the image
        M_shear = np.float32([[1, 0.5, 0], [0.5, 1, 0]])  # Shearing matrix
        sheared_image = cv2.warpAffine(image, M_shear, (image.shape[1], image.shape[0]))
        display(sheared_image)
        
    elif choice == 6:
        # Apply Gaussian blur
        blurred_image = cv2.GaussianBlur(image, (7, 7), 0)
        display(blurred_image)
        
    else:
        messagebox.showerror("Error", "Invalid choice.")

# Function to display enhanced image
def display(image):
    img = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    img = img.resize((300, 300), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    image_label.config(image=img)
    image_label.image = img

# Initialize Tkinter window
root = tk.Tk()
root.title("Art Collection Image Enhancer")

# Create main frame
main_frame = ttk.Frame(root, padding="20")
main_frame.grid(row=0, column=0)

# Email entry
email_label = ttk.Label(main_frame, text="Email:")
email_label.grid(row=0, column=0, sticky="w")
email_entry = ttk.Entry(main_frame, width=30)
email_entry.grid(row=0, column=1, padx=5, pady=5)

# Age entry
age_label = ttk.Label(main_frame, text="Age:")
age_label.grid(row=1, column=0, sticky="w")
age_entry = ttk.Entry(main_frame, width=30)
age_entry.grid(row=1, column=1, padx=5, pady=5)

# Category selection
category_label = ttk.Label(main_frame, text="Category:")
category_label.grid(row=2, column=0, sticky="w")
category_var = tk.IntVar()
category_combobox = ttk.Combobox(main_frame, textvariable=category_var, values=[1, 2, 3], state="readonly", width=28)
category_combobox.current(0)
category_combobox.grid(row=2, column=1, padx=5, pady=5)

# Authenticate button
authenticate_button = ttk.Button(main_frame, text="Authenticate", command=authenticate)
authenticate_button.grid(row=3, column=0, columnspan=2, pady=10)

# Image enhancement section
enhancement_label = ttk.Label(main_frame, text="Image Enhancement:")
enhancement_label.grid(row=4, column=0, sticky="w")
enhancement_var = tk.IntVar()
enhancement_radiobutton1 = ttk.Radiobutton(main_frame, text="Translate", variable=enhancement_var, value=1)
enhancement_radiobutton1.grid(row=4, column=1, sticky="w")
# Add other enhancement options as needed

# Enhance button
enhance_button = ttk.Button(main_frame, text="Enhance", command=enhance)
enhance_button.grid(row=5, column=0, columnspan=2, pady=10)

# Image display
image_label = ttk.Label(main_frame)
image_label.grid(row=6, column=0, columnspan=2, pady=10)

root.mainloop()
