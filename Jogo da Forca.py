#   pensamento do jogo da forca:
#   perguntar se quer jogar
#   aceitou?
#   faz um def pra definir qual vai ser a palavra escolhida
#   def para começar o jogo
#   pede uma letra
#   verifica se a letra está na palavra
#   se estiver, mostra o local da letra na palavra
#   caso contrário, coloca a letra na lista de letras erradas (máximo de 6 > cabeça, tronco, braços, pernas)
#   ao faltarem 2 letras, pergunta se quer tentar chutar a palavra
#   sim> acertou? ganhou!
#   sim> errou? continua
#   não> continua
#   acabaram os pontos? > jogo acabou, humilhação e pode tentar novamente
#   se acertou a palavra, ganhou o jogo
#   nas duas situações ele vai dar a opção de jogar novamente

import random

mensagens = {
    'entrada' : f'oii! você quer jogar um jogo? responda com sim ou não!',
    'nao_quer_jogar': f'ok, tudo bem !',
    'tentativa' : 'Chute uma letra! \n',
    'resposta_chute': 'Você quer tentar advinhar qual é a palavra?\n',
    'chute': 'Certo! que fruta você acha que é?\n',
    'certoLetra' : 'Boa! essa letra faz parte do nome da fruta escolhida.',
    'erradoLetra' : 'Olha, não tem essa letra... Mas você pode tentar novamente!',
    'certoPalavra' : '\nParabéns! Você acertou a fruta. <3',
    'erradoPalavra' : 'Você errou a palavra, mas pode continuar tentando!',
    'final' : lambda palavra: f'O boneco morreu e você não acertou, burro. \n A fruta escolhida era {palavra}',
    'erro' : 'Só são aceitas letras! isso que você colocou é inválido.',
    'denovo' : 'você quer jogar novamente? \n',
    'repetida': 'você já inseriu essa letra anteriormente!'
    }

frutas = [
    "abacaxi", "uva", "melão", "atemoia", "laranja", "morango", "melancia", 
    "cereja", "amora", "maça", "banana", "pêra", "caju", "kiwi", "ameixa", 
    "goiaba", "limão", "maracujá", "bergamota", "carambola"
]

def palavra():
    return random.choice(frutas)

def jogo():
    escolhida = palavra()
    palavra_oculta = ["_"] * len(escolhida)
    tentativas = 6
    letras_certas = []
    letras_erradas = []
    ja_perguntou = False

    print(mensagens['entrada'])
    if input().lower() != 'sim':
        print(mensagens['nao_quer_jogar'])
        return
    
    while tentativas > 0:
        print(f"\nPalavra: {' '.join(palavra_oculta)}")
        print(f"Letras erradas até agora: {', '.join(letras_erradas)}")
        print(f"Número de tentativas restantes: {tentativas}")


        letra = input(mensagens['tentativa']).lower()

        if len(letra) != 1 or not letra.isalpha():
            print(mensagens['erro'])
            continue

        if tentativas == 3 and not ja_perguntou:
            ja_perguntou = True
            pergunta_chute = input(mensagens['resposta_chute']).lower()
    
            if pergunta_chute == "sim":
                chute = input(mensagens['chute']).lower()
                
                if chute == escolhida:
                    print(mensagens['certoPalavra'])
                    return 
                else:
                    print(mensagens['erradoPalavra'])
    
            elif pergunta_chute in ["não", "nao"]:
                pass 


        if letra in letras_certas or letra in letras_erradas:
            print(mensagens['repetida'])
            continue

        if letra in escolhida:
            print(mensagens['certoLetra'])
            letras_certas.append(letra)
            for i, j in enumerate(escolhida):
                if j == letra:
                    palavra_oculta[i] = letra
        else:
            print(mensagens['erradoLetra'])
            letras_erradas.append(letra)
            tentativas -= 1

        if '_' not in palavra_oculta:
            print(mensagens['certoPalavra'])
            break

    if tentativas == 0:
        print(mensagens['final'] + escolhida)

    
def jogar_novamente():
    play_again = input(mensagens['denovo']).lower()
    if play_again == "sim":
        jogo()

    else:
        print(mensagens['nao_quer_jogar'])

jogo()
jogar_novamente()

