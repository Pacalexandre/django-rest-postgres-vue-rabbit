# django-rest-postgres-vue-rabbit# django-channel-cryptocoin

Uma aplicação com Django Bootsrap Websocket Vue channels Rabbit - consulting realtime devcontainer  
Nesse exemplo vamos criar uma pagina web que vai consultar um website de crypto moedas e atualizar  
automaticamente com websockets, utilizadno redis e vue utilizando decontainer da microsoft.

para o uso é necessário:  
- [x] pré requisitos
    - [x] docker - Docker version 20.10.8, build 3967b7d
    - [x] docker-compose - Docker Compose version v2.2.2
    - [x] visual studio
    - [x] extensions: Remote - Containers
    - [x] [documentação](https://code.visualstudio.com/docs/remote/containers)

## Get Started
...
```<script src="https://unpkg.com/vue@3"></script>```

## Roteiro de implementação 

- [x] criação do devcontainer
- [x] instalação django (sistema)
- [x] instalando postgres
- [x] instalação rabbitmq
- [x] instalacao redis
- [x] criando html com bootstrap vue e configurações de rota
- [x] definindo diretorios de static e subindo pagina html
- [x] chamando a API de cryptos montando a pagina com os dados
- [x] instalando e configurando celery para realizar as buscas
- [x] configurando admin model no django admin e criando superuser
- [x] rodando celery gravando banco de dados e registrando dados na model
- [x] instalando e configurando channels para websocket
- [x] criando rotas de websocket para aplicacão em routing 
- [x] chamada das tarefas dentro do channels layers
- [x] configuração dos consumers e ligação na pagina com vue3


## Ajudas e curiosidades


## Referencias

 - https://getbootstrap.com/
 - https://www.postgresql.org/docs/
 - https://docs.celeryq.dev/en/stable/
 - https://docs.djangoproject.com/en/4.0/
 - https://www.rabbitmq.com/management.html#configuration
 - https://x-team.com/blog/set-up-rabbitmq-with-docker-compose/
 
 
