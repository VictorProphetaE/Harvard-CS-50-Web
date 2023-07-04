#  Projeto Wiki 

Este é um projeto Django para criar uma enciclopédia de conteúdo. O objetivo é permitir que os usuários visualizem, pesquisem, criem e editem páginas de conteúdo usando a linguagem de marcação Markdown.

## Arquivos principais

- views.py: Este arquivo contém as funções de visualização que são responsáveis por renderizar os templates HTML, lidar com requisições e retornar respostas apropriadas.

- util.py: Este arquivo contém funções utilitárias que são usadas pelas funções de visualização para realizar operações no sistema de arquivos, como listar entradas, salvar e obter conteúdo de uma entrada.

- layout.html: Este é o arquivo de layout base usado pelos templates HTML. Ele define a estrutura geral da página e carrega os estilos CSS necessários.

## Funcionalidades principais

### Página inicial

A função index renderiza a página inicial da enciclopédia. Ela lista todas as entradas disponíveis e as exibe na página.

### Visualização de uma entrada

A função entry é responsável por renderizar a página de uma entrada específica. Ela recebe o título da entrada como parâmetro e verifica se a entrada existe. Se a entrada existir, o conteúdo é exibido no formato Markdown. Caso contrário, uma página de erro é exibida.

### Pesquisa

A função search realiza uma pesquisa no conteúdo da enciclopédia com base em um termo fornecido pelo usuário. Ela verifica se há correspondências parciais ou completas no título das entradas. Se houver várias correspondências, uma lista de entradas relacionadas é exibida. Se houver uma correspondência exata, o usuário é redirecionado para a página da entrada.

### Criação de uma nova página

A função newpage lida com a criação de uma nova página. Ela exibe um formulário onde o usuário pode inserir o título e o conteúdo da nova página. Se o formulário for válido e o título da página não existir, a nova página é salva e o usuário é redirecionado para a página recém-criada.

### Edição de uma página existente

A função edit permite que o usuário edite o conteúdo de uma página existente. Ela exibe um formulário pré-preenchido com o conteúdo atual da página. Quando o formulário é enviado, o conteúdo é atualizado e o usuário é redirecionado para a página atualizada.

### Página aleatória

A função random_ent redireciona o usuário para uma página aleatória da enciclopédia.

## Arquivos estáticos

O projeto também inclui alguns arquivos estáticos, como CSS e imagens, que são usados para estilizar as páginas.

## Como executar o projeto

Certifique-se de ter o Django instalado em seu ambiente. Você pode instalar o Django usando o pip:
    `pip install Django`

Após instalar o Django, você pode executar o projeto usando o seguinte comando:
    `python manage.py runserver`

Isso iniciará o servidor de desenvolvimento do Django e você poderá acessar a enciclopédia em seu navegador através do endereço `http://localhost:8000/`.

Acesse a [página do desafio](https://cs50.harvard.edu/web/2020/projects/1/wiki/) para acessar a página do desafio. 
