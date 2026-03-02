class Aluno:
    def __init__(self, nome, matricula):
        # Atributos privados
        self.__nome = None
        self.__matricula = None
        self.__notas = []

        # Usando setters para validar na criação
        self.set_nome(nome)
        self.set_matricula(matricula)

    # =========================
    # Getter e Setter do Nome
    # =========================
    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        if isinstance(nome, str) and nome.strip():
            self.__nome = nome.strip()
        else:
            print("Nome inválido. Por favor, insira um nome válido.")

    # =========================
    # Getter e Setter da Matrícula
    # =========================
    def get_matricula(self):
        return self.__matricula

    def set_matricula(self, matricula):
        if isinstance(matricula, str) and matricula.isdigit() and 8 <= len(matricula) <= 10:
            self.__matricula = matricula
        else:
            print("Matrícula inválida. Deve conter entre 8 e 10 dígitos numéricos.")

    # =========================
    # Métodos de Notas
    # =========================
    def adicionar_nota(self, nota):
        if isinstance(nota, (int, float)) and 0 <= nota <= 10:
            self.__notas.append(float(nota))
        else:
            print("Nota inválida! A nota deve estar entre 0 e 10.")

    def calcular_media(self):
        if len(self.__notas) == 0:
            return 0
        return sum(self.__notas) / len(self.__notas)

    # =========================
    # Método para mostrar dados
    # =========================
    def mostrar_dados(self):
        print("===== Dados do Aluno =====")
        print(f"Nome: {self.get_nome()}")
        print(f"Matrícula: {self.get_matricula()}")
        print(f"Notas: {self.__notas}")
        print(f"Média: {self.calcular_media():.2f}")
        print("===========================")


# =========================
# Testando a Classe
# =========================

aluno1 = Aluno("João", "2025101035")

aluno1.adicionar_nota(8.0)
aluno1.adicionar_nota(7.0)
aluno1.adicionar_nota(9.5)

aluno1.mostrar_dados()