from lottery.models import Lottery
from lottery.storage import BancoJSON
from pathlib import Path
import os

class App:
    def __init__(self, ):
        self.sorteio = Lottery(1, 20)
        self.db = BancoJSON('data/db.numbers.json')

    def pergunta(self):
        """OBJETIVO: REDUZIR AS REPETICÕES ANINHADAS"""
        while True:
            try:
                resposta = int(input('\n\nOutra sequência numérica: 1(Sim) ou 2(Não): \n'))
            except ValueError:
                print('Entrada inválida')
                continue
            if resposta == 1:
                return 'continuar'
            elif resposta == 2:
                return 'Encerrar'
            else:
                print('RESPOSTA INVÁLIDA. TENTE NOVAMENTE')


    def menu(self):

        while True:
            print('Bem vindo ao Programa: ')
            print('1. Resultado Mega Sena')
            print('2. Cálculo de Possibilidades.')
            print('3. listar itens na memória.')
            print('4. Apagar dados')
            print('5. Sair')
            print('0. Limpar terminal')
            try:
                op = int(input('Qual opção seria? '))
        
                if op == 1:
                    while True:
                        sorteio = self.sorteio.draw_number()
                        self.db.adicionar(sorteio)

                        print('Os números sorteados foram: ', end=' ')
                        for numero in sorteio: 
                            print(f'{numero} ', end=' ')
            
                        if self.pergunta() == 'continuar':
                            continue
                        break

                elif op == 2:
                    self.sorteio.my_bet()
                    resultado, mensagem, numero_sorteado = self.sorteio.comparar()
                    if numero_sorteado:
                        self.db.adicionar(numero_sorteado)
                    print(f'Tentativas: {resultado} | {mensagem}')

                elif op == 3:
                    if self.db.dados:
                        for lista in self.db.dados:
                            print(f"\n{lista}")
                        print()
                    else:
                        print('Sem dados no sistema!!!')

                elif op == 4:
                    print(self.db.apagar())

                elif op == 5:
                    print('Programa Encerrado.')
                    break
                
                elif op == 0:
                    limpar_terminal()

                else:
                    print("Opção inválida. Tente novamente.\n")
                
                

            except ValueError as erro:
                print('Entrada inválida.\n', erro)
                continue

def limpar_terminal():
    os.system('cls')


if __name__ == "__main__":
    app = App()
    app.menu()
