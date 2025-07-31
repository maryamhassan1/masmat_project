# masmat_project
# masmat_project — Preprocessing Utilities

This repository contains Python scripts for preprocessing DICOM and PNG images as part of a brain MRI segmentation pipeline. These tools were used before running MASMAT on mouse brain MRIs.

## Contents

- `check_dicom_header.py`: View the metadata of a DICOM file.
- `dicom_to_png.py`: Convert DICOM image slices to grayscale PNGs.
- `png_to_dicom.py`: Convert PNGs (e.g., manual segmentations) back to DICOM using metadata from template files.

## How to Use

1. Clone this repo or copy the scripts locally.
2. Edit the folder paths in each script to match your own system.
3. Run the scripts using Python 3.x.

## Requirements

- `pydicom`
- `numpy`
- `Pillow`
- `matplotlib`

You can install them via:

```bash
pip install pydicom numpy Pillow matplotlib
