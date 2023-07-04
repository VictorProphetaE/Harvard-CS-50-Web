# Projeto Rede Social 

Este é um aplicativo de rede social simples, desenvolvido em Django, que permite que os usuários se registrem, façam login, postem mensagens, sigam outros usuários e curtam as postagens.

## Requisitos

- Python (versão 3.x)
- Django (versão 3.x)

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

## Uso

- Acesse a página de registro para criar uma nova conta de usuário.

- Faça login com a conta criada.

- Na página inicial, você pode visualizar as postagens feitas pelos usuários. As postagens são ordenadas pela data de publicação.

- Para criar uma nova postagem, clique no link "New Post" na barra de navegação superior e escreva sua mensagem.

- Na página do perfil de cada usuário, você pode ver todas as suas postagens e a quantidade de seguidores e pessoas que ele segue.

- Para seguir ou deixar de seguir um usuário, visite o perfil dele e clique no botão "Follow" ou "Unfollow".

- Para curtir ou descurtir uma postagem, clique no botão de coração (Like) ao lado da postagem.

## Funcionalidades

- Registro de usuário: os usuários podem se registrar fornecendo um nome de usuário, um endereço de e-mail e uma senha. O aplicativo verifica se o nome de usuário já está em uso e se as senhas correspondem.

- Login: os usuários podem fazer login fornecendo seu nome de usuário e senha. O aplicativo verifica se as credenciais fornecidas são válidas.

- Logout: os usuários podem fazer logout de suas contas.

- Página inicial: a página inicial exibe todas as postagens dos usuários, ordenadas por tempo decrescente. Cada postagem exibe o nome de usuário do autor, o conteúdo da postagem e o número de curtidas que recebeu. Os usuários autenticados podem curtir as postagens.

- Novo post: os usuários autenticados podem criar novas postagens, digitando o conteúdo da postagem em um campo de texto e clicando no botão "Postar". A postagem é então exibida na página inicial.

- Perfil do usuário: cada usuário tem uma página de perfil que exibe suas postagens, número de seguidores e número de pessoas que ele está seguindo. Os usuários autenticados podem seguir ou deixar de seguir outros usuários a partir de suas páginas de perfil.

 -Página de seguindo: a página de seguindo exibe as postagens dos usuários que o usuário está seguindo, ordenadas por tempo decrescente.

