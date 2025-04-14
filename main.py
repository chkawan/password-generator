import random
import string

# Símbolos seguros e aceitos na maioria dos sistemas
SIMBOLOS_SEGUROS = "!@#$%&*-_+="

def gerar_senha(tamanho, usar_maiusculas, usar_minusculas, usar_numeros, usar_simbolos):
    caracteres = ''
    if usar_maiusculas:
        caracteres += string.ascii_uppercase
    if usar_minusculas:
        caracteres += string.ascii_lowercase
    if usar_numeros:
        caracteres += string.digits
    if usar_simbolos:
        caracteres += SIMBOLOS_SEGUROS

    if not caracteres:
        return "Escolha pelo menos um tipo de caractere!"

    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

def main():
    print("=== Gerador de Senhas Seguras ===")
    try:
        tamanho = int(input("Tamanho da senha: "))
        usar_maiusculas = input("Incluir letras maiúsculas? (s/n): ").lower() == 's'
        usar_minusculas = input("Incluir letras minúsculas? (s/n): ").lower() == 's'
        usar_numeros = input("Incluir números? (s/n): ").lower() == 's'
        usar_simbolos = input("Incluir símbolos? (s/n): ").lower() == 's'

        senha = gerar_senha(tamanho, usar_maiusculas, usar_minusculas, usar_numeros, usar_simbolos)
        print("\nSenha gerada:", senha)
    except ValueError:
        print("Por favor, insira um número válido.")

if __name__ == "__main__":
    main()
