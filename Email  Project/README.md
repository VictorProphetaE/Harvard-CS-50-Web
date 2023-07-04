#  Projeto Email Application

Esta é uma aplicação de email simples desenvolvida usando o framework Django. A aplicação permite que os usuários autenticados enviem e recebam emails, arquivem emails, marquem emails como lidos e respondam a emails.

## Requisitos

- Python 3.x
- Django (versão 3.x ou superior)

## Instalação e Configuração

Siga as etapas abaixo para configurar e executar a aplicação:

1. Certifique-se de ter o Django instalado em seu ambiente de desenvolvimento.

2. Clone o repositório ou faça o download dos arquivos.

3. Navegue até o diretório do projeto.

4. Execute as migrações do banco de dados:
    `python manage.py migrate`

5. Crie um superusuário (administrador) para acessar a página de administração:
    `python manage.py createsuperuser`

6. Inicie o servidor de desenvolvimento:
    `python manage.py runserver`

7. Acesse a aplicação em seu navegador usando o seguinte URL:
    `http://localhost:8000/`

## Arquivos Principais

- views.py: Contém as visualizações (views) que processam as solicitações HTTP e retornam respostas.
- urls.py: Define os padrões de URL da aplicação.
- models.py: Define os modelos de dados usados pela aplicação.
- inbox.js: Contém scripts JavaScript para manipular as visualizações da caixa de entrada de emails.
- styles.css: Folha de estilos CSS personalizada para a aplicação.

## Funcionalidades

A aplicação possui as seguintes funcionalidades:

- Autenticação de usuários: os usuários podem se autenticar usando seu endereço de email e senha.
- Visualização de caixa de entrada: os usuários autenticados podem visualizar sua caixa de entrada de emails.
- Composição de emails: os usuários autenticados podem compor e enviar novos emails.
- Visualização de email: os usuários podem visualizar o conteúdo de um email específico.
- Marcação de emails como lidos: os usuários podem marcar emails como lidos.
- Arquivamento de emails: os usuários podem arquivar ou desarquivar emails.
- Resposta a emails: os usuários podem responder a um email específico.