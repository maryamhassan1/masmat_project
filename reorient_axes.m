% script to reorient NIfTI volumes by permuting and flipping axes for MASMAT

% folder with original .nii.gz files
input_dir = '/path/to/original/nifti';      
% folder to save  files
output_dir = '/path/to/save/reoriented/nifti'; 

% create output folder if it doesn't exist
if ~exist(output_dir, 'dir')
    mkdir(output_dir);
end

% get all .nii.gz files in the input directory
nii_files = dir(fullfile(input_dir, '*.nii.gz'));

% loop through each file
for k = 1:length(nii_files)
    filename = nii_files(k).name;
    input_path = fullfile(input_dir, filename);

    % load the NIfTI file (set last argument to 1 to preserve orientation)
    nii = load_nii(input_path, '', '', '', '', '', 1);

    % swap Y and Z axes, then flip along the new Z-axis (slice axis)
    reoriented_img = permute(nii.img, [1 3 2]);
    reoriented_img = flip(reoriented_img, 3);  % flip along slices

    % update image data
    nii.img = reoriented_img;

    % save the updated NIfTI
    output_path = fullfile(output_dir, filename);
    save_nii(nii, output_path);

end
