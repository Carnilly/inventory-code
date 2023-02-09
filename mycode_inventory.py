import os
import csv
inventory = []
orders = []
shows = []
password = "Forget-75"


def add_card(item, price, show):
    # Add the card to the inventory list
    inventory.append({'item': item, 'price': price, 'show': show})

    # Write the updated inventory to a CSV file
    with open('inventory.csv', 'w', newline='') as csvfile:
        fieldnames = ['item', 'price', 'show']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for card in inventory:
            writer.writerow(card)
            
            
def delete_card(item):
    for i, card in enumerate(inventory):
        if card['item'] == item:
            del inventory[i]
            break

    # Write the updated inventory to a CSV file
    with open('inventory.csv', 'w', newline='') as csvfile:
        fieldnames = ['item', 'price', 'show']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for card in inventory:
            writer.writerow(card)



def view_inventory():
    while True:
        print("Inventory:")
        for i, item in enumerate(inventory):
            print(f"{i + 1}. {item['item']} - ${item['price']} (From: {item['show']})")
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

def sell_card(item, price):
    for i, card in enumerate(inventory):
        if card['item'] == item:
            net_sale = round(price * 0.88, 2)
            order = {'item': item, 'price': price, 'net_sale': net_sale}
            orders.append(order)
            del inventory[i]
            break

    # Write the new order to a CSV file
    with open('orders.csv', 'a', newline='') as csvfile:
        fieldnames = ['item', 'price', 'net_sale']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(order)


def view_orders():
    print("Orders:")
    for i, order in enumerate(orders):
        print(f"{i + 1}. {order['item']} - ${order['price']} (Net Sale: ${order['net_sale']})")


def add_show(show):
    shows.append(show)
    write_to_file('shows.txt', shows)


def view_shows():
    print("Shows:")
    for i, show in enumerate(shows):
        print(f"{i + 1}. {show}")


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
        ''')
        choice = input("Select Choice: ")
        if choice == '1':
            item = input("Enter Card: ")
            price = float(input("Enter Price: "))
            show = input("Enter Show: ")
            add_card(item, price, show)
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
            item = input("Enter the card you want to delete: ")
            delete_card(item)

        else:
            print("Invalid Choice")


if __name__ == '__main__':
    main()

