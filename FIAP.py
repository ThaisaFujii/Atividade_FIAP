rom random import randint

class servicoHumanitario:
    def __init__(self):
        self.tempoIteracoes = 0
        self.pessoa = 0
        self.calculoRM = (71 % 3) + 1
        self.repeticaoRM = 0
        self.voluntarios = 1
        self.gerarSenha()
        self.gerarTempo()    

    def gerarSenha(self):
        #criar uma fila de atendimento com quantidade aleatoria de senha
        self.senhaEntregue = [0 for x in range(0, randint(1,15))]

    def gerarTempo(self):
        while True: #looping infinito
            if self.tempoIteracoes >= 100:
                self.verificarPessoa()
                self.tirarDaFila()

            self.tempoIteracoes += 1

            if len(self.senhaEntregue) <= 0: #freiar possiveis valores de zero a negativo
                break
    # a cada 2 min entra uma pessoa na fila// a cada 10repeticoes - 1min
    
    def verificarPessoa(self):
        if self.pessoa >= 20:
            self.pessoa = 0
            self.acrescentarNaFila()
        else:
            self.pessoa += 1
    
    def acrescentarNaFila(self):
        if len(self.senhaEntregue) < 15:
            self.senhaEntregue.append(self.tempoIteracoes)
            print("Foi adicionado outro morador")
    
    def tirarDaFila(self):
        if len(self.senhaEntregue) > 0 and self.repeticaoRM >= self.calculoRM * 10:
            remover = self.repeticaoRM = 0
            if len(self.senhaEntregue) > (3 * self.voluntarios):
                remover = 3 * self.voluntarios
            else:
                remover = len(self.senhaEntregue)
            print(f"Foram atendido(s) {remover} moradore(s) de rua, e o tempo de espera foi de:") # pessoas atendidas conforme a distribuição de comida
            for satisfeito in self.senhaEntregue[0:remover]:
                min = int((self.tempoIteracoes - satisfeito) / 10)
                print(f"{min} minutos \n")
            
            del self.senhaEntregue[0:remover] 
            print(f"Total de moradores {len(self.senhaEntregue)}") 

        else:
            self.repeticaoRM += 1
            
servicoHumanitario()
