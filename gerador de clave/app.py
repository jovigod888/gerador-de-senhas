import sqlite3, secrets, string

conm = sqlite3.connect("chaves.db")
cursor = conm.cursor()

cursor.execute("""
create table if not exists chaves (
               id integer primary key autoincrement,
               chave text
)
""")

chave = secrets.token_hex(16)

cursor.execute("insert into chaves (chave) values (?)", (chave,))

conm.commit()
conm.close()

print(f"Chave gerada: {chave}")