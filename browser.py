from selenium import webdriver
from config import currencies, cr_roadmap
from time import sleep
from BaseAppException import BaseAppException


class ParsError(BaseAppException):
    pass


class ExecuteActionsError(BaseAppException):
    pass


class Browser:

    def __init__(self):
        """
        Инициализация и настройка робота
        :return:
        """
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option(
            "prefs",
            {"profile.default_content_setting_values.notifications": 2}
        )
        chrome_options.add_argument("start-maximized")

        try:
            self.browser = webdriver.Chrome(chrome_options=chrome_options)
        except Exception as e:
            print(e)
            print("Driver init error!\nExit.")
            exit()

    def get_currency_rate(self, key):
        """
            Возвращает список строк таблицы
        :param key:
        :return:
        """
        print(f"Open {key}...", end='')

        select = self.browser.find_element_by_id('ctl00_PageContent_CurrencySelect')
        select.send_keys(currencies[key])

        table = self.browser.find_element_by_class_name("tablels")
        t_raw_text = table.text.replace(",", ".")
        t_lines = t_raw_text.split('\n')[2:]   #

        sleep(1)
        print("SUCCESS!")

        return t_lines

    def execute_action(self, act_list):
        """
            Выполняет действия описанные в словаре

        :param act_list: список словарей с действиями и параметрами
        :return:
        """

        functions = {
            "class_name": self.browser.find_element_by_class_name,
            "link_text": self.browser.find_element_by_link_text,
            "get": self.browser.get
        }

        for action in act_list:
            try:
                elem = functions[action['func']].__call__(action['args'])
                if "click" in action.keys():
                    elem.click()
                if "delay" in action.keys():
                    sleep(action["delay"])
            except:
                raise ExecuteActionsError(f"Action '{action}' was not execute", func="execute_action")

    def get_all_currency_rate(self, currencies):
        """
         Возвращает словарь со списками строк таблиц курсов всех валют указанных в конфиге
        :param currencies:
        :return:
        """
        self.execute_action(cr_roadmap)

        tables_dict = dict()

        def format_(input_):
            out = list()
            for i in input_:
                out.append(i.split(' ')[:2])
            return out

        for key in currencies.keys():
            tables_dict.update({key: format_(self.get_currency_rate(key))})

        return tables_dict

    def __del__(self):
        """
         закрывает браузер
        :return:
        """
        print(f"{self} deleted.")
        self.browser.close()
        self.browser.quit()
