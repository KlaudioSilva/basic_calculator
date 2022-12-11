print('''
--------------------------------------
 BEM VINDO À CALCULADORA BÁSICA v.1.0
--------------------------------------
''')
res = 'SN'
while True:
    # escolha uma operação
    operation = input ('''
Escolha qual operação matemática você deseja executar: 
    + para adição
    - para subtração
    * para multiplicação
    / para divisão
-->  ''')[0]

    # corrigindo operador inválido
    while operation not in '+-*/':
        operation = input('Você não escolheu um operador válido. Tente outra vez: ')[0]

    print('-' * 30)
    num1 = int(input('Primeiro número: '))
    num2 = int(input('Segundo número: '))
    print('-' * 30)

    # adição
    if operation == '+':
        print(f'{num1} + {num2} = ')
        print(num1 + num2)

    # subtração
    elif operation == '-':
        print(f'{num1} - {num2} = ')
        print(num1 - num2)

    # multiplicação
    elif operation == '*':
        print(f'{num1} x {num2} = ')
        print(num1 * num2)

    # divisão
    elif operation == '/':
        # tratando o erro da divisão de zero
        while num1 == 0:
            num1 = int(input('ERRO! Impossível divisão do zero. Digite outro número: '))
        print(f'{num1} ÷ {num2} = ')
        print(num1 / num2)

    res = str(input('''
Você deseja continuar?
Digite S para SIM e N para NÃO: 
-->  ''')).strip().upper()[0]

    # validando a resposta
    while res not in 'SN':
        res = str(input('''
Resposta Inválida! Você deseja continuar?
Digite S para SIM e N para NÃO: 
-->  ''')).strip().upper()[0]

    if res == 'N':
        break
    else:
        print('-' * 50)
        
print('-' * 50)
print('Até Logo.')
print()
