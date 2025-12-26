# Simple Shopping Cart Program
print("welcome Simple Shopping Cart Program")

# Initialize an empty cart
cart = []

while True:
    # Display menu options
    print("\n----- Cart Menu -----")
    print("1. Add item")
    print("2. View items")
    print("3. Remove item")
    print("4. Checkout")

    # Get user choice safely
    try:
        choice = int(input("Enter your choice (1-4): "))
    except ValueError:
        print("Please enter a valid number between 1 and 4.")
        continue

    # Option 1: Add item
    if choice == 1:
        print("\nAdd your item")
        item = input("Enter your item: ").strip()
        if item:  # Avoid adding empty strings
            cart.append(item)
            print(f"'{item}' added to cart.")
        else:
            print("Item name cannot be empty.")

    # Option 2: View items
    elif choice == 2:
        print("\nYour items:")
        if len(cart) == 0:
            print("Cart is empty.")
        else:
            for i, item in enumerate(cart, 1):
                print(f"{i}. {item}")

    # Option 3: Remove item
    elif choice == 3:
        if len(cart) == 0:
            print("Cart is empty, nothing to remove.")
        else:
            name = input("Enter the item to remove: ").strip()
            if name in cart:
                cart.remove(name)
                print(f"'{name}' removed from cart.")
            else:
                print(f"'{name}' not found in cart.")

    # Option 4: Checkout
    elif choice == 4:
        print("\n----- Checkout -----")
        print(f" You purchased {len(cart)} item(s).")
        print("Your items are:", cart)
        print("Thank you for shopping!")
        break  # Exit the loop

    # Invalid input
    else:
        print("Invalid choice. Please select between 1 and 4.")