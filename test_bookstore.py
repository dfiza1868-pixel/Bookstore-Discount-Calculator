from bookstore import calculate_bill


def test_less_than_five_books():
    assert calculate_bill(3, 100) == (300, 0, 300)


def test_five_books():
    assert calculate_bill(5, 100) == (500, 50, 450)


def test_ten_books():
    assert calculate_bill(10, 200) == (2000, 400, 1600)


def test_total_amount():
    total, discount, payable = calculate_bill(4, 150)
    assert total == 600


def test_discount_amount():
    total, discount, payable = calculate_bill(5, 100)
    assert discount == 50


def test_final_payable_amount():
    total, discount, payable = calculate_bill(10, 200)
    assert payable == 1600