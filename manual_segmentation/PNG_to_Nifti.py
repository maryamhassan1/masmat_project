import os
import numpy as np
from PIL import Image
import nibabel as nib
from scipy.ndimage import zoom
import re

# folder to your labeled PNG slices
input_dir = "/path/to/LabelMasks"
# output of label masks as a nii.gz
output_nifti = "/path/to/output/LabelMasks.nii.gz"

# input your target dimensions based on your necessities 
# width of each slice (x)
target_width = 
# height of each slice (y)
target_height =  
# voxel dimensions in mm (X, Y, Z)
voxel_size = (, , )  

def extract_slice_num(filename):
    """
    Extracts a slice index from a filename using regex.
    Assumption: files are named like: slice_0_labeled.png
    """
    match = re.search(r'(\d+)', filename)  # looks for digits 
    if match:
        return int(match.group(1))         # returns an integer
    else:
        return -1 

# sort slice files by extracted number
all_files = os.listdir(input_dir)
png_files_unsorted = []
for f in all_files:
    if f.lower().endswith(".png"):
        png_files_unsorted.append(f)

# sort them by the slice number
png_files = sorted(png_files_unsorted, key=extract_slice_num)

#load and process each image
slices = []
for fname in png_files:
    img_path = os.path.join(input_dir, fname)
    img = Image.open(img_path).convert("L") 
    img_np = np.array(img, dtype=np.uint8)

    # optional: change/ reorient based on the orientation you need
    # img_np = np.fliplr(np.rot90(img_np, k=3))

    # resample to target shape 
    orig_h, orig_w = img_np.shape
    zoom_y = target_height / orig_h
    zoom_x = target_width / orig_w
    resampled = zoom(img_np, (zoom_y, zoom_x), order=0)

    slices.append(resampled)

volume = np.stack(slices, axis=-1)

# create affine for voxel size
affine = np.eye(4)
# x direction
affine[0, 0] = voxel_size[0]
# y direction
affine[1, 1] = voxel_size[1]
# z direction
affine[2, 2] = voxel_size[2]

# save as a NIFTI
nifti_img = nib.Nifti1Image(volume, affine)
nib.save(nifti_img, output_nifti)
