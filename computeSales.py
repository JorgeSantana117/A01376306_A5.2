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
        print(f"ERROR: The file '{file_path}' was not found.")
    except json.JSONDecodeError:
        print(f"ERROR: The file '{file_path}' contains invalid JSON format.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
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
        # Handling common variations in JSON keys
        name = item.get("Product") or item.get("title")
        price = item.get("Price") or item.get("price")
        if name and price is not None:
            price_map[name] = price

    total_cost = 0.0
    items_processed = 0
    errors = []

    # Process each sale
    for sale in sales_data:
        product_name = sale.get("Product") or sale.get("product")
        quantity = sale.get("Quantity") or sale.get("quantity", 0)
        
        if product_name in price_map:
            total_cost += price_map[product_name] * quantity
            items_processed += 1
        else:
            err = f"INVALID DATA: Product '{product_name}' not in catalogue. Skipping."
            print(err)
            errors.append(err)

    # Final result calculation
    elapsed_time = time.time() - start_time
    
    # Final Output Display
    report = []
    report.append("=" * 40)
    report.append("          SALES EXECUTION REPORT")
    report.append("=" * 40)
    report.append(f"Catalogue File:    {price_file_path}")
    report.append(f"Sales Record File: {sales_file_path}")
    report.append("-" * 40)
    report.append(f"Total Sales Items: {items_processed}")
    report.append(f"Total Cost:        ${total_cost:,.2f}")
    report.append(f"Execution Time:    {elapsed_time:.6f} seconds")
    report.append("=" * 40)
    
    if errors:
        report.append(f"\nNotes: {len(errors)} errors encountered during processing.")

    final_output = "\n".join(report)

    # Print to Screen
    print(final_output)

    # Print to File
    try:
        with open("SalesResults.txt", "w", encoding="utf-8") as f:
            f.write(final_output)
    except Exception as e:
        print(f"Error saving the results file: {e}")

if __name__ == "__main__":
    main()