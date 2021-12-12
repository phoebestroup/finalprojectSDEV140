import sqlite3


class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS shoelist (id INTEGER PRIMARY KEY, sku integer, style text, color text, size float, qty integer, price float)")
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM shoelist")
        rows = self.cur.fetchall()
        return rows

    def insert(self, sku, style, color, size, qty, price):
        self.cur.execute("INSERT INTO shoelist VALUES (NULL, ?, ?, ?, ?, ?, ?)", (sku, style, color, size, qty, price))
        self.conn.commit()

    def remove(self, id):
        self.cur.execute("DELETE FROM shoelist WHERE id=?", (id,))
        self.conn.commit()

    def update(self, id, sku, style, color, size, qty, price):
        self.cur.execute("UPDATE shoelist SET sku=?, style=?, color=?, size=?, qty=?, price=? WHERE id=?",
                         (sku, style, color, size, qty, price, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()


# db = Database("store.db")
# db.insert(	"1144033"	,	"M9160"	,	"BLK"	,	"6"	,	"63"	,	"54.95"	)
# db.insert(	"1144034"	,	"M9160"	,	"BLK"	,	"6.5"	,	"122"	,	"54.95"	)
# db.insert(	"1144038"	,	"M9160"	,	"BLK"	,	"8.5"	,	"75"	,	"54.95"	)
# db.insert(	"1144039"	,	"M9160"	,	"BLK"	,	"9"	,	"80"	,	"54.95"	)
# db.insert(	"1144040"	,	"M9160"	,	"BLK"	,	"9.5"	,	"98"	,	"54.95"	)
# db.insert(	"1144041"	,	"M9160"	,	"BLK"	,	"10"	,	"76"	,	"54.95"	)
# db.insert(	"1144042"	,	"M9160"	,	"BLK"	,	"10.5"	,	"93"	,	"54.95"	)
# db.insert(	"1144047"	,	"M9160"	,	"BLK"	,	"13"	,	"96"	,	"54.95"	)
# db.insert(	"1144048"	,	"M9160"	,	"BLK"	,	"13.5"	,	"56"	,	"54.95"	)
# db.insert(	"1144049"	,	"M9160"	,	"BLK"	,	"14"	,	"78"	,	"54.95"	)
# db.insert(	"1144131"	,	"M9697"	,	"NVY"	,	"5"	,	"96"	,	"49.76"	)
# db.insert(	"1144132"	,	"M9697"	,	"NVY"	,	"5.5"	,	"76"	,	"49.76"	)
# db.insert(	"1144133"	,	"M9697"	,	"NVY"	,	"6"	,	"39"	,	"49.76"	)
# db.insert(	"1144134"	,	"M9697"	,	"NVY"	,	"6.5"	,	"94"	,	"49.76"	)
# db.insert(	"1144135"	,	"M9697"	,	"NVY"	,	"7"	,	"76"	,	"49.76"	)
# db.insert(	"1144136"	,	"M9697"	,	"NVY"	,	"7.5"	,	"285"	,	"49.76"	)
# db.insert(	"1144137"	,	"M9697"	,	"NVY"	,	"8"	,	"63"	,	"49.76"	)
# db.insert(	"1144138"	,	"M9697"	,	"NVY"	,	"8.5"	,	"49"	,	"49.76"	)
# db.insert(	"1144139"	,	"M9697"	,	"NVY"	,	"9"	,	"102"	,	"49.76"	)
# db.insert(	"1144140"	,	"M9697"	,	"NVY"	,	"9.5"	,	"54"	,	"49.76"	)
# db.insert(	"1144141"	,	"M9697"	,	"NVY"	,	"10"	,	"98"	,	"49.76"	)
# db.insert(	"1144142"	,	"M9697"	,	"NVY"	,	"10.5"	,	"75"	,	"49.76"	)
# db.insert(	"1144143"	,	"M9697"	,	"NVY"	,	"11"	,	"63"	,	"49.76"	)
# db.insert(	"1144144"	,	"M9697"	,	"NVY"	,	"11.5"	,	"45"	,	"49.76"	)
# db.insert(	"1144145"	,	"M9697"	,	"NVY"	,	"12"	,	"23"	,	"49.76"	)
# db.insert(	"1144146"	,	"M9697"	,	"NVY"	,	"12.5"	,	"96"	,	"49.76"	)
# db.insert(	"1144147"	,	"M9697"	,	"NVY"	,	"13"	,	"85"	,	"49.76"	)
# db.insert(	"1144148"	,	"M9697"	,	"NVY"	,	"13.5"	,	"146"	,	"49.76"	)
# db.insert(	"1144149"	,	"M9697"	,	"NVY"	,	"14"	,	"56"	,	"49.76"	)
# db.insert(	"1197921"	,	"M7652"	,	"OPT"	,	"5"	,	"89"	,	"55"	)
#db.insert("1197922", "M7653", "OPT", "5.5", "64", "55")
#db.insert("1197922", "M7654", "OPT", "6", "89", "55")
#db.insert("1197922", "M7655", "OPT", "6.5", "76", "55")
#db.insert("1197922", "M7656", "OPT", "7", "53", "55")
#db.insert("1197922", "M7657", "OPT", "7.5", "120", "55")
#db.insert("1197922", "M7658", "OPT", "8", "69", "55")
#db.insert("1197922", "M7659", "OPT", "8.5", "86", "55")
#db.insert("1197922", "M7660", "OPT", "9", "34", "55")
#db.insert("1197922", "M7661", "OPT", "9.5", "56", "55")
#db.insert("1197922", "M7662", "OPT", "10", "92", "55")
#db.insert("1197922", "M7663", "OPT", "10.5", "78", "55")
#db.insert("1197922", "M7664", "OPT", "11", "94", "55")
#db.insert("1197922", "M7665", "OPT", "11.5", "56", "55")
#db.insert("1197922", "M7666", "OPT", "12", "91", "55")
#db.insert("1197922", "M7667", "OPT", "12.5", "46", "55")
#db.insert("1197922", "M7668", "OPT", "13", "89", "55")
#db.insert("1197922", "M7669", "OPT", "13.5", "67", "55")
#db.insert("1197922", "M7670", "OPT", "14", "39", "55")
#db.insert("1953761", "W9696", "RED", "5", "64", "54.95")
#db.insert("1953762", "W9696", "RED", "5.5", "64", "54.95")
#db.insert("1953763", "W9696", "RED", "6", "79", "54.95")
#db.insert("1953764", "W9696", "RED", "6.5", "37", "54.95")
#db.insert("1953765", "W9696", "RED", "7", "89", "54.95")
#db.insert("1953766", "W9696", "RED", "7.5", "59", "54.95")
#db.insert("1953767", "W9696", "RED", "8", "86", "54.95")
#db.insert("1953768", "W9696", "RED", "8.5", "97", "54.95")
#db.insert("1953769", "W9696", "RED", "9", "68", "54.95")
#db.insert("1953770", "W9696", "RED", "9.5", "39", "54.95")
#db.insert("1953771", "W9696", "RED", "10", "91", "54.95")
#db.insert("1953772", "W9696", "RED", "10.5", "87", "54.95")
#db.insert("1953773", "W9696", "RED", "11", "94", "54.95")
#db.insert("1953774", "W9696", "RED", "11.5", "68", "54.95")
#db.insert("1953775", "W9696", "RED", "12", "89", "54.95")
#db.insert("1953776", "W9696", "RED", "12.5", "97", "54.95")
#db.insert("1953777", "W9696", "RED", "13", "46", "54.95")
#db.insert("1953778", "W9696", "RED", "13.5", "96", "54.95")
#db.insert("1953779", "W9696", "RED", "14", "82", "54.95")
