from random import randint

def main():

    def guess(x):

        random_number = randint(1,x)
        print(random_number)

        while True:
            num = int(input("Guess a number!\n"))
            if abs(num - random_number) >= 20:
                print("Cold!")
                continue
            if abs(num - random_number) >= 10:
                print("Lukewarm.")
                continue
            if abs(num - random_number) <= 10 and num != random_number:
                print("Hot!")
                continue
            else:
                print("You got it!")
                break


    guess(50)

if __name__ == '__main__':
    main()