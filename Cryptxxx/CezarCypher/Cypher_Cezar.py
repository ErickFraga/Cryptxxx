from Alphabet import Alpha
import os

def CypherMenu():
    while True:
        os.system("cls")

        print('-'*10 + ' ==Cezar_Cypher== ' + '-'*10, end='\n\n')
        print('\t- 1 : Encriptar')
        print('\t- 2 : Desencriptar')
        print('\t- 0 : Sair')
        op = int(input('\n\tO que deseja fazer? '))
        if op > 2 or op < 0:
            print('\n\tValor invalido, apenas valores do 1 a 2.')
        else:

            if op == 1:
                CypherMode = True
            elif op == 2:
                CypherMode = False
            else:
                break
            final_word = CezarCypher(word=input('Palavra : '), key=int(input('Chave inteira : ')), CripMode=CypherMode)
            print(final_word, end='\n' + '_'*38 + '\n')
            os.system("pause")


def CezarCypher(key, word, CripMode=bool()):
    word = word.lower()
    if not CripMode:
        key *= -1

    if key == len(Alpha) or key == 0:
        return word

    else: 
        key = key % len(Alpha)	# Permite o usuario enserir qualauer tamanho dechave
        #if key < 0:		# Se a chave inserida e negativa
        #	key += len(Alpha)	# key recebe o equivalente a positivo da chave

        idx_word = list()	# Lista para armazenar os index da palavra nova
        final_word = ''	# Inicia umastring para conter a Palavra encriptada

        for idx, letter in enumerate(word):		# Loop para percorrer a palvavra
            alpha_index = int(Alpha.find(letter))	# Pega a posição de cada letra enrelação ao alfabeto
            enc_index = key + alpha_index		# enc_index recebe a posição da aletra mais a chave

            if enc_index >= len(Alpha):	# Se a posicao do index e menor que 25
                enc_index -= len(Alpha) # então deminui o tamanho de Alpha
            final_word += Alpha[enc_index] 	# adiciona a letra de alpha na string reposta

        return final_word
