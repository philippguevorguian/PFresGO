import pickle
import numpy

def read_pickle_file(file_path):
    try:
        with open(file_path, 'rb') as file:
            data = pickle.load(file)
            return data
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except pickle.UnpicklingError:
        print(f"Error: Failed to unpickle the file '{file_path}'.")
        return None

# Replace 'data.pickle' with the actual path to your pickle file
file_path = './BP_PFresGO_results.pckl'
pickle_data = read_pickle_file(file_path)

if pickle_data is not None:
    print("Contents of the pickle file:")
    print(pickle_data.keys())
    for key,value in pickle_data.items():
        print(key)
        print(type(value))
        if isinstance(value,numpy.ndarray):
            print(len(value[0]))
        print(len(value))
