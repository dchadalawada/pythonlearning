my_name = 'Deepak Kumar Chadalawada'
my_age = 30 #not a lie
my_hieght = 176 #In cms
my_weight = 70 #In kilograms
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print "lets talk about %s." % my_name
print "He is %d cms tall" % my_hieght
print "He is %d kgs heavy" % my_weight
print "Actually thats not too heavy"
print "He got %s eyes and %s hair." %(my_eyes	,my_hair	)
print "His teeth usually %s in color" %my_teeth	 
print "If i add %d,%d and %d I get %d." %(my_age,my_hieght,my_weight,my_age	+my_hieght	+my_weight		)

mylist = [1,2,3,4,5]
print	"A list %r" %mylist	
print	"A list %s" %mylist	

data = ("John","Doe",53.55)
format_string = "Hello"

print (format_string	%data	)