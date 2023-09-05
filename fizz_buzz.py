def fizzbuzz():
    a = int(input('Enter the starting number:'))
    b = int(input('Enter the number to end:'))
    for i in range(a,b+1):
        if (i%3 == 0) & (i%5 == 0):
            print(i, 'is FizzBuzz')
        elif i%5 == 0:
            print(i, 'is Buzz')
        elif i%3 == 0:
            print(i, 'is Fizz')

if __name__ == '__main__':
    fizzbuzz()