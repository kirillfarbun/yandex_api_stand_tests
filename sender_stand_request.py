import configuration
import requests
import data

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,  # тут тело
                         headers=data.headers)  # а здесь заголовки

response = post_new_user(data.user_body)
print(response.status_code)
print(response.json())

authToken = response.json()['authToken']

def get_users_table():
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)

response = get_users_table()
# print(response.text)
print(response.status_code)


def post_new_card(body):
    data.headers_kits["Authorization"] = data.headers_kits["Authorization"] + authToken
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_KITS,
                        json = body,  # тут тело
                        headers = data.headers_kits)  # а здесь заголовки

response = post_new_card(data.kit_body)
print(response.status_code)
print(response.json())

def get_cards():
    data.headers_get_kits["Authorization"] = data.headers_get_kits["Authorization"] + authToken
    return requests.get(configuration.URL_SERVICE + configuration.GET_USER_KITS,
                        headers = data.headers_get_kits)  # а здесь заголовки)

response = get_cards()
print(response.text)
print(response.status_code)
