from conectar import cursor
from conectar import conexao
from twilio.rest import Client


def edv_cadastrado(edv):
    try:
        sql = f"SELECT * from usuarios WHERE edv = '{edv}'"
        cursor.execute(sql)
        cadastrado = True
        linhas = cursor.fetchall()
        return cadastrado, linhas[0][1]

    except:
        cadastrado = False

        return cadastrado, None


def cripto_edv(edv):
    lista = []
    lista_edv = []

    for a in edv:
        lista.append(a)

    for i in lista:
        if i == "0":
            lista_edv.append('a')
        elif i == "1":
            lista_edv.append('b')
        elif i == "2":
            lista_edv.append('c')
        elif i == "3":
            lista_edv.append('d')
        elif i == "4":
            lista_edv.append('e')
        elif i == "5":
            lista_edv.append('f')
        elif i == "6":
            lista_edv.append('g')
        elif i == "7":
            lista_edv.append('h')
        elif i == "8":
            lista_edv.append('i')
        elif i == "9":
            lista_edv.append('j')

    lista1 = ''.join(lista_edv)
    return lista1


def add_user(nome, telefone, edv):
    edv_cripto = cripto_edv(edv)
    adicionar_usuarios = f"""INSERT INTO usuarios(nome, telefone, edv)
           values
           ('{nome}', '{telefone}', '{edv}');"""
    cursor = conexao.cursor()
    cursor.execute(adicionar_usuarios)
    conexao.commit()
    adicionar_tabela_edv = f"CREATE TABLE {edv_cripto}(id INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(255), edv VARCHAR(255), data VARCHAR(255), hora VARCHAR(255), vezes int(11))"
    cursor = conexao.cursor()
    cursor.execute(adicionar_tabela_edv)
    conexao.commit()


def comprovante(nome, edv, dia, hora):
    account_sid = "ACb659a80a8bb0c11746b9eabdc5c303ce"
    auth_token = "446dd64a48949491cdd171fef50df9ef"
    client = Client(account_sid, auth_token)
    message = client.messages.create(
    body=f"Comprovante de ponto. Robert Bosch LTDA CNPJ. 455590181000000178 NSR: 00312865 ROD. ANHANGUERA, KM 98 S/N"
         f"VILA BOA VISTA CAMPINAS -SP NF: 000003457 1P NOME: {nome} EDV: {edv} DIA: {dia} HORA: {hora} STATUS: Ponto Validado  "
         f"PIS: 0000000000435345435347632478567823465786912634791625612677293048098-123487678213478623477861278346521783468762134",
    from_="+16813666265",
    to="+5519994117595"
    )
    print(message.sid)

