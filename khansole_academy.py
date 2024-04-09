import random

def generate_addition_problem():
    num1 = random.randint(10, 99)
    num2 = random.randint(10, 99)
    return num1, num2, num1 + num2

def main():
    print("Khansole Academy")
    
    consecutive_correct = 0
    
    while consecutive_correct < 3:
        num1, num2, sum_ = generate_addition_problem()
        print("What is {} + {}?".format(num1, num2))
        
        try:
            guess_sum = int(input("Your answer: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        continue
        
        if guess_sum == sum_:
            consecutive_correct += 1
            print("Correct! You've gotten {} correct in a row.".format(consecutive_correct))
        else:
            consecutive_correct = 0
            print("Incorrect.")
            print("The expected answer is", sum_)
    
    print("\nCongratulations! You mastered addition.")

if __name__ == '__main__':
    main()