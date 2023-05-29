#importações para ler o arquivo excel
import pandas as pd #álias para o pandas

from selenium import webdriver #chamando navegador
from selenium.webdriver.common.by import By #chamar os elementos
from selenium.webdriver.common.keys import Keys #para digitar na web
import time
urldosite = "https://zoom.us/signin#/login"

#Ler usuário e senha na planilha
nome_do_arquivo = 'zoom.xlsx'
df = pd.read_excel(nome_do_arquivo)

for index,row in df.iterrows():
    print("Index: " + str(index) + "E email do fulano é " + row["Email"])#consigo pegar linha da planilha

#Abrir navegador no https://zoom.us/signin#/login
chrome = webdriver.Chrome(executable_path='chromedriver.exe')
chrome.get(urldosite)
time.sleep(5)

elemento_texto_email = chrome.find_element(By.XPATH, '//*[@id="email"]')
elemento_texto_senha = chrome.find_element(By.XPATH,'//*[@id="password"]')

elemento_texto_email.send_keys(row["Email"])
elemento_texto_senha.send_keys(row["Senha"])

chrome.find_element(By.XPATH, '//*[@id="js_btn_login"]').click()

time.sleep(3)
#exemplo nome da variavel.click()
chrome.quit




#Fazer Login e Senha
#Clicar em Build App
#Clicar em Create Server-to-Server OAuth



