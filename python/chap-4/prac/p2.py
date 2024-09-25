Marks = []; 
mark1 = int(input("Enter mark 1: "));
Marks.append(mark1) 
mark2 = int(input("Enter mark 2: "));
Marks.append(mark2) 
mark3 = int(input("Enter mark 3: "));
Marks.append(mark3) 
mark4 = int(input("Enter mark 4: "));
Marks.append(mark4) 
mark5 = int(input("Enter mark 5: "));
Marks.append(mark5) 
mark6 = int(input("Enter mark 6: "));
Marks.append(mark6) 
mark7 = int(input("Enter mark 7: "));
Marks.append(mark7) 
Marks.sort() # ab yaha jo marks ayy hain wo string kiu kay input() string return krta hai toh ab kiu kay jab wo string hain toh wo usko alphabetic order may hi sort krega iss lia uper first integer ma convert kra hai.
print(" ".join(Marks)) # ab jasay jo Marks wo array hai toh agr hum chahtay hain kay jo array print ho wo array ka format ma print na ho balka as a string return ho toh jasa JS ma hum .join() ka method ka through kreinga or python ma bs yeh difference haka pehla seprator lagana hai like here we write " " which is seprator or phr .join(arrayName) array pss krdena hai.

