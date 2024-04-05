class Candidatos:
  def __init__(self, name, notas):
      self.name = name
      self.notas = notas

def cadastrar_candidatos(matriz_candidatos):
  quantidade_alunos = int(input("Digite a quantidade de candidatos: "))
  for _ in range(quantidade_alunos):
      nome = input("Digite o nome do candidato: ")
      nota_e = input("Digite a nota de entrevista do candidato: ")
      nota_t = input("Digite a nota do teste teórico do candidato: ")
      nota_p = input("Digite a nota do teste prático do candidato: ")
      nota_s = input("Digite a nota da avaliação de soft skills do candidato: ")
      notas = f"e{nota_e}_t{nota_t}_p{nota_p}_s{nota_s}"
      matriz_candidatos.append(Candidatos(nome, notas))

def procurar_candidatos(matriz_candidatos, pesquisar_entrevista, pesquisar_teórico, pesquisar_prático, pesquisar_soft_skills):
  candidato_encontrado = False
  for candidato in matriz_candidatos:
      notas = candidato.notas
      nota_e = int(notas.split('_')[0][1:])
      nota_t = int(notas.split('_')[1][1:])
      nota_p = int(notas.split('_')[2][1:])
      nota_s = int(notas.split('_')[3][1:])
      if nota_e >= pesquisar_entrevista and nota_t >= pesquisar_teórico and nota_p >= pesquisar_prático and nota_s >= pesquisar_soft_skills:
          print(f"Nome: {candidato.name}")
          print(f"Notas: {candidato.notas}")
          print()
          candidato_encontrado = True

  if not candidato_encontrado:
      print("Nenhum candidato encontrado com as notas mínimas especificadas.")

matriz_candidatos = []

while True:
  print("Menu:\n[1] Cadastrar candidatos\n[2] Procurar candidatos\n[0] Sair")
  opcao = input("Escolha uma opção: ")

  if opcao == "1":
      cadastrar_candidatos(matriz_candidatos)
  elif opcao == "2":
      pesquisar_entrevista = int(input("Digite a nota mínima da entrevista: "))
      pesquisar_teórico = int(input("Digite a nota mínima do teste teórico: "))
      pesquisar_prático = int(input("Digite a nota mínima do teste prático: "))
      pesquisar_soft_skills = int(input("Digite a nota mínima da avaliação de soft skills: "))
      procurar_candidatos(matriz_candidatos, pesquisar_entrevista, pesquisar_teórico, pesquisar_prático, pesquisar_soft_skills)
  elif opcao == "0":
      print("Saindo do programa...")
      break
  else:
      print("Opção inválida. Tente novamente.")

