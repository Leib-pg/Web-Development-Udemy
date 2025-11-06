
import random

def main():
    lista_alunos = []
    for i in range(4):
        nome = input(f'Digite o nome do {i+1}º aluno: ').strip()
        if nome == "":
            print("Nome vazio. Tente novamente.")
            return
        lista_alunos.append(nome)

    escolhido = random.choice(lista_alunos)
    print(f'O aluno sorteado foi: {escolhido}')

if __name__ == "__main__":
    main()
