"""Program that read two json file inputs. The first
input contains the price and the second the quantity,
the program calculate the sales
"""
import json
import time
import sys


def load_json_file(file_path):
    """Function that read a json. The two json files
    accepted for this program are: one of prices and
    second of quantities
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def calculate_total_cost(catalogue, sales):
    """Function that does the product between two json
    files to get the sales
    """
    total_cost = 0
    for sale in sales:
        product_name = sale["Product"]
        quantity = sale["Quantity"]

        # Find the product in the catalogue
        product = next((item for item in catalogue
                        if item["title"] == product_name), None)

        if product:
            total_cost += quantity * product["price"]

    return total_cost


def main():
    """Function that contains the logic of the program.
    Use the two arguments in the function
    calculate_total_cost and print the result on the screen"""
    if len(sys.argv) != 3:
        print("Usage: python computeSales.py priceCatalogue.json \
                salesRecord.json")
        sys.exit(1)

    catalogue_file = sys.argv[1]
    sales_file = sys.argv[2]

    # Load catalogue and sales data
    catalogue = load_json_file(catalogue_file)
    sales = load_json_file(sales_file)

    # Calculate total cost
    start_time = time.time()
    total_cost = calculate_total_cost(catalogue, sales)
    end_time = time.time()

    # Print results to screen
    print(f"Total Cost: ${total_cost:.2f}")
    print(f"Time Elapsed: {end_time - start_time:.4f} seconds")

    # Write results to file
    with open("SalesResults.txt", 'w', encoding='utf-8') as results_file:
        results_file.write(f"Total Cost: ${total_cost:.2f}\n")
        results_file.write(f"Time Elapsed: \
                            {end_time - start_time:.4f} seconds\n")


if __name__ == "__main__":
    main()
