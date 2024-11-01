#under 12,000 = 5% tax rate             #for single filers
#12,000-24,999.99 = 10% tax rate
#25,000 - 74,999.99 = 15% tax rate
#75,000 and over = 20% tax rate
#
#
#under 12,000 = 0%                  #joint filers
#12,000- 24,999.99 = 6%
#25,000- 74,999.99 = 11%
#75,000 and over = 20%

def caclulate_gross_pay(pay_rate, hours_worked):
    max_hours = 40
    if hours_worked > 40:
        overtime_hours = hours_worked - max_hours
        weekly_gross_pay = (max_hours * pay_rate) + (overtime_hours * pay_rate * 1.5)
    else:
        weekly_gross_pay= hours_worked * pay_rate
    print(f'The hours worked this week is {hours_worked} and your pay rate is {pay_rate}')
    print(f'gross pay is {weekly_gross_pay}')
    return weekly_gross_pay

def calculate_tax_witholdings(annual_income, filing_status):
    if filing_status == 'single':
        if annual_income < 12000:
            tax_rate = .05
        elif 12000 <= annual_income < 25000:
            tax_rate = .10
        elif 25000<= annual_income < 75000:
            tax_rate = .15
        else:
            tax_rate = .20
    elif filing_status == 'joint':
        if annual_income < 12000:
            tax_rate = 0
        elif 12000 <= annual_income < 25000:
            tax_rate =.06
        elif 25000 <= annual_income < 75000:
            tax_rate = .11
        else 
