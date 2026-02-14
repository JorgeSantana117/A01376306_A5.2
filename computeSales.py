import sys
import time
import json

def main():
    # Start the timer
    start_time = time.time()

    # sys.argv[0] is the script name, [1] and [2] should be the files
    if len(sys.argv) != 3:
        print("Usage: python computeSales.py priceCatalogue.json salesRecord.json")
        return

    price_file = sys.argv[1]
    sales_file = sys.argv[2]

    print(f"--- Execution Started ---")
    print(f"Loading Catalogue: {price_file}")
    print(f"Loading Sales Record: {sales_file}")
    
    # Placeholder for total
    total_cost = 0.0

    # Calculate elapsed time
    end_time = time.time()
    elapsed_time = end_time - start_time

    # Final Output Display
    print("\n" + "="*30)
    print(f"TOTAL SALES COST: ${total_cost:,.2f}")
    print(f"Execution Time: {elapsed_time:.4f} seconds")
    print("="*30)

if __name__ == "__main__":
    main()