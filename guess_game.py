import random

def guess_the_number():
    number_to_guess = random.randint(1, 100)
    attempts = 0

    print("🎯 Welcome to 'Guess the Number'!")
    print("🤖 I've picked a number between 1 and 100. Try to guess it!")

    while True:
        try:
            guess = int(input("🔢 Enter your guess: "))
            attempts += 1

            if guess < number_to_guess:
                print("📉 Too low!")
            elif guess > number_to_guess:
                print("📈 Too high!")
            else:
                print(f"🎉 Congratulations! You guessed the correct number {number_to_guess} in {attempts} attempts.")
                break
        except ValueError:
            print("❌ Please enter a valid number.")

# Run the game
guess_the_number()
