# Classe Curso
class Curso:
    def __init__(self, nome, duracao):
        self.nome = nome
        self.duracao = duracao

    def descricao(self):
        return f"Curso: {self.nome} - Duração: {self.duracao} semestres"


# Classe base
class Aluno:
    def __init__(self, nome, matricula, curso):
        self.__nome = None
        self.__matricula = None
        self.__notas = []
        self.curso = curso

        self.set_nome(nome)
        self.set_matricula(matricula)

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        if nome and nome.strip():
            self.__nome = nome
        else:
            print("Nome inválido.")

    def get_matricula(self):
        return self.__matricula

    def set_matricula(self, matricula):
        if matricula.isdigit() and 8 <= len(matricula) <= 10:
            self.__matricula = matricula
        else:
            print("Matrícula inválida.")

    def adicionar_nota(self, nota):
        if 0 <= nota <= 10:
            self.__notas.append(nota)
        else:
            print("Nota inválida!")

    def calcular_media(self):
        if not self.__notas:
            return 0
        return sum(self.__notas) / len(self.__notas)

    def mostrar_dados(self):
        print(f"Nome: {self.get_nome()}")
        print(f"Matrícula: {self.get_matricula()}")
        print(f"Média: {self.calcular_media():.2f}")
        print(self.curso.descricao())


# Herança
class AlunoIntegrado(Aluno):
    def __init__(self, nome, matricula, curso, curso_tecnico):
        super().__init__(nome, matricula, curso)
        self.curso_tecnico = curso_tecnico

    def mostrar_dados(self):
        super().mostrar_dados()
        print(f"Curso Técnico: {self.curso_tecnico}")


class AlunoGraduacao(Aluno):
    def __init__(self, nome, matricula, curso, curso_graduacao):
        super().__init__(nome, matricula, curso)
        self.curso_graduacao = curso_graduacao

    def mostrar_dados(self):
        super().mostrar_dados()
        print(f"Graduação: {self.curso_graduacao}")


class AlunoPosGraduacao(Aluno):
    def __init__(self, nome, matricula, curso, pos_graduacao):
        super().__init__(nome, matricula, curso)
        self.pos_graduacao = pos_graduacao

    def mostrar_dados(self):
        super().mostrar_dados()
        print(f"Pós-graduação: {self.pos_graduacao}")


class AlunoSubsequente(Aluno):
    def __init__(self, nome, matricula, curso, curso_tecnico):
        super().__init__(nome, matricula, curso)
        self.curso_tecnico = curso_tecnico

    def mostrar_dados(self):
        super().mostrar_dados()
        print(f"Técnico: {self.curso_tecnico}")


# Criando cursos
curso0 = Curso("Técnico em Informática", 6)
curso1 = Curso("Informática", 8)
curso2 = Curso("Sistema de Informação", 7)


# Criando alunos
aluno1 = AlunoIntegrado("João", "20251010", curso1, "Informática")
aluno2 = AlunoGraduacao("Maria", "20251011", curso2, "ADS")

# Lista de alunos
alunos = [aluno1, aluno2]


# Entrada de notas
for aluno in alunos:
    print(f"\nAdicionando notas para {aluno.get_nome()}:")
    for i in range(2):
        while True:
            entrada = input(f"Digite a nota {i+1} para {aluno.get_nome()}: ")
            if entrada.strip() == "":
                print("Entrada vazia. Digite uma nota válida.")
                continue
            try:
                nota = float(entrada)
                if 0 <= nota <= 10:
                    aluno.adicionar_nota(nota)
                    break
                else:
                    print("A nota deve estar entre 0 e 10.")
            except ValueError:
                print("Valor inválido. Digite um número.")


# Exibir dados
print("\n--- Dados dos Alunos ---")
aluno1.mostrar_dados()
print("----")
aluno2.mostrar_dados()