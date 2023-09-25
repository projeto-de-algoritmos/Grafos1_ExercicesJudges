# Integrantes

|                         Nome                         | Matrícula |
| :--------------------------------------------------: | :-------: |
|  [Pedro Torreão](https://github.com/PedroTorreao21)  | 190036761 |
| [Matheus Perillo](https://github.com/MatheusPerillo) | 190093421 |

# Introdução

Este repositório foi criado para o desenvolvimento do primeiro módulo sobre Grafos 1 da disciplina Projeto de Algoritmos do Professor Maurício Serrano.

# Apresentação

[Link para a apresentação da dupla](https://youtu.be/R7xIfYTEdRc)

# Foram feitos os exercícios no LeetCode

## [785. Is Graph Bipartite (Medium)](https://leetcode.com/problems/is-graph-bipartite/description/)

Há um grafo não direcionado com n nós, onde cada nó é numerado de 0 a n - 1. Você recebe uma matriz 2D chamada 'graph', onde 'graph[u]' é uma matriz de nós aos quais o nó u é adjacente. Mais formalmente, para cada v em 'graph[u]', há uma aresta não direcionada entre o nó u e o nó v. O grafo possui as seguintes propriedades:

Não existem autoarestas (a matriz 'graph[u]' não contém o próprio u).
Não existem arestas paralelas (a matriz 'graph[u]' não contém valores duplicados).
Se v estiver em 'graph[u]', então u estará em 'graph[v]' (o grafo é não direcionado).
O grafo pode não estar conectado, o que significa que pode haver dois nós u e v nos quais não há um caminho entre eles.
Um grafo é bipartido se os nós puderem ser divididos em dois conjuntos independentes A e B de forma que cada aresta no grafo conecte um nó no conjunto A a um nó no conjunto B.

Retorne verdadeiro se e somente se o grafo for bipartido.

![785. Is Graph Bipartite](/images/785.jpeg)

## [684. Redudant Connection (Medium)](https://leetcode.com/problems/redundant-connection/description/)

Neste problema, uma árvore é um grafo não direcionado que é conectado e não tem ciclos.

Você recebe um grafo que começou como uma árvore com n nós rotulados de 1 a n, com uma aresta adicional adicionada. A aresta adicionada tem dois vértices diferentes escolhidos de 1 a n e não era uma aresta que já existia. O grafo é representado como uma matriz chamada 'edges' de comprimento n, onde 'edges[i] = [ai, bi]' indica que existe uma aresta entre os nós ai e bi no grafo.

Retorne uma aresta que pode ser removida para que o grafo resultante seja uma árvore com n nós. Se houver várias respostas, retorne a resposta que ocorre por último na entrada.

![684. Redudant Connection](/images/684.jpeg)

## [2608. Shortest Cycle in a Graph (Hard)](https://leetcode.com/problems/shortest-cycle-in-a-graph/description/)

Existe um gráfico bidirecional com n vértices, onde cada vértice é rotulado de 0 a n - 1. As arestas no gráfico são representadas por uma determinada matriz de inteiros 2D arestas, onde arestas[i] = [ui, vi] denota uma aresta entre o vértice ui e o vértice vi. Cada par de vértices é conectado por no máximo uma aresta, e nenhum vértice possui uma aresta própria.

Retorne a duração do ciclo mais curto no gráfico. Se não existir nenhum ciclo, retorne -1.

Um ciclo é um caminho que começa e termina no mesmo nó, e cada aresta do caminho é usada apenas uma vez.

![2608. Shortest Cycle in a Graph](/images/2608.jpg)

## [2360. Longest Cycle in a Graph (Hard)](https://leetcode.com/problems/longest-cycle-in-a-graph/description/)

Você recebe um gráfico direcionado de n nós numerados de 0 a n - 1, onde cada nó tem no máximo uma aresta de saída.

O gráfico é representado com arestas de array indexadas em 0 de tamanho n, indicando que há uma aresta direcionada do nó i para as arestas do nó [i]. Se não houver aresta de saída do nó i, então arestas[i] == -1.

Retorne a duração do ciclo mais longo no gráfico. Se não existir nenhum ciclo, retorne -1.

Um ciclo é um caminho que começa e termina no mesmo nó.

![2360. Longest Cycle in a Graph](/images/2360.jpg)

# Instalação

Pré-Requisitos: Os códigos devem ser rodados na própria plataforma do Leetcode, tendo em vista o uso de uma classe Solution, bem como o uso correto dos inputs por parte da plataforma.

Caso queira rodar local, é necessário somente chamar o método da classe com os paramêtros condizente com a assinatura de acordo com a linguagem desenvolvida.

# Uso

## Passo 1: Copiar o código

Entre na pasta do exercício específico, clique no arquivo e copie-o.

## Passo 2: Entrar na página do exercício

Ao clicar no título de cada questão presente neste README, você será redirecionado para a página da questão.

## Passo 3: Alterar linguagem

Selecione a linguagem.

## Passo 4: Colar o código

Cole o código copiado no editor.

## Passo 5: Rodar o código

Abaixo do editor de código, clique em Run para executar o código.
