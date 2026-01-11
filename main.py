import products
import store


# setup initial stock of inventory
product_list = [
    products.Product("MacBook Air M2", price=1450, quantity=100),
    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
    products.Product("Google Pixel 7", price=500, quantity=250),
]
best_buy = store.Store(product_list)


def start(store_object):
    while True:
        print("\nStore Menu")
        print("----------")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Please choose a number: ").strip()

        if choice == "1":
            active_products = store_object.get_all_products()
            if not active_products:
                print("No active products in store.")
            else:
                for p in active_products:
                    p.show()

        elif choice == "2":
            print(store_object.get_total_quantity())

        elif choice == "3":
            active_products = store_object.get_all_products()
            if not active_products:
                print("No active products available to order.")
                continue

            print("------")
            for i, p in enumerate(active_products, start=1):
                # Ausgabe wie in Demo (ungefähr)
                print(f"{i}. {p.name}, Price: ${p.price}, Quantity: {p.get_quantity()}")
            print("------")
            print("When you want to finish order, enter empty text.")

            shopping_list = []
            cart_summary = {}  # product -> total qty (für Anzeige am Ende)

            while True:
                product_input = input("Which product do you want to order? ").strip()

                if product_input == "":
                    break

                if not product_input.isdigit():
                    print("Please enter a valid product number.")
                    continue

                product_index = int(product_input)
                if product_index < 1 or product_index > len(active_products):
                    print("Product number out of range.")
                    continue

                selected_product = active_products[product_index - 1]

                qty_input = input("How many do you want? ").strip()
                if qty_input == "" or not qty_input.isdigit():
                    print("Please enter a valid amount.")
                    continue

                qty = int(qty_input)
                if qty <= 0:
                    print("Amount must be greater than 0.")
                    continue

                shopping_list.append((selected_product, qty))
                cart_summary[selected_product] = cart_summary.get(selected_product, 0) + qty

            if not shopping_list:
                print("No items ordered.")
                continue

            try:
                total_price = store_object.order(shopping_list)

                print("\nYour order:")
                print("-----------")
                for product_obj, total_qty in cart_summary.items():
                    line_price = product_obj.price * total_qty
                    print(f"- {product_obj.name} x{total_qty} = ${line_price}")
                print("-----------")
                print(f"Total price: ${total_price}")

            except Exception as e:
                print(f"Order failed: {e}")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    start(best_buy)