import os
import sqlite3


def conectar_bd():
    error_bd = sqlite3.Error
    bd = sqlite3.connect("./bd/bancodedados.db")
    cursor = bd.cursor()
    return bd, cursor, error_bd
