import random

def guessing_game():
    answer = random.randint(0, 100)
    while True:
        user_guess = int(input('What is your guess? '))
        if user_guess == answer:
            print(f'Right!The answer is {user_guess}')
            break
        if user_guess < answer:
            print(f'Your guess of {user_guess} is too low!')
        else:
            print(f'Your guess of {user_guess} is too high!')

# guessing_game()

# def mysum(*numbers):
#     output = 0 
#     for number in numbers: 
#         output += number 
#         return output 


def run_timing():
    """Asks the user repeatedly for numeric input. Prints the average time an d number of runs."""
    number_of_runs = 0
    total_time = 0
    while True:
        one_run = input('Enter 10 km run time: ')
        if not one_run:
            break
        number_of_runs += 1
        total_time += float(one_run)
        average_time = total_time / number_of_runs
        print(f'Average of {average_time}, over {number_of_runs} runs')

# run_timing()


# # """ Chapter2 String """

# def pig_latin(word): 
#     if word[0] in 'aeiou': 
#         return f'{word}way' 
#     else:
#         return f'{word[1:]}{word[0]}ay' 
        

def main():
    
    run_timing()
    print(pig_latin('pythonic'))
    print(mysum(10, 20, 30, 40))

if __name__ == '_main__':
    guessing_game()
