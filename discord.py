import random, string
amount = int(input('Nombre de nitros à generer: '))
value = 1
while value <= amount: 
    code = "https://discord.gift/" + ('').join(random.choices(string.ascii_letters + string.digits, k=16))
    f = open('Codes.txt', "a+")
    f.write(f'{code}\n')
    f.close()
    print(f'Générer | {code}')
    value +=1