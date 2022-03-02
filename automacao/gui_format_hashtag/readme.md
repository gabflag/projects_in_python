# GUI_format_hashtags

# Linguagem utilizada:
  - Python 3.9.7
  - Para iniciar a Interface Gráfica do Usuário(GUI) basta iniciar o programa no seu interpretador Python.

# A respeito do programa:
  Exibe uma Interface gráfica para o usuário poder formatar hashtags. O usuário ira inserir um blobo de hashtags que gostaria de conferir se:

    - Não possue palavras repitidas;
    - Remove caracteres indesejados;
    - Padronizar espaçamentos;
    - Deixar todas as palavras em minúsculo;
    - Adiciona três pontos acima das hashtags.
  
  Após inserir o texto no campo indicado basta clicar no botão "Fazer formatação" que no campo ao lado virá o texto formatado.
  
# Conceitos abordados:

    - Módulos: re and tkinter;
    - Manipulação de string e listas;
    - Criação de uma GUi.

# Exemplo de utilização:
  ![image](https://user-images.githubusercontent.com/95552879/147715825-0a7b5532-e834-4dce-bf35-e3e2fee7aa79.png)
  ![image](https://user-images.githubusercontent.com/95552879/147715862-56cbcd93-54fa-43c5-ba4e-74cb331f6b6e.png)


# Experiência pelo DEV:

  Como foi meu primeiro projeto trabalhando com uma GUI acredito que tem muito a ser melhorado. Acredito que posso melhorar em alguns aspectos. Em especial,
  não estou muito crente da utilização que fiz do método INSERT para alterar o texto, foi funcional... solução encontrada.
  
  Em resumo, tive dificuldades em mostrar o resultado (texto formatado) dentro da GUI, conseguia capturar o texto do usuário mas exibia somente no interpretador,
  a solução encontrada fica clara dentro do código mas como resolvi foi:
    - Capturo o texto do usuário na entrada, armazeno em uma variavel e posterior executo a função normalmente até obter o texto formatado;
    - Feito isso, excluo o conteúdo que existe dentro da minha caixa de texto de saída (vem setado como: "resultado") e depois faço uma nova inserção, 
      mas dessa vêz com o resultado.
  
  Talvez fique a pergunta... Não era mais fácil criar um elemento do tipo Label e depois alterar o texto dentro?
  Até poderia fazer isso, mas como é necessário poder selecionar o texto para poder copiar se fez necessário se fazer dessa forma.
  
# Pontos a ser melhorados:

    - Ter seu programa de teste;
    - Ornamentar e talvez adicionar funções que se considerem interessantes.
  
# Observações:

  Considero um projeto interessante para trabalhar com manipulação de strings com o módulo re, trabalhar com listas e principalmente ter uma experiência com o TKinter.
  Com certeza nesse código terá erros de lógica, ausencia de um algoritimo melhor ou a não utilização de funções especificas, mas espero sua compreensão e que de 
  alguma forma te ajude. Aprecio sugestões para melhorar. Forte abraço.
