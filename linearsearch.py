Certainly! Here's a simple Python program that performs a linear search to find a product in a list:

```python
def linear_search_product(products, target_product):
    for index, product in enumerate(products):
        if product == target_product:
            return index
    return -1  # Return -1 if the target product is not found

# Example usage:
products_list = ["Laptop", "Phone", "Tablet", "Camera", "Headphones"]

target_product = input("Enter the product you're searching for: ")

index = linear_search_product(products_list, target_product)

if index != -1:
    print(f"{target_product} found at index {index}.")
else:
    print(f"{target_product} not found in the list.")
```

In this program, the `linear_search_product` function takes a list of products and a target product as parameters. It iterates through the list using a linear search and returns the index of the target product if found, otherwise, it returns -1. The example usage demonstrates how to use this function to search for a product in a list.
