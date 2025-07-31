import os
import numpy as np
from PIL import Image
# custom color-to-label mapping dictionary
from color_to_label_map import COLOR_TO_LABEL 

# RGB-segmented PNG slices (manually painted regions)
input_dir = "/path/to/manualsegmentedpngs"  
# Folder where the grayscale label masks will be saved
output_dir = "/path/to/outputted_label_masks"
os.makedirs(output_dir, exist_ok=True)

# convert each RGB slice to label mask
for filename in sorted(os.listdir(input_dir)):
    if filename.lower().endswith(".png"):
        img_path = os.path.join(input_dir, filename)
        base_name = os.path.splitext(filename)[0]

        # load image and convert to RGB
        img = Image.open(img_path).convert("RGB")
        img_np = np.array(img)

        # create an empty mask (same dimensions, all zeros)
        label_mask = np.zeros((img_np.shape[0], img_np.shape[1]), dtype=np.uint8)

        # loop through each defined RGB color in the dictionary
        for color, label in COLOR_TO_LABEL.items():
            # create a mask where all pixels matching this color are True
            mask = np.all(img_np == color, axis=-1)
            label_mask[mask] = label

        output_path = os.path.join(output_dir, f"{base_name}_labeled.png")
        Image.fromarray(label_mask, mode='L').save(output_path)

