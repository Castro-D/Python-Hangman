from random_words import RandomWords
rw = RandomWords()
word = rw.random_word()
print("""
                                        |    |    |_______    |\        /|       /\        |\    |
                |       |       /\      |\   |    |           | \      / |      /  \       | \   |
                |       |      /  \     | \  |    |   __ _    |  \    /  |     /----\      |  \  |
                |-------|     /----\    |  \ |    |      |    |   \  /   |    /      \     |   \ |
                |       |    /      \   |   \|    |______|    |    \/    |   /        \    |    \|              
""")

print(f'word is {len(word)} characters long')
max_tries = 6
guess = 0
output = ['_'] * len(word)
used_letters = set()


def hang_man(guess):
    if guess == 1:
        print("""
        -----|
        |    |
        |    O
        |
        |
       _____    
        """)
    elif guess == 2:
        print("""
        -----|
        |    |
        |    O
        |    |
        |    |
       _____    
        """)
    elif guess == 3:
        print("""
        -----|
        |    |
        |    O
        |   /|
        |    |
       _____    
        """)
    elif guess == 4:
        print(r"""
        -----|
        |    |
        |    O
        |   /|\
        |    |
       _____   
        """)
    elif guess == 5:
        print(r"""
        -----|
        |    |
        |    O
        |   /|\
        |    |
       _____/    
        """)
    else:
        print(r"""
        -----|
        |    |
        |    O
        |   /|\
        |    |
       _____/ \   
        """)

        
while guess < max_tries:
    letter = input('\n\nguess a letter (whenever you wanna guess the word, type risk ): ')
    try:
        if letter.isalpha() != True:
            raise Exception
    except Exception as e:
        print('Not a letter!, try again.')
        continue
    else:
        pass
    if letter == 'risk':
        prediction = input('guess the word: ')
        if prediction == word:
            print('you won!')
            break
        else:
            print('Wrong!, you lost.')
            hang_man(6)
            break
    if letter in word:
        for i, x in enumerate(word):
            if x == letter:
                output[i] = letter
            else:
                pass
        print(''.join(output))
        if ''.join(output) == word:
            print('you won!')
            break
    else:
        print(''.join(output))
        if letter in used_letters:
            hang_man(guess)
        else:
            guess += 1
            hang_man(guess)

    used_letters.add(letter)
    print(f'letters already used: {used_letters}')

if guess == max_tries:
    print(f'You lost. The word was {word}')
