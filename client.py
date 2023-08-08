import connection as cn
import random 
import time

s = cn.connect(2037)

# inicializar tabela com valores aleatórios? ---------------------------------------------------
# epsilon gradient decay n sei o que ------------------------------------------------------------

# globais
qtable = [[0.0 for i in range(3)] for j in range(96)] # qtable[i][j] = qualidade da ação j a partir do estado i
jogadas = ["left", "right", "jump"] # Define as possíveis jogadas
alfa = 0.2 # Taxa de aprendizagem
gama = 0.5 # Taxa de desconto

def update(estado, acao, recompensa, prox_estado):
    mx = max(qtable[prox_estado][0],qtable[prox_estado][1],qtable[prox_estado][2]) # ação de melhor qualidade possível a partir de next_state
    estimativa = recompensa + gama * mx
    qtable[estado][acao] = qtable[estado][acao] + alfa*(estimativa - qtable[estado][acao])

# linhas 0 a 3: plataforma 1, Norte Leste Sul Oeste
# linhas 4 a 7: plataforma 2, NSLO

satual = 0 # estado inicial ---------------------------------------------
#corrigir lógica se tiver tudo 1 based

i = 100

while (i > 0):
    action = random.randint(0,2)
    action_str = jogadas[action]
    # Recebe o estado e a recompensa resultantes da ação
    state_in, reward = cn.get_state_reward(s, action_str)
    
    state_in = str(state_in)
    platform = int(state_in[2:7], 2) # Converting platform number to integer
    direction = int(state_in[7:9], 2) # North = 00 / East = 01 / South = 10 / West= 11
    print(state_in)

    state = (platform * 4) + (direction % 4) # corresponde à linha

    update(satual, action, reward, state)

    satual = state

    time.sleep(5)

    i = i - 1

with open('resultado.txt', 'w') as f:
    for i in range(96):
        for j in range(3):
            f.write(str(qtable[i][j]) + " ")
        f.write("\n")


