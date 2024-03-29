# Definição das perguntas e respostas como variáveis
pergunta_1 = "QUAL É O NOME COMPLETO DA PROTAGONISTA DO EPISÓDIO?"
resposta_1 = "Joan Tait"

pergunta_2 = "QUEM DIRIGE A VIDA DE JOAN EM TEMPO REAL PARA UMA SÉRIE DE TELEVISÃO?"
resposta_2 = "O próprio celular da Joan"

pergunta_3 = "QUAL É O NOME DO SERVIÇO DE STREAMING FICTÍCIO QUE PARODIA A NETFLIX NO EPISÓDIO?"
resposta_3 = "Streamberry"

pergunta_4 = "COMO JOAN DESCOBRE A EXISTÊNCIA DA SÉRIE SOBRE SUA VIDA?"
resposta_4 = "Ela descobre pois tem a plataforma na própria tv, tal plataforma que conseguiu ter os dados dela, pois ela assinou o termo que dava direito a plataforma pegar sua vida e transformar em uma série."

pergunta_5 = "QUAL É A REAÇÃO INICIAL DE JOAN AO DESCOBRIR A SÉRIE E O QUE ELA FAZ EM RESPOSTA?"
resposta_5 = "Ela fica chocada, acabada, a vida dele vira de 'cabeça para baixo', pois toda a rotina dela é destruída, assim como a vida, de primeira ela tem uma super recaída, mas depois começa a fazer cenas desagradantes na tentativa de fazer a Sama Haik desligar o programa, porém isso desbloqueia outra ocorrência de fatos com uma atriz que interpreta a Joan na série, já que ela deu os direitos autorais dela para a empresa que coloca a série dela, então ambas não tem poder de conseguir parar o programa."

pergunta_6 = "QUAIS SÃO OS TEMAS PRINCIPAIS EXPLORADOS NESTE EPISÓDIO DE BLACK MIRROR?"
resposta_6 = "Privacidade de dados, inteligência artificial, o futuro em relação à área de direito (mais em relação aos dados), a forma como a empresa usa os funcionários, como a economia pode influenciar não só a sociedade, mas a internet e como ambas acabam inspirando umas às outras, além de parecer um caso do qual o mundo não estava preparado para essa evolução tecnológica."

pergunta_7 = "O EPISÓDIO TERMINA DE MANEIRA TÍPICA PARA A SÉRIE BLACK MIRROR? EXPLIQUE."
resposta_7 = "Não, acredito que na última temporada os episódios estavam mais pessimistas, nesse episódio o final foi melhor, pois teve um desfecho do qual as duas personagens ficaram bem."

# Frase do usuário
while True:
    frase_usuario = input("Digite sua pergunta ou 's' para sair: ").upper()

    # Verificação se o usuário deseja sair
    if frase_usuario == 'S':
        print("Saindo...")
        break
    
    # Identificação da pergunta e exibição da resposta correspondente
    if "PROTAGONISTA" in frase_usuario and "NOME" in frase_usuario:
        print(resposta_1)
    elif "DIRIGE" in frase_usuario and "VIDA" in frase_usuario:
        print(resposta_2)
    elif "NOME" in frase_usuario and "SERVIÇO" in frase_usuario:
        print(resposta_3)
    elif "DESCOBRE" in frase_usuario and "SÉRIE" in frase_usuario:
        print(resposta_4)
    elif "REAÇÃO" in frase_usuario and "INICIAL" in frase_usuario:
        print(resposta_5)
    elif "TEMAS" in frase_usuario and "PRINCIPAIS" in frase_usuario:
        print(resposta_6)
    elif "TERMINA" in frase_usuario and "TÍPICA" in frase_usuario:
        print(resposta_7)
    else:
        print("Pergunta não reconhecida.")
