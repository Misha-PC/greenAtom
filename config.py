"""==================== parser ===================="""
moex_url = r"http://moex.com"
cr_roadmap = [
    {'func': "get",        'args': moex_url},
    {'func': "class_name", 'args': "js-menu-dropdown",   'click': True, 'delay': 1},
    {'func': "link_text",  'args': "Срочный рынок",      'click': True},
    {'func': "link_text",  'args': "Согласен",           'click': True, 'delay': 2},
    {'func': "link_text",  'args': "Индикативные курсы", 'click': True},
]
currencies = {
    # "CAD/RUB": "CAD/RUB - Канадский доллар к российскому рублю",
    # "CHF/RUB": "CHF/RUB - Швейцарский франк к российскому рублю",
    # "CNY/RUB": "CNY/RUB - Китайский юань к российскому рублю",
    "EUR/RUB": "EUR/RUB - Евро к российскому рублю",
    # "JPY/RUB": "JPY/RUB - Японская йена к российскому рублю",
    # "TRY/RUB": "TRY/RUB - Турецкая лира к российскому рублю",
    # "UAH/RUB": "UAH/RUB - Украинская гривна к российскому рублю",
    # "USD/CAD": "USD/CAD - Доллар США к канадскому доллару",
    # "USD/CHF": "USD/CHF - Доллар США к швейцарскому франку",
    # "USD/JPY": "USD/JPY - Доллар США к японской йене",
    # "USD/INR": "USD/INR - Индикативный курс доллара США к индийской рупии",
    "USD/RUB": "USD/RUB - Доллар США к российскому рублю",
    # "USD/TRY": "USD/TRY - Доллар США к турецкой лире",
    # "USD/UAH": "USD/UAH - Доллар США к украинской гривне",
    # "INR/RUB": "INR/RUB – Индийская рупия к российскому рублю"
}
chrome_driver_path = "chromedriver.exe"

""""==================== excel table ===================="""
column_type = {
    'date':    [1, 4],
    'finance': [2, 5],
    'num':     [7]
}
header = ["Дата", "Курс", "Изменение", "Дата", "Курс", "Изменение", "Отношение"]
file_path = "output/currencies_rate.xlsx"
sheet_name = "Sheet1"


""""==================== config ===================="""
log_ = True
cfg_path = "output/log.txt"
cfg_max_lines = 50


""""==================== mail ===================="""
sender = "misha.rus95@mail.ru"
password = "pkRHrtpEeqoVshoIPasK"
recipients = ["misha.rus.ru@gmail.com"]
admin_mails = ["misha.rus.ru@gmail.com"]
smtp_server = "smtp.mail.ru"
mail_subject = "Moex currencies rate"
