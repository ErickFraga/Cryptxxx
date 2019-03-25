# Cryptxxx
- Um programa com varias cifras de sbstituição
- Todos os alfabetos podem ser alterados para ter mais segurança. Dando origem a uma cifra de duas chaves
- Caso esteja lendo isso e tenha alguma ideia de como importar pastas para um script me ajude com isso XD
- Em breve esse post tera um pdf explicando cada cifra
________________________________________________________________________________________________________
- Cryptxxx/CezarCypher
	- A Cifra de Cézar se baseia em substituir as letras de uma palavra
	- Essas substituição e feita com base em uma chave
	- para encriptar a palavra, deve-se substituir a letra original pela letra equivalente a letra orignal mais a cifra.
	- Exemplo:
		- Criptografar a palavra "bola" com a chave 8
		- letra a letra se soma a poiscão mais 8
			- b + 8 = j
			- o + 8 = w
			- l + 8 = t
			- a + 8 = i
		- Logo CezarCypher(bola) == jwti
________________________________________________________________________________________________________
- Cryptxxx/ErickCypher
	- Cifra baseada na cifra de cezar utilizando uma chave simples para substituir a letra orignal
	- A partir do binario da chave, e decidido se ela sera adcionada ou subtraida a posição da letra original
	- Exemplo:
		- Criptografar a palavra "martelo" com a chave 90
		- A representação binaria de 90 e 1011010. Que sera usado como uma especie de mascara para a palvra orignal
            	- Logo se relaciona cada letra da palavra com cada digito binario
			- m-a-r-t-e-l-o
			- 1-0-1-1-0-1-0
		- depois se analiza cada letra e cada digito
		- Caso o digito seja 1 a chave 90 será adicionada a letra em questão
		- Caso o digito seja 0 a chave 90 será subtraida a letra em questão
		- Logo temos (m+90)-(a-90)-(r+90)-(t+90)-(e-90)-(l+90)-(o-90)
		- Como 90 e um numero maior que o alfabeto convencional de 26 letras, convem usar o resto da divisão de 90 pelo tamanho do alfabeto
		- Logo(m+12)-(a-12)-(r+12)-(t+12)-(e-12)-(l+12)-(o-12)
		- entao ErickCypher(martelo) == amfhqza
		- Caso o tamanho da palvra e do binario sejam diferentes, deve-se iguala-los repetindo o binario ou, eliminando casas mais a direita.
_________________________________________________________________________________________________________

	
