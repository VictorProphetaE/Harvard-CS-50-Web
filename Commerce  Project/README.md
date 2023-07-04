# Projeto Leilão Online

Este é um projeto de um sistema de leilão online desenvolvido com o framework Django. O sistema permite que os usuários cadastrem itens para serem leiloados, façam lances em itens de outros usuários, adicionem itens à lista de observação (watchlist) e façam comentários nos leilões. Além disso, o sistema possui categorias de itens para facilitar a busca e a exibição de itens relacionados.

## Requisitos

- Python 3.x
- Django 3.x

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

## Funcionalidades

O sistema possui as seguintes funcionalidades principais:

- Autenticação de usuários: Os usuários podem se cadastrar e fazer login para acessar as funcionalidades do sistema.

- Listagem de leilões ativos: Os usuários podem ver todos os leilões ativos na página inicial.

- Criação de novos leilões: Os usuários autenticados podem criar novos leilões, especificando o item, descrição, preço inicial e categoria.

- Fazer lances em leilões: Os usuários podem fazer lances em leilões ativos. O sistema verifica se o valor do lance é maior que o preço atual antes de registrar o lance.

- Lista de observação (watchlist): Os usuários podem adicionar ou remover itens da lista de observação para acompanhar os leilões de interesse.

- Comentários: Os usuários podem fazer comentários nos leilões para deixar mensagens ou fazer perguntas aos vendedores.

- Categorias: Os leilões são organizados por categorias, permitindo que os usuários encontrem facilmente itens de interesse.

## Uso

- Crie uma conta ou faça login se já possuir uma.

- Na página inicial, você poderá ver todas as listagens ativas.

- Para criar uma nova listagem, clique em "Nova Listagem" e preencha as informações solicitadas.

- Para fazer um lance em uma listagem, acesse a página da listagem e insira o valor desejado no campo de lance.

- Você também pode adicionar comentários nas listagens.

- Para acompanhar uma listagem, clique em "Adicionar à Lista de Observação" na página da listagem.

- Você pode visualizar suas listas de observação clicando em "Lista de Observação" no menu superior.

- Ao encerrar uma listagem, o vencedor será exibido na página da listagem e as informações de contato serão fornecidas.

- As listagens podem ser filtradas por categoria, selecionando uma categoria na página inicial.

## Arquivos principais

- views.py: Contém as views (funções que processam as requisições HTTP) do sistema.

- urls.py: Contém as configurações das URLs do sistema.

- models.py: Define os modelos de dados utilizados pelo sistema.

- categories.html: Template para exibir os leilões de uma categoria específica.

- closed_listing.html: Template para exibir os detalhes de um leilão fechado.

- index.html: Template para exibir a lista de leilões ativos na página inicial.