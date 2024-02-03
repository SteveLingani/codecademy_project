weight = 1.50
#Ground Shipping
if weight <= 2:
  cost = weight * 1.5 + 20
elif weight <= 6:
  cost = weight * 3 +20
elif weight <= 10:
  cost = weight * 4 + 20
else:
  cost = weight * 4.75 + 20

print ('Ground Shipping:', cost)

cost_ground_premium = 125.00

print("Ground Shipping Premium $", cost_ground_premium)
#Drone Shipping
if weight <= 2:
  cost = weight * 4.50
elif weight <= 6:
  cost = weight * 9.00
elif weight <= 10:
  cost = weight * 12.00
else:
  cost = weight * 14.25
print ('Drone Shipping:', cost)
