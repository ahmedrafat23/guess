import random

def guess_the_number():
    number_to_guess = random.randint(1, 100)
    attempts = 0

    print("🎯 مرحباً بك في لعبة 'خمن الرقم'!")
    print("🤖 اخترت رقماً بين 1 و 100. حاول أن تخمنه!")

    while True:
        try:
            guess = int(input("🔢 أدخل رقمك: "))
            attempts += 1

            if guess < number_to_guess:
                print("📉 الرقم أكبر من ذلك!")
            elif guess > number_to_guess:
                print("📈 الرقم أصغر من ذلك!")
            else:
                print(f"🎉 تهانينا! لقد خمّنت الرقم الصحيح {number_to_guess} بعد {attempts} محاولة.")
                break
        except ValueError:
            print("❌ من فضلك أدخل رقماً صحيحاً.")

# تشغيل اللعبة
guess_the_number()
