import sqlite3


class DBHandler:
    def __init__(self, db_name='sogreym_db'):
        self.db_name = db_name
        # self.conn = sqlite3.connect(self.db_name)

    def edit_price(self, product: str = None):
        pass

    def edit_stock(self):
        pass

    def get_drywall(self, description: str = None) -> str or None:
        types = [
            'Огнеупорный',
            'Влагостойкий',
            'Обычный'
        ]
        if not description or description not in types:
            return
        conn = sqlite3.connect(self.db_name)
        row = conn.execute(
            "SELECT name, price "
            "FROM goods "
            f"WHERE description = '{description}' AND in_stock = 1"
        )
        data = row.fetchall()
        if data:
            answer = '💵 Цена за 1 лист 1200*2500мм (3м2): 💵\n\n'
            for dry in data:
                answer += f'🔸 {dry[0]}: <b>{"%.2f" % dry[1]} руб.</b>\n'
        else:
            answer = 'К сожалению, на текущий момент товара нет в наличии...'
        conn.close()
        return answer

# conn = sqlite3.connect('../sogreym_db')
# cursor = conn.cursor()
#
# res = cursor.execute('SELECT * FROM category;')
# print(res.fetchall())
