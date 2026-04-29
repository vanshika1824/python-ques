def vending_machine():
    trays = {
        '1': ("Snacks", {
            'a': ("Lays", 25),
            'b': ("Uncle Chips", 20),
            'c': ("Doritos", 30)
        }),
        '2': ("Beverages", {
            'a': ("Diet Coke", 40),
            'b': ("Pepsi", 35),
            'c': ("RED BUll", 30)
        }),
        '3': ("Chocolates", {
            'a': ("Dairy Milk", 50),
            'b': ("KitKat", 45),
            'c': ("Snickers", 60)
        })
    }

    cart = []
    total = 0

    while True:
        print("\n--- Vending Machine ---")
        print("1: Snacks")
        print("2: Beverages")
        print("3: Chocolates")
        print("c: Checkout")
        print("0: Exit")

        tray = input("Select option: ")

        if tray == '0':
            print("Exiting...")
            return

        if tray == 'c':
            break   #  go to payment

        if tray not in trays:
            print("Invalid choice!")
            continue

        tray_name, items = trays[tray]
        print(f"\n{tray_name}:")

        for key, val in items.items():
            print(f"{key}. {val[0]} ({val[1]})")

        choice = input("Choose item: ")

        if choice not in items:
            print("Invalid item!")
            continue

        item_name, price = items[choice]
        cart.append((item_name, price))
        total += price

        print(f" {item_name} added to cart. Total = {total}")

    # BILL + PAYMENT
    if not cart:
        print("Cart is empty.")
        return

    print("\n--- BILL ---")
    for item in cart:
        print(f"{item[0]} - {item[1]}")
    print(f"Total: {total}")

    try:
        amount = int(input("Enter payment: "))
    except ValueError:
        print("Invalid input!")
        return

    if amount < total:
        print(" Not enough money!")
    else:
        print(f"Paid: {amount}")
        print(f"Change: {amount - total}")
        print(" Thank you! Collect your items.")


vending_machine()
