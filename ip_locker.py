import socket
from requests import get

hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
public_ip = get('https://geo.ipify.org/api/v2/country?apiKey=at_G7qIijjDfQoKBGMi7tP2CEHidA39V&ipAddress=8.8.8.8').text

print(f'Хост: {hostname}')
print(f'Локальный IP: {local_ip}')
print(f'Публичный IP: {public_ip}')
