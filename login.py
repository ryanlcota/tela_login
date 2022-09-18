#criando meu primeiro codigo de login


#print escreve algo na tela para o usuario
print('LOGIN DE SEGURANCA')

#usuario e confirmacao_usuario sao variaveis ( que sao utilizadas para guardar valores)

#input e utilizado para o usuario inserir algo
usuario=input('crie seu login\n')
confirmacao_usuario=input ('repita seu login\n')

#while e utilizado para enquanto algo estiver acontencendo
while usuario != confirmacao_usuario:
    usuario = input('crie seu login\n')
    confirmacao_usuario = input('repita seu login\n')

senha=input('crie uma senha\n')
confirmacao_senha=input("confirme sua senha")

while senha != confirmacao_senha:

    senha = input('crie uma senha\n')
    confirmacao_senha = input("confirme sua senha")

print('cadastro realizado com sucesso')


