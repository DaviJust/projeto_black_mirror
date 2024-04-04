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
      notas = f"e{nota_e}t{nota_t}p{nota_p}s{nota_s}"  
      matriz_candidatos.append(Candidatos(nome, notas))

def procurar_candidatos(matriz_candidatos, pesquisar):
  candidato_encontrado = False
  for candidato in matriz_candidatos:
      notas = candidato.notas
      nota_e = int(notas[1])
      nota_t = int(notas[4])
      nota_p = int(notas[6])
      nota_s = int(notas[10])

      if nota_e >= pesquisar and nota_t >= pesquisar and nota_p >= pesquisar and nota_s >= pesquisar:
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
      pesquisar = int(input("Digite a nota mínima do candidato: "))
      procurar_candidatos(matriz_candidatos, pesquisar)
  elif opcao == "0":
      print("Saindo do programa...")
      break
  else:
      print("Opção inválida. Tente novamente.")
