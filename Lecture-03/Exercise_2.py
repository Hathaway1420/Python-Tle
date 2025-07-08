pay1 = float(input("Enter the  number of hours worked"))
pay2 = float(input("Enter  the  hourly pay rate" )) 

if pay1 > 40:
    gross_pay = ((pay1 -40) * 1.5 * pay2 ) +( 40 * pay2)
else:
    gross_pay = pay1 * pay2
    print("The gross pay",gross_pay)