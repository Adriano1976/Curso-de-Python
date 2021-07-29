def jogar():

    print()
    print(
        '-------------------------------------------------------------------------------------------------------------')
    print(
        '------------------------    PERGUNTAS RELACIONADAS AS ESCRITURAS DO NOVO TESTAMENTO    ----------------------')
    print(
        '-------------------------------------------------------------------------------------------------------------')

    perguntas = {
        'Pergunta 1': {
            'pergunta': 'Se não nascer da água e do Espírito, não podereis entrar no Reino de Deus.',
            'respostas': {'a': 'Hebreus 12:19', 'b': 'João 3:5', 'c': 'João 7:17', },
            'resposta_certa': 'b',
        },

        'Pergunta 2': {
            'pergunta': 'Se me amares, guardareis os meus mandamentos.',
            'respostas': {'a': 'Lucas 24:36-39', 'b': 'João 14:15', 'c': 'Atos 3:19', },
            'resposta_certa': 'b',
        },

        'Pergunta 3': {
            'pergunta': 'Só podemos conhecer as coisas de Deus por meio do Espírito Santos.',
            'respostas': {'a': '1 Coríntios 2:5, 9-11', 'b': 'João 17:7', 'c': '2 Tessalonicenses 2:1-3', },
            'resposta_certa': 'a',
        },

        'Pergunta 4': {
            'pergunta': 'Somente juntos homem e mulher podem cumprir o plano do Senhor.',
            'respostas': {'a': 'Apocalípse 20:12', 'b': 'João 3:5', 'c': '1 Coríntios 11:11', },
            'resposta_certa': 'c',
        },

        'Pergunta 5': {
            'pergunta': 'A Igreja do Senhor é alicerçada sobre apóstolos e profetas.',
            'respostas': {'a': 'Tiago 1:5', 'b': 'Efésios 2:19-20', 'c': 'Tiago 2:17', },
            'resposta_certa': 'b',
        },

        'Pergunta 6': {
            'pergunta': 'As escrituras podem tornar-nos sábios para recebermos a salvação.',
            'respostas': {'a': 'João 15:16', 'b': '2 Timótio 3:15-17', 'c': 'Hebreus 12:9', },
            'resposta_certa': 'b',
        },

        'Pergunta 7': {
            'pergunta': 'Se algum de vós tem falta de sabedoria, peça a Deus que dá a todos liberalmente.',
            'respostas': {'a': '1 Coríntios 11:11', 'b': 'Efésios 2:19', 'c': 'Tiago 1:5-6', },
            'resposta_certa': 'c',
        },

        'Pergunta 8': {
            'pergunta': 'Cada pessoa se apresentará perante Deus para ser julgado segundo suas obras.',
            'respostas': {'a': 'Apocalípse 20:12', 'b': 'Hebreus 12:7', 'c': 'João 15:16', },
            'resposta_certa': 'a',
        },

        'Pergunta 9': {
            'pergunta': 'Jesus Cristo ressuscitou com um corpo de carne e ossos.',
            'respostas': {'a': 'João 15:16', 'b': 'Lucas 24:36-39', 'c': 'João 17:3', },
            'resposta_certa': 'b',
        },

        'Pergunta 10': {
            'pergunta': 'Deixe sua luz brilhar como um exemplo para outras pessoas.',
            'respostas': {'a': 'João 7:17', 'b': 'Mateus 5:14-16', 'c': 'Mateus 16:15', },
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
            print(
                '-------------------------------------------------------------------------------------------------------------')
            correctAnswer += 1
        else:
            print('\nVOCÊ ERROU A QUESTÃO!')
            print(
                '-------------------------------------------------------------------------------------------------------------')

        print()

    qtd_question = len(perguntas)
    porcentagem_acerto = (correctAnswer / qtd_question) * 100

    print(
        '-------------------------------------------------------------------------------------------------------------')
    print(
        '-----------------------------------    RESULTADO DO QUESTIONÁRIO / QUIZ    ----------------------------------')
    print(
        '-------------------------------------------------------------------------------------------------------------')
    print(f'                                  Você acertou "{correctAnswer}" respostas.')
    print(f'                          Sua porcentagem de acerto foi de {porcentagem_acerto}%.')
    print(
        '-------------------------------------------------------------------------------------------------------------')
    print('')

    import menu
    menu.menu()
