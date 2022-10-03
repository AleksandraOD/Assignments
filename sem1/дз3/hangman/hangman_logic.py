import random


def get_random_word():
    dictionary = ["биосфера", "отчисление", "алкоголизм", "амбидекстрия",
                  "мировоззрение", "бесперспективняк"]
    return random.choice(dictionary)


def get_guessed_word(secret_word, used_letters):
    blanks_new = ""
    for letter in secret_word:
        if letter in used_letters:
            blanks_new += letter + " "
        else:
            blanks_new += "_ "
    return blanks_new


def is_letter_guessed(secret_word, letter):
    if letter in secret_word:
        return True
    else:
        return False


def valid_letters(letter, alphabet):
    if letter not in alphabet or len(letter) != 1:
        raise ValueError("Некорректный ввод")
    else:
        return True


def is_word_guessed(secret_word, blanks_new):
    if blanks_new == secret_word:
        return True
    else:
        return False
