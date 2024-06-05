
def poisson():
    sum = 0
    for k in range(51,101):
        factorial = 1
        for i in range(1, k+1):
            factorial *= i
        sum += (1e-10 * pow(10, k)) / factorial
    print(sum)
        
if __name__ == "__main__": 
    poisson()