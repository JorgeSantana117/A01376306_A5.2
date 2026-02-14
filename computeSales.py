"""
This module computes the total sales from a price catalogue and a sales record.
"""
# pylint: disable=invalid-name
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
    except OSError as error:
        print(f"ERROR: OS error occurred: {error}")
    return None


def calculate_total_sales(catalogue, sales):
    """
    Computes total cost and tracks errors for missing products.
    Returns (total_cost, items_processed, error_list).
    """
    # Create lookup map for O(1) efficiency
    price_map = {}
    for item in catalogue:
        name = item.get("Product") or item.get("title")
        price = item.get("Price") or item.get("price")
        if name and price is not None:
            price_map[name] = price

    total_cost = 0.0
    items_processed = 0
    errors = []

    for sale in sales:
        product_name = sale.get("Product") or sale.get("product")
        quantity = sale.get("Quantity") or sale.get("quantity", 0)

        if product_name in price_map:
            try:
                total_cost += price_map[product_name] * float(quantity)
                items_processed += 1
            except (ValueError, TypeError):
                msg = f"DATA ERROR: Invalid quantity for '{product_name}'."
                print(msg)
                errors.append(msg)
        else:
            msg = f"CATALOGUE ERROR: Product '{product_name}' not found."
            print(msg)
            errors.append(msg)

    return total_cost, items_processed, errors


def main():
    """Main execution flow of the program."""
    start_time = time.time()

    # Arguments
    if len(sys.argv) != 3:
        print("Usage: python computeSales.py price.json sales.json")
        return

    price_file_path = sys.argv[1]
    sales_file_path = sys.argv[2]

    # Loading Data
    catalogue_data = load_json_file(price_file_path)
    sales_data = load_json_file(sales_file_path)

    if catalogue_data is None or sales_data is None:
        return

    # Calculations
    total_cost, processed, errors = calculate_total_sales(
        catalogue_data, sales_data
    )

    # Formatting and Output
    elapsed_time = time.time() - start_time

    report_lines = [
        "=" * 50,
        "             SALES EXECUTION REPORT",
        "=" * 50,
        f"Catalogue:      {price_file_path}",
        f"Sales Record:   {sales_file_path}",
        "-" * 50,
        f"Total Items:    {processed}",
        f"Total Cost:     ${total_cost:,.2f}",
        f"Time Elapsed:   {elapsed_time:.6f} seconds",
        "=" * 50
    ]

    if errors:
        report_lines.append(f"\nIssues encountered: {len(errors)}")

    final_report = "\n".join(report_lines)

    # Output to screen and file
    print(final_report)
    try:
        with open("SalesResults.txt", "w", encoding="utf-8") as f:
            f.write(final_report)
    except IOError as e:
        print(f"CRITICAL: Could not write result file: {e}")


if __name__ == "__main__":
    main()
