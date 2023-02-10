import os
import csv

inventory = []
orders = []
shows = []
password = "Forget-75"


def add_card(item, show):
    # Add the card to the inventory list
    inventory.append({'item': item, 'show': show})

    # Write the updated inventory to a CSV file
    with open('inventory.csv', 'a', newline='') as csvfile:
        fieldnames = ['item', 'show']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, extrasaction='ignore')
        writer.writeheader()
        for card in inventory:
            writer.writerow(card)


def delete_card(item):
    for i, card in enumerate(inventory):
        if card['item'] == item:
            del inventory[i]
            break
    else:
        print("Card not found in inventory.")
        return

    # Write the updated inventory to a CSV file
    with open('inventory.csv', 'w', newline='') as csvfile:
        fieldnames = ['item', 'price', 'show']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for card in inventory:
            writer.writerow(card)
    print("Card deleted successfully.")


def view_inventory():
    while True:
        print("Inventory:")
        for i, item in enumerate(inventory):
            print(f"{i + 1}. {item['item']} - (From: {item['show']})")
        print("\n")
        print("0. Back")
        choice = input("Enter the number of the card you want to view or 0 to go back: ")
        if choice.isdigit() and 0 < int(choice) <= len(inventory):
            print(
                f"\n{inventory[int(choice) - 1]['item']} - ${inventory[int(choice) - 1]['price']} (From: {inventory[int(choice) - 1]['show']})\n")
        elif choice == '0':
            break
        else:
            print("Invalid Choice!")


def sell_card(item, net_sale):
    for i, card in enumerate(inventory):
        if card['item'] == item:
            net_sale = round(net_sale * 0.88, 2)
            order = {'item': item, 'net_sale': net_sale}
            orders.append(order)
            del inventory[i]
            break
    else:
        print(f"Item '{item}' not found in inventory.")
        return

    # Write the new order to a CSV file
    with open('orders.csv', 'a', newline='') as csvfile:
        fieldnames = ['item', 'net_sale']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(order)
    print(f"Item '{item}' sold for {net_sale} and added to orders.")


def view_orders():
    while True:
        print("Orders:")
        for i, item in enumerate(orders):
            print(f"{i + 1}. {item['item']} - (From: {item['net_sale']})")
        print("\n")
        print("0. Back")
        choice = input("Enter the number of the card you want to view or 0 to go back: ")
        if choice.isdigit() and 0 < int(choice) <= len(orders):
            print(
                f"\n{orders[int(choice) - 1]['item']} - (From: {orders[int(choice) - 1]['net_sale']})\n")
        elif choice == '0':
            break
        else:3
            print("Invalid Choice!")
    '''print("Orders:")
    try:
        with open("orders.csv", "r") as file:
            reader = csv.DictReader(file)
            order_list = list(reader)
            if not order_list:
                print("No orders found.")
            else:
                for i, order in enumerate(order_list):
                    print(
                        f"{i + 1}. {order['item']} - ${float(order['price']):.2f} (Net Sale: ${float(order['net_sale']):.2f})")
    except Exception as e:
        print(f"An error occurred while trying to read the file: {e}")'''


def add_show(show):
    shows.append(show)
    write_to_file('shows.txt', shows)


def view_shows():
    print("Shows:")
    for i, show in enumerate(shows):
        print(f"{i + 1}. {show}")


def delete_order(order_id):
    # Read the CSV file into a list of dictionaries
    with open('orders.csv', 'r') as file:
        reader = csv.DictReader(file)
        orders = list(reader)

    # Find the order with the specified order_id
    for i, order in enumerate(orders):
        if order['item'] == order_id:
            # Remove the order from the list
            del orders[i]
            break
    else:
        # If the order was not found, print an error message
        print(f"Error: Order with ID {order_id} was not found.")
        return

    # Write the updated orders back to the file
    with open('orders.csv', 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['item', 'price', 'net_sale'])
        writer.writeheader()
        writer.writerows(orders)

    print(f"Order with ID {order_id} was deleted.")


def logout():
    os.exit(0)


def write_to_file(filename, data):
    with open(filename, 'w') as file:
        for item in data:
            file.write(str(item) + '\n')


def main():
    print("Enter password: ")
    entered_password = input()
    if entered_password != password:
        print("Incorrect password, exiting...")
        os.exit(0)

    while True:
        print('''
        1.) Add Inventory
        2.) View Inventory
        3.) Sell Card
        4.) View Orders
        5.) Add Show
        6.) View Shows
        7.) Logout
        8.) Delete Card
        9.) Delete Order
        ''')
        choice = input("Select Choice: ")
        if choice == '1':
            item = input("Enter Card: ")
            show = input("Enter Show: ")
            add_card(item, show)
        elif choice == '2':
            view_inventory()
        elif choice == '3':
            item = input("Enter Card: ")
            price = float(input("Enter Price: "))
            sell_card(item, price)
        elif choice == '4':
          view_orders()
        elif choice == '5':
            show = input("Enter Show: ")
            add_show(show)
        elif choice == '6':
            view_shows()
        elif choice == '7':
            logout()
        elif choice == '8':
            item = input("Enter the name of the card to delete: ")
            delete_card(item)
        elif choice == '9':
            order_id = input("Enter the order # you would like to delete: ")
            delete_order(order_id)
        else:
            print("Invalid Choice")


if __name__ == '__main__':
    main()
