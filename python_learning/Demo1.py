Cars = 100
Spaca_in_Car = 4
Drivers = 30 
PAssangers = 90
Cars_not_driving = Cars - Drivers
Cars_Driven = Drivers
carpool_capacity = Drivers*Spaca_in_Car
avg_passangers_per_car = PAssangers/Drivers


print "There are", Cars , "cars available."
print "There are only" , Drivers , "are available."
print "There are " , Cars_not_driving , "empty today"
print "we can transport" , carpool_capacity , "today"
print "we have " , PAssangers , " are there in carpool today"
print "we need to put " ,avg_passangers_per_car," each car today" 
print "Hey %s there. " % "you"