

# Sistema de Empréstimos

# Restrições: 

# O VALOR DA PARCELA NÃO PODE SER MAIOR QUE 30% DO SALÁRIO

# A QUANTIDADE DE PARCELAS NÃO PODE SER MAIOR QUE 360

aprovado = 0

while aprovado == 0:
    print(""" 
              ----------------------------------------------
              Seja bem-vindo ao nosso sistema de empréstimos
              ----------------------------------------------
              \n""")
              
    salario = float(input('Por favor, digite o seu SALÁRIO: '))
    print(f'\nMuito bem! Seu salário é de R${salario}!')
    valor_emprestimo = float(input('\nAgora, digite o valor do empréstimo que quer efetuar: '))
    print(f'\nMuito bem! Você quer realizar um empréstimo de R${valor_emprestimo}!')
    qnt_parcelas = int(input('Agora, digite a quantidade de parcelas que você vai efetuar: '))
    if qnt_parcelas > 360:
        print('\nVocê só pode fazer parcelas de até 360 meses!')
        break
    else:
        valor_parcela = valor_emprestimo / qnt_parcelas
        teste_dos_30 = salario * 0.3 > valor_parcela
        if teste_dos_30:
            print(f''' 
                  
Muito bem! Empréstimo de R${valor_emprestimo} efetuado.
                  

O valor de R${valor_parcela} deve ser pago mensalmente por {qnt_parcelas} parcelas/meses.
                       
Se não, será cobrada uma taxa adicional pelo serviço.''')
        else:
            print(f'''\n
O seu sálario de R${salario} não é suficiente para realizar este empréstimo.
Porfavor, realizar a solicitação com um valor menor.
                       ''')
        aprovado += 1