# OOP
# as we know that there are 3 things in OOP:
# 1-class -> class refer to blueprint or in other word we can say it as 'Noun' like Employee,Car,Mobile.
# 2-attribute/properties -> it refers to adjectives of that Noun which we define, mtlb kay jasay jo class hai agr wo ek Car ki class hai ok thk hai, but Car ek noun hai likin their are so many Cars and every car has its own properties like colour,name,design so these are known as attributes.

# 3-methods/functionality -> taking the above example ab Car class hai ab jasa har Car ka apna name,colour,design hai isi tarah har Car ka features and uski functionality wo bi different hogi so that are called methods/functions.


# syntax
class Car:
    # attributes
    company = "toyota"; 
    transmission = "auto"; 
    

Car1 = Car()
print(Car1.company,Car1.transmission) # right now company and transmission both attribute will be same for both Car1 and Car2, But if want to know car1 ka kya name hai and car2 ka kya name hai so for that we can add the attribute which are also known as instance/object attribute.
Car2 = Car()
print(Car2.company,Car1.transmission)

# adding attribute specific to their instance
Car1.name = "prado"; 
print(Car1.name,Car1.company,Car1.transmission); 

Car2.name = "fortuner"; 
print(Car2.name,Car2.company,Car2.transmission); 


# now remember here 'name' attribute is known as instance attribute kiu kay wo jo instance create kia hai uska according hai and "company" and 'transmission' these attribute known as class attribute bcuz they directly belong to class. 
