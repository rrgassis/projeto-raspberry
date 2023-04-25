import datetime
import time
from datetime import date

from conectar import conexao, cursor
from funcoes import cripto_edv


def dia_hora():
    horano = datetime.datetime.now()
    datono = datetime.date.today()
    data = datono.strftime("%d-%m-%Y")
    hora = horano.strftime("%H:%M")
    return data, hora


def vesez_ponto_batido(edv):
    edv_cripto = cripto_edv(edv)
    try:
        sql = f"SELECT * from {edv_cripto} WHERE edv = '{edv}'"
        cursor.execute(sql)
        linhas = cursor.fetchall()
        vesez_ponto = linhas[0][5]
        vesez = vesez_ponto + 1
        return vesez

    except:
        vezes = 1
        return vezes


def validacao(edv, nome):
    data: date
    data, hora = dia_hora()
    edv_cripto = cripto_edv(edv)
    vesez = vesez_ponto_batido(edv)
    ponto_bate = f"""INSERT INTO {edv_cripto}(nome, edv, data, hora, vezes)
               values
               ('{nome}', '{edv}', '{data}', '{hora}', {vesez});"""
    cursor = conexao.cursor()
    cursor.execute(ponto_bate)
    conexao.commit()