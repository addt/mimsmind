import sys
import random
import traceback

# Generate a random no with lentgth provided by command line.
def get_length():
    length = 3
    if len(sys.argv) > 1:
        try:
            length = int(sys.argv[1])
        except:
            print("Enter a valid no pls")
    return length

def gen_random_no(length):
    random_no = random.randint(0, 10**length -1)
    max_rounds = 2**length + length
    random_no_str = pad_convert(random_no, length)
    return random_no_str, max_rounds

def pad_convert(random, length):
    random_no = str(random)
    if len(str(random)) < length:
        for i in range(0, length - len(str(random))):
            random_no = "0" + random_no
    return random_no

def prompt_user(random, length, count , limit, message):
    guess = input(message)
    try:
        guess = pad_convert(int(guess), length)
        gen_response(guess, random, count, limit, length)
    except Exception as e:
        if (limit - 1) == 0:
              print("Sorry, out of guesses")
              sys.exit(0)
        prompt_user(random, length, count + 1, limit -1, "0 bull(s), 0 cow(s). Try again:")

def gen_response(guessed, random_no, count, limit, length):
    bulls = 0
    cows = 0
    compare_guess = list(str(guessed))
    post_compare = []
    if str(guessed) == random_no:
        print("Congratulations. You guessed the correct number in {} tries.".format(count + 1))
        sys.exit(0)
    else:
        zipped = zip(compare_guess, list(random_no))
        for i in zipped:
            if i[0] == i[1]:
                bulls += 1
            else:
                post_compare += [i[0]]
        for i in post_compare:
            if i in random_no:
                cows += 1
        message_send = "{} bull(s), {} cow(s). Try again:".format(bulls,cows)
        if (limit - 1) == 0:
            print("Sorry, out of guesses")
            sys.exit(0)
        prompt_user(random_no, length, count + 1, limit - 1, message_send)
                

def main():
    length = get_length()
    random_no, limit = gen_random_no(length)
    print("Let's play the mimsmind1 game. You have {} guesses.".format(limit))
    initial_message = "Guess a {}-digit number:".format(str(length))
    prompt_user(str(random_no), length, 0, limit, initial_message)

if __name__ == "__main__":
    main()
