# -*- coding: utf-8 -*-
"""
@author: Bruno Portes
@python 3.6
"""
import numpy as np
import sqlite3

class CorrecaoInflacao:

    def __init__(self, anoBase, anoValor, valor):
        try:
           self.anoBase = int(anoBase)
           self.anoValor = int(anoValor)
           self.valor = float(valor)
        except:
           print("Os valores devem ser numéricos!")

        try:
            self.conn = conn = sqlite3.connect(r'database.db')
        except:
            print("Erro de conexão com o banco de dados")

    def ipca(self):
        cur = self.conn.cursor()
        listaIndice = []
        anoOrigem = self.anoValor
        while anoOrigem < self.anoBase:
             cur.execute("select correcao from ipca where ano = ? ", (anoOrigem,))
             aux = cur.fetchone()
             listaIndice.append(aux[0])
             anoOrigem += 1
        return (self.valor*np.prod(listaIndice))

    def icv(self):
        cur = self.conn.cursor()
        listaIndice = []
        anoOrigem = self.anoValor
        while anoOrigem < self.anoBase:
             cur.execute("select correcao from icv where ano = ? ", (anoOrigem,))
             aux = cur.fetchone()
             listaIndice.append(aux[0])
             anoOrigem += 1
        return (self.valor*np.prod(listaIndice))

    def inpc(self):
        cur = self.conn.cursor()
        listaIndice = []
        anoOrigem = self.anoValor
        while anoOrigem < self.anoBase:
             cur.execute("select correcao from inpc where ano = ? ", (anoOrigem,))
             aux = cur.fetchone()
             listaIndice.append(aux[0])
             anoOrigem += 1
        return (self.valor*np.prod(listaIndice))
