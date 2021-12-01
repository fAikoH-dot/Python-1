meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

def mes():                                          #função mês
    n = int(input("Digite o número do mês: "))      #recebe o número do mês
    while n<=0 or n>12:                             #para valores inválidos
        n = int(input("Digite o número do mês: "))  
    print(meses[n-1])                               #retorna o nome do mês

mes()                                               #chama a função
