# Recursion
# recursion ka concept hai kay koi be asa process jo ek initial level say start ho kar final level tk na pounch jaye, tab tk wo chlta rahega.
# like in computer humna ek task diya kay we want the factorial of 5 , ab jasa humay pta hai kay kisi be num ka factorial find krna ho toh jab wo '1' or '0' tk nhi pounchega wo factorial finding ka process chlta rahega. isi lia hum usmay ek base condition be set krdetay hain kay takay jab wo process uss base condition pa pounchy toh stop hojaye otherwise age base condition nhi lgye gy toh wo process infinite hojayega.

def factorial(num):
    if num == 0 or num == 1:
        return 1; 
    
    return num * factorial(num-1)


print(factorial(6))


# basically, recursive function ma jo technique hai for returning value wo hai LIFO (Last In First Out) mtlb kay let say agr hum fectorial(6) -> ab yeh func callstack may as a main func jayega , then call stack ma iss func ka uper further return 6 X factorial(5) ajyega, then iska uper return 5 X factorial(4) and so on till the base condition.But remember srf return keyword sth likha hai but abhi tk return nhi huye.
# Ab jab yeh function base condition ko hit krega toh then phr uska bad return ka process start hojayega. mtlb kay ab kiu kay callStack ma stack bn gya hai mtlb kay ek kay uper dusra func hai ab jo mena start ma kaha tha kay recursive func return value by using LIFO technique toh mtlb kay jo last ma ayi hai wo pehlay return hogi. toh here last ma base codnition hit hui hai toh wo '1' return kregi, ab yeh jo value return hui hai yeh jo uss previous hai usma use hogi which is 2 X factorial(1) toh ab jab '2' return hoga toh wo '1' say multiply hokay return hoga.    

# to understand recursion must read the below articles 
# https://medium.com/swlh/visualizing-recursion-6a81d50d6c41 (first)
# https://web.mit.edu/6.005/www/fa16/classes/14-recursion/#:~:text=To%20visualize%20the%20execution%20of,functions%20as%20the%20computation%20proceeds.&text=In%20the%20diagram%2C%20we%20can,not%20make%20a%20recursive%20call. (second)