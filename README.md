# Algoritmo A* para Busca de Caminhos

### 👥 Dupla:
- **Willian Dias**
- **Alesson Tito**

## 🧠 O que é o algoritmo A*?

O algoritmo A* (A Estrela) é um algoritmo de busca heurística muito utilizado para encontrar o menor caminho entre dois pontos em um grafo, mapa ou grid. Ele combina os melhores aspectos da busca por custo uniforme (BFS com prioridade) e da busca gulosa, utilizando uma função de custo `f(n) = g(n) + h(n)`:

- `g(n)`: custo real do início até o ponto atual.
- `h(n)`: estimativa heurística do custo do ponto atual até o destino.

No nosso projeto, utilizamos o A* para buscar caminhos em um mapa representado por números, respeitando as seguintes **regras**:

- Paredes (representadas por `1`) não podem ser atravessadas.
- Somente os caminhos livres (`0`) são válidos.
- Movimentações **diagonais** só são permitidas quando **não há parede entre os dois pontos adjacentes na horizontal/vertical**.

### 🗺️ MAPA
![image](https://github.com/user-attachments/assets/f20640b5-ddd7-4176-9208-d6598de24195)

## 📄 Como rodar a aplicação

### 1. Clone o repositório:

bash
git clone https://github.com/WillianDias1/Busca-A-estrela-.git

cd Busca-A-estrela-

### 2. Requisitos
Python 3.x instalado

Biblioteca openpyxl (para leitura de planilhas)

Instale com:
pip install openpyxl

### 3. Execute o programa
Você pode rodar o script principal com:
python main.py

O programa vai solicitar o ponto inicial e o ponto final (conforme a numeração da planilha). Em seguida, ele irá:

Carregar o mapa

Aplicar o algoritmo A*

Exibir o menor caminho entre os dois pontos (ou informar se não há caminho possível)