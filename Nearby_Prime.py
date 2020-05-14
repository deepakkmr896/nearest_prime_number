input_val = int(input("Input a value\n")) # Get the input from the entered number
nearestPrimeNum = [];

# Define a function to check the prime number
def isPrime(num):
    isPrime = True
    for i in range(2, (num // 2) + 1):
        if(num % i == 0):
            isPrime = False
    return isPrime

# Assuming 10 as the maximum gap between the successive prime number
for i in range(1, 11):
    precVal = input_val - i;
    forwVal = input_val + i;
    
    # Check both the preceding and succeeding number for the prime and capture whichever is found first or both (e.g. 3 and 5 for 7)
    if (precVal > 1):
        if (isPrime(precVal) == True):
            nearestPrimeNum.append(precVal)
    if (isPrime(forwVal) == True):
        nearestPrimeNum.append(forwVal)
    if (len(nearestPrimeNum) > 0):
        break

if (len(nearestPrimeNum) > 0):
    print("Nearest prime no/nos is: {}".format(' and '.join(map(str, nearestPrimeNum))))
else:
    print("There is no prime number exists nearby") 
