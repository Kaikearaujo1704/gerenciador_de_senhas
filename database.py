import sqlite3


class Banco:

    def __init__(self):

        self.conexao = sqlite3.connect("dados/senhas.db")

        self.cursor = self.conexao.cursor()

        self.criar_tabela()

    def criar_tabela(self):

        self.cursor.execute("""

            CREATE TABLE IF NOT EXISTS contas(

                id INTEGER PRIMARY KEY AUTOINCREMENT,

                site TEXT NOT NULL,

                usuario TEXT NOT NULL,

                senha TEXT NOT NULL

            )

        """)

        self.conexao.commit()

    def adicionar(self, site, usuario, senha):

        self.cursor.execute("""

            INSERT INTO contas(site, usuario, senha)

            VALUES (?, ?, ?)

        """, (site, usuario, senha))

        self.conexao.commit()

    def listar(self):

        self.cursor.execute("SELECT * FROM contas")

        contas = self.cursor.fetchall()

        if not contas:

            print("\nNenhuma conta cadastrada.")

            return

        print()

        for conta in contas:

            print(f"ID: {conta[0]}")
            print(f"Site: {conta[1]}")
            print(f"Usuário: {conta[2]}")
            print(f"Senha: {conta[3]}")
            print("-" * 35)

    def buscar(self, site):

        self.cursor.execute(

            "SELECT * FROM contas WHERE site = ?",

            (site,)

        )

        conta = self.cursor.fetchone()

        if conta:

            print()

            print(f"Site: {conta[1]}")
            print(f"Usuário: {conta[2]}")
            print(f"Senha: {conta[3]}")

        else:

            print("\nConta não encontrada.")

    def alterar(self, site, senha):

        self.cursor.execute("""

            UPDATE contas

            SET senha = ?

            WHERE site = ?

        """, (senha, site))

        self.conexao.commit()

    def excluir(self, site):

        self.cursor.execute(

            "DELETE FROM contas WHERE site = ?",

            (site,)

        )

        self.conexao.commit()
