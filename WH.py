from time import sleep
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


s = Service('chrom\chromedriver.exe')
url = 'https://web.whatsapp.com'

options = webdriver.ChromeOptions()
options.add_argument('user-data-dir=C:\\Users\\qwe\\AppData\\Local\\Google\\Chrome\\User Data\\Default')
driver = webdriver.Chrome(service=s, options=options)


#Основная функция
def send_wa_msg(text):
    try:
        driver.get(url=url)
        sleep(15)
        phones = open('telefon.py', 'r')
        for phone in phones:
            driver.get(url=f'https://web.whatsapp.com/send?phone={phone}')#Загрузка ссылки с чатом
            sleep(10)
            # Отправка Сообщения
            try:
                sleep(10)
                text_box = driver.find_element(By.XPATH,
                                               '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')

                text_box.send_keys(text)
                sleep(3)
                text_box.send_keys(Keys.ENTER)
                sleep(5)
                print(f'Send message for {phone}')

            # Если номера нет в WhatsApp переходим к другому номеру и записываем в отдельный список
            except NoSuchElementException:
                driver.find_element(By.XPATH,
                                    '//*[@id="app"]/div[1]/span[2]/div[1]/span/div[1]/div/div/div/div/div[2]/div').is_enabled()
                with open('notinwhaatsapp.py', 'a') as file:
                    file.write(phone)
                print(f'this {phone}, dont work')
                continue

    except Exception as _ex:
        print(_ex)
    finally:
        driver.close()
        driver.quit()
    #
    # return 'Worl done! Thanks for using.'

def main():
    text = input('Enter the message:')
    send_wa_msg(text=text)

if __name__ == '__main__':
    main()
