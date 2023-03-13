meses = ['jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']

for mes in meses:
    print('Mês {0} ->'.format(mes), end=' ')

    if mes in (meses[1]):
        for dia in range(1, 29):
            print(dia, end=' ')
        print()

    elif mes in (meses[3],meses[5],meses[8],meses[10]):
        for dia in range(1, 31):
            print(dia, end=' ')
        print()

    else:
        for dia in range(1, 32):
            print(dia, end=' ')
        print()
