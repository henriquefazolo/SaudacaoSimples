'''
Escreva na tela “Boa Madrugada”, “Bom dia”, “Boa tarde” ou “Boa noite”
dependendo da hora do dia que o usuário digitar no teclado.
Caso a hora seja inválida mostre: “Erro. Hora inválida”. O
pcional: mostre uma imagem diferente para cada alternativa.
'''


class Saudacao:
    def __init__(self):
        self.hora = -1
        self.minutos = -1

    def set_relogio(self):
        """
        Usuario deve inserir numeros inteiro para horas e minutos
        """
        while self.hora not in range(0, 24):
            self.hora = int(input('Insira a hora : '))
            if self.hora not in range(0, 24):
                print('Erro. Hora inválida.Insira uma valor de 0 a 23')

        while not 0 <= self.minutos < 60:
            self.minutos = int(input('Insira os minutos : '))
            if self.hora not in range(0, 60):
                print('Erro. minuto inválido. Insira uma valor de 0 a 59')

    def get_relogio(self):
        """

        :return: Retorna sts das horas
        """
        return f'\nHora :  {self.hora}:{self.minutos} \n'

    def saudacao(self):
        """
        :return: Retorna uma saudação conforme a hora informada.
        """
        if self.hora in range(0, 7):
            return 'Boa Madrugada'
        elif self.hora in range(7, 13):
            return 'Bom dia'
        elif self.hora in range(13, 19):
            return 'Boa tarde'
        elif self.hora in range(19, 24):
            return 'Boa noite'


a = Saudacao()
a.set_relogio()
print(a.get_relogio())
print(a.saudacao())

