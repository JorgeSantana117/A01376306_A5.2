import sys
import time
import json
import os

def load_json_file(file_path):
    """
    Loads a JSON file and handles potential errors.
    Returns the data if successful, or None if an error occurs.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except json.JSONDecodeError:
        print(f"Error: The file '{file_path}' contains invalid JSON format.")
    except Exception as e:
        print(f"An unexpected error occurred while reading '{file_path}': {e}")
    return None

def main():
    # Start the timer
    start_time = time.time()

    # sys.argv[0] is the script name, [1] and [2] should be the files
    if len(sys.argv) != 3:
        print("Usage: python computeSales.py priceCatalogue.json salesRecord.json")
        return

    price_file_path = sys.argv[1]
    sales_file_path = sys.argv[2]

    # Loading Data
    print(f"--- Processing Files ---")
    
    catalogue_data = load_json_file(price_file_path)
    sales_data = load_json_file(sales_file_path)

    # If either file failed to load, we cannot proceed with calculations
    if catalogue_data is None or sales_data is None:
        print("Execution halted due to file errors.")
        return

    # --- Verification Step ---
    print(f"Success: Loaded {len(catalogue_data)} items from catalogue.")
    print(f"Success: Loaded {len(sales_data)} sales records.")

    # Final Output Display
    elapsed_time = time.time() - start_time
    print("\n" + "="*30)
    print(f"Execution Time: {elapsed_time:.4f} seconds")
    print("="*30)

if __name__ == "__main__":
    main()