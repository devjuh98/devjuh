import mysql.connector
banco = mysql.connector.connect(host="localhost",
                                user="root",
                                password="123456",
                                database="turma_d")
meucursor = banco.cursor()
print(f"Menu\n"
      f"[1]Mostrar tabela\n"
      f"[2]Inserir alunos\n"
      f"[3]Sair")
opcao = 0
while opcao!="3":
    opcao = input("Digite o número: ")
    if opcao=="1":

        pesquisa = "select * from alunos;"
        meucursor.execute(pesquisa)
        resultado = meucursor.fetchall()
        for x in resultado:
            print(x)
    if opcao=="2":
        nome1 = input("Digite o seu nome: ")
        telefone1 = int(input("Digite o seu telefone: "))
        sql = "INSERT INTO alunos (nome,telefone) VALUES (%s,%s)"
        data = (nome1,telefone1)
        meucursor.execute(sql,data)
        banco.commit()

meucursor.close()
banco.close()