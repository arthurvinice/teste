# 2) Escreva um programa que verifique, em uma string, a existência da letra ‘a’, 
seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.

def check_string(str):
    if 'a' in str.lower() or 'A' in str:
        count = 0
        for char in str:
            if char.lower() == 'a':
                count += 1
        return count
    else:
        return False

def main():
    str_test = str(input('Digite uma string: '))
    result = check_string(str_test)
    if result:
        print(f"A letra 'a' aparece {result} vezes na string.")
    else:
        print("A letra 'a' não existe na string.")

main()
