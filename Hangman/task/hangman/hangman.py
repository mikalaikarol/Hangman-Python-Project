import random

print("H A N G M A N")

new_word_list = ["java", "kotlin", "python", "javascript"]
new_word = random.choice(new_word_list)
hidden_word = ("-" * len(new_word))
number_of_tries = 8
used_letters = []
decision = input('Type "play" to play the game, "exit" to quit: ')
result = "".join(hidden_word)
while decision == "play":
    if result == new_word:
        break
    print()
    while number_of_tries != 0:

        print(result)
        user_input = input('Input a letter: ')
        number_of_tries -= 1
        for letter in user_input:
            if len(user_input) > 1:
                print("You should input a single letter")
                number_of_tries += 1
                if number_of_tries < 1:
                    pass
                else:
                    print()
                break
            else:
                if user_input.islower() is False:
                    print("It is not an ASCII lowercase letter")
                    number_of_tries += 1
                    if number_of_tries < 1:
                        pass
                    else:
                        print()
                        break

                if user_input in used_letters:
                    print("You already typed this letter")
                    number_of_tries += 1
                    if number_of_tries < 1:
                        pass
                    else:
                        print()
                    break
                else:
                    if letter not in new_word:
                        print("No such letter in the word")
                        used_letters.append(letter)
                        if number_of_tries < 1:
                            pass
                        else:
                            print()
                    if letter in result:
                        print("You already typed this letter")
                        number_of_tries += 1
                        if number_of_tries < 1:
                            pass
                        else:
                            print()
                    else:
                        if letter in new_word:
                            hidden_word = list(hidden_word)
                            index = new_word.find(letter)
                            hidden_word[index] = letter
                            number_of_tries += 1
                            count_letter = new_word.count(letter)
                            n = 1  # n represents the number of i to be found
                            while count_letter > 1:
                                n += 1
                                x = new_word.find(letter, n)
                                hidden_word[x] = letter
                                count_letter -= 1
                            result = "".join(hidden_word)
                            if number_of_tries > 0 and result == new_word:
                                print()
                                break
                            elif number_of_tries == 0 and result != new_word:
                                pass
                            else:
                                print()

        if result == new_word:
            print(result)
            print("You guessed the word " + result + "!")
            print("You survived!")
            print()
            break
        elif result != new_word and number_of_tries == 0:
            print("You lost!")
            print()
            break
    if decision == 'exit':
        break
    else:
        break
