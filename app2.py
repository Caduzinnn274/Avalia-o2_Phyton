
credenciais_Cliente = {
    'alice123': {'username': 'alice123',
                 'password': 'alic3P@pass0rd',
                 'status': 'active',
                },
    'bob456': {'username': 'bob456',
                 'password': 'bobP@xssword',
                 'status': 'inactive',
                },
    'charlie789': {'username': 'charlie789',
                 'password': 'Ch@rliecP@ss9',
                 'status': 'active',

                }
}

alerta = 'Enviar alerta!' if credenciais_Cliente.get('bob456', {}).get('status') == 'inactive' else 'sem alerta!'
print(credenciais_Cliente)
print(alerta)