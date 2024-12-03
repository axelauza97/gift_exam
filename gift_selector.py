import sys


def is_integer(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


try:
    # Predefined list of gifts
    gifts = [
        "Book",
        "Toy",
        "Gadget",
        "Video Game",
        "Headphones",
        "Smartphone",
        "Laptop",
        "Watch",
        "Shoes",
        "Wallet",
        "Headset",
        "Camera",
        "Drone",
        "Smart Watch",
        "Bluetooth Speaker",
    ]

    # Display available gifts
    print("<html><head><title>Gift Selector</title></head><body>")
    print("<h2>Available Gifts:</h2>")
    for index, gift in enumerate(gifts):
        print(f"<p>{index}: {gift}</p>")

    # Get user input for selected gift indices
    input_string = sys.argv[1]

    # Split the input string by commas to get individual values
    inputs = input_string.split(",")

    if len(inputs) < 1:
        print("<p>Error: At least one input value is required.</p>")
        raise "Error"

    # Check if all inputs are integers and within the valid range
    if not all(
        is_integer(val.strip()) and 0 <= int(val.strip()) < len(gifts) for val in inputs
    ):
        print("<p>Error: All inputs must be valid indices of the gift list.</p>")
        raise "Error"

    # Convert inputs to integers
    selected_indices = [int(val.strip()) for val in inputs]

    # Calculate the unique gift code using bitwise OR
    gift_code = 0
    selected_gifts = []
    for index in selected_indices:
        gift_code |= 1 << index
        selected_gifts.append(gifts[index])

    # Generate HTML output
    print("<h2>Selected Gifts:</h2>")
    print(f"<p>{', '.join(selected_gifts)}</p>")
    print(f"<p>Unique Gift Code: {gift_code}</p>")
    print("</body></html>")

except Exception as e:
    print(f"<html><body><p>Error: {str(e)}</p></body></html>")
