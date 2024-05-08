Carros = {
    'opala':{
        'ano': 1977,
        'direção':"Mecânica",
        'Carburador':'Sim',
    },
    'Jetta':{
        'ano': 2017,
        'direção':"Hidráulica",
        'Carburador':'não',
    },

      'Porsche':{
      
        'ano': 2024,
        'direção':"Elétrica",
        'Carburador':'não',
    }

}

carro_desejado = input("qual carro você deseja visualizar?")

for carro_dejado in Carros:

    print("Este carro está disponivel em estoque!!")

else:
   print("Carro não encontrado")