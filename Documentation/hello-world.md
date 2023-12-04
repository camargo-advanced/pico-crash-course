## Projeto: 'Hello World'

Com o cabo micro USB conectado ao seu computador o Thonny é capaz de se comunicar com o seu Raspberry Pi Pico usando o **REPL** ou loop de leitura-avaliação-escrita (Read–Eval–Print Loop em inglês), o que permite que você digite código Python no painel do Shell e veja a saída imediatamente. Dessa forma você pode digitar comandos diretamente no painel do Shell e eles serão executados no seu Raspberry Pi Pico de forma interativa.

> **`Importante`**: Antes de continuar, certifique-se de que o seu Raspberry Pi Pico está conectado ao seu computador e que você selecionou o interpretador "MicroPython (Raspberry Pi Pico)".

No painel do Shell, localizado na parte inferior do editor Thonny, digite o seguinte comando. 

```Python
print('Hello World!')
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