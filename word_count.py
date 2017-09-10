user_text = 'привет как дела'
print(user_text)
    
number_of_spaces = 0
for spacing in user_text:
    if spacing == ' ':
        number_of_spaces = number_of_spaces + 1
print(number_of_spaces)        

number_of_words = number_of_spaces + 1