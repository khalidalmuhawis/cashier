def main():
    item = 0
    list = []
    total = 0

    while item != "done":
        items = {}
        item = input("Enter item name: ")
        if item != "done":
            price = int(input("Enter item price: "))
            quantity = int(input("Enter item quantity: "))
            items["name"] = item
            items["price"] = price
            items["quantity"] = quantity
            list.append(items)

    for x in list:
        total += x["price"] * x["quantity"]

    for x in list:
        print(x["quantity"] , x["name"] , x["price"] * x["quantity"])

    print("Total Price: " , total)


if __name__ == '__main__':
    main()
