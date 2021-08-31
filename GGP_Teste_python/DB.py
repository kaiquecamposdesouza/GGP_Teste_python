import psycopg2

class Inserir():

    def start(self):
        con = psycopg2.connect(host='ec2-107-22-83-3.compute-1.amazonaws.com', database='d6ror24c3d0r04',
                       user='grszehrcqoeofv', password='fe7ee4089879623a5b959fdd204a174f84e18d2af1c35133cc6d0502eb6c5399')
        return con

    def inseri_dados_produtos(self, descricao, valor, quantidade, con):
        Cursor_inserir = con.cursor()
        Cursor_inserir.execute(
                "INSERT INTO Produtos (Descricao, Valor, Quantidade) VALUES (%s,%s,%s)",
                (descricao, valor, quantidade))

        con.commit()
        con.close()

class Seleciona():

    def start(self):
        con = psycopg2.connect(host='ec2-107-22-83-3.compute-1.amazonaws.com', database='d6ror24c3d0r04',
                       user='grszehrcqoeofv', password='fe7ee4089879623a5b959fdd204a174f84e18d2af1c35133cc6d0502eb6c5399')
        return con 

    def selec_produtos(self, con):
        dados=[]
        Cursor_seleciona = con.cursor()
        Cursor_seleciona.execute("SELECT * FROM Produtos")
        for item in Cursor_seleciona:
            dados.append(item)
        con.close()

        return dados