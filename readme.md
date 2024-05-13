# Medical Data Visualizer

Este é um projeto Python que lida com análise e visualização de dados médicos. Ele inclui funções para adicionar uma coluna indicando se um paciente está com sobrepeso, normalizar dados, criar gráficos de contagem de variáveis categóricas e gerar um mapa de calor para mostrar a correlação entre diferentes variáveis médicas.

## Instalação

Para executar este projeto, siga estas etapas:

1. Certifique-se de ter Python instalado em seu sistema. Você pode baixá-lo em [python.org](https://www.python.org/).
2. Clone este repositório em seu ambiente local usando `git clone`.
3. Certifique-se de ter um arquivo `medical_examination.csv` contendo seus dados médicos no mesmo diretório.

## Uso

Este projeto consiste em três partes principais:

1. **medical_data_visualizer.py**: Este arquivo contém as funções para adicionar uma coluna indicando sobrepeso, normalizar os dados, criar gráficos de contagem de variáveis categóricas e gerar um mapa de calor para mostrar a correlação entre diferentes variáveis médicas.

2. **main.py**: Este arquivo executa o código principal do projeto. Ele importa as funções do `medical_data_visualizer.py`, carrega os dados do arquivo CSV, executa as funções para processar e visualizar os dados e mostra os resultados.

3. **test_module.py**: Este arquivo contém testes unitários para as funções em `medical_data_visualizer.py`. Ele verifica se as funções estão produzindo os resultados esperados.

Para executar o projeto, basta executar o arquivo `main.py`:

```bash
python main.py
```

## Contribuição

Se você quiser contribuir com melhorias para este projeto, sinta-se à vontade para abrir uma issue ou enviar um pull request. Toda contribuição é bem-vinda!

