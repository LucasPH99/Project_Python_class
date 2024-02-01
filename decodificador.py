alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def codificar_mensagem(mensagem, deslocamento):
    mensagem_codificada = ''
    for char in mensagem:
        if char.isalpha():
            maiuscula = char.isupper()
            indice = (alfabeto.index(char.upper()) + deslocamento) % 26
            novo_char = alfabeto[indice]
            mensagem_codificada += novo_char if maiuscula else novo_char.lower()
        else:
            mensagem_codificada += char
    return mensagem_codificada

def decodificar_mensagem(mensagem, deslocamento):
    return codificar_mensagem(mensagem, -deslocamento)

if __name__ == "__main__":
    mensagem_original = input("Digite a mensagem: ")
    deslocamento = int(input("Digite o valor de deslocamento: "))

    mensagem_codificada = codificar_mensagem(mensagem_original, deslocamento)
    print("Mensagem Codificada:", mensagem_codificada)

    mensagem_decodificada = decodificar_mensagem(mensagem_codificada, deslocamento)
    print("Mensagem Decodificada:", mensagem_decodificada)
