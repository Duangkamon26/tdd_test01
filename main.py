from test_motorcycle_payment import calculate_monthly_payment

def main():
    # ให้ผู้ใช้ป้อนราคารถจักรยานยนต์และเงินดาวน์
    while True:
        try:
            motorcycle_price = float(input("Enter the motorcycle price : "))
            if motorcycle_price <= 0:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please enter a positive number.")
    while True:
        try:
            down_payment = float(input("Enter the down payment: "))
            if down_payment <= 0 or down_payment < motorcycle_price * 0.2:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please enter a positive number.")
            print("Down payment must be at least 20% of the motorcycle price.")

    # คำนวณการชำระเงินรายเดือนโดยใช้ฟังก์ชัน
    monthly_payment = calculate_monthly_payment(motorcycle_price, down_payment)

    # แสดงการชำระเงินรายเดือนแก่ผู้ใช้
    print("Monthly payment: {:.2f} Baht".format(monthly_payment))

if __name__ == '__main__':
    main()
