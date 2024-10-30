


def caclulate_gross_pay(pay_rate, hours_worked):
    if hours_worked > 40:
        max_hours = 40
        overtime_hours = hours_worked - max_hours
        gross_pay = (max_hours * pay_rate) + (overtime_hours * pay_rate * 1.5)
    else:
        gross_pay = hours_worked * pay_rate
    print(f'The hours worked this week is {hours_worked} and your pay rate is {pay_rate}')
    print(f'gross pay is {gross_pay}')
    return gross_pay

caclulate_gross_pay((35), int(60))
caclulate_gross_pay(35, 40)
caclulate_gross_pay (40, 35)
caclulate_gross_pay (40, 41)
caclulate_gross_pay (41, 40)