# FP: 1o Projeto

## Curso: LEIC-A

### Aluno: ist1110034 - Marta Costa Braga

## Objetivo

Este projeto consiste na implementação de um conjunto de funções que permitem obter algumas informações sobre o estado de um território retangular formado por caminhos verticais e horizontais. As interseções dos caminhos podem ou não ser ocupadas por montanhas, formando cadeias de montanhas e vales.

## Funcionalidades

O projeto inclui as seguintes funções:

### 1. `eh_territorio(arg)`
Verifica se o argumento recebido é um território válido. Um território válido é um tuplo de tuplos em que cada tuplo representa um caminho vertical. Cada caminho deve ser identificado por uma letra entre 'A' e 'Z' e conter apenas valores 0 ou 1, correspondendo a espaços livres ou montanhas, respetivamente.

### 2. `obtem_ultima_intersecao(t)`
Retorna a interseção do extremo superior direito do território.

### 3. `eh_intersecao(arg)`
Verifica se um argumento representa uma interseção válida no formato ('letra', 'número'), onde 'letra' é uma única letra maiúscula entre 'A' e 'Z' e 'número' é um inteiro entre 1 e 99.

### 4. `eh_intersecao_valida(t, i)`
Verifica se uma interseção fornecida pertence ao território fornecido.

### 5. `eh_intersecao_livre(t, i)`
Verifica se uma interseção específica do território corresponde a um espaço livre (sem montanha).

### 6. `obtem_intersecoes_adjacentes(t, i)`
Retorna um tuplo com as interseções adjacentes à interseção fornecida dentro do território.

### 7. `ordena_intersecoes(tup)`
Ordena um tuplo de interseções de acordo com a ordem de leitura do território.

### 8. `territorio_para_str(t)`
Gera uma representação textual do território, onde os espaços livres são representados por '.' e as montanhas por 'X'.

### 9. `obtem_cadeia(t, i)`
Retorna todas as interseções conectadas à interseção fornecida, independentemente de serem espaços livres ou montanhas.

### 10. `obtem_vale(t, i)`
Retorna todas as interseções que fazem parte do vale ao redor de uma montanha específica.

### 11. `verifica_conexao(t, i1, i2)`
Verifica se duas interseções fazem parte da mesma cadeia, ou seja, se estão conectadas diretamente ou indiretamente.

### 12. `calcula_numero_montanhas(t)`
Calcula o número total de interseções ocupadas por montanhas dentro do território.

### 13. `calcula_numero_cadeias_montanhas(t)`
Calcula quantas cadeias de montanhas existem no território.

### 14. `calcula_tamanho_vales(t)`
Calcula o número total de interseções correspondentes a vales dentro do território.

## Como Usar
Para utilizar este projeto, basta importar as funções necessárias e aplicar os métodos de acordo com as especificações fornecidas acima.

## Exemplo de Uso
```python
territorio_exemplo = ((0,1,0), (1,0,1), (0,1,0))
print(eh_territorio(territorio_exemplo))  # True
print(obtem_ultima_intersecao(territorio_exemplo))  # ('C', 3)
print(territorio_para_str(territorio_exemplo))
```

## Erros e Exceções
Caso algum argumento inválido seja fornecido às funções, um erro `ValueError` será levantado para indicar a falha.


