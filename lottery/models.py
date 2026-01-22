from random import randint

class Lottery:
    """Teste"""
    
    def __init__(self, inicio=1, fim=60):
        self.inicio = inicio 
        self.fim = fim 
        self.my_numbers = [0, 0, 0, 0, 0, 0]

    def _numerical_sequence (self):
        """Gera uma sequência de números aleatórios para a lista"""
        lista = []

        while len(lista) < 6:
            aleatorio = randint(self.inicio, self.fim)
            if aleatorio not in lista:
                lista.append(aleatorio)
        lista.sort()
        return lista
        
    def draw_number(self):
        ultimo_sorteio = self._numerical_sequence()
        return ultimo_sorteio

    def my_bet(self):
        numbers = []
        for number in range(6):
            while True:
                mensagem_erro = ""
                try:
                    chosen_number = int(input(f'Escolha o {number+1}º número: '))
                except ValueError as erro:
                    print('Tipo de erro:', erro)
                    continue
                if chosen_number in numbers:
                    mensagem_erro = 'Número repetido. Insira outro número. '
                elif chosen_number > 60:
                    mensagem_erro = 'Número maior que 60. Escolha um número de 1 a 60'
                elif chosen_number < 1:
                    mensagem_erro = 'Número menor que 1. Escolha um número de 1 a 60'
                if mensagem_erro:
                    print(mensagem_erro)
                    continue
                break
            numbers.append(chosen_number)
        numbers.sort()
        self.my_numbers = numbers

    def comparar(self):
        for n in range(10000):
            numero_comparar = self.draw_number()
            if self.my_numbers == numero_comparar:
                msg = 'Você ganhou!'
                return n+1, msg, numero_comparar
        msg = 'Tentativas esgotadas, você perdeu!'   
        return n+1, msg, None