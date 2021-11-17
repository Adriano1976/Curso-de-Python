import csv

all_product = {}


def main():
    product_index = 0
    name_index = 1
    price_index = 2
    quantity_index = 1
    product_request_index = 0

    read_product_store = read_product(
        "products.csv",
        product_index,
        name_index,
        price_index,
    )

    print()
    with open("products.csv", 'r', encoding='utf8', newline='') as product_file:
        product = csv.reader(product_file)
        for products in product:
            print(products)

    print()
    with open("request.csv", 'r', encoding='utf8', newline='') as request_file:
        request = csv.reader(request_file)
        for products in request:
            print(products)

        for row in request:
            product_name = row[0]
            quantity = row[quantity_index]
            price = row[price_index]

            all_product[product_name] = [quantity, price]

            print(all_product)


def read_product(filename, key_product, value_name, value_price):
    with open(filename, "r") as infile:
        reader = csv.reader(infile)

        for row in reader:
            product = row[key_product]
            name = row[value_name]
            price = row[value_price]

            all_product[product] = [name, price]
    return all_product


if __name__ == "__main__":
    main()
