import sys
import time
import json

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
    catalogue_data = load_json_file(price_file_path)
    sales_data = load_json_file(sales_file_path)

	# If either file failed to load, we cannot proceed with calculations
    if catalogue_data is None or sales_data is None:
        return

    
    # Create a price lookup dictionary for efficiency
    # Mapping "Product Name" -> Price
    price_map = {}
    for item in catalogue_data:
        name = item.get("title") or item.get("product") # Support common JSON keys
        price = item.get("price")
        if name and price is not None:
            price_map[name] = price

    total_cost = 0.0
    errors_found = []

    # Process sales
    for sale in sales_data:
        product_name = sale.get("product")
        quantity = sale.get("quantity", 0)
        
        # Check if product exists in our catalogue
        if product_name in price_map:
            unit_price = price_map[product_name]
            total_cost += unit_price * quantity
        else:
            error_msg = f"Warning: Product '{product_name}' not found in catalogue."
            print(error_msg)
            errors_found.append(error_msg)

    # Final result calculation
    elapsed_time = time.time() - start_time

    # Final Output Display
    print("\n" + "="*40)
    print("           SALES REPORT")
    print("="*40)
    print(f"Total Items Processed: {len(sales_data)}")
    print(f"Total Sales Cost:      ${total_cost:,.2f}")
    print(f"Execution Time:        {elapsed_time:.4f} seconds")
    print("="*40)

if __name__ == "__main__":
    main()