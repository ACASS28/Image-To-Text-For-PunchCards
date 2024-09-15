from tkinter import *
from tkinter import filedialog
from PIL import Image  # Importing from Pillow


def openFile():
    filepath = filedialog.askopenfilename(initialdir="C:\\Users\\Cakow\\PycharmProjects\\Main",
                                          title="Open file okay?",
                                          filetypes=(("PNG files", "*.png"),
                                                     ("All files", "*.*")))
    if not filepath:
        return  # If no file is selected, return

    output_path = filepath[:-4] + ".txt"

    # Open the image and convert it to grayscale
    image = Image.open(filepath).convert('L')

    # Ensure the image width is between 1 and 24 pixels
    width, height = image.size
    if width > 24 or width < 1:
        raise ValueError("Image width must be between 1 and 24 pixels.")

    # Write grayscale interpretation to file
    with open(output_path, 'w') as f:
        for y in range(height):
            row = ""
            for x in range(width):
                pixel_value = image.getpixel((x, y))
                # If pixel value is closer to black (0), use 'x', otherwise use '-'
                row += 'x' if pixel_value < 128 else '-'
            f.write(row + '\n')

    # Now open the file and print the content
    with open(output_path, 'r') as f:
        content = f.read()
        print(content)


window = Tk()
button = Button(window, text="Open", command=openFile)
button.pack()
window.mainloop()
