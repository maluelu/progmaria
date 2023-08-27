import random
from palavras import words
from hangman_visual import lives_visual_dict
import string


def get_valid_word(words):
    word = random.choice(words) 
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  
    alphabet = set(string.ascii_uppercase)
    used_letters = set() 

    lives = 7


    while len(word_letters) > 0 and lives > 0:
 
    
        print('Você tem', lives, 'vidas restantes e você usou essas cartas: ', ' '.join(used_letters))

  
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(lives_visual_dict[lives])
        print('Palavras Atual: ', ' '.join(word_list))

        user_letter = input('Adivinhe: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')

            else:
                lives = lives - 1  # takes away a life if wrong
                print('\n Sua palavra,', user_letter, 'não está na palavra.')

        elif user_letter in used_letters:
            print('\nVocê já usou essa carta. Adivinhe outra carta.')

        else:
            print('\nEssa não é uma carta válida.')


    if lives == 0:
        print(lives_visual_dict[lives])
        print('Parabénsss', word)
    else:
        print('Perdeummm', word, '!!')


if __name__ == '__main__':
    hangman()