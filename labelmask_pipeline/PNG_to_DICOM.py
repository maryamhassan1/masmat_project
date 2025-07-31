import os
import numpy as np
import pydicom
from PIL import Image
from pydicom.uid import generate_uid

# folder with the original DICOMs (used as templates)
dicom_folder = "/path/to/original_dicom"  
# folder with the PNGs you want to convert
png_folder = "/path/to/png_folder" 
# where the new DICOMs will be saved
output_folder = "/path/to/output_dicom_folder"

# create the output directory if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# loop through each PNG in the folder
for png_file in os.listdir(png_folder):
    if not png_file.endswith(".png"):
        continue  # Skip non-PNG files

    # match the PNG with the DICOM using base name
    base_name = os.path.splitext(png_file)[0]
    dicom_path = os.path.join(dicom_folder, f"{base_name}.dcm")
    png_path = os.path.join(png_folder, png_file)

    if not os.path.exists(dicom_path):
        continue

    # load the original DICOM:  gives us the metadata/header
    dicom_dataset = pydicom.dcmread(dicom_path)

    # load PNG and convert to grayscale ('L' = 8-bit pixels, black and white)
    image = Image.open(png_path).convert("L")
    pixel_array = np.array(image, dtype=np.uint8)

    # Replace pixel data in DICOM and update key metadata fields
    dicom_dataset.Rows, dicom_dataset.Columns = pixel_array.shape
    dicom_dataset.PhotometricInterpretation = "MONOCHROME2"  # 0 = black
    dicom_dataset.SamplesPerPixel = 1
    dicom_dataset.BitsAllocated = 8
    dicom_dataset.BitsStored = 8
    dicom_dataset.HighBit = 7
    dicom_dataset.PixelRepresentation = 0  
    dicom_dataset.PixelData = pixel_array.tobytes()

    # generate new unique identifiers
    dicom_dataset.SOPInstanceUID = generate_uid()
    dicom_dataset.SeriesInstanceUID = generate_uid()
    dicom_dataset.StudyInstanceUID = generate_uid()

    # save the updated DICOM to the output folder
    out_path = os.path.join(output_folder, f"{base_name}.dcm")
    dicom_dataset.save_as(out_path)

