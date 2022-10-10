import sqlite3

from ppt_price_for_one_calculator import get_price_for_one


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
        """ Минеральная вата """

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

    def get_ppt_cubic_meter(self) -> str:
        """ Пенопласт за 1 м3 """

        conn = sqlite3.connect(self.db_name)
        row = conn.execute(
            "SELECT name, price "
            "FROM goods "
            "WHERE category = 8 AND in_stock = 1 "
            "ORDER BY price ASC"
        )
        data = row.fetchall()
        if data:
            answer = '💵 Цена за 1м3: 💵\n\n'
            for dry in data:
                answer += f'🔸 {dry[0]}: <b>{"%.2f" % dry[1]} руб.</b>\n'
        else:
            answer = 'К сожалению, на текущий момент товара нет в наличии...'
        conn.close()
        return answer

    def get_ppt_one_sheet(self) -> str:
        """ Пенопласт за 1 лист """

        conn = sqlite3.connect(self.db_name)
        row = conn.execute(
            "SELECT name, price "
            "FROM goods "
            "WHERE category = 8 AND in_stock = 1 "
        )
        prices_per_cubic_meter = {i[0]: i[1] for i in row.fetchall()}
        answer = '💵 Цена за 1 лист: 💵\n\n' \
                 '📏 Размер листа: 1000*500мм:\n'
        data = get_price_for_one(prices_per_cubic_meter)

        answer += f'\nПлотность: 10-A\n\n'
        for p in data['ППТ-10-А']['1000*500мм']:
            answer += f"🔸 {p}: <b>{'%.2f' % data['ППТ-10-А']['1000*500мм'][p]} руб.</b>\n"
        answer += f'\nПлотность: 15-A\n\n'
        for p in data['ППТ-15-А']['1000*500мм']:
            answer += f"🔸 {p}: <b>{'%.2f' % data['ППТ-15-А']['1000*500мм'][p]} руб.</b>\n"
        answer += f'\nПлотность: 15-Б\n\n'
        for p in data['ППТ-15-Б']['1000*500мм']:
            answer += f"🔸 {p}: <b>{'%.2f' % data['ППТ-15-Б']['1000*500мм'][p]} руб.</b>\n"
        answer += f'\nПлотность: 20-А\n\n'
        for p in data['ППТ-20-А']['1000*500мм']:
            answer += f"🔸 {p}: <b>{'%.2f' % data['ППТ-20-А']['1000*500мм'][p]} руб.</b>\n"
        answer += f'\nПлотность: 25-А\n\n'
        for p in data['ППТ-25-А']['1000*500мм']:
            answer += f"🔸 {p}: <b>{'%.2f' % data['ППТ-25-А']['1000*500мм'][p]} руб.</b>\n"
        answer += f'\nПлотность: 25-Б\n\n'
        for p in data['ППТ-25-Б']['1000*500мм']:
            answer += f"🔸 {p}: <b>{'%.2f' % data['ППТ-25-Б']['1000*500мм'][p]} руб.</b>\n"
        answer += f'\nПлотность: 35-A\n\n'
        for p in data['ППТ-35-А']['1000*500мм']:
            answer += f"🔸 {p}: <b>{'%.2f' % data['ППТ-35-А']['1000*500мм'][p]} руб.</b>\n"
        answer += '\n📏 Размер листа: 1000x1000мм:\n'
        answer += f'\nПлотность: 10-A\n\n'
        for p in data['ППТ-10-А']['1000*1000мм']:
            answer += f"🔸 {p}: <b>{'%.2f' % data['ППТ-10-А']['1000*1000мм'][p]} руб.</b>\n"
        answer += f'\nПлотность: 15-A\n\n'
        for p in data['ППТ-15-А']['1000*1000мм']:
            answer += f"🔸 {p}: <b>{'%.2f' % data['ППТ-15-А']['1000*1000мм'][p]} руб.</b>\n"
        answer += f'\nПлотность: 15-Б\n\n'
        for p in data['ППТ-20-А']['1000*1000мм']:
            answer += f"🔸 {p}: <b>{'%.2f' % data['ППТ-20-А']['1000*1000мм'][p]} руб.</b>\n"
        answer += f'\nПлотность: 25-А\n\n'
        for p in data['ППТ-25-А']['1000*1000мм']:
            answer += f"🔸 {p}: <b>{'%.2f' % data['ППТ-25-А']['1000*1000мм'][p]} руб.</b>\n"
        answer += f'\nПлотность: 35-A\n\n'
        for p in data['ППТ-35-А']['1000*1000мм']:
            answer += f"🔸 {p}: <b>{'%.2f' % data['ППТ-35-А']['1000*1000мм'][p]} руб.</b>\n"

        conn.close()
        return answer

    def get_profile(self) -> str:
        """ Профиль для гипсокартона """

        conn = sqlite3.connect(self.db_name)
        row = conn.execute(
            "SELECT name, price "
            "FROM goods "
            "WHERE category = 7 AND in_stock = 1 "
            "ORDER BY name"
        )
        data = row.fetchall()
        if data:
            answer = '💵 Цена 1шт (3м): 💵\n\n'
            for dry in data:
                answer += f'🔸 {dry[0]}: <b>{"%.2f" % dry[1]} руб.</b>\n'
        else:
            answer = 'К сожалению, на текущий момент товара нет в наличии...'
        conn.close()
        return answer

    def get_fiberglass_mesh(self) -> str:
        """ Сетка штукатурная """

        conn = sqlite3.connect(self.db_name)
        row = conn.execute(
            "SELECT name, price "
            "FROM goods "
            "WHERE category = 5 AND in_stock = 1 "
            "ORDER BY price"
        )
        data = row.fetchall()
        if data:
            answer = '💵 Цена за 1м2: 💵\n\n'
            for dry in data:
                answer += f'🔸 {dry[0]}: <b>{"%.2f" % dry[1]} руб.</b>\n'
        else:
            answer = 'К сожалению, на текущий момент товара нет в наличии...'
        conn.close()
        return answer

    def get_steel(self, description: str = None) -> str or None:
        """ Сталь """

        types = [
            'Арматура',
            'Трубы профильные',
            'Уголок стальной'
        ]
        if not description or description not in types:
            return

        conn = sqlite3.connect(self.db_name)
        row = conn.execute(
            "SELECT name, price "
            "FROM goods "
            f"WHERE description = '{description}' AND in_stock = 1 "
        )
        data = row.fetchall()
        if data:
            answer = '💵 Цена за 1 прут: 💵\n\n'
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
