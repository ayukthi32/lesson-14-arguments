#activity2
def factorial(n): 
    if n==0 or n == 1:
        return 1
    else:
        print("hello")
        return n * factorial (n-1)
    
num = int(input("Enter a num"))

print("the factorial of" , num , "is", factorial(num))