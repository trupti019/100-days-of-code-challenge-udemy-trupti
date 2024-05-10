with open ('names.txt', 'r') as file:
    list_names= file.readlines()

with open ('letter.txt', 'r') as p:
    letter_content = p.read()
    for i in list_names:
        name= i.strip()
        new_letter= letter_content.replace('[name]', name)
        with open (f'{name}_gm.txt', 'w') as f:
            f.write(new_letter)