val = int(input("Input a value\n"))
nearestPrimeNum = [];
def isPrime(num):
    isPrime = True
    for i in range(2, (num // 2)):
        if(num % i == 0):
            isPrime = False
    return isPrime

for i in range(1, 11):
    precVal = val - i;
    forwVal = val + i;
    
    if (precVal > 0):
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
