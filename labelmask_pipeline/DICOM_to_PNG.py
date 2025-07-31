import os  # to manipulate the files
import pydicom  # works with DICOM images
import matplotlib.pyplot as plt  # used to save images as PNGs

# path to folder containing DICOM slices
dicom_folder = '/path/to/your/dicom/folder'

# output folder for PNGs
output_folder = os.path.join(dicom_folder, "PNG")
os.makedirs(output_folder, exist_ok=True)

# convert each DICOM file to PNG
for filename in os.listdir(dicom_folder):
    if filename.endswith(".dcm"):
        file_path = os.path.join(dicom_folder, filename)
        dicom_dataset = pydicom.dcmread(file_path)
        image = dicom_dataset.pixel_array

        png_name = filename.replace(".dcm", ".png")
        png_path = os.path.join(output_folder, png_name)
        # save as greyscale image
        plt.imsave(png_path, image, cmap="gray")
