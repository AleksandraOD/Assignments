import hangman_logic as hg

print("Добро пожаловать в игру 'Виселица'!1!1!!")
secret_word = hg.get_random_word()
used_letters = set()
attempts = 0
alphabet = "абвгдеёжзийклмнопрстуфхцчщъыьэюя"
blanks_new = ""
print("\nУгадай слово из ", len(secret_word), "букв")
while attempts < 6 and blanks_new != secret_word:
    # print("Ты использовал буквы: ", used_letters)
    letter = input("\nВведите букву: ", )
    letter = letter.lower()
    while hg.valid_letters(letter, alphabet) is not True:
        print("\nВведите букву: ")
        letter = input()
    while letter in used_letters:
        print("\nТы уже использовал эту букву. Введи другую: ", )
        letter = input()
    used_letters.add(letter)
    if hg.is_letter_guessed(secret_word, letter) is True:
        print("\nТы угадал! Такая буква есть в слове")
        blanks_new = hg.get_guessed_word(secret_word, used_letters)
        print(blanks_new)
        print("У тебя осталось ", 6 - attempts, "попыток")
    elif hg.is_letter_guessed(secret_word, letter) is False:
        print("К сожалению такой буквы нет:(\n")
        print("Ты уже использовал буквы: ", used_letters)
        attempts += 1
        print("У тебя осталось ", 6 - attempts, "попыток")
if hg.is_word_guessed(secret_word, blanks_new) is True and attempts < 6:
    print("Ты угадал слово! Молодец, возьми с полки пирожок")
elif attempts >= 6 and hg.is_word_guessed(secret_word, blanks_new) is False:
    print("Не повезло, дружок:( Ты не угадал слово: ", secret_word)
