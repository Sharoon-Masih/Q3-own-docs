# remember instance attributes take preference over class attributes during assignment & retrieval.


class Bike:
    company = "honda"; 
    model = "CBR500R"

Bike1 = Bike(); 
Bike1.company = "yamaha" # now as we are seeing that '.company' is already a class attribute so when we are again setting same attribute so what will happen.
print(Bike1.company); # so A/c to top statement that jo instance attribute hoga uski priority zeada hogi class attribute say which means kay agr humna jis name ka class attribute rakha hai ussi name ka instance attribute be rakheinga toh jo instance attribute hoga uski priority hogi.

Bike2 = Bike()
print(Bike2.company) # but agr yaha par ma '.company' attribute ko access krwaoga basically joka Bike2 ek new instance hai usme say access hoga toh that will print the class attribute. 

# isi lia jo uper top pa statement likhi hai usme yebi likha hai instance attribute ko preference srf at the time of assignment or retrieval milegi na kay ab wo jo class may attribute uski hi value ko override krdega.

