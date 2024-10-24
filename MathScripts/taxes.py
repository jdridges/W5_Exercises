yearly_salary = 100000.00
federal_tax_percent = .23
monthly_witheld_taxes = (yearly_salary/ 12)*.23

print("$" + format(monthly_witheld_taxes, ".2f") + " is witheld each month for taxes")