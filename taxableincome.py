

income= float(input("Enter income:"))
if 0 <= income <= 486535:
    tax =  income * 0.15

elif 486535 < income <= 97069:
    tax = 48535 * 0.15 + (income - 48535) * 0.205

elif 97069 < income <= 150473:
    tax = 48535 * 0.15 + 48534 * 0.205 + (income - 48535 - 48534) * 0.26

elif 150473 < income <= 214368:
    tax = 48535 * 0.15 + 48534 * 0.205 + 53404 * 0.26 + (income - 48535 - 48534 - 53404) * 0.29

else:
    tax = 48535 * 0.15 + 48534 * 0.205 + 53404 * 0.26 + 63895 * 0.29 + (income - 48535 - 48534 - 53404 - 63895) * 0.33

print("Tax:"  , round(tax, 2))
    
