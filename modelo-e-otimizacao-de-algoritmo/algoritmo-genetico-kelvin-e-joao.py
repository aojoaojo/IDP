import pygame
import random
import math

TAMANHO_POP = 50
SELECIONADOS_POR_GEN = 4
MUTACAO = 0.05
LARGURA, ALTURA = 800, 600
CICLO_DE_VIDA = 75

pygame.init()
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Algoritmo Genético - Mosca na Comida")
clock = pygame.time.Clock()

class Individuo:
    def __init__(self):
        self.posicao = [random.randint(0, LARGURA), random.randint(0, ALTURA)]
        self.movimentos = [[random.uniform(-5, 5), random.uniform(-5, 5)] for _ in range(CICLO_DE_VIDA)]
        self.index_mov = 0
        self.fitness = float('inf')
        self.eh_pai = False

    def calcula_adaptacao(self, objetivo):
        dist = math.dist(self.posicao, objetivo)
        self.fitness = dist

    def move(self):
        if self.index_mov < len(self.movimentos):
            self.posicao[0] += self.movimentos[self.index_mov][0]
            self.posicao[1] += self.movimentos[self.index_mov][1]
            self.index_mov += 1

    def __repr__(self):
        return f"Posição: {self.posicao} | Fitness: {self.fitness:.2f}"

class Populacao:
    def __init__(self, objetivo):
        self.individuos = [Individuo() for _ in range(TAMANHO_POP)]
        self.objetivo = objetivo
        self.num_geracao = 0

    def calcula_qualidade(self):
        for ind in self.individuos:
            ind.calcula_adaptacao(self.objetivo)

    def selecao_natural(self):
        self.individuos.sort(key=lambda x: x.fitness)
        selecionados = self.individuos[:SELECIONADOS_POR_GEN]
        selecionados += random.sample(self.individuos[SELECIONADOS_POR_GEN:], SELECIONADOS_POR_GEN * 3)
        return selecionados

    def crossover(self, pai1, pai2):
        filho = Individuo()
        filho.posicao[0] = (pai1.posicao[0] + pai2.posicao[0]) / 2
        filho.posicao[1] = (pai1.posicao[1] + pai2.posicao[1]) / 2
        return filho

    def mutacao(self, ind):
        if random.random() < MUTACAO:
            ind.posicao[0] = random.randint(0, LARGURA)
            ind.posicao[1] = random.randint(0, ALTURA)

    def nova_geracao(self):
        selecionados = self.selecao_natural()
        for i in selecionados:
            i.eh_pai = True
        nova_geracao = selecionados[:]
        while len(nova_geracao) < TAMANHO_POP:
            pai1, pai2 = random.sample(selecionados, 2)
            filho = self.crossover(pai1, pai2)
            self.mutacao(filho)
            nova_geracao.append(filho)
        self.individuos = nova_geracao
        self.num_geracao += 1

def algoritmo_genetico():
    objetivo = [LARGURA // 2, ALTURA // 2]
    populacao = Populacao(objetivo)

    rodando = True
    while rodando:
        tela.fill((0, 0, 0))
        pygame.draw.circle(tela, (0, 255, 0), objetivo, 10)  # Desenhar a comida

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

        for ind in populacao.individuos:
            ind.move()
            if ind.eh_pai:
                pygame.draw.circle(tela, (255, 255, 0), (int(ind.posicao[0]), int(ind.posicao[1])), 5)
            else:
                pygame.draw.circle(tela, (255, 0, 0), (int(ind.posicao[0]), int(ind.posicao[1])), 5)

        populacao.calcula_qualidade()
        if all(ind.index_mov >= len(ind.movimentos) for ind in populacao.individuos):
            populacao.nova_geracao()

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    algoritmo_genetico()