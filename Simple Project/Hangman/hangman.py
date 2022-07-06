import random
from words import words
import string


def get_valid_words(words):
    word = random.choice(words)  # mengambil kata random dari list
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    word = get_valid_words(words)
    word_letters = set(word)  # huruf dalam sebuah kata
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # huruf yang telah ditebak

    lives = 10

    # mengambil inputan user
    while len(word_letters) > 0 and lives > 0:
        #kata yang telah digunakan
        # ' '.join(['a', 'b', 'cd']) akan jadi 'a b cd'
        print (f'Kamu masih punya, {lives} nyawa, dan kamu  telah menggunakan kata ini: ','|'.join(used_letters))
        #what current word is (ie W-R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ',''.join(word_list))

        user_letter = input('Tebak Sebuah Kata: ').upper()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1 #tiap salah, nyawa berkurang 1

        elif user_letter in used_letters:
            print('Kamu telah memilih kata tadi, coba lagi!')

        else:
            print('Karakter Invalid, coba lagi!')

    #kalau perulangannya berhenti, maka kita akan sampai di line ini!
    if lives == 0:
        print (f'Maaf kamu kalah, kata yang sebenarnya adalah {word}')
    else:
        print (f'Selamat, kamu berhasil menebak kata {word} dengan benar')


hangman()