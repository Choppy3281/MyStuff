def main():
    gross_pay = float(input("Enter your gross pay: $"))
    tax_rate = float(input("Enter the tax rate: "))
    deductions = float(input("Enter the total deductions: "))
    net_pay = 0.0
    
    
    net_pay = CalcNet(gross_pay, tax_rate, deductions)
    print("Your total net pay is: $", format(net_pay, ',.2f'))
    
def CalcNet(gross_pay, tax_rate, deductions):
    net_pay = (gross_pay * (1 - tax_rate)) - deductions
    
    return net_pay

main()

