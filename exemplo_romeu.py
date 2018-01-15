import codificador as cod

# Exemplo de mensagem
t = open('romeu.dat')
#t = open('romeu_full.dat')

texto = ''
for ti in t:
    texto += ti

print('\nMensagem Original:\n')
print(texto)
enc = cod.Encripta(1.0, 1.01, 1.1, texto)

# Encripta a mensagem
print('\nMensagem encriptada:\n')
texto_enc = enc.encripta
print(texto_enc)

# Decripta a mensagem encriptada
print('\nMensagem decriptada a partir da mensagem encriptada:\n')
dec = cod.Decripta(1.0, 1.01, 1.1, texto_enc)
print(dec.decripta)

# Decripta a mensagem encriptada, mas com a chave diferente
print('\nMensagem decriptada a partir da mensagem encriptada, mas com chave errada:\n')
dec_fail = cod.Decripta(1.0+1.0e-15, 1.01, 1.1, texto_enc)
print(dec_fail.decripta)
print('\n')