import requests 

res = requests.get('http://automatetheboringstuff.com/files/rj.txt')
res.status_code

res.raise_for_status()
print(res.text[:500])

playFile = open('RomeoAndJulia.txt', 'wb')

for chunk in res.iter_content(100000):
    playFile.write(chunk)

playFile.close()