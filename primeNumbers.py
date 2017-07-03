## This function will print out prime numbers .
def primeNumbers() :
    start_num = 0;
    end_num = input("Please provide a number");
    if end_num > 1 :
        for num in range(start_num, end_num + 1) :
            for i in range(2, num) :
                if num % i == 0: 
                    break
            else :
                print(num)

if __name__ == '__main__':
    primeNumbers()