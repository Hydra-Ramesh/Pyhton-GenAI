# Electric Bill Calculator

# Consumer Input
consumer_name = str(input("Enter Consumer Name: "))
units_consumed = int(input("Enter Units Consumed: "))
# Rate per Unit
rate_per_unit = float(input("Enter Rate per Unit: "))
#Fixed Charges
fixed_charges = float(input("Enter Fixed Charges: "))
# Calculate Total Bill
energy_charge = units_consumed * rate_per_unit
net_bill = energy_charge + fixed_charges

cgst= energy_charge * 0.09
sgst= energy_charge * 0.09
total_tax= cgst + sgst
total_bill = total_tax + net_bill

# Display Bill
print("\nElectricity Bill")
print("Consumer Name:", consumer_name)
print("Units Consumed:", units_consumed)
print("Rate per Unit: Rs.", rate_per_unit)
print("Fixed Charges: Rs.", fixed_charges)
print("Energy Charge: Rs.", energy_charge)
print("Net Bill (Energy Charge + Fixed Charges): Rs.", net_bill)
print("CGST (9%): Rs.", cgst)
print("SGST (9%): Rs.", sgst)
print("Total Tax: Rs.", total_tax)
print("Total Bill Amount: Rs.", total_bill)
print("Thank you for using the Electric Bill Calculator!")
