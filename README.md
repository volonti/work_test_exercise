# Test_exercise

Добрый день!

Задание выполнено 2 способами - ручным и автоматизированным тестированием.

*Шаги по выполнению задания в ручном режиме:*
- файл index.html открыт в браузере
- открыт инструмент разработчика (DevTools)
- в консоли вкладки Elements c помощью команды ctrl+F найден элемент с id=important (CSS-селектор div#important) и 
взято значение атрибута data-value
- осуществлен переход во вкладку Network
- значение атрибута data-value введено в поле ввода Important parameter на странице в браузере и нажата кнопка Submit
- в открытой вкладке Network в Headers у направленного get-запроса взято значение у хедера Secret
- осуществлен переход во вкладку Elements c помощью команды ctrl+F найден элемент с id=special (CSS-селектор div#special) и 
взято значение атрибута data-value
- открыт инструмент Postman, где направлен Post-запрос: endpoint - http://qatest.etprf.ru/api/stage2,  во вкладке params - 
в поле KEY введено secret, в поле VALUE - значение хедера Secret (либо значение можно передать параметр, добавив к endpoint ?secret=), 
во вкладке body, row выбран формат JSON и введено в поле
{"special": "значение атрибута data-value элемента с id=special"}
- итоговый ответ получен из тела ответа

*Шаги по выполнению задания в автоматическом режиме описаны в комментариях в тесте test.py*

