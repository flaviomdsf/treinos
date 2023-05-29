import requests
import datetime
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep
navegador = webdriver.Chrome(executable_path= r"D:\Users\t_flaviomendes.JFCE\Downloads\python\chromedriver")
from selenium.webdriver.common.keys import Keys

sleep(3)

navegador.get('https://app2.pontomais.com.br/registrar-ponto')

sleep(7)

login = navegador.find_elements_by_tag_name('input')[0]
login.send_keys('04508536328')

sleep(1)

passwd = navegador.find_elements_by_tag_name('input')[1]
passwd.send_keys('flavio144F!@')

sleep(1)

passwd.send_keys(Keys.ENTER)

sleep(10)

localizacao = navegador.find_element_by_xpath('/html/body/app-root/app-side-nav-outer-toolbar/dx-drawer/div/div[2]/dx-scroll-view/div[1]/div/div[1]/div[2]/div[1]/app-container/time-card-register/div/div[2]/div[2]/pm-time-card-register/pm-card/div/div[2]/div[1]/div[2]/address-time-card-register/div[2]/p[3]/small')

sleep(2)

localizacao.click()

sleep(3)

bater = navegador.find_element_by_xpath('/html/body/app-root/app-side-nav-outer-toolbar/dx-drawer/div/div[2]/dx-scroll-view/div[1]/div/div[1]/div[2]/div[1]/app-container/time-card-register/div/div[2]/div[2]/pm-time-card-register/pm-card/div/div[2]/div[1]/div[2]/div/pm-button/button')
bater.click()


agora = datetime.datetime.now()

navegador.quit



with open('ponto.txt', 'a') as arquivo:
    arquivo.write(str(agora) + '\n')
