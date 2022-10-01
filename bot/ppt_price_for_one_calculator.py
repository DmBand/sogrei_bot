def get_price_for_one(proce_per_cubic_metr):
    ppt_price_for_one = {
        'ППТ-10-А':
            {
                '1000*500мм':
                    {
                        '2см': 0.01 * proce_per_cubic_metr['ППТ-10-А'],
                        '3см': 0.015 * proce_per_cubic_metr['ППТ-10-А'],
                        '5см': 0.025 * proce_per_cubic_metr['ППТ-10-А'],
                        '10см': 0.05 * proce_per_cubic_metr['ППТ-10-А'],
                    },
                '1000*1000мм':
                    {
                        '2см': 0.02 * proce_per_cubic_metr['ППТ-10-А'],
                        '3см': 0.03 * proce_per_cubic_metr['ППТ-10-А'],
                        '5см': 0.05 * proce_per_cubic_metr['ППТ-10-А'],
                        '10см': 0.1 * proce_per_cubic_metr['ППТ-10-А'],
                    }
            },
        'ППТ-15-А':
            {
                '1000*500мм':
                    {
                        '2см': 0.01 * proce_per_cubic_metr['ППТ-15-А'],
                        '3см': 0.015 * proce_per_cubic_metr['ППТ-15-А'],
                        '5см': 0.025 * proce_per_cubic_metr['ППТ-15-А'],
                        '7см': 0.035 * proce_per_cubic_metr['ППТ-15-А'],
                        '10см': 0.05 * proce_per_cubic_metr['ППТ-15-А'],
                    },
                '1000*1000мм':
                    {
                        '2см': 0.02 * proce_per_cubic_metr['ППТ-15-А'],
                        '3см': 0.03 * proce_per_cubic_metr['ППТ-15-А'],
                        '5см': 0.05 * proce_per_cubic_metr['ППТ-15-А'],
                        '7см': 0.07 * proce_per_cubic_metr['ППТ-15-А'],
                        '10см': 0.1 * proce_per_cubic_metr['ППТ-15-А'],
                    }
            },
        'ППТ-15-Б':
            {
                '1000*500мм':
                    {
                        '5см': 0.025 * proce_per_cubic_metr['ППТ-15-Б'],
                    },
            },
        'ППТ-20-А':
            {
                '1000*500мм':
                    {
                        '1см': 0.005 * proce_per_cubic_metr['ППТ-20-А'],
                        '2см': 0.01 * proce_per_cubic_metr['ППТ-20-А'],
                        '3см': 0.015 * proce_per_cubic_metr['ППТ-20-А'],
                        '5см': 0.025 * proce_per_cubic_metr['ППТ-20-А'],
                        '7см': 0.035 * proce_per_cubic_metr['ППТ-20-А'],
                        '10см': 0.05 * proce_per_cubic_metr['ППТ-20-А'],
                    },
                '1000*1000мм':
                    {
                        '2см': 0.02 * proce_per_cubic_metr['ППТ-20-А'],
                        '3см': 0.03 * proce_per_cubic_metr['ППТ-20-А'],
                        '5см': 0.05 * proce_per_cubic_metr['ППТ-20-А'],
                        '10см': 0.1 * proce_per_cubic_metr['ППТ-20-А'],
                    }
            },
        'ППТ-25-А':
            {
                '1000*500мм':
                    {
                        '1см': 0.005 * proce_per_cubic_metr['ППТ-25-А'],
                        '2см': 0.01 * proce_per_cubic_metr['ППТ-25-А'],
                        '3см': 0.015 * proce_per_cubic_metr['ППТ-25-А'],
                        '4см': 0.02 * proce_per_cubic_metr['ППТ-25-А'],
                        '5см': 0.025 * proce_per_cubic_metr['ППТ-25-А'],
                        '7см': 0.035 * proce_per_cubic_metr['ППТ-25-А'],
                        '8см': 0.04 * proce_per_cubic_metr['ППТ-25-А'],
                        '10см': 0.05 * proce_per_cubic_metr['ППТ-25-А'],
                    },
                '1000*1000мм':
                    {
                        '2см': 0.02 * proce_per_cubic_metr['ППТ-25-А'],
                        '3см': 0.03 * proce_per_cubic_metr['ППТ-25-А'],
                        '5см': 0.05 * proce_per_cubic_metr['ППТ-25-А'],
                        '10см': 0.1 * proce_per_cubic_metr['ППТ-25-А'],
                    }
            },
        'ППТ-25-Б':
            {
                '1000*500мм':
                    {
                        '5см': 0.025 * proce_per_cubic_metr['ППТ-25-Б'],
                    },
            },
        'ППТ-35-А':
            {
                '1000*500мм':
                    {
                        '1см': 0.005 * proce_per_cubic_metr['ППТ-35-А'],
                        '2см': 0.01 * proce_per_cubic_metr['ППТ-35-А'],
                        '3см': 0.015 * proce_per_cubic_metr['ППТ-35-А'],
                        '5см': 0.025 * proce_per_cubic_metr['ППТ-35-А'],
                        '10см': 0.05 * proce_per_cubic_metr['ППТ-35-А'],
                    },
                '1000*1000мм':
                    {
                        '2см': 0.02 * proce_per_cubic_metr['ППТ-35-А'],
                        '3см': 0.03 * proce_per_cubic_metr['ППТ-35-А'],
                        '5см': 0.05 * proce_per_cubic_metr['ППТ-35-А'],
                        '10см': 0.1 * proce_per_cubic_metr['ППТ-35-А'],
                    }
            },
    }
    return ppt_price_for_one
