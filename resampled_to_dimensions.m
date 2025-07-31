% folder with NIfTI files to resample
input_dir = "/path/to/niftis"; 
% output folder
output_dir = "/path/to/output/folder";
% reference NIfTI for orientation (optional)
ref_path = "/path/to/reference/nifti";

% create output directory 
if ~exist(output_dir, 'dir')
    mkdir(output_dir);
end

% load reference NIfTI 
ref_nii = load_nii(ref_path, '', '', '', '', '', 1);

% target dimensions and voxel size
% these were used for my MASMAT sizes
% in (X, Y, Z)
target_dim = [150, 30, 120]; 
% in (X, Y, Z) in mm
target_vox = [0.1, 0.5, 0.1];

% list all NIfTI files in the folder
nii_files = dir(fullfile(input_dir, '*.nii.gz'));

% process each file
for k = 1:length(nii_files)
    filename = nii_files(k).name;
    input_path = fullfile(input_dir, filename);
    output_path = fullfile(output_dir, filename);

    % load the NIfTI file
    nii = load_nii(input_path, '', '', '', '', '', 1);

    % resample the image to target dimensions
    resampled_img = imresize3(nii.img, target_dim, 'nearest');

    % update metadata and header information
    nii.img = resampled_img;
    nii.hdr.dime.dim(2:4) = target_dim;
    nii.hdr.dime.pixdim(2:4) = target_vox;

    % save the new file
    save_nii(nii, output_path);

end
