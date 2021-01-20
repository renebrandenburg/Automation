import requests
from bs4 import BeautifulSoup
import smtplib
import time

url = "https://www.amazon.nl/dp/B08H93ZRK9/?tag=reshift-gaming-21"

headers = {"User-Agent": "vulhier je useragent in"}

def check_avaible():
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    
    title = soup.find(id="productTitle").get_text()
    available = soup.find(id="availability").get_text()
    #  als id av
    if 'Op voorraad.' in available:
        send_mail()
        
    print(title.strip())
    print(available.strip())

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login("jouwemail@gmail.com","vulhierjeww maak hier gebruik van google app password")

    Onderwerp = "Playstion 5 weer beschikbaar!"
    Body = "Check de Amazon link https://www.amazon.nl/dp/B08H93ZRK9/?tag=reshift-gaming-21"

    msg = f"Onderwerp: {Onderwerp}\n\n{Body}"

    server.sendmail(
        "afzender@mail.com",
        "ontvanger",
        msg
    )

    print("E-mail is verzonden!")
    server.quit()


check_avaible()

while(True):
    check_avaible()
    time.sleep(60 * 60)