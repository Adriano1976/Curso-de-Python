def jogar():

    print()
    print(
        '-------------------------------------------------------------------------------------------------------------')
    print(
        '------------------------    PERGUNTAS RELACIONADAS AS ESCRITURAS DO LIVRO DE MÓRMON    ----------------------')
    print(
        '-------------------------------------------------------------------------------------------------------------')

    perguntas = {
        'Pergunta 1': {
            'pergunta': 'O Senhor prepara um caminho para obedecermos a Seus mandamentos.',
            'respostas': {'a': 'Mosias 4:9', 'b': '1 Nefi 3:7', 'c': 'João 7:17', },
            'resposta_certa': 'b',
        },

        'Pergunta 2': {
            'pergunta': 'Se nos banquetearmos com as palavras de Cristo, podemos saber todas as coisas que devemos fazer.',
            'respostas': {'a': 'Mosias 2:17', 'b': '2 Nefi 32:3', 'c': 'Atos 3:19', },
            'resposta_certa': 'b',
        },

        'Pergunta 3': {
            'pergunta': 'Se orarmos sempre, Deus consagrará a nossa ação para o bem-estar de nossa alma.',
            'respostas': {'a': '2 Néfi 32:8-9', 'b': 'João 17:7', 'c': 'Mosias 4:9', },
            'resposta_certa': 'a',
        },

        'Pergunta 4': {
            'pergunta': 'Despojar-se do homem natural e tornar-se santo pela Expiação.',
            'respostas': {'a': '1 Nefi 3:7', 'b': 'João 3:5', 'c': 'Mosias 3:19', },
            'resposta_certa': 'c',
        },

        'Pergunta 5': {
            'pergunta': 'Jesus Cristo experimentou nossas dores e venceu o pecado e a morte.',
            'respostas': {'a': 'Alma 39:9', 'b': 'Alma 7:11-13', 'c': 'Tiago 2:17', },
            'resposta_certa': 'b',
        },

        'Pergunta 6': {
            'pergunta': 'Jesus Cristo fez a vontade do Pai em todas as coisas.',
            'respostas': {'a': 'João 15:16', 'b': '3 Nefi 11:10-11', 'c': 'Éter 12:27', },
            'resposta_certa': 'b',
        },

        'Pergunta 7': {
            'pergunta': 'Vigiai e orai sempre em nome de Jesus Cristo.',
            'respostas': {'a': 'Éter 12:6', 'b': 'Efésios 2:19', 'c': '3 Néfi 18:15', },
            'resposta_certa': 'c',
        },

        'Pergunta 8': {
            'pergunta': 'O Salvador pode fazer com que as coisas frecas se tornem fortes.',
            'respostas': {'a': 'Éter 12:27', 'b': 'Hebreus 12:7', 'c': 'Éter 12:6', },
            'resposta_certa': 'a',
        },

        'Pergunta 9': {
            'pergunta': 'Jesus Cristo nos convida a nos tornarmos perfeito.',
            'respostas': {'a': '2 Néfi 26:33', 'b': '3 Nefí 12:48', 'c': 'João 17:3', },
            'resposta_certa': 'b',
        },

        'Pergunta 10': {
            'pergunta': 'O Espírito Santo revela a verdade àqueles que perguntam a Deus com real intenção.',
            'respostas': {'a': 'Mosias 39:9', 'b': 'Morôni 10:4-5', 'c': 'Mateus 16:15', },
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
