try:
    a = int(input('Numerador: '))
    b = int(input('Demonimador: '))
    r = a / b
except (ValueError, TypeError):
    print('Tivemos um problema com os titpos dados que você digitou')
except (ZeroDivisionError):
    print('Não é possível dividir um númeo por zero!')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados!')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre! Muito obrigado!')