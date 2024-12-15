# projeto-ramsoware

Este repositório contém dois scripts básicos para criptografia e descriptografia de arquivos, implementados em Python.

---

## Código de Criptografia (`encrypter.py`):
- Uso de `with open()` para garantir que os arquivos sejam fechados automaticamente.
- Verificação se o arquivo existe antes de tentar abri-lo.
- Tratamento de exceções gerais com uma mensagem de erro útil, como `FileNotFoundError` se o arquivo não existir.

---

## Código de Descriptografia (`decrypter.py`):
- O arquivo criptografado é verificado antes de ser aberto.
- A função descriptografar_arquivo é usada para separar a lógica e facilitar a reutilização do código.
- Uso de with open() para garantir que os arquivos sejam fechados automaticamente.
