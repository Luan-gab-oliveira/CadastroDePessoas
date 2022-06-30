from modules import os, pymysql
connection = {
    'db':{
        'database': 'dbCadastro',
        'charset': 'utf8mb4',
        'cursorclass': pymysql.cursors.DictCursor,
        'host': 'localhost',
        'username': 'root', 
    },
}
