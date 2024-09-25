# property decorator -> yeh basically iss lia use kia jata hai takay jasay normally hum instance attribute krletay hain like:
# E1.name = 'shah khan' # ab yeh name ek new instance attribute ban gya thk hai. But agr may iss 'name' attribute ko use krtay huway orr instance attribute create krna chaho toh uskay liya we have to use this @property decorator yeh basically ek method ko as a property declare krdeta hai. like:

class Employee:
    a = 1; ()

    def show(self):
        print(f"printing the class attribute {self.a}")

    @property # -> this is also known as getter method.
    def name(self):
        return f'your name is: {self.ename}'

    @name.setter
    def name(self, value):
        print(value)
        self.fname = value.split(' ')[0] # yeh basic jo 'fullname' hai usko break kia hai.
        self.lname = value.split(' ')[1]

    def  getFirstName(self):
        return self.fname; 

    def  getLastName(self):
        return self.lname; 

E2 = Employee(); 

E2.ename = 'John wylie' # ab yeh yaha basic simple attribute ko nhi set kr rhay blkay jo 'name' method ka andar property pss ki hai wo pass kr rhay hain.
print(E2.name) # yeh dekhnay ma toh asa lg rha hai jasay 'name' property access kr rhay hain but yaha 'name' method ko basic access kia hai or yehi faida haka property decorater ka kay wo method ko as a property declare krdeta hhai.

# ab basic property decorator and setter ko use krnay ka mtlb hota hai kay jasa user nay toh 'name' set krdia but agr ma firstName and lastName extract krna chahta hunn or alag instance attribute may store krna hai toh we can do it as well by using setter methood.
print(E2.fname,' ',E2.lname)
print(E2.getFirstName())
print(E2.getLastName())

# cant understand now about setter and getter properly.