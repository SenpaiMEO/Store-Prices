Number = 7
def is_prime(Number): #Function Name
    if Number < 2: #Because numbers less than 2 are not prime
        return False
    for i in range(2, Number): #Check for factors from 2 to Number-1
        if Number % i == 0: #i here is each number in the range including 2 and excluding last number & if equal to 0 then it is not prime
            return False
    return True

Result = is_prime(Number)
print(f"Is {Number} prime? {Result}")