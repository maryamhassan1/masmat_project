# masmat_project — Preprocessing for Mouse Brain Segmentation

This repository contains Python and MATLAB scripts for preprocessing and evaluating mouse brain MRIs before and after running MASMAT. It includes utilities to convert between DICOM, PNG, and NIfTI formats, create label masks, reorient/resample volumes, and evaluate MASMAT outputs using Dice similarity coefficients.

---

##  Project Structure

```
masmat_project/
├── labelmask_pipeline/          # Scripts to convert between DICOM, PNG, and back
│   ├── Check_DICOM_Header.py
│   ├── DICOM_to_PNG.py
│   ├── PNG_to_DICOM.py
│
├── manual_segmentation/         # Create label masks from coloured PNGs
│   ├── Color_to_Label_Map.py
│   ├── Create_Label_Masks.py
│   ├── PNG_to_Nifti.py
│
├── reorient_axes.m              # Reorients NIfTI volumes (permute + flip)
├── resampled_to_dimensions.m    # Resamples NIfTI volumes to target MASMAT shape/voxel size
├── calculate_dice_coefficient.py # Compares MASMAT outputs to manual segmentation
├── README.md
```


---

## Scripts Overview

### `labelmask_pipeline/`
- `Check_DICOM_Header.py`: View metadata of a DICOM file.
- `DICOM_to_PNG.py`: Convert DICOM image slices to grayscale PNGs.
- `PNG_to_DICOM.py`: Convert PNGs (e.g., overlays or masks) back to DICOM using a template DICOM stack.

### `manual_segmentation/`
- `Color_to_Label_Map.py`: Define RGB → label index mapping for each brain region.
- `Create_Label_Masks.py`: Convert PNG masks into integer-labeled masks.
- `PNG_to_Nifti.py`: Stack label PNGs into a 3D NIfTI volume.

### `MATLAB_scripts/`
- `reorient_axes.m`: Fixes image orientation by permuting and flipping axes.
- `resampled_to_dimensions.m`: Resamples NIfTI volumes 

### `Evaluation/`
- `calculate_dice_coefficient.py`: Calculates Dice score for each brain region (1–40) comparing MASMAT outputs to manual labels.

---

## How to Use

1. Clone this repo or download the scripts you need.
2. Update input/output paths in each script to match your directory structure.
3. Run each script individually using Python 3.x or MATLAB.

---

## Dependencies

**Python**
- `numpy`
- `pydicom`
- `Pillow`
- `matplotlib`
- `nibabel`

Install them with:

```bash
pip install numpy pydicom Pillow matplotlib nibabel

### MATLAB
Requires the **NIfTI Toolbox**:
- Functions used: `load_nii`, `save_nii`




