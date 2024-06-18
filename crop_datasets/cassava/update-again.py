from PIL import Image
import glob
import os

def create_new_image(image_path, count):
    try:
        # Load the image
        image = Image.open(image_path)
        print(f"Loaded image: {image_path}")
        
        # Create a new file name in the same directory with count
        dir_name = os.path.dirname(image_path)
        new_image_path = os.path.join(dir_name, f"sugarcane_{count}.jpg")
        
        # Save the image to a new file in the same directory
        image.save(new_image_path)
        print(f"Created new image: {new_image_path}")
    except Exception as e:
        print(f"Failed to process image {image_path}: {e}")

# Specify the correct directory where images are stored
image_directory = r'd:/MS/Gideon_Mpungu_Computer_Vision_Project/garden_dataset/sugarcane/'

# Change the current working directory to the image directory
os.chdir(image_directory)

# Print the current directory
current_directory = os.getcwd()
print(f"Current directory: {current_directory}")

# List all files in the current directory
files_in_directory = os.listdir(current_directory)
print(f"Files in directory: {files_in_directory}")

# Process all .jpg images in the specified directory
jpg_images = glob.glob('*.jpg')
print(f"Found {len(jpg_images)} .jpg images")

for count, image_path in enumerate(jpg_images, start=1):
    create_new_image(image_path, count)

print("Script completed.")
