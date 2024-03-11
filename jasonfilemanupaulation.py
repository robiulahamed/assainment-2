import json
import os

def read_json_file(filename):
    
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
        return None
    except PermissionError:
        print(f"Error: Permission denied to open the file '{filename}'.")
        return None
    except json.JSONDecodeError as e:
        print(f"Error: JSON decoding failed: {e}")
        return None
    except Exception as e:
        print(f"An error occurred while reading the file '{filename}': {e}")
        return None

def write_json_file(filename, data):
    
    try:
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)
        print(f"Data has been written to '{filename}' successfully.")
    except PermissionError:
        print(f"Error: Permission denied to write to the file '{filename}'.")
    except Exception as e:
        print(f"An error occurred while writing to the file '{filename}': {e}")

def update_json_data(filename, updates):
   
    
    existing_data = read_json_file(filename) or {}


    existing_data.update(updates)

  
    write_json_file(filename, existing_data)

if __name__ == "__main__":
   
    updates = {
        "name": "Ahamed  Robiul",
        "age": 22,
        "city": "Mymensingh"
    }

    
    json_file = "data.json"

   
    update_json_data(json_file, updates)
