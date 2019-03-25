from Alphabet import Alpha
import os

def CypherMenu():
    PrintSteps = False
    while True:
        os.system("cls")
        print(PrintSteps)
        print('-'*10 + ' ==Erick_Cypher== ' + '-'*10, end='\n\n')
        print('\t- 1 : Encriptar')
        print('\t- 2 : Desencriptar')
        print('\t- 3 : Mostra passos')
        print('\t- 4 : Não Mostra passos')
        print('\t- 0 : Sair')
        op = int(input('\n\tO que deseja fazer? '))
        if op > 4 or op < 0:
            print('\n\tValor invalido, apenas valores do 1 a 2.')
        else:

            if op == 1:
                CypherMode = False
                encriptedWord = ErickCypher(word=input('Palavra : '), key=int(input('Chave : ')), CripMode=CypherMode, PrintSteps=PrintSteps)
                print(encriptedWord, end='\n' + '_'*38 + '\n')
            elif op == 2:
                CypherMode = True
                encriptedWord = ErickCypher(word=input('Palavra : '), key=int(input('Chave : ')), CripMode=CypherMode, PrintSteps=PrintSteps)
                print(encriptedWord, end='\n' + '_'*38 + '\n')
            elif op == 3:
                PrintSteps = True
            elif op == 4:
                PrintSteps = False   
            else:
                break
            
            
            os.system("pause")






def sing(x):
    """
    :Param:
        x: int/float
    :return:
         1 se o numero e positivo
        -1 se o numero e negativo
         0 se o numero e igual a zero
    """
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0

def CreateMask(key, key_Alpha, lenWord, CripMode, PrintSteps):
    """
    :Param:
        key:        int - cifra inteira
        key_Alpha:  int - cifra dividida pelo tamanho do alfabeto/conjuntoUniverso
        lenWord:    str - Tamanho da string que esta sendo encriptada
        CripMode:    bol - False:(desencriptar) inverte os bits do binario da key

    :retunr:
        list- Lista binaria contendo +-key_Alpha que serve como base
            - para adicionar ou subtrair posicoes no alfabeto
    """
    strMask = str(bin(key)).replace('0b', '')
    
    while len(strMask) < lenWord:
        strMask += strMask

    real_Mask = list()
    for num in strMask:
        if int(num):
            real_Mask.append(key_Alpha)
        else:
            real_Mask.append(-1 * key_Alpha)

    if CripMode == False:
        for idx, num in enumerate(real_Mask):
            real_Mask[idx] = -1 * num
    if PrintSteps == True:
        print(f'Mascara da cifra : \t{real_Mask}')
    
    return real_Mask

def SetKeyLetters(word=str(), PrintSteps=True):
    """
    :Param:
        word:   str - palavra que sera encripitada

    :return:
        wordIndex:     list- uma lista contendo os enderecos da letras pa palavra no alfabeto
    """
    wordIndex = list()
    for n in word:
        wordIndex.append(int(Alpha.find(n)))

    if PrintSteps == True:
        print(f'chave das letras: \t{wordIndex}')

    return wordIndex

def ErickCypher(key, word, CripMode=True, PrintSteps=True):
    """
    :Param:
        key:        int - Cifra para somar/subtrair da Palavra
        word:       str - palavra para ser encripitada
        CripMode:    bol - T-> modo Encriptar
                        - F-> modo Desencriptar
    :return:
        encriptedWord:  str - palavra encriptada
    """
    key_Alpha = int(key % len(Alpha))
    if key_Alpha == 0 or key_Alpha == len(Alpha):
        return word
    else:
        mask = CreateMask(key, key_Alpha, len(word), CripMode, PrintSteps)
        keyLetters = SetKeyLetters(word, PrintSteps)
        encriptedWord = ''
        for ind, num in enumerate(keyLetters):
            addLetters = num + mask[ind]
            if addLetters >= len(Alpha) or addLetters <0:
                addLetters += (-1 * sing(mask[ind]) * len(Alpha))

            encriptedWord += Alpha[addLetters]

        print(f'Palavra',end='')
        if CripMode:
            print('encripitada : \t',end='')
        else:
            print('Desencriptada : \t',end='')

        return encriptedWord
