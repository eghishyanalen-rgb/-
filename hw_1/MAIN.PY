travelers = int(input("Number of travelers: "))
nights = int (input("number of nights: "))
accommodation =float(input("accommodation per night:  "))
transport = float(input( "total transport cost: "))
food = float (input("food per person per day: "))
days = nights + 1
total_accommodation = accommodation * nights 
total_food = travelers * days * food 
total_trip = total_accommodation + transport + total_food 
cost_per_person = total_trip / travelers
print("total accommodation:" ,total_accommodation)
print("total trip:", total_trip)
print ("cost per person:", cost_per_person)
print ("total food:" , total_food) 
