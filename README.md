# Arquivos e Pastas: 

/info.txt   
- Informações sobre instalação de bibliotecas e outros

/server.py  
- Arquivo principal, que une tudo e roda o servidor flask
- Só é necessário executar esse arquivo

/download_df.py 
- Arquivo que faz o download das bases direto do site
- Não é necessário rodar esse arquivo, pois as bases já foram baixadas

/func_auxiliares.py 
- Arquivo com algumas funções auxiliares
- Conversão de siglas, abreviaturas, trabalhar com as datas e outros

/Insomnia_requisicoes_GET.json  
- São as requisições GET para JSON
- Para importar no Insomnia: 
    - Application/Preferences/Data/Import Data/From file

/Bases/ 
- Nessa pasta estão as duas bases de dados(formato xlsx)
- cada arquivo, é separado por páginas:
    - Base por estados: Ocorrências e Vítimas
    - Base por Municípios: siglas dos estados

/Metodos_GET/   
- Nesta pasta, tem um arquivo para cada pessoa editar
- Nesse arquivo, só deve ter as classes e os métodos GET
- Cada método GET, chama uma função da pasta /Funcoes/

/Funcoes/   
- Nesta pasta, tem um arquivo para cada pessoa editar
- Nesse arquivo deve ser adicionado a função que o GET chama
- É aqui que são realizadas as manipulações de dados das bases

# O que alterar?

Quando as funções forem divididas para cada integrante: 

- No arquivo server.py, na sessão com seu nome, inserir as rotas das suas funções

- Na pasta /Metodos_GET/, no arquivo com seu nome, inserir os métodos GET

- Na pasta /Funcoes/, no arquivo com seu nome, inserir as funções que trabalham com as bases de dados

- Caso precise de funções auxiliares, adicione no arquivo func_auxiliares.py, na sessão com seu nome

- Caso precise, crie outros arquivos

# Padronização das rotas (e outras coisas):

1. Estados: <br/>
    Sempre que nas rotas(url) tiver que passar um estado, sempre usar siglas em maiúsculo<br/>
    Exemplo: "/CE/"<br/>
    A função "converte_sigla_em_nome" converte no uma sigla em nome do estado<br/>

2. Datas:<br/>
    Nas rotas usar o formato "jan-2019", mês abreviado e separado por "-"<br/>
    Exemplo: "fev-2019"<br/>
    Usar funções:<br/>
    "pega_mes" para converter a string "jan-2019" em "janeiro" (Para base de estados)<br/>
    "pega_ano" para converter a string "jan-2019" em "2019" (Para base de estados)<br/>
    "converte_para_data" para converter a string "jan-2019" em "2019-01-01" (Para base de cidades) (Não ta pronto)<br/>
    
3. Ordem das Datas: <br/>
        Sempre que usar datas, colocar primeiro a data inicial e depois a data final, incluir na busca os meses de inicio e fim<br/>
        Exemplo: /jan-2017/ago-2019/ <br/>
                Uma busca de janeiro de 2017 até agosto de 2019<br/>

4. Nomes de Crimes e Cidades:<br/>
    Nas rotas quando o crime/cidade for formado por duas ou mais palavras, usar "-" para separa-las <br/>
    Exemplo: para a cidade "Cruzeiro do Sul" -> /Cruzeiro-do-Sul/<br/>
    Na url o nome do crime deve ser o mesmo que o desejado para a busca, Podendo variar entre maiúsculas e minúsculas, acentuadas e não acentuadas<br/>
    Exemplo: Para o crime "Roubo seguido de morte (latrocínio)" são aceitos os formatos:
    - /Roubo-seguido-de-morte-(latrocínio)/
    - /ROUBO-segUIdo-de-mORte-(latrocinio)/
    - /Roubo-seguido-de-mórté-(látrócínío)/
    - /Roubo-seguido-de-morte-(latricinio)/<br/>
    E outras variações<br/>
    Usar as funções:<br/>
    "trata_palavra", que retorna a palavra com espaços no lugar de "-", sem acentos, e minúscula<br/>
    "trata_vetor_palavra", que aplica a função "trata_palavra" para todas as palavras de um vetor, e retorna um array<br/>

5. Se as datas estiverem invertidas na url, retornar = []<br/>
    Exemplo: /jan-2020/fev-2019/<br/>

6. Quando houver erros na url, evitar erros no código que retornam: Internal Server Error: 500<br/>
    Usar try,except nos métodos GET, para sempre que der algo errado retornar = []<br/>
