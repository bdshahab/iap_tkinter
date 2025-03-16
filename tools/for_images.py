# You may need to install Pillow for handling images.
from PIL import Image, ImageTk


# Function to flip the image horizontally
def change_image_direction_size(image_path, flip_h, width, height):
    # Open the image
    image = Image.open(image_path).resize((width, height))

    # Flip the image horizontally
    if flip_h:
        image = image.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
    return ImageTk.PhotoImage(image)
