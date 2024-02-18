import sender_stand_request
import data

# Функция для создания копии тела запроса создания набора для того чтобы заменить параметр "name" на тестовые данные
def get_kit_body(name):
    # Создаем копию тела запроса создания набора
    current_body = data.kit_body.copy()
    # Заменяем параметр "Имя" в теле запроса создания набора на переменную "name" в копии
    current_body["name"] = name
    return current_body

# Функция для позитивной проверки
def positive_assert(name):
    # В переменную kit_body сохраняется обновленное тело запроса
    kit_body = get_kit_body(name)
    # В переменную card_response сохраняется результат запроса на создание набора
    card_response = sender_stand_request.post_new_card(kit_body)
    # Проверяется, что код ответа равен 201
    assert card_response.status_code == 201
    # Проверяется, что в ответе есть поле "name", и оно не пустое
    assert card_response.json()["name"] != ""
    # В переменную kits_table_response сохраняется результат запроса на получение данных из таблицы kit_model
    kits_table_response = sender_stand_request.get_cards()
    # Строка, которая должна быть в ответе
    str_user = str(card_response.json()['id']) + ',' + kit_body["name"] + ',,' + str(kit_body["productsCount"]) + ',,'
    # Проверка, что такой набор есть, и он единственный
    assert kits_table_response.text.count(str_user) == 1

# Функция для негативной проверки недопустимых символов
def negative_assert_symbol(name):
    # В переменную kit_body сохраняется обновленное тело запроса
    kit_body = get_kit_body(name)
    # В переменную card_response сохраняется результат запроса на создание набора
    card_response = sender_stand_request.post_new_card(kit_body)
    # Проверка, что код ответа равен 400
    assert card_response.status_code == 400
    # Проверка, что в теле ответа атрибут "code" равен 400
    assert card_response.json()["code"] == 400

# Функция для негативной проверки ввода пустых данных
def negative_assert_no_name(kit_body):
    card_response = sender_stand_request.post_new_card(kit_body)
    assert card_response.status_code == 400
    assert card_response.json()["code"] == 400

# Тест 1.
def test_1_dopustimoe_kollichestvo_simvolov_1():
    positive_assert("a")

# Тест 2.
def test_2_dopustimoe_kollichestvo_simvolov_511():
    positive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")

# Тест 3
def test_3_kolichestvo_simvolov_mensche_dopustimogo_0():
    negative_assert_symbol("")

# Тест 4
def test_4_kolichestvo_simvolov_bolsche_dopustimogo_512():
    negative_assert_symbol("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")

# Тест 5
def test_5_razrescheny_angliyskie_bukvi():
    positive_assert("QWErty")

# Тест 6
def test_6_razrescheny_russkie_bukvi():
    positive_assert("Мария")

# Тест 7
def test_7_razrescheny_specsimvoly():
    positive_assert('"№%@",')

# Тест 8
def test_8_razrescheny_probely():
    positive_assert("Человек и КО")

# Тест 9
def test_9_razrescheny_zifry():
    positive_assert("123")

# Тест 10. Ошибка, в запросе нет параметра name
def test_10_parametr_ne_peredan_v_zaprose():
    # Копируется словарь с телом запроса из файла data в переменную kit_body
    kit_body = data.kit_body.copy()
    # Удаление параметра name из запроса
    kit_body.pop("name")
    # Проверка полученного ответа
    negative_assert_no_name(kit_body)

# Тест 11. Ошибка Тип параметра name: число
def test_11_peredan_drugoy_tip_parametra_chislo():
    # В переменную kit_body сохраняется обновлённое тело запроса
    kit_body = get_kit_body(123)
    # В переменную kit_response сохраняется результат запроса на создание набора:
    kit_response = sender_stand_request.post_new_card(kit_body)
    # Проверка кода ответа
    assert kit_response.status_code == 400