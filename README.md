### inf1048-IA-T3

TRABALHO 3 - Repositório da disciplina de Inteligência Artificial (INF01048), Instituto de Informática, UFRGS.  
Kit para implementar agentes de **Value Iteration** e **Q-Learning** e testar em Gridworld, Crawler e Pacman.

## Alunos 
GUILHERME MERLINI DE SOUZA - 342474
VICTOR DE SOUZA ARNT   - 291097


---

### Conteúdo do repositório

Arquivos que você deve **editar**:

- **valueIterationAgents.py** — implementar o agente de iteração de valor.  
- **qlearningAgents.py** — implementar agentes Q-learning e Approximate Q-learning.  
- **analysis.py** — respostas às questões analíticas do enunciado.

Arquivos que você deve **ler, mas não editar**:

- **mdp.py** — definição de MDPs.  
- **learningAgents.py** — classes base ValueEstimationAgent e QLearningAgent.  
- **util.py** — utilitários, incluindo util.Counter.  
- **gridworld.py** — implementação do Gridworld.  
- **featureExtractors.py** — extratores de features para Q-learning aproximado.

Arquivos opcionais / de suporte (não editar):

- **environment.py**, **graphicsGridworldDisplay.py**, **textGridworldDisplay.py**, **crawler.py**, **graphicsCrawlerDisplay.py**, **autograder.py**, **testCases/**, **reforcementTestClasses.py**, entre outros.

---

### Requisitos

- **Python 3** (testado com versões 3.7+; recomenda-se 3.9).  
- Dependências padrão do kit; nenhuma biblioteca externa obrigatória para executar os exemplos básicos.  
- Para a interface gráfica do Gridworld ou Crawler, siga as instruções específicas no enunciado se desejar usar GUI.

---

### Como executar e testar

Executar Gridworld em modo manual:

```bash
python gridworld.py -m
```

Executar agente de iteração de valor (exemplo):

```bash
python gridworld.py -a value -i 100 -k 10
```

Executar agente Q-learning no Gridworld (modo manual):

```bash
python gridworld.py -a q -k 5 -m
```

Executar o crawler com Q-learning:

```bash
python crawler.py
```

Executar Pacman com o agente Q-learning (treinamento e teste):

```bash
python pacman.py -p PacmanQAgent -x 2000 -n 2010 -l smallGrid
```

Usar o **autograder** local para verificar cada questão:

```bash
python autograder.py
python autograder.py -q q1
python autograder.py -q q2
python autograder.py -q q3
python autograder.py -q q4
python autograder.py -q q5
python autograder.py -q q6
```

Para executar um teste específico do autograder:

```bash
python autograder.py -t test_cases/q2/1-bridge-grid
```

---

### Tarefas e critérios principais

- **Questão 1 — Iteração de Valor**: implementar ValueIterationAgent com atualização em batch, `computeQValueFromValues` e `computeActionFromValues`.  
- **Questão 2 — BridgeGrid**: alterar apenas **um** parâmetro (desconto ou ruído) para que a política ótima atravesse a ponte; resposta em `analysis.py`.  
- **Questão 3 — Q-Learning**: implementar `update`, `computeValueFromQValues`, `getQValue`, `computeActionFromQValues`.  
- **Questão 4 — Epsilon Greedy**: implementar seleção epsilon-greedy em `getAction`.  
- **Questão 5 — Pacman**: treinar e testar PacmanQAgent; parâmetros padrão do PacmanQAgent já definidos.  
- **Questão 6 (extra)** — Q-Learning aproximado: implementar `ApproximateQAgent` usando extratores de features e atualização de pesos.

---

### Avaliação e entrega

**Rubrica resumida**:

- Questão 1: 30 pontos  
- Questão 2: 5 pontos  
- Questão 3: 40 pontos  
- Questão 4: 10 pontos  
- Questão 5: 10 pontos  
- Estrutura e group.md: 5 pontos  
- Questão 6 (extra): 10 pontos  
- Nota máxima: 100 pontos

**Entrega**: enviar um arquivo `.zip` com os seguintes arquivos na raiz do zip:

1. **valueIterationAgents.py**  
2. **qlearningAgents.py**  
3. **analysis.py**  
4. **group.md** — arquivo de texto simples com nomes, números de matrícula e turma dos integrantes do grupo

Todos os quatro arquivos devem estar na raiz do `.zip`.

---

### Dicas e observações

- Use **util.Counter** para armazenar valores e Q-values.  
- Garanta que `computeActionFromQValues` e `getAction` tratem corretamente ações não vistas, considerando valor-Q igual a zero.  
- Para o ApproximateQAgent, implemente pesos como um dicionário mapeando features para valores e atualize-os pela regra de Q-learning aproximado.  
- Não altere assinaturas de funções ou nomes de classes fornecidos pelo kit, pois isso pode quebrar o autograder.  
- Em caso de dúvidas, consulte a equipe do curso e evite postar soluções completas publicamente para não gerar spoilers.

---

Se quiser, eu posso gerar um **modelo de `group.md`** pronto para você preencher com os dados do grupo e um checklist de testes a executar antes de compactar o `.zip`. Quer que eu gere esses arquivos agora?