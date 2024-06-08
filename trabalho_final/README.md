# Pensamento-de-Lean-simulado-em-netlogo

- Netlogo - lean thinking - queue - Campus Dining

## Simulação de Fluxo de Pessoas

Este projeto simula o fluxo de pessoas através de vários estágios utilizando NetLogo. A simulação permite observar o tempo médio gasto por pessoas em diferentes estágios de um sistema definido.

### Visão Geral

A simulação modela a passagem de estudantes por uma série de estágios: `ENTRY`, `PAY`, `B1`, `B2`, `B3`, `B4`, `B5`, `B6`, `B7`, e `EXIT`. A cada tick, os estudantes podem se mover de um estágio para o próximo, dependendo de certas condições. O objetivo é calcular e exibir o tempo médio que os estudantes passam em cada estágio.

### Estrutura do Código

- **setup**: Inicializa a simulação, criando os patches e estudantes.
- **create-sector**: Define os patches que representam cada estágio.
- **create-public**: Cria os estudantes e os posiciona no estágio inicial (`ENTRY`).
- **go**: Função principal de execução que move os estudantes e exibe os tempos médios.
- **move-students**: Lógica de movimento dos estudantes entre os estágios.
- **update-stage-time**: Atualiza o tempo total e a contagem de estudantes em cada estágio.
- **average-time**: Calcula o tempo médio para um dado estágio.
- **display-average-times**: Exibe os tempos médios para todos os estágios.

### Instalação

1. Certifique-se de ter o [NetLogo](https://ccl.northwestern.edu/netlogo/) instalado em sua máquina.
2. Clone este repositório ou faça o download dos arquivos.

```sh
git clone https://github.com/seu-usuario/simulacao-fluxo-pessoas.git
```

3. Abra o NetLogo e carregue o arquivo .nlogo do projeto.

### Uso

1. Abra o NetLogo.
2. Carregue o modelo .nlogo do projeto.
3. Clique no botão Setup para inicializar a simulação.
4. Clique no botão Go para iniciar a simulação. A simulação continuará até que todos os estudantes tenham passado pelo estágio EXIT.
5. Observe os tempos médios exibidos na interface para cada estágio.

### Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

### Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo LICENSE para obter mais informações.

### Contato

Para mais informações, entre em contato através do [email](<raphael.mauricio@gmail.com>).

### Agradecimentos

Agradeço ao professor Gilberto Gil pelas aulas incriveis, aos colegas pelo suporto e coleguismo em aula, a UFRJ e a Universidade Northwestern pelo desenvolvimento do NetLogo.
