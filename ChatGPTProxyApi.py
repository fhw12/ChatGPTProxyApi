import requests
import json

import random
import time

class ChatGPT:
	def __init__(self):
		self.url = 'https://chatgptproxy.me/api/v1/chat'
		self.session_id = ''
		self.user_id = ''
		self.parent_id = 0

		for i in range(16):
			self.session_id += random.choice("q w e r t y u i o p a s d f g h j k l z x c v b n m".split())
			self.user_id += random.choice("q w e r t y u i o p a s d f g h j k l z x c v b n m".split())

	def question(self, text):
		conversation =  requests.post(
			f'{self.url}/conversation',
			json = {
				'data': {
					'parent_id': f'{self.parent_id}',
					'question': text,
					'session_id': self.session_id,
					'user_fake_id': self.user_id,
				}
			}
		)

		conversation = json.loads(conversation.text)
		self.parent_id = conversation['resp_data']['chat_id']

	def result(self):
		result = requests.post(
			f'{self.url}/result',
			json = {
				'data': {
					'chat_id': f'{self.parent_id}',
					'session_id': self.session_id,
					'user_fake_id': self.user_id,
				}
			}
		)

		try:
			result = json.loads(result.text)

			if result['resp_data']['status'] == 3:
				return result['resp_data']['answer']
		except:
			pass

		return ''