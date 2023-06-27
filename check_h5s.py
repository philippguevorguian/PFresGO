import h5py
import argparse


parser = argparse.ArgumentParser(description="confirm existence and validity of generated embeddings")
parser.add_argument('file_path', type=str, help='Path to the h5 embedding file')
args = parser.parse_args()
file_path = args.file_path
# Open the HDF5 file in read mode
file = h5py.File(file_path, 'r')

# Get a list of all dataset names in the file
dataset_names = list(file.keys())

# Print the dataset names
for name in dataset_names:
    print(name)
    print(file[name])


# Close the file when finished
file.close()
