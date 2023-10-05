import os
import sqlite3


def conectar_bd():
    error_bd = sqlite3.Error
    if os.path.isfile("./.teste"):
        bd = sqlite3.connect('file:memdb?mode=memory&cache=shared')

    else:
        bd = sqlite3.connect("./bd/bancodedados.db")
    cursor = bd.cursor()
    return bd, cursor, error_bd
