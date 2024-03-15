weight = float(input("Enter the weight of the package in pounds."))

# Ground shipping
if weight <= 2.0:
  cost_ground = weight * 1.5 + 20
elif weight >= 2.0 and weight <= 6.0:
  cost_ground = weight * 3.0 + 20
elif weight >= 6.0 and weight <= 10.0:
  cost_ground = weight * 4.0 + 20
elif weight >= 10:
  cost_ground = weight * 4.75 * 20

print("Cost for ground shipping", cost_ground)

# Ground shipping premium
cost_ground_premium = 125.00
print("Cost for premium ground shipping", cost_ground_premium)

# Drone shipping
if weight <= 2.0:
  drone_shipping = weight * 4.5 + 0
elif weight >= 2.0 and weight <= 6.0:
  drone_shipping = weight * 9.0 + 0
elif weight >= 6.0 and weight <= 10.0:
  drone_shipping = weight * 12.0 + 0
elif weight >= 10:
  drone_shipping = weight * 14.25 * 0

print("Cost for drone shipping", drone_shipping)

# Determine cheapest shipping option for customer
if drone_shipping <= cost_ground and drone_shipping <= cost_ground_premium:
  print("Drone shipping recommended")
elif cost_ground <= drone_shipping and cost_ground <= cost_ground_premium:
  print("Ground shipping recommended")
elif cost_ground_premium <= drone_shipping and cost_ground_premium <= cost_ground:
  print("Premium ground shipping recommended")