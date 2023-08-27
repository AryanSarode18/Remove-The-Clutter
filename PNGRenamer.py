# Importing os Module to Rename the File
import os

# List all files in the "png" directory
files = os.listdir("png")

# Initialize a counter for renaming
i = 1

# Iterate through each file in the directory
for img in files:
    # Check if the file is a PNG image
    if img.endswith(".png"):
        # Print the current image file name
        print(img)

        # Rename the image file using the counter
        os.rename(f"png/{img}", f"png/{i}.png")

        # Increment the counter
        i = i + 1

# Display a completion message
print("Thanks For Using This Function")
print("All Your PNG Files are Renamed")
