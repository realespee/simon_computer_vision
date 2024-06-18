import os
import shutil

# Count the number of images in each class directory
cassava = len(os.listdir('./crop_datasets/cassava'))
maize = len(os.listdir('./crop_datasets/maize'))
sugarcane = len(os.listdir('./crop_datasets/sugarcane'))
grass = len(os.listdir('./crop_datasets/grass'))

print(f"{cassava} Cassava Images")
print(f"{maize} Maize Images")
print(f"{sugarcane} Sugar Cane Images")
print(f"{grass} Grass Images")

def populate_train_val_test_directories(root_dir='data', training_ratio=0.75, validation_ratio=0.1):
    """
    Populate train/val/test directories based on the specified ratios.
    
    Args:
    - root_dir: The root directory for train/val/test directories.
    - training_ratio: The ratio of images to be used for training.
    - validation_ratio: The ratio of images to be used for validation.
    """
    classes = [
        {
            "dir": 'crop_datasets/cassava',
            'text_label': 'cassava',
            "label": 0
        },
        {
            "dir": 'crop_datasets/grass',
            'text_label': 'grass',
            "label": 1
        },
        {
            "dir": 'crop_datasets/maize',
            'text_label': 'maize',
            "label": 2
        },
        {
            "dir": 'crop_datasets/sugarcane',
            'text_label': 'sugarcane',
            "label": 3
        }
    ]
    for dataset_class in classes:
        label = dataset_class['label']
        folder = dataset_class['text_label']
        src = dataset_class['dir']
        images = os.listdir(src)
        split = int(len(images) * training_ratio)

                # Create directories if they don't exist
        for directory in ['train', 'val', 'test']:
            os.makedirs(os.path.join(root_dir, directory, folder), exist_ok=True)
            
        for i, img in enumerate(images):
            train_limit = int(split * (1 - validation_ratio))
            if i < split:
                if i < train_limit:
                    shutil.copy(os.path.join(src, img), os.path.join(f"{root_dir}/train/{folder}", img))
                else:
                    shutil.copy(os.path.join(src, img), os.path.join(f"{root_dir}/val/{folder}", img))
            else:
                shutil.copy(os.path.join(src, img), os.path.join(f"{root_dir}/test/{folder}", img))

# Call the function to populate train/val/test directories
populate_train_val_test_directories()
