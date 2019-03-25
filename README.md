# Cryptxxx
- Um pragrama com varias cifras de sbstituição
- Todos os alfabetos pode ser alterados para ter mais segurança. Utilizando como uma cifra de duas chaves
- Caso esteja lendo isso e tenha alguma ideia de como importar pastas para um script me ajude com isso XD
- Em breve esse post tera um pdf explicando cada cifra

- Cryptxxx/ErickCypher
    - Cifra baseada na cifra de cezar utilizando uma chave simples para substituir
    - A partir do binario a chave se decide se ela sera adcionada ou subtraida
    - Exemplo:
            - Criptografar a palavra "martelo" com a chave 90
            - A representação binaria de 90 e 1011010. Que sera usado como uma especie de mascara
            - Logo re relaciona cada letra da palavra com cada digito binario
                    m-a-r-t-e-l-o
                    1-0-1-1-0-1-0
            - depois se analiza cada letra e cada digito
            - Caso o digito seja 1 a chave 90 será adicionada a letra em questão
            - Caso o digito seja 0 a chave 90 será subtraida a letra em questão
            - Logo temos (m+90)-(a-90)-(r+90)-(t+90)-(e-90)-(l+90)-(o-90)
            - Como 90 e um numero maior que o alfabeto convencional de 26 letras, convem usar o resto da divisão de 90 pelo tamanho do alfabeto
  - Logo(m+12)-(a-12)-(r+12)-(t+12)-(e-12)-(l+12)-(o-12)
  - entao ErickCypher(martelo) == amfhqza
