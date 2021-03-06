'''
This is a program that calculates the tip and the bill total.
The bill can also be split.
'''

tip_amount = 0
total_bill = 0
split_bill = 0


def calculate_bill(original_bill_amount, tip_percentage = 18, split_number = 1):
    global tip_amount
    tip_amount = original_bill_amount * tip_percentage * .01
    global total_bill
    total_bill = original_bill_amount + tip_amount
    global split_bill
    split_bill = total_bill / split_number


def main():
    original_bill = 100
    calculate_bill(original_bill)
    print "original bill is", original_bill
    print "tip amount", tip_amount
    print "total bill", total_bill
    print "split amount", split_bill

    calculate_bill(original_bill, tip_percentage=20)
    print "original bill is", original_bill
    print "tip amount", tip_amount
    print "total bill", total_bill
    print "split amount", split_bill

    calculate_bill(original_bill, split_number=4)
    print "original bill is", original_bill
    print "tip amount", tip_amount
    print "total bill", total_bill
    print "split amount", split_bill

    calculate_bill(original_bill, 20, 3)
    print "original bill is", original_bill
    print "tip amount", tip_amount
    print "total bill", total_bill
    print "split amount", split_bill


if __name__ == "__main__":
    main()
