# servidor_local_python

Esse arquivo tem o intuito de registrar como pode ser feito um servidor local com Python. O localhost é interessante para quem está buscando uma forma alternativa do protocolo file://.

Certo, preliminarmente vamos criar uma pasta especifica para subir esse serviço (vou deixar ela anexada - servidor_teste), dentro desse directório vou apenas deixar um arquivo index.html, que por padrão, o Python executa se ele existir.


![image](https://user-images.githubusercontent.com/95552879/156078832-8062f5c0-f2eb-44e0-b57e-3f2e7bc8fcb0.png)


Ok! Agora vem a parte bacana, ativar o serviço. Dentro da pasta abra o seu Prompt de Comando (cmd), feito isso, basta executar a seguinte linha de código:

python -m http.server 8080

- python para chamar o Python
- -m tem o intuito de ressalta que o módulo a ser chamado não está localizado na página atual
- http.server define classes para a implementação de servidores HTTP.
- 8080 é a porta aonde o serviço está disponibilizado


Apenas para reitar, usuários linux podem utilizar a função wget (uma vez que as máquinas estejam na mesma rede) para fazer o download dos arquivos nesse servidor. O comando é simples:
wget http://255.255.255.01:8080/passwd.txt

Inicializado:

![image](https://user-images.githubusercontent.com/95552879/156079556-924293df-7bb0-4843-8405-2e87a187587f.png)


Arquivo index.html sendo utlizado:

![image](https://user-images.githubusercontent.com/95552879/156079572-27995ac9-fcff-41c7-af36-d2bdc863ced8.png)

Tentando uma requisição inexistente na pasta aonde esse serviço está rodando:

![image](https://user-images.githubusercontent.com/95552879/156079726-9bcfe6ad-3da6-41f1-ac36-c3b801581f2f.png)

Requisição de uma pasta que existe dentro do local que está rodando o serviço:

![image](https://user-images.githubusercontent.com/95552879/156079834-11988547-751e-4a6d-b011-5625e75f3e08.png)





