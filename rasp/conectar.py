import mysql.connector


conexao = mysql.connector.connect(
    host='localhost',
    database='rasp_user',
    user='root',
    password=''
)
cursor = conexao.cursor()
"""
cursor.execute('select database();')
linha = cursor.fetchone()"""