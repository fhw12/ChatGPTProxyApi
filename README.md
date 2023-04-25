# ChatGPTProxyApi

![screenshot](screen.png)

Взаимодействуйте с [ChatGPTProxy](https://chatgptproxy.me/) через Python3

Класс ChatGPT предназначен для взаимодействия с ChatGPTProxy через API.
Метод **question** отправляет вопрос ChatGPTProxy через API. Метод принимает в качестве аргумента строку, представляющую вопрос пользователя.
Метод **result** отправляет запрос к ChatGPTProxy, метод возвращает ответ в виде строки. Если произошла ошибка или ответ от чат-бота не был получен, метод возвращает пустую строку.

 ```
import time
import ChatGPTProxyApi

def input_msg(chat):
	value = input("> ")
	if value == ':q':
		exit()
	else:
		chat.question(value)

chat = ChatGPTProxyApi.ChatGPT()
input_msg(chat)

while True:
	time.sleep(0.5)
	result = chat.result()

	if len(result) > 0:
		print(f"\x1b[38;2;255;255;150m{result}\x1b[0m\n")
		input_msg(chat)
 ```