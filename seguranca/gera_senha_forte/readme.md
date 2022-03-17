# Gera_senha_forte

# Linguagem utilizada:
  - Python 3.9.7
  - Roda no seu interpretador python.

# A respeito do programa:
  Recebe um número e retorna uma senha forte com o quantidade total de caracteres iguais ao número da entrada;

  A senha gerada deverá conter(Não exclusivamente, o programa escolherá a melhor opção):

      Letra Maiuscula
      Letra Minuscula
      Caracter especial
      Número
      
 ![image](https://user-images.githubusercontent.com/95552879/158895181-96f11d83-3c2a-4adc-a607-e58ade8682bb.png)

# Conceitos abordados

  - Módulos: string e secrets;
  - Programação orientada a objetos;
  - GUI (Graphical User Interface)
  - 
# Lógica por trás do desenvolvimento:

  Um jeito de gerar uma senha forte seria criar uma lista dos itens (letras, símbolos e numeros) manualmente e sortear 
  um dos itens dessa lista aleatóriamente. Executar essa tarefa de sortear até preencher uma string vazia com o número 
  total de caracteres. No fim, iria embaralhar essa string para garatir não ficar nenhum registro lógico de como a senha foi bolada.
  
  Porem, o Python disponibiliza duas bibliotecas muito interessantes para fazer isso, string e secrets.

  Ao invés de criar uma lista com todos os caracteres da senha e posterior fazer o sorteio com o randon,
  utilizei o módulo string para criar todos os caracteres, e posterior, fazer a escolha desses caracteres
  com o módulo secrets, que é muito mais adequando (segundo a documentação) para esse tipo de situação (geração de senhas).
  
# O que foi refatorado nesse código:
  
  Fiz uma atualização pequena para pode usar via CMD graças a um laço de repetição. Mas como venho usando bastante esse programa considerei interessante possuir uma interface grafica. Tem como melhorar, não me atrai a forma como a entrada de caracteres está disposta, muito larga... fica o desafio para o leitor.
  
# Observações:
  É um projeto interessante para conhecer uma nova biblioteca e gerar uma senha forte :D.
  Caso tenha algum erro de lógica no código, ortografia ou melhores maneiras de serem executadas as
  tarefas dispostas ficaria grato pela compreensão. Aprecio sugestões para melhorar. Forte abraço.
