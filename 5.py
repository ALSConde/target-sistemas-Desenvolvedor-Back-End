# Escreva um programa que inverta os caracteres de um string.

# IMPORTANTE:
# a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
# b) Evite usar funções prontas, como, por exemplo, reverse;

string = input("Digite uma string: ")
# string = "Eu desejo entrar neste time!"

inverted_string = ""

for i in range(len(string) - 1, -1, -1):
    inverted_string += string[i]

print(f"A string invertida é: {inverted_string}")
