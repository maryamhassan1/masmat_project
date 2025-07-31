import nibabel as nib
import numpy as np
import csv
import os

# get the dice score
def dice(mask1, mask2):
    """calculate Dice score between two  masks."""
    intersection = np.logical_and(mask1, mask2).sum()
    total = mask1.sum() + mask2.sum()
  
    if total == 0:
        return np.nan
      
    dice_score = 2 * intersection / total
    return dice_score

# input your paths
# path to the manual segmentation file as a NifTI
manual_path = "/path/to/manual_segmentation.nii.gz"
# path to the output file from MASMAT as a NifTI
masmat_folder = "/path/to/masmat_outputs"
# csv file for the dice scores/per label 
output_csv = "/path/to/save/dice_scores.csv"

# load the manual segmentation
manual = nib.load(manual_path).get_fdata()

# get the MASMAT result files
masmat_files = sorted([f for f in os.listdir(masmat_folder) if f.endswith(".nii.gz")])

results = []

# compare each MASMAT Output to Manual
for file in masmat_files:
    path = nib.load(os.path.join(masmat_folder, file)
    data = nib.load(path).get_fdata()
    data = np.rint(data).astype(int) 

    row = [file]
    # skip background (0)
    # MASMAT has 40 labels
    for label in range(1, 41): 
        m_mask = (manual == label)
        p_mask = (data == label)
        score = dice(m_mask, p_mask)
        row.append(round(score, 4))
    results.append(row)

# save as a csv file! 
header = ["Filename"] + [f"Label_{i}" for i in range(1, 40)]
with open(output_csv, "w", newline="") as f:
    csv.writer(f).writerows([header] + results)
