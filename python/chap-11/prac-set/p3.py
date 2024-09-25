class Employee:
    salary = 200; 
    increment = 20; 

    @property
    def  salaryAfterIncre(self): # ab basic jab be yeh func call hoga salary ma increment hoga on the basis of increment attribute.
        return  self.salary + self.salary * (self.increment/100)
    @salaryAfterIncre.setter # yeh iss lia set kia agr hum yeh check krna chahtay hain kay salary ma increment kitnay ka aya hai toh iss lia 'setter' ko use kia toh hoga yeh kay ab jab be salaryAfterIncre method access hoga toh 'setter' be chlega and A/c to formula jo humnay lgya hai 'increment' attribute ki value hai wo set hojayegi.
    def salaryAfterIncre(self,newSalary): # remember 'setter' kay 2nd parameter may humesha wo value ayegi jo 'getter' return krega or getter jo uper humna @property decorator ka sth salaryAfterIncre bnaya hai usi ko 'getter' be kaheinga bcuz uskay through salary get hogi.. 
        self.increment = ((newSalary/self.salary) -1) * 100


e1 = Employee()
print(e1.salaryAfterIncre) # yaha auto incre honay ka bd salary ajayegi. bcuz yaha salaryAfterIncre method call ho rha hai toh usme jo be functionality hai wo perform hojayegi.
print(e1.increment) # yaha increment attribute ma jo value setter ka through hui hogi wo ajyegi.
e1.salaryAfterIncre = 280; # or yaha salaryAfterIncre kiu kay as a property be hai or method be hai toh yaha basically salaryAfterIncre as a property use ho rha hai. toh usko yeh static value set krdi hai salary ki explicitly 
print(e1.increment) # or yaha jo increment ma new value ayi hai wo print hojayegi.