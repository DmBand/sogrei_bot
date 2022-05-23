categories = [
    'Гипсокартон',
    'Клей',
    'Пенопласт',
    'Сетка штукатурная',
    'OSB-плиты влагостойкие',
]

# Гипсокартон
DRYWALL = {
    'Огнеупорный':
        {
            '12,5мм тип DF, Кнауф, Беларусь': 23.04
        },
    'Влагостойкий':
        {
            '9,5мм Danogips, Беларусь': 22.05,
            '12,5мм Danogips, Беларусь': 23.10,
            '9,5мм Кнауф, РФ': 23.10,
            '12,5мм Кнауф, РФ': 22.96,
        },
    'Обычный':
        {
            '9.5мм Danogips, Беларусь': 14.81,
            '12.5мм Danogips smart, Беларусь': 18.44,
            '9.5мм стандарт Кнауф, РФ': 17.79,
            '12.5мм стандарт Кнауф, РФ': 18.87
        }
}

GLUES = {
    'Люкс Плюс КС1, 25кг': 15.31,
    'Тайфун Мастер №50, 25кг': 12.62,
    'Тайфун Мастер №51, 25кг': 17.33
}

# Цены на ППТ
PPT_PRICE_PER_CUBIC_METER = {
    'ППТ-10-A': 171.00,
    'ППТ-10-Б': 193.00,
    'ППТ-15-А': 213.00,
    'ППТ-15-Б': 234.00,
    'ППТ-20-А': 259.00,
    'ППТ-20-Б': 270.00,
    'ППТ-25-А': 317.00,
    'ППТ-25-Б': 340.00,
    'ППТ-35-А': 423.00,
    'ППТ-35-Б': 466.00
}

PPT_PRICE_FOR_ONE = {
    'ППТ-10-А':
        {
            '1000*500мм':
                {
                    '2см': 0.01 * PPT_PRICE_PER_CUBIC_METER['ППТ-10-A'],
                    '3см': 0.015 * PPT_PRICE_PER_CUBIC_METER['ППТ-10-A'],
                    '5см': 0.025 * PPT_PRICE_PER_CUBIC_METER['ППТ-10-A'],
                    '10см': 0.05 * PPT_PRICE_PER_CUBIC_METER['ППТ-10-A'],
                },
            '1000*1000мм':
                {
                    '2см': 0.02 * PPT_PRICE_PER_CUBIC_METER['ППТ-10-A'],
                    '3см': 0.03 * PPT_PRICE_PER_CUBIC_METER['ППТ-10-A'],
                    '5см': 0.05 * PPT_PRICE_PER_CUBIC_METER['ППТ-10-A'],
                    '10см': 0.1 * PPT_PRICE_PER_CUBIC_METER['ППТ-10-A'],
                }
        },
    'ППТ-15-А':
        {
            '1000*500мм':
                {
                    '2см': 0.01 * PPT_PRICE_PER_CUBIC_METER['ППТ-15-А'],
                    '3см': 0.015 * PPT_PRICE_PER_CUBIC_METER['ППТ-15-А'],
                    '5см': 0.025 * PPT_PRICE_PER_CUBIC_METER['ППТ-15-А'],
                    '10см': 0.05 * PPT_PRICE_PER_CUBIC_METER['ППТ-15-А'],
                },
            '1000*1000мм':
                {
                    '2см': 0.02 * PPT_PRICE_PER_CUBIC_METER['ППТ-15-А'],
                    '3см': 0.03 * PPT_PRICE_PER_CUBIC_METER['ППТ-15-А'],
                    '5см': 0.05 * PPT_PRICE_PER_CUBIC_METER['ППТ-15-А'],
                    '7см': 0.07 * PPT_PRICE_PER_CUBIC_METER['ППТ-15-А'],
                    '10см': 0.1 * PPT_PRICE_PER_CUBIC_METER['ППТ-15-А'],
                }
        },
    'ППТ-15-Б':
        {
            '1000*500мм':
                {
                    '5см': 0.025 * PPT_PRICE_PER_CUBIC_METER['ППТ-15-Б'],
                },
        },
    'ППТ-20-А':
        {
            '1000*500мм':
                {
                    '1см': 0.005 * PPT_PRICE_PER_CUBIC_METER['ППТ-20-А'],
                    '2см': 0.01 * PPT_PRICE_PER_CUBIC_METER['ППТ-20-А'],
                    '3см': 0.015 * PPT_PRICE_PER_CUBIC_METER['ППТ-20-А'],
                    '5см': 0.025 * PPT_PRICE_PER_CUBIC_METER['ППТ-20-А'],
                    '10см': 0.05 * PPT_PRICE_PER_CUBIC_METER['ППТ-20-А'],
                },
            '1000*1000мм':
                {
                    '2см': 0.02 * PPT_PRICE_PER_CUBIC_METER['ППТ-20-А'],
                    '3см': 0.03 * PPT_PRICE_PER_CUBIC_METER['ППТ-20-А'],
                    '5см': 0.05 * PPT_PRICE_PER_CUBIC_METER['ППТ-20-А'],
                    '10см': 0.1 * PPT_PRICE_PER_CUBIC_METER['ППТ-20-А'],
                }
        },
    'ППТ-25-А':
        {
            '1000*500мм':
                {
                    '1см': 0.005 * PPT_PRICE_PER_CUBIC_METER['ППТ-25-А'],
                    '2см': 0.01 * PPT_PRICE_PER_CUBIC_METER['ППТ-25-А'],
                    '3см': 0.015 * PPT_PRICE_PER_CUBIC_METER['ППТ-25-А'],
                    '4см': 0.02 * PPT_PRICE_PER_CUBIC_METER['ППТ-25-А'],
                    '5см': 0.025 * PPT_PRICE_PER_CUBIC_METER['ППТ-25-А'],
                    '7см': 0.035 * PPT_PRICE_PER_CUBIC_METER['ППТ-25-А'],
                    '8см': 0.04 * PPT_PRICE_PER_CUBIC_METER['ППТ-25-А'],
                    '10см': 0.05 * PPT_PRICE_PER_CUBIC_METER['ППТ-25-А'],
                },
            '1000*1000мм':
                {
                    '2см': 0.02 * PPT_PRICE_PER_CUBIC_METER['ППТ-25-А'],
                    '3см': 0.03 * PPT_PRICE_PER_CUBIC_METER['ППТ-25-А'],
                    '5см': 0.05 * PPT_PRICE_PER_CUBIC_METER['ППТ-25-А'],
                    '10см': 0.1 * PPT_PRICE_PER_CUBIC_METER['ППТ-25-А'],
                }
        },
    'ППТ-25-Б':
        {
            '1000*500мм':
                {
                    '5см': 0.025 * PPT_PRICE_PER_CUBIC_METER['ППТ-25-Б'],
                },
        },
    'ППТ-35-А':
        {
            '1000*500мм':
                {
                    '1см': 0.005 * PPT_PRICE_PER_CUBIC_METER['ППТ-35-А'],
                    '2см': 0.01 * PPT_PRICE_PER_CUBIC_METER['ППТ-35-А'],
                    '3см': 0.015 * PPT_PRICE_PER_CUBIC_METER['ППТ-35-А'],
                    '5см': 0.025 * PPT_PRICE_PER_CUBIC_METER['ППТ-35-А'],
                    '10см': 0.05 * PPT_PRICE_PER_CUBIC_METER['ППТ-35-А'],
                },
            '1000*1000мм':
                {
                    '2см': 0.02 * PPT_PRICE_PER_CUBIC_METER['ППТ-35-А'],
                    '3см': 0.03 * PPT_PRICE_PER_CUBIC_METER['ППТ-35-А'],
                    '5см': 0.05 * PPT_PRICE_PER_CUBIC_METER['ППТ-35-А'],
                    '10см': 0.1 * PPT_PRICE_PER_CUBIC_METER['ППТ-35-А'],
                }
        },
}

# Сетка штукатурная
FIBERGLASS_MESH = {
    'Стеклосетка Lihtar Prorab яч. 5х5мм, Китай': 2.28,
    'Стеклосетка Kronex яч. 4x4мм белая, Китай': 1.79,
    'Стеклосетка Мастер яч. 5х5мм, Беларусь': 2.64
}

# OSB
OSB_PLATE = {
    'OSB-3 9*1250*2500мм, РФ': 39.14,
    'OSB-3 9*1220*2440мм, Беларусь': 37.27,
    'OSB-3 12*1250*2500мм, РФ': 75.19,
    'OSB-3 12*1250*2500мм, Беларусь': 75.19,
    'OSB-3 18*1250*2500мм, Беларусь': 109.19,
    'OSB-3 22*1250*2500мм, Беларусь': 134.99
}

# Цены на экструзию
# EXTRUSION_PRICES = {
#     'Вид1': 11.11,
#     'Вид2': 11.11,
#     'Вид3': 11.11,
#     'Вид4': 11.11,
#     'Вид5': 11.11,
#     'Вид6': 11.11,
# }
