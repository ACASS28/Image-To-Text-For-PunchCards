from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import numpy as np
from sklearn.cluster import KMeans
from pc_generator import PCGenerator
import xml.etree.ElementTree as ET
from svgoutline import svg_to_outlines
import svgwrite
from tkinter import messagebox
import math


def openFile():
    global cluster_centers, labels, image_shape

    # Get the number of colors from the user input
    num_colors = int(color_count.get())

    # File dialog to select the image
    filepath = filedialog.askopenfilename(initialdir="C:\\Users\\Cakow\\PycharmProjects\\Main",
                                          title="Open file okay?",
                                          filetypes=(("PNG files", "*.png"),
                                                     ("All files", "*.*")))
    if not filepath:
        return  # If no file is selected, return

    # Open the image (assuming it is a pixel image with a user-specified number of colors)
    image = Image.open(filepath)
    image_shape = image.size  # Store image size for later use
    

    # Convert the image to RGB
    image = image.convert('RGB')

    # Get the pixel data from the image
    image_array = np.array(image)
    reshaped = image_array.reshape(-1, 3)  # Flatten the 3D image array to 2D array of RGB values
   

    # Perform K-Means clustering to group colors into 'num_colors' clusters
    kmeans = KMeans(n_clusters=num_colors, random_state=0)
    kmeans.fit(reshaped)
    cluster_centers = kmeans.cluster_centers_.astype(int)  # These are the representative colors
    labels = kmeans.labels_.reshape(image_array.shape[:2])  # The labels correspond to pixels in the image

    # Display the image in the window using Tkinter's Label widget
    tk_image = ImageTk.PhotoImage(image)
    image_label = Label(window, image=tk_image)
    image_label.image = tk_image  # Keep a reference to the image to prevent garbage collection
    image_label.grid(row=2, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)  # Center image horizontally

    # Clear previous color options if they exist
    for widget in window.grid_slaves():
        if int(widget.grid_info()["row"]) > 2:
            widget.grid_forget()

    # Create dropdowns for each unique color
    global color_labels
    color_labels = []
    for i, color in enumerate(cluster_centers):
        color_label = StringVar(window)
        color_label.set(f"Label {i+1}")  # Default value in dropdown
        dropdown = OptionMenu(window, color_label, *[f"Label {j}" for j in range(1, num_colors+1)])  # Assume labels based on num_colors
        dropdown.grid(row=i+3, column=1, sticky="nsew", padx=10, pady=5)  # Center dropdowns horizontally
        color_labels.append(color_label)

    # Display the unique cluster colors for user to see
    for i, color in enumerate(cluster_centers):
        color_box = Canvas(window, width=50, height=50)
        color_box.grid(row=i+3, column=0, sticky="nsew", padx=10, pady=5)
        color_box.create_rectangle(0, 0, 50, 50, fill=f'#{color[0]:02x}{color[1]:02x}{color[2]:02x}')
    repeatAmount =0
    if(math.floor(999/image_shape[1])<=10):
        repeatAmount = math.floor(999/image_shape[1])
    else:
        repeatAmount = 10
    # Add the vertical repeat slider
    vert_repeat_slider = Scale(window, from_=1, to=10, orient=HORIZONTAL, variable=vert_repeat, label="Vertical Repeats")
    vert_repeat_slider.grid(row=num_colors+4, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)

    # Add a button to save the file once colors are labeled
    save_button = Button(window, text="Save to Text and SVG File", command=lambda: save_to_file(filepath))
    save_button.grid(row=num_colors+5, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)  # Center save button

    # Hide the initial widgets for selecting the number of colors and opening the file
    color_dropdown.grid_forget()
    button.grid_forget()
    color_label_widget.grid_forget()  # Hide the number of colors label

    # Replace the initial widgets with a Restart button
    restart_button = Button(window, text="Restart", command=restart_program)
    restart_button.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)  # Center restart button



def save_to_file(filepath):
    # Prepare the output file path
    output_path = filepath[:-4] + "_output.txt"
    
    # List to store the main color for each row
    main_color_list = []
    vertical_repeats = vert_repeat.get()
    # Get the labels selected by the user
    user_labels = [label.get() for label in color_labels]

    with open(output_path, 'w') as f:
        for repeats in range(vertical_repeats):
            if len(user_labels) == 2:
                # If there are only two colors, we stick to the original behavior (one line per row)
                for y in range(labels.shape[0]):
                    row_output = ""
                    for x in range(labels.shape[1]):
                        cluster_idx = labels[y, x]  # Get the cluster index for this pixel
                        if user_labels[cluster_idx] == "Label 1":
                            row_output += 'x'
                        else:
                            row_output += '-'
                    f.write(row_output + '\n')

                    # Append 1 for each row (since there are only two colors)
                    main_color_list.append(0)

            else:
                # For more than two colors, process each row and append its main color once
                for y in range(labels.shape[0]):
                    color_counts = {label: 0 for label in user_labels}  # Count occurrences of each color

                    # Count occurrences of each color in the row
                    for x in range(labels.shape[1]):
                        cluster_idx = labels[y, x]
                        if cluster_idx < len(user_labels):  # Safeguard
                            color_label = user_labels[cluster_idx]
                            color_counts[color_label] += 1

                    # Determine the main color (the one that appears most frequently)
                    main_color = max(color_counts, key=color_counts.get)
                    try:
                        main_color_number = int(main_color.split()[-1])
                    except (ValueError, IndexError):
                        print(f"Unexpected main color format: {main_color}")
                        main_color_number = 1  # Default in case of error
                    

                    # Write the multiple lines for the row based on unique colors
                    unique_colors_in_row = np.unique(labels[y, :])
                    
                    for unique_color in unique_colors_in_row:
                        main_color_list.append(unique_color)
                        
                        row_output = ''
                        for x in range(labels.shape[1]):
                            if labels[y, x] == unique_color:
                                row_output += 'x'
                            else:
                                row_output += '-'
                        f.write(row_output + '\n')

    print(f"File saved to: {output_path}")
    
    # Get the value of vertical repeats from the slider
    print(len(main_color_list))

    # Call PCGenerator to generate SVG after saving the text file
    pc_gen = PCGenerator(None, output_path, 'your_machine_id', vert_repeat=vertical_repeats, maincolors=main_color_list)
    svg_output = pc_gen.generate()

    # Save the generated SVG to a file
    svg_filepath = output_path.replace('.txt', '.svg')
    with open(svg_filepath, 'w') as svg_file:
        svg_file.write(svg_output)

    messagebox.showinfo("Info", "File and SVG saved successfully.")
    
    # Prompt user before restarting
    restart_program()

# def generate_svg(data, output_file):
#     # Create a new SVG drawing
#     dwg = svgwrite.Drawing(output_file, profile='tiny')

#     for color, stroke_width, points in data:
#         # Convert color tuple (0-1 range) to a valid SVG color (0-255 range)
#         r, g, b, _ = color  # Ignore the alpha channel for now
#         svg_color = f'rgb({int(r * 255)}, {int(g * 255)}, {int(b * 255)})'

#         # Add the line to the SVG
#         dwg.add(dwg.line(start=points[0], end=points[1], stroke=svg_color, stroke_width=stroke_width))

#     # Save the drawing
#     dwg.save()
#     print(f"SVG saved to {output_file}")

def restart_program():
    """Reset the window to its initial state."""
    # Clear all widgets from the window
    for widget in window.winfo_children():
        widget.destroy()

    # Recreate the initial widgets (color dropdown and Open Image button)
    global color_label_widget
    color_label_widget = Label(window, text="Enter the number of colors (2-4):")
    color_label_widget.grid(row=0, column=0, sticky="e", padx=10, pady=10)  # Align label to the right
    
    global color_count
    color_count = StringVar(window)
    color_count.set("2")  # Default number of colors
    global color_dropdown
    color_dropdown = OptionMenu(window, color_count, "2", "3", "4")
    color_dropdown.grid(row=0, column=1, sticky="w", padx=10, pady=10)  # Align dropdown to the left

    global button
    button = Button(window, text="Open Image", command=openFile)
    button.grid(row=1, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)  # Center button horizontally



# Create the main window
window = Tk()
window.title('PunchCard Maker')

# Set a larger window size
window.geometry("300x800")  # You can adjust the size as needed

# Now create the IntVar for vertical repeats after the Tk window is created
vert_repeat = IntVar()
vert_repeat.set(1)  # Default value for vertical repeats

# Create a label and an entry for user to specify number of colors
global color_label_widget
color_label_widget = Label(window, text="Enter the number of colors (2-4):")
color_label_widget.grid(row=0, column=0, sticky="e", padx=10, pady=10)  # Align label to the right

# Dropdown or text entry for specifying the number of colors
color_count = StringVar(window)
color_count.set("2")  # Default number of colors
color_dropdown = OptionMenu(window, color_count, "2", "3", "4")
color_dropdown.grid(row=0, column=1, sticky="w", padx=10, pady=10)  # Align dropdown to the left

# Button to open the file
button = Button(window, text="Open Image", command=openFile)
button.grid(row=1, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)  # Center button horizontally

window.mainloop()








