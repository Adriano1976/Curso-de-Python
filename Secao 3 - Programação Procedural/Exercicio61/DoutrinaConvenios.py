def jogar():

    print()
    print(
        '-------------------------------------------------------------------------------------------------------------')
    print(
        '--------------------    PERGUNTAS RELACIONADAS AS ESCRITURAS DE DOUTRINA & CONVÊNIOS    ---------------------')
    print(
        '-------------------------------------------------------------------------------------------------------------')

    perguntas = {
        'Pergunta 1': {
            'pergunta': 'A voz do Senhor e a de Seus servos é a mesma.',
            'respostas': {'a': 'Mosias 4:9', 'b': 'D&C 1:37-38', 'c': 'D&C 1:30', },
            'resposta_certa': 'b',
        },

        'Pergunta 2': {
            'pergunta': 'O Espítiro Santos fala à nossa mente e ao nosso coração.',
            'respostas': {'a': 'Mosias 2:17', 'b': 'D&C 8:2-3', 'c': 'D&C 1:30', },
            'resposta_certa': 'b',
        },

        'Pergunta 3': {
            'pergunta': 'O Salvador sofreu por nossos pecados para que pudésse-mos arrepender-nos',
            'respostas': {'a': 'D&C 19:16-19', 'b': 'D&C 42:11', 'c': 'Mosias 4:9', },
            'resposta_certa': 'a',
        },

        'Pergunta 4': {
            'pergunta': 'Ao recebermos as palavras dos profetas com paciência e fé, Deus afastará de nós os poderes das trevas.',
            'respostas': {'a': '1 Nefi 3:7', 'b': 'D&C 42:11', 'c': 'D&C 21:4-6', },
            'resposta_certa': 'c',
        },

        'Pergunta 5': {
            'pergunta': 'Cristo virá novamente com poder e glória.',
            'respostas': {'a': 'D&C 1:30', 'b': 'D&C 29:10-11', 'c': 'Tiago 2:17', },
            'resposta_certa': 'b',
        },

        'Pergunta 6': {
            'pergunta': 'O casamento entre homem e mulher foi ordenado por Deus.',
            'respostas': {'a': 'D%C 18:10-11', 'b': 'D&C 49:15-17', 'c': 'Éter 12:27', },
            'resposta_certa': 'b',
        },

        'Pergunta 7': {
            'pergunta': 'Para nos arrependermos, precisamos confessar e abondonar os pecados.',
            'respostas': {'a': 'Éter 12:6', 'b': 'D&C 13:1', 'c': 'D%C 58:42', },
            'resposta_certa': 'c',
        },

        'Pergunta 8': {
            'pergunta': 'O Senhor está obrigado quando fazermos o que Ele diz.',
            'respostas': {'a': 'D&C 82:10', 'b': 'D&C 42:11', 'c': 'Éter 12:6', },
            'resposta_certa': 'a',
        },

        'Pergunta 9': {
            'pergunta': 'O poder da divindade se manifesta nas ordenanças do sacerdócio.',
            'respostas': {'a': '2 Néfi 26:33', 'b': 'D&C 84:20-22', 'c': 'D&C 6:36', },
            'resposta_certa': 'b',
        },

        'Pergunta 10': {
            'pergunta': 'O novo e eterno convênio do casamento.',
            'respostas': {'a': 'Mosias 39:9', 'b': 'D&C 131:1-4', 'c': 'D&C 58:42', },
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
