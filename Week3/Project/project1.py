# Import libraries
import re
import cv2
import os
import time
import csv
import numpy as np
import matplotlib.pyplot as plt


# Profile Images Directory
dir_path = f"{os.getcwd()}\\Week3\\Project\\img"

def is_valid_email(email):
    """Check if the email address is valid."""
    # Regular expression pattern for validating email addresses
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email)

def authenticate(email, age, category):
    """Authenticate the user's email, age, and category."""
    # Check if the email is valid
    if not is_valid_email(email):
        print("invalid email address")
        return True, "Invalid email address"
    
    # Check if the age is above 18
    try:
        age = int(age)
        if age < 18:
            print("you are not up to 18 years")
            return True, "You must be 18 years or older to access the content"
    except ValueError:
        return True, "Invalid age. Please enter a valid age."
    
    # Check if the category is valid
    if category not in [1, 2, 3]:
        print("invalid category")
        return True, "Invalid category. Please select a valid category (1, 2, or 3)."
    
    # If all checks pass, return False for login_failed and None for window_name
    return False, None
import os
import time

def get_image(category, image):
    """Fetch profile picture from database/directory"""
    folders = {1: 'Contemporary', 2: 'Modern', 3: 'Traditional'}
    folder = folders.get(category)
    if not folder:
        print("Invalid category.")
        return False, None
    
    image_path = os.path.join(dir_path, folder, f"image{image}.jpg")
    
    print("Fetching profile picture...")
    time.sleep(0.5)  # Simulate fetching process
    print(image_path)
    if os.path.exists(image_path): 
        return True, image_path
    else:
        print("Sorry, picture was not found.")
        return False, None
    
def enhance(choice, image):
    """Enhancement Technique\n
       Choice -> for technique chosen\n
       Image -> image being fed into function"""
    plt.subplot(1, 2, 1)
    plt.title("Original")
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    if choice == 1:
        # Translate the image
        M_translate = np.float32([[1, 0, 50], [0, 1, 50]])  # Translation matrix
        translated_image = cv2.warpAffine(image, M_translate, (image.shape[1], image.shape[0]))
        plt.subplot(1,2,2)
        plt.title("Translated Image")
        plt.imshow(cv2.cvtColor(translated_image, cv2.COLOR_BGR2RGB))
        
    elif choice == 2:
        # Reflect the image
        reflected_image = cv2.flip(image, 1)
        plt.subplot(1,2,2)
        plt.title("Reflected Image")
        plt.imshow(cv2.cvtColor(reflected_image, cv2.COLOR_BGR2RGB))
        
    elif choice == 3:
        # Rotate the image
        rows, cols, _ = image.shape
        M_rotate = cv2.getRotationMatrix2D((cols / 2, rows / 2), 45, 1)  # Rotation matrix
        rotated_image = cv2.warpAffine(image, M_rotate, (cols, rows))
        plt.subplot(1,2,2)
        plt.title("Rotated Image")
        plt.imshow(cv2.cvtColor(rotated_image, cv2.COLOR_BGR2RGB))
        
    elif choice == 4:
        # Crop the image
        cropped_image = image[50:image.shape[0] - 50, 50:image.shape[1] - 50]
        plt.subplot(1,2,2)
        plt.title("Cropped Image")
        plt.imshow(cv2.cvtColor(cropped_image, cv2.COLOR_BGR2RGB))
        
    elif choice == 5:
        # Shear the image
        M_shear = np.float32([[1, 0.5, 0], [0.5, 1, 0]])  # Shearing matrix
        sheared_image = cv2.warpAffine(image, M_shear, (image.shape[1], image.shape[0]))
        plt.subplot(1,2,2)
        plt.title("Sheared Image")
        plt.imshow(cv2.cvtColor(sheared_image, cv2.COLOR_BGR2RGB))
        
    elif choice == 6:
        # Apply Gaussian blur
        blurred_image = cv2.GaussianBlur(image, (7, 7), 0)
        plt.subplot(1,2,2)
        plt.title("Blurred Image")
        plt.imshow(cv2.cvtColor(blurred_image, cv2.COLOR_BGR2RGB))
        
    else:
        print("Invalid choice.")
    
    plt.show()


def main():
    redo = True
    print("Hey fellow classmates. You've reached my Image Enhancement Interface. \nPlease enter your username and password to enhance your profile picture.")
    
    while redo:
        email = input("Enter your email: ")
        age = input("Enter your age: ")
        category = int(input("Select a category;\n"
                             "(1) Contemporary\n"
                             "(2) Modern\n"
                             "(3) Traditional\n"
                             "Choice:"))

        login_failed, window_name = authenticate(email, age, category)
        
        if not login_failed:
            while redo:
                image_choice = input("Select an image:\n"
                "(1) Image One\n"
                "(2) Image Two\n"
                "(3) Image Three\n"
                "Choice:")
                
                choice = int(input("Select a number to apply one of our enhancement techniques to your profile picture;\n"
                                   "(1) Translate the image\n"
                                   "(2) Reflect the image\n"
                                   "(3) Rotate the image\n"
                                   "(4) Crop the image\n"
                                   "(5) Shear the image\n"
                                   "(6) Apply Gaussian blur\n\n"
                                   "Choice: "))
                
                image_found, image_path = get_image(category, image_choice)
                
                if image_found:
                    image = cv2.imread(image_path)
                    enhance(choice, image)
                else:
                    print("Sorry, picture was not found.")
                
                choice = input("Do you wish to perform another image enhancement technique? (Y/N): ").strip().lower()
                if choice != "y":
                    print("Thank You and Goodbye!")
                    redo = False




if __name__ == "__main__":
    main()


