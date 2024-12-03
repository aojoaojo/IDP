import random

# Configurações do problema
horas_totais = 8  # Total de horas disponíveis por dia
atividades = ["Estudo", "Academia", "Compras", "Trabalho", "Lazer"]
min_tempo = [2, 1, 1.5, 3, 0]  # Tempo mínimo para cada atividade
max_tempo = [3, 2, 2, 4, 1]  # Tempo máximo para cada atividade

# Função de avaliação (fitness)
def calcular_fitness(individuo):
    produtividade = individuo[0] + individuo[3]  # Estudo + Trabalho
    bem_estar = individuo[1] + individuo[4]  # Academia + Lazer
    penalidade = max(0, sum(individuo) - horas_totais) * 10  # Penalidade se exceder 8h
    return produtividade + bem_estar - penalidade

# Gera um indivíduo aleatório
def gerar_individuo():
    return [random.uniform(min_tempo[i], max_tempo[i]) for i in range(len(atividades))]

# Gera a população inicial
def gerar_populacao(tamanho):
    return [gerar_individuo() for _ in range(tamanho)]

# Seleção por torneio
def selecao(populacao):
    torneio = random.sample(populacao, 3)
    return max(torneio, key=calcular_fitness)

# Cruzamento (crossover)
def cruzamento(pai1, pai2):
    ponto_corte = random.randint(1, len(atividades) - 1)
    filho = pai1[:ponto_corte] + pai2[ponto_corte:]
    return filho

# Mutação
def mutacao(individuo, taxa_mutacao=0.1):
    if random.random() < taxa_mutacao:
        indice = random.randint(0, len(atividades) - 1)
        individuo[indice] = random.uniform(min_tempo[indice], max_tempo[indice])
    return individuo

# Algoritmo genético principal
def algoritmo_genetico(geracoes, tamanho_populacao):
    populacao = gerar_populacao(tamanho_populacao)
    
    for _ in range(geracoes):
        nova_populacao = []
        
        for _ in range(tamanho_populacao):
            pai1 = selecao(populacao)
            pai2 = selecao(populacao)
            filho = cruzamento(pai1, pai2)
            filho = mutacao(filho)
            nova_populacao.append(filho)
        
        populacao = nova_populacao
    
    melhor_individuo = max(populacao, key=calcular_fitness)
    return melhor_individuo, calcular_fitness(melhor_individuo)

# Configurações do algoritmo
tamanho_populacao = 20
geracoes = 50

# Executa o algoritmo
melhor_rotina, melhor_fitness = algoritmo_genetico(geracoes, tamanho_populacao)

# Exibe os resultados
print("Melhor rotina encontrada:")
for i, atividade in enumerate(atividades):
    print(f"{atividade}: {melhor_rotina[i]:.2f} horas")
print(f"Fitness: {melhor_fitness:.2f}")
