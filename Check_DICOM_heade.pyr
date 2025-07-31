import os # to manipulate the files
import pydicom # works with DICOM images

#path to folder 
folder_path = '/path/to/your/dicom/folder'
for filename in os.listdir(folder_path):
    if filename.endswith(".dcm"):
        file_path = os.path.join(folder_path, filename)
        dcm = pydicom.dcmread(file_path)
        print(dcm)  # prints the full DICOM header
