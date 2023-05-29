import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import openpyxl
from openpyxl import Workbook, load_workbook

nome_do_arqvuio = "zoomteste.xlsx"
urlzoom = "https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&ct=1684327852&rver=7.0.6737.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26RpsCsrfState%3d62185d90-5b52-2c65-3cf9-8c891fc7f89d&id=292841&aadredir=1&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=90015"
df = pd.read_excel(nome_do_arqvuio)

for index,row in df.iterrows():
    #print("Index: " + str(index) + "E o Email" + row["Email"])
    chrome = webdriver.Chrome()
    chrome.get(urlzoom)

    time.sleep(3)

    # texto_teste = chrome.find_element(By.XPATH, "//*[@id='app']/div/div[2]/div/div[3]/div/div/p/span").text
    # texto_teste2 = chrome.find_element(By.XPATH, "//*[@id='app']/div/div[2]/div/div[1]/form/div[3]/button[1]/span").text

           

    #df.loc[len('Email')] = texto_teste
    #df.to_excel("zoomteste1.xlsx", index=False)
    #chrome.find_element(By.XPATH, "//*[@id='onetrust-accept-btn-handler']").click()

    #time.sleep(2)

    email = chrome.find_element(By.XPATH, "//*[@id='i0116']")
    email.send_keys(row["Email"])

    chrome.find_element(By.XPATH, "//*[@id='idSIButton9']").click()

    time.sleep(3)

    senha = chrome.find_element(By.XPATH, "//*[@id='i0118']")
    senha.send_keys(row["Senha"])

    time.sleep(2)

    chrome.find_element(By.XPATH, "//*[@id='idSIButton9']").click()

    time.sleep(10)

    chrome.find_element(By.XPATH, "//*[@id='idSIButton9']").click()

    time.sleep(15)
    chrome.find_element(By.XPATH, "//*[@id='O365_MainLink_Me']/div/div[2]").click()

    time.sleep(2)
    
    texto_teste = chrome.find_element(By.XPATH, "//*[@id='mectrl_currentAccount_primary']").text
    texto_teste2 = chrome.find_element(By.XPATH, "//*[@id='mectrl_currentAccount_secondary']").text

    mail = row["Email"]
    
    planilha = load_workbook("zoomteste.xlsx")
    aba_ativa = planilha.active
    for celula in aba_ativa["A"]:
        if celula.value == mail:
            linha = celula.row
            aba_ativa[f"C{linha}"] = texto_teste
            aba_ativa[f"D{linha}"] = texto_teste2

    planilha.save("zoomteste.xlsx") 

    time.sleep(3)

    chrome.quit

