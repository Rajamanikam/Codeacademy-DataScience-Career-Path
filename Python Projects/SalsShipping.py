def ground_shipping(weight):
  if weight <= 2:
    return weight * 1.50 + 20.00
  elif weight <= 6 and weight > 2:
    return weight * 3.00 + 20.00
  elif weight <= 10 and weight > 6:
    return weight * 4.00 + 20.00
  else:
    return weight * 4.75 + 20.00

print(ground_shipping(4.8))

premium_ground_shipping = 125.00

def drone_shipping(weight):
  if weight <= 2:
    return weight * 4.50
  elif weight <= 6 and weight > 2:
    return weight * 9.00
  elif weight <= 10 and weight > 6:
    return weight * 12.00
  else:
    return weight * 14.25

print(drone_shipping(4.8))

#Function to determine Cheapest shipping Method

def cheap_shipping(weight):
  if (ground_shipping(weight)) < (drone_shipping(weight)) and (ground_shipping(weight)) < (premium_ground_shipping):
    print("Cheap Shipping Method : Ground shipping and Cost : ${}".format(ground_shipping(weight)))
  elif (drone_shipping(weight)) < (ground_shipping(weight)) and (drone_shipping(weight)) < (premium_ground_shipping):
    print("Cheap Shipping Method : Drone shipping and Cost : ${}".format(drone_shipping(weight)))
  else:
    print("Cheap Shipping Method : Premium ground shipping and Cost : $125.00")

cheap_shipping(4.8)
cheap_shipping(41.5)

