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
        """ Гипсокартон """

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

    def get_dowel(self, description: str = None) -> str or None:
        """ Дюбеля для теплоизоляции """

        types = [
            'Стальной гвоздь',
            'Пластиковый гвоздь',
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
            answer = '💵 Цена за 1шт: 💵\n\n'
            for dry in data:
                answer += f'🔸 {dry[0]}: <b>{"%.2f" % dry[1]} руб.</b>\n'
        else:
            answer = 'К сожалению, на текущий момент товара нет в наличии...'
        conn.close()
        return answer

    def get_paints(self, description: str = None, description2: str = None) -> str or None:
        """ Краски """

        types = [
            'Тайфун Мастер',
            'Condor',
            'Kapral',
            'Sniezka',
            'Malevanka'
        ]
        if not description or description not in types:
            return

        conn = sqlite3.connect(self.db_name)
        if description2:
            row = conn.execute(
                "SELECT name, price "
                "FROM goods "
                f"WHERE description = '{description}' "
                f"AND description_2 = '{description2}'"
                f"AND in_stock = 1"
            )
        else:
            row = conn.execute(
                "SELECT name, price "
                "FROM goods "
                f"WHERE description = '{description}' AND in_stock = 1"
            )

        data = row.fetchall()
        if data:
            answer = '💵 Цена за 1 ведро: 💵\n\n'
            for dry in data:
                answer += f'🔸 {dry[0]}: <b>{"%.2f" % dry[1]} руб.</b>\n'
        else:
            answer = 'К сожалению, на текущий момент товара нет в наличии...'
        conn.close()
        return answer

    def get_mineral_wool(self) -> str:
        conn = sqlite3.connect(self.db_name)
        row = conn.execute(
            "SELECT name, price "
            "FROM goods "
            "WHERE category = 6 AND in_stock = 1"
        )
        data = row.fetchall()
        if data:
            answer = '💵 Цена за 1 упаковку: 💵\n\n'
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
