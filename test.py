import os
import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


def test_exercise():
    """инициализируем браузер Chrome"""
    browser = webdriver.Chrome(ChromeDriverManager().install())

    """открываем страницу в браузере"""
    browser.get("file://" + os.getcwd() + "/index.html")

    """находим элемент с id=important и забираем данные из атрибута data-value"""
    data_value = browser.find_element(By.CSS_SELECTOR, "div#important").get_attribute("data-value")

    """закрываем браузер"""
    browser.quit()

    """имитируем ввод данных в поле и нажатие кнопки посредством get запроса. В параметрах передаем значение data-value
    Ответ записываем в переменную responce_stage1"""
    responce_stage1 = requests.get(f"http://qatest.etprf.ru/api/stage1", params={"important": data_value})

    """проверяем, что получили успешный статус ответа от сервера"""
    assert responce_stage1.status_code == 200

    """из Headers забираем значение хедера Secret и записываем его в переменную secret_value"""
    secret_value = responce_stage1.headers["Secret"]

    """из json ответа сервера забираем значение ключа special и записываем его в переменную data_value_special"""
    data_value_special = responce_stage1.json()["special"]

    """отправляем post запрос, передавая в параметрах secret со значением переменной secret_value, а также json 
    в теле запроса с полем special и значением переменной data-value_special"""
    responce_stage2 = requests.post(f"http://qatest.etprf.ru/api/stage2",
                                    params={"secret": secret_value}, json={"special": data_value_special})

    """проверяем, что получили успешный статус ответа от сервера"""
    assert responce_stage2.status_code == 200

    """выводим текст из полученного ответа с финальным результатом"""
    print(responce_stage2.text)
