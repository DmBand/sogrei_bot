# @dp.message_handler(commands=['admin'])
# async def admin(message: types.Message):
#     if not check_permission(message):
#         await message.answer('У Вас нет доступа к панели администратора.')
#     else:
#         admin_menu = 'Выберите операцию:\n' \
#                      '1. <code>Изменить цену</code>\n'
#         await message.answer(
#             text=admin_menu,
#             parse_mode='HTML'
#         )
#
#         @dp.message_handler(Text(equals=[
#             'Изменить цену',
#             'изменить цену'
#         ]))
#         async def change_price(message: types.Message):
#             categories = db.get_categories()
#             text = 'Выберите категорию товара:\n'
#             for position, cat in enumerate(categories):
#                 text += f'<code>{position + 1}_{cat}</code>\n'
#             await message.answer(
#                 text=text,
#                 parse_mode='HTML'
#             )