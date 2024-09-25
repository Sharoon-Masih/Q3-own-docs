# try - finally block
# sometime we want a code that will execute in both situation . mtlb kay try block chlay tab be wo code execute ho ya agr except block chlay tab be wo code execute ho.

try:
    n = int(input("enter num: "))
    print(n)
except Exception as e:
    print(e)
finally:  # it will run in both situation.
    print("input done")

# or mainly finally use hota  hai jab humay function may yeh btana haka function execute hogya hai. like:


def main():
    try:
        print("try block")
        return # as we know kay jab ek dafa function ma return krday toh usse next code nhi chlta but remember jab 'finally' block set hoga toh it will must execute.
    except:
        print("except block")
        return
    finally:
        print("function execute finally ")

main()