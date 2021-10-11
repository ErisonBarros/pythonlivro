# Ambientes de Trabalho

## Jupyter notebooks 

A instalação básica do Anaconda vem com vários pacotes que iremos cobrir neste livro, incluindo NumPy, pandas e SciPy, para computação matemática e análise de dados; Matplotlib para visualização de dado; scikit-learn, para aprendizagem de máquina. Além disso, Anaconda conta também com a ferramenta Jupyter Notebooks, um ambiente computacional Web, composto de células que podem conter código, texto (usando [Markdown](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)), fórmulas e mídias, permitindo um rápido e interativo desenvolvimento exploratório de soluções em diversas linguagens, como Python, R, Julia, Haskell, Javascript, etc (o termo Jupyter vem de Julia, Python e R). No campo acadêmico, os notebooks oferecem a possibilidade de posicionar texto e fórmulas (como e arquivos LaTeX) próximos aos códigos correspondentes, favorecendo a reproducibilidade dos resultados.

Jupyter notebooks são inclusive a base para a construção deste material, permitindo, por exemplo, que a célula de código abaixo seja totalmente interativa, caso o(a) leitor(a) esteja acessando a versão online do livro. Para modificar o código, basta clicar no ícone em formato de lápis que aparece à direita da célula quando o ponteiro do mouse é posicionado sobre ela. Pode-se também clicar no botão "Interagir", posicionado no topo da tela. Para testar a(s) modificação(ões), basta clicar em _run_. O resultado da primeira execução pode demorar um pouco. 

print('Hello World!')

### Usando Jupyter notebooks

Devido a sua característica de interatividade e sua capacidade de misturar vários tipos diferentes de conteúdos, os notebooks são ideais para estudar e praticar Python. Portanto, é interessante aprender a usá-los antes mesmo de começar o estudo da linguagem de programação em si. Para começar, crie uma pasta para os seus notebooks, abra um terminal (ou prompt de comandos no Windows) e faça:

```bash
cd meusnotebooks
jupyter notebook
```
O segundo comando irá iniciar um servidor jupyter automaticamente e abrirá uma aba no seu navegador com o conteúdo mostrado na {numref}`jupyter-home`.


:::{figure-md} jupyter-home
<img src="images/jupyter-home.png" alt="Tela inicial da ferramenta Jupyter notebooks"/>

Tela inicial da ferramenta Jupyter notebooks.
:::

Esta tela lista os notebooks que forem salvos na pasta _meusnotebooks_. Além disso, é possível criar novos notebooks, bastando clicar no botão _New_ e escolher a opção _Python 3_ (ou a opção que corresponde à versão de Python que está sendo executada), o que irá abrir outra aba no seu navegador, como mostra a {numref}`jupyter-notebook`.

:::{figure-md} jupyter-notebook
<img src="images/jupyter-notebook.png" alt="Jupyter notebook recém criado"/>

Jupyter notebook recém criado.
:::

Para dar um nome ao seu notebook, basta clicar em _Untitled_, no topo da tela. O notebook já é criado com uma célula de código. Usando o menu _Insert_, é possível adicionar novas células acima (_above_) ou abaixo (_below_) da célula selecionada. No menu _Cell_ é possível executar a célula selecionada, o que também pode ser feito por meio do botão _Run_ ou apertando as teclas _shift + Enter_. 

O menu _Cell_ também permite mudar o tipo da célula selecionada, incluindo células de [Markdown](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) e de código. Ao executar células Markdown, seu conteúdo é processado e transformado em texto formatado de acordo com as marcações usadas. Já as células de código podem ter saídas de texto, gráficos ou nenhuma saída. Variáveis inicializadas (mais sobre isso mais à frente) em células executadas podem ser lidas em células posicionadas mais abaixo no notebook.

## Outros ambientes de desenvolvimento

Há muitos outros ambientes de desenvolvimento disponíveis para Python, como mostra a {numref}`poll-top-python-ide`, construída com base em respostas de mais de 1900 desenvolvedores à pergunta "Que editores Python ou IDEs você mais usou em 2018?", feita pelo website KDnuggets {cite}`piatetskyPopular2018`. Os resultados somam para mais de 100% porque os desenvolvedores podiam indicar até 3 escolhas, com cerca de 43% relatando apenas uma escolha, 30% indicando duas e os 27% restantes com 3 escolhas.   

:::{figure-md} poll-top-python-ide
<img src="images/poll-top-python-ide.jpg" alt="IDEs e editores de texto para Python mais populares em dezembro de 2018"/>

IDEs e editores de texto para Python mais populares em dezembro de 2018.
:::

Já discutimos as vantagens dos notebooks Jupyter acima, mas eles entram em desvantagem quando o objetivo é desenvolver um projeto complexo, com múltiplos módulos interconectados. Nesses casos, o ideal é adotar um ambiente de desenvolvimento integrado (IDE, do inglês _integrated development environment_) ou um editor de texto dedicado, que forneça ferramentas para detecção e correção de erros, controle de versão, formatação de código, etc. A {numref}`poll-top-python-ide` mostra que, além dos notebooks Jupyter, as três ferramentas mais usadas para desenvolvimento em Python são PyCharm, Spyder e Visual Studio Code.

### PyCharm

[PyCharm](https://www.jetbrains.com/pycharm/) é uma IDE desenvolvida especificamente para Python e já vem de fábrica com várias ferramentas para auxiliar no desenvolvimento de projetos escritos nessa linguagem, incluindo completação inteligente e inspeção de código, destaque automático de erros de código (acompanhado de soluções rápidas para problemas comuns), refatoração automática, etc. 

Também há ferramentas excelentes para investigação dinâmica de erros (_debugging_), integração com Git, diferentes temas para customização de sua aparência e extenso suporte para ferramentas de desenvolvimento web, como Django, Flask, HTML/CSS, etc (mais sobre essas ferramentas e como desenvolver serviços web em Python mais à frente no livro). 

A principal vantagem do PyCharm é oferecer uma experiência fácil para o iniciante em Python, sem exigir muitas configurações iniciais de ambiente. No entanto, todas essas ferramentas juntas tem um custo de desempenho e o PyCharm pode ter uma execução mais "pesada" do que as outras opções. 


### Spyder

[Spyder](https://docs.spyder-ide.org/) é uma IDE Python que foi desenvolvida com foco em cientistas de dados e outras profissões que trabalham com computação científica. Devido a esse foco, Spyder tem integração com diversos pacotes científicos populares, como NumPy, SciPy, Pandas, Matplotlib, IPython, etc. Suas ferramentas podem também ser estendidas por meio da instalação de plugins. 

Assim como PyCharm, Spyder fornece ferramentas de destaque de sintaxe, completação de código e _debugging_. Além disso, ele também disponibiliza um avaliador de tempo de execução e quantidade de chamadas para cada função definida em um arquivo, o que pode ajudar a otimizar o código. Há também um analisador estático de código (_linter_), que detecta problemas de estilo, más práticas e outros problemas de qualidade no código. Por fim, há também uma aba de "Ajuda", que permite buscar informações sobre pacotes e bibliotecas. Uma desvantagem é que o software suporta apenas Python, o que não ajuda em projetos que envolvem mais de uma linguagem de programação.

### Visual Studio Code

[Visual Studio Code](https://code.visualstudio.com) (VS Code para os íntimos) é um editor de texto desenvolvido pela Microsoft, com capacidades de IDE, totalmente customizável, extensível e de execução leve e eficiente. Sua ferramenta de completação de código é mais avançada que as dos concorrentes, fazendo recomendações inteligentes baseadas em tipos de variáveis, definições de funções e posição (escopo) do código. Suas ferramentas de _debugging_ incluem pontos de parada que podem ser definidos para valores específicos de variáveis, dispensando alterações de código comuns para detecção de erro, o que também é uma vantagem sobre os concorrentes. 

O VS Code também tem excelente integração com ferramentas de controle de versão, em especial Git, e tem integração com o Microsoft Azure, tecnologia de computação na nuvem que fornece serviços de armazenamento, servidor para websites, computação de alta performance, big data, aprendizagem de máquina, etc. O editor dá suporte a mais de 40 linguagens de programação e de marcação, permitindo o desenvolvimento de projetos heterogêneos ou de diferentes projetos em diferentes linguagens usando o mesmo ambiente.

