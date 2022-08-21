from random import sample

palavra = input("digite a palavra a ser embaralhada: ")

def embaralhar (palavra):
    palavra = sample(palavra, len(palavra))
    palavra = ''.join(palavra)
    return palavra.lower() 

print(embaralhar(palavra))