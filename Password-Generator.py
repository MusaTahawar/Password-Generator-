import random

alphabets_lower = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
alphabets_upper = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
numbers = [0,1,2,3,4,5,6,7,8,9]
symbols = ["#","$","@","*","_"]

def password_generator():
    password = []
    for i in range(16):
        category = random.randint(1, 4)
        if category == 1:
            password.append(random.choice(alphabets_lower))
        elif category == 2:
            password.append(random.choice(alphabets_upper))
        elif category == 3:
            password.append(str(random.choice(numbers)))
        else:
            password.append(random.choice(symbols))

    return "".join(password)

generated_password = password_generator()
print(generated_password)
