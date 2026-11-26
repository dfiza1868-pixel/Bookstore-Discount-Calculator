def calculate_bill(quantity, price):
    total = quantity * price

    if quantity >= 10:
        discount_rate = 0.20
    elif quantity >= 5:
        discount_rate = 0.10
    else:
        discount_rate = 0.0

    discount = total * discount_rate
    payable = total - discount

    return total, discount, payable


if __name__ == "__main__":
    quantity = int(input("Enter number of books: "))
    price = float(input("Enter price per book: "))

    total, discount, payable = calculate_bill(quantity, price)

    print("\n--- Bookstore Bill ---")
    print("Total Amount: Rs.", total)
    print("Discount: Rs.", discount)
    print("Final Payable Amount: Rs.", payable)