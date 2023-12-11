## Capítulo 4: Projeto: "Hello World"

Bem-vindo ao mundo da programação interativa com o Raspberry Pi Pico e o Thonny! Neste capítulo, vamos explorar uma forma dinâmica de interagir com o seu Raspberry Pi Pico usando o Thonny, através do REPL (Read–Eval–Print Loop em inglês). Esta é uma oportunidade emocionante para aprender a se comunicar diretamente com o seu microcontrolador e ver instantaneamente os resultados das suas linhas de código.

Com o cabo micro USB conectado e o Thonny configurado para trabalhar com o interpretador MicroPython do Raspberry Pi Pico, você está pronto para mergulhar nesse processo interativo. A capacidade de digitar código no painel do Shell do Thonny e testá-lo imediatamente no Raspberry Pi Pico é uma maneira poderosa de experimentar e testar suas ideias.

Vamos começar explorando como enviar comandos Python, como o famoso "Hello World!", para o Raspberry Pi Pico e visualizar a saída no painel do Shell do Thonny. Este é apenas o começo de uma jornada que o levará a compreender melhor a comunicação direta entre o código e o hardware. 

> **`Importante`**: Antes de continuar, certifique-se de que o seu Raspberry Pi Pico está conectado ao seu computador e que você selecionou o interpretador "MicroPython (Raspberry Pi Pico)".

No painel do Shell, localizado na parte inferior do editor Thonny, digite o seguinte comando. 

```Python
print("Hello World!")
```

Pressione a tecla `Enter` e você verá a saída.

![Thonny shell após execução de Hello World](/images/thonny-shell-hellow.png "Thonny shell após execução de Hello World")

### Escrevendo mensagens de texto

A função `print` em Python escreve mensagens de texto na saída padrão, que por padrão é a tela do seu computador. Você pode usar a `print` para mostrar mensagens, resultados de cálculos, variáveis e outros tipos de dados durante a execução de um programa. Nesse caso a função apresentou a mensagem 'Hello World' no painel do Shell.

Uma string em Python é uma sequência de caracteres, ou seja, um conjunto ordenado de caracteres alfanuméricos, símbolos ou espaços em branco. As strings são usadas para representar texto em programas Python. Em Python as strings devem estar entre aspas simples `'`, ou aspas entre aspas duplas `"`. Dessa forma ambas as strings que seguem são válidas.

```Python
'Hello World.'
"Hello World."
```

O importante é ser consistente: se você iniciou uma string com aspas simples, feche-a com aspas simples. Se iniciou com aspas duplas, feche-a com aspas duplas.

As funções em Python, assim como na maioria das linguagens de programação, utilizam um par de parenteses `()` para indicar onde os argumentos devem ser colocados.  Por isso a string 'Hello World!' foi colocada dentro dos parênteses da função `print`.

### Exercícios

#### Exercício 4.1: Explorando o Shell Integrado

Abra o Thonny e explore o shell Python integrado na parte inferior da interface.
Experimente realizar operações matemáticas simples, como adição, subtração, multiplicação e divisão.

#### Exercício 4.2: Escrevendo outras mensagens

Mensagens Simples: Escreva um código Python que exiba mensagens simples, como "Olá, mundo!" ou seu próprio nome na tela.

### Conclusão

Parabéns por explorar e experimentar o poder da programação interativa com o Raspberry Pi Pico através do Thonny! Neste capítulo, você aprendeu a enviar comandos Python ao Raspberry Pi Pico, observando imediatamente suas saídas no Thonny. Compreendeu também a importância da função `print` em exibir mensagens e resultados na tela do seu computador, bem como o uso adequado de strings em Python para representar texto.

Esse conhecimento inicial é fundamental para aprofundar sua compreensão da programação física e do controle direto de dispositivos usando o MicroPython. Continue explorando e experimentando, pois cada passo nessa jornada de aprendizado o aproximará cada vez mais da criação de projetos cada vez mais fascinantes e desafiadores. Até breve!

