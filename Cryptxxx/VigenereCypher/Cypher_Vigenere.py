import Alphabet
import os

def CypherMenu():
    while True:
        os.system("cls")

        print('-'*10 + ' ==Vigenere_Cypher== ' + '-'*10, end='\n\n')
        print('\t- 1 : Encriptar')
        print('\t- 2 : Desencriptar')
        print('\t- 3 : Mostrar Tabelas')
        print('\t- 4 : Não Mostrar Tabelas')
        print('\t- 0 : Sair')
        op = int(input('\n\tO que deseja fazer? '))
        if op > 2 or op < 0:
            print('\n\tValor invalido, apenas valores do 1 a 2.')
        else:

            if op == 1:
                CypherMode = True
            elif op == 2:
                CypherMode = False
            elif op == 3:
                ShowTable = True
            elif op == 4:
                ShowTable = False
            else:
                break
            final_word = VigenereCypher(word=input('Palavra : '), keyWord=input('Palavra-Chave : '), CripMode=CypherMode)
            print(final_word, end='\n' + '_'*38 + '\n')
            os.system("pause")

def MatchLegth(word, keyWord):
    """
    :param:
        word : palavra-original
        keyWord : palavra-chave
    :return:
        keyWord: keyWord com o tamanho agual ao da palavra-original
    """
    while len(keyWord) < len(word): # Iguala o tamanho da palavra chavo com o tamanho da palavra-orignal
        keyWord += keyWord # Repete a palavra-chave
        if len(keyWord) > len(word): # Se maior que a palavra-orignal
            keyWord = keyWord[0 : len(word)]    # Iguala os tamanhos
    return keyWord

def EncriptWord(word, keyWord, VigTable):
    """
    :param:
        word : palavra-original
        keyWord : palavra-chave
    :return:
        enc_word: palavra encriptada
    """
    Alpha = Alphabet.GetAlphabet()
    enc_word = ''
    for itm_w, itm_kw in zip(word, keyWord): # For para percorrer a palavra-chave e a palavra-original
        enc_word += VigTable[Alpha.index(itm_kw)][Alpha.index(itm_w)] # adiciona o caractere na posição da tabela à palavra
    return enc_word

def DecriptWord(word, keyWord, VigTable):
    Alpha = Alphabet.GetAlphabet()
    dec_word= ''
    for itm_w, itm_kw in zip(word, keyWord):
        dec_word += Alpha[VigTable[Alpha.index(itm_kw)].index(itm_w)]
    return dec_word




def InssertSpaces(spaces, enc_word):
    """
    :param:
        word : palavra-original
        keyWord : palavra-chave
    :return:
        enc_word : palavra-encriptada com seus devidos espaços (caso exixtam)
    """
    if len(spaces): # Caso exista algum espaço
        for idx, itm in enumerate(spaces): # Restabelesce os espaços
            enc_word = enc_word[:itm] + ' ' + enc_word[itm:]
    return enc_word

def VigenereCypher(word, keyWord, CripMode=True):
    """
    word.............:  abacate
    key-word.........:  sol
    eciripted-word...:  [ s: a] /+ [ o: b] + [ l: a] + [ s: c] + [ o: a] + [ l: t] + [ s: e]
                        [19:00] + [15:01] + [12:00] + [19:02] + [15:00] + [12:20] + [19:04]

    """
    Alpha = Alphabet.GetAlphabet() # Carrega o alfabeto
    Alphabet.GenerateVigenereTable() # Gera a tabela novamente, Para o caso de uma ateração no alfabeto
    VigTable = Alphabet.LoadVigenereTable() # Carrega a tabela de vigenere

    spaces = []     # Lista para armazenar a posição dos espaços caso nao estejam no alfabeto
    for idx, itm in enumerate(word):    # For para percorrer a palavra
        if itm not in Alpha:    # Verifica se cada caractere da palavra esta no alfabeto
            if itm.isupper(): # tratamento da erro para Letras maiusculas caso nao estejam no alfabeto
                lowerItm = itm.lower()
                word = word.replace(itm, itm.lower())
            elif itm.isspace(): # tratamento da erro para espaços caso nao estejam no alfabeto
                spaces.append(idx)
                word = word.replace(itm, '')
            else: # caso o carctere não seja nem uma letra maiuscula nem um espaço e nao esteja no alfabeto, será removido
                word = word.replace(itm, '')

    keyWord = MatchLegth(word=word, keyWord=keyWord) # Igualar tamanho da palavra-orignal e palavra-chave

    if CripMode:
        final_word = EncriptWord(word=word, keyWord=keyWord, VigTable=VigTable) # Encripta a palavra e retorna uma String
    else:
        final_word = DecriptWord(word=word, keyWord=keyWord, VigTable=VigTable) # Desencripta a palavra e retorna uma String

    final_word = InssertSpaces(spaces=spaces, enc_word=final_word) # Reestabelece os Espaços da paavra

    return final_word
