import h5py
import glob
import os
import argparse

def copy(dest, name):
    g = dest.require_group(name)
    def callback(name, node):
        if isinstance(node, h5py.Dataset):
            if name not in g:  # Check if dataset already exists
                try:
                    g.create_dataset(name, data=node[:])
                except MemoryError:  # Handle large datasets
                    # Read and write in chunks
                    dset_out = g.create_dataset(name, shape=node.shape, dtype=node.dtype)
                    for i in range(node.shape[0]):
                        dset_out[i] = node[i]
                except Exception as e:
                    print(f'Error copying dataset {name}: {e}')
            else:
                print(f'Dataset {name} already exists in group {g.name}')
        elif isinstance(node, h5py.Group):
            if node.attrs:  # If group has attributes
                for key, value in node.attrs.items():
                    g.attrs[key] = value
    return callback

def merge_files(directory, output_file):
    # Use glob to find all .h5 files in the directory that include the substring "_res"
    files = glob.glob(os.path.join(directory, '*_res_*.h5'))
    if not files:
        print(f"No files found in directory {directory} with '_res' in the name.")
        return
    with h5py.File(output_file, 'w') as h5_out:
        for f_in in files:
            try:
                with h5py.File(f_in, 'r') as h5_in:
                    h5_in.visititems(copy(h5_out, f_in))
            except Exception as e:
                print(f'Error processing file {f_in}: {e}')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Merge .h5 files')
    parser.add_argument('directory', help='Directory containing .h5 files')
    parser.add_argument('output_file', help='Output file name')
    args = parser.parse_args()

    merge_files(args.directory, args.output_file)

