import mysql.connector

con = mysql.connector.connect(host='localhost', database='r_programming_test', user='root', port=3306, password='!q@w#e$r%t')

if con.is_connected():
    db_info = con.get_server_info()
    print("Conectado ao servidor MySQL versão ", db_info)
    cursor = con.cursor()
    cursor.execute("SELECT database();")
    linha = cursor.fetchone()
    print("Conectado ao banco de dados", linha)

if con.is_connected():
    cursor.close()
    con.close()
    print("A conexão ao MySQL foi encerrada")
