import os
import pyaes

def descriptografar_arquivo(file_name, key):
    try:
        # Verificar se o arquivo criptografado existe
        if not os.path.isfile(file_name):
            raise FileNotFoundError(f"Arquivo {file_name} não encontrado.")

        # Abrir e ler o arquivo criptografado
        with open(file_name, "rb") as file:
            file_data = file.read()

        # Descriptografar os dados
        aes = pyaes.AESModeOfOperationCTR(key)
        decrypted_data = aes.decrypt(file_data)

        # Apagar o arquivo criptografado
        os.remove(file_name)

        # Criar o arquivo original
        original_file = file_name.replace(".ransomwaretroll", "")
        with open(original_file, "wb") as dec_file:
            dec_file.write(decrypted_data)

        print(f"Arquivo descriptografado com sucesso! O arquivo original é {original_file}.")
    
    except Exception as e:
        print(f"Erro ao descriptografar o arquivo: {e}")

# Chave para descriptografia
key = b"testeransomwares"
# Nome do arquivo criptografado
file_name = "teste.txt.ransomwaretroll"

# Chamar a função de descriptografia
descriptografar_arquivo(file_name, key)
