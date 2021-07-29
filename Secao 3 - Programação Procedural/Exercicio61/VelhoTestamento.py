def jogar():

    print()
    print('-------------------------------------------------------------------------------------------------------------')
    print('-----------------------    PERGUNTAS RELACIONADAS AS ESCRITURAS DO VELHO TESTAMENTO    ----------------------')
    print('-------------------------------------------------------------------------------------------------------------')

    perguntas = {
        'Pergunta 1': {
            'pergunta': 'Portanto, deixará o homem o seu pai e sua mãe, e apegar-se-á à sua mulher, e serão ambos '
                        'uma carne. ',
            'respostas': {'a': 'Amós 3:7', 'b': 'Gêneses 2:24', 'c': 'Josué 24:15', },
            'resposta_certa': 'b',
        },

        'Pergunta 2': {
            'pergunta': 'Frutificai e multiplicai-vos, e enchei a terra, e sujeitai-a; e dominai sobre os '
                        'peixes do mar...',
            'respostas': {'a': 'Malaquias 4:5-6', 'b': 'Gêneses 1:28', 'c': 'Gêneses 2:24', },
            'resposta_certa': 'b',
        },

        'Pergunta 3': {
            'pergunta': 'Antes que te formasse no ventre, te conheci, e antes que saisse da madre, te santifiquei, e as '
                        'naçoes te dei por profeta.',
            'respostas': {'a': 'Jeremias 1:4-5', 'b': 'Gênesis 39:9', 'c': 'Isaías 5:20', },
            'resposta_certa': 'a',
        },

        'Pergunta 4': {
            'pergunta': 'Certamente o Senhor Deus não fará coisa alguma, sem ter revelado o seu segredo ao seus servos, '
                        'os profetas.',
            'respostas': {'a': 'Moisés 1:37', 'b': 'Malaquias 4:5', 'c': 'Amós 3:7', },
            'resposta_certa': 'c',
        },

        'Pergunta 5': {
            'pergunta': 'Roubará o homem a Deus? Porque vós me roubais, e dizeis: Em que te roubamos? Nos dízemos '
                        'e nas ofertas.',
            'respostas': {'a': 'Isaías 1:18', 'b': 'Malaquias 3:8', 'c': 'Gênese 1:28', },
            'resposta_certa': 'b',
        },

        'Pergunta 6': {
            'pergunta': 'Confia no Senhor de todo o teu coração, e Ele endireitará as tuas veredas.',
            'respostas': {'a': 'Êxodo 19:5-6', 'b': 'Provérbios 3:5', 'c': 'Hebreus 12:9', },
            'resposta_certa': 'b',
        },

        'Pergunta 7': {
            'pergunta': 'Ai dos que ao mal chamam bem, e ao bem mal.',
            'respostas': {'a': '1 Coríntios 11:11', 'b': 'Malaquias 3:8', 'c': 'Isaías 5:20', },
            'resposta_certa': 'c',
        },

        'Pergunta 8': {
            'pergunta': 'Jejuar nos ajuda a soltar as ligadoras da impiedade, desfazer as cordas do jugo e prover aos pobres.',
            'respostas': {'a': 'Isaías 58:6-7', 'b': 'Êxodo 20:3', 'c': 'João 15:16', },
            'resposta_certa': 'a',
        },

        'Pergunta 9': {
            'pergunta': 'Buscai-me em cada pensamento; não duvideis, não temais.',
            'respostas': {'a': 'João 15:16', 'b': 'Malaquias 3:8', 'c': 'Isaías 1:18', },
            'resposta_certa': 'b',
        },

        'Pergunta 10': {
            'pergunta': 'Eis que eu vos envio o profeto Elias, antes que venha o grande e terrível dia do Senhor;',
            'respostas': {'a': 'João 7:17', 'b': 'Malaquias 4:5', 'c': 'Isaías 58:6-7', },
            'resposta_certa': 'b',
        },
    }
    correctAnswer = 0

    for chave, question in perguntas.items():
        print(f'{chave}: {question["pergunta"]}')

        print('RESPOSTAS ALTERNATIVAS: ')
        for chave, answer in question['respostas'].items():
            print(f'[{chave}]: {answer}')

        answerUsuary = input('SUA RESPOSTA: ')

        if answerUsuary == question['resposta_certa']:
            print('\nVOCÊ ACERTOU A QUESTÃO!')
            print('-------------------------------------------------------------------------------------------------------------')
            correctAnswer += 1
        else:
            print('\nVOCÊ ERROU A QUESTÃO!')
            print('-------------------------------------------------------------------------------------------------------------')

        print()

    qtd_question = len(perguntas)
    porcentagem_acerto = (correctAnswer / qtd_question) * 100

    print('-------------------------------------------------------------------------------------------------------------')
    print('-----------------------------------    RESULTADO DO QUESTIONÁRIO / QUIZ    ----------------------------------')
    print('-------------------------------------------------------------------------------------------------------------')
    print(f'                                  Você acertou "{correctAnswer}" respostas.')
    print(f'                          Sua porcentagem de acerto foi de {porcentagem_acerto}%.')
    print('-------------------------------------------------------------------------------------------------------------')
    print('')

    import menu
    menu.menu()