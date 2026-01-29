#workbook 3 Coding challenge
#At least 5 string variables (trip_name, driver_name, car_model, etc.)
trip_name = input("Name of trip: ")
trip_date = input("Date of trip: ")
driver_name = input("Name of Driver: ")
car_make = input("Make of the car: ")
car_model = input ("Model of car: ")
car_year = input ("Year of car: ")
car_details = (car_make, car_model, car_year)
separator = " "
car_joined = separator.join(car_details)
gas_price = float(input ("Price per gallon (e.g. 2.20): "))
car_mpg = int(input ("Average miles per gallon (e.g. 30): "))
#At least 3 lists (destinations, distances, packing items, etc.)
destinations = [input("Destination 1: "), input("Destination 2: "),input("Destination 3: ")]
distances = [200,500,1230]
packing_list=["Camera", "Nuka-Cola", "Rad Away", "Grognak Comics", "Sugar Bombs"]


# List indexing to access items (destinations[0], distances[-1], etc.)
destination_distance = (destinations[0],distances[0], destinations[1],distances[1], destinations[2],distances[2] )
#One calculation (total distance, gas cost, total items, etc.)
total_distance = sum(distances)
#At least 3 f-strings to display informationa
#between_twocities1 = sum(distances[0] - distances [-1])
between_twocities1 = distances[1] - distances [0]
between_twocities2 = distances[2] - distances [1]
between_twocities3 = distances[2] - distances [0]
gas_cost = (total_distance / car_mpg ) * gas_price
print(f"The name of our trip is: {trip_name}")
print(f"{driver_name} is our driver for the trip.")
print(f"Our first stop is {destinations[0]}")
print(f"They are driving a {car_joined}")
print(f"Followed by {destinations[1]} and {destinations[2]}")
print(f"It will cost us ${gas_cost:.2f} in gas if we don't get lost.")
print(f"{driver_name} packed {len(packing_list)} things.")
print(f"I don't know why {driver_name.upper()} needs a {packing_list[0]}, {packing_list[1]}, {packing_list[2]}, and {packing_list[3]}")



#print(f"{between_twocities1}")
#print(f"{between_twocities2}")
#print(f"{between_twocities3}")
#print(f"{destination_distance}")
#print(f"{packing_list}")
#print(f"{gas_cost:.2f}")

