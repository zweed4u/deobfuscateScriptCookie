#!/usr/bin/python3
#In future, url discovery on product page  |  Workaround '\\' in response for jsbeautifier  |  Better parsing method
#Local library imports
import requests#,jsbeautifier

print()
print('### p a r l e y  u l t r a b o o s t : h t t p : / / w w w . a d i d a s . c o m / u s / n m d _ a s s e t s / j s o n / 3 5 1 5 6 8 4 1 2 6 5 8 . j s')  #h k x e s n e c e e f h c i p y i t v y 
print('### r 1  n m d :                       h t t p : / / w w w . a d i d a s . c o m / u s / n m d _ a s s e t s / j s o n / 3 5 1 9 8 3 2 4 8 9 6 1 . j s')
print('### b a p e  n m d :                   h t t p : / / w w w . a d i d a s . c o m / u s / n m d _ a s s e t s / j s o n / 3 5 1 9 8 3 2 4 8 9 6 . j s')    #_ _ a d i _ r t _ s t p a k a
print()

def deobfuscate(unicodeResponse):
	"""
	Not so much as to deobfuscate but rather change encoding
	:param unicodeRepsonse: unicode from response of request
	:return: concatenated string with proper cookie value
	"""
	enc = str(unicodeResponse).encode('utf_8')
	dec = enc.decode('unicode_escape')
	return 'Cookie: '+dec.split('","createCookie"]')[0].split('"')[-1]

url=input('a d i d a s  script url: ')
session=requests.session()
response = session.get(url, headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36'})

print(deobfuscate(response.text))