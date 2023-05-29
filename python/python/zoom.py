import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import openpyxl
from openpyxl import Workbook, load_workbook


nome_do_arqvuio = "zoom.xlsx"
urlzoom = "https://marketplace.zoom.us/"

df = pd.read_excel(nome_do_arqvuio)

for index,row in df.iterrows():
    #print("Index: " + str(index) + "E o Email" + row["EMAIL"])
    chrome = webdriver.Chrome()
    chrome.get(urlzoom)

    time.sleep(5)

    chrome.find_element(By.XPATH, "//*[@id='onetrust-accept-btn-handler']").click()

    time.sleep(3)

    chrome.find_element(By.XPATH, "//*[@id='app']/div/div[1]/div/div/div[2]/div[2]/button[1]").click()

    time.sleep(3)

    email = chrome.find_element(By.XPATH, "//*[@id='email']")
    senha = chrome.find_element(By.XPATH, "//*[@id='password']")

    email.send_keys(row["EMAIL"])
    senha.send_keys(row["SENHA"])

    time.sleep(2)

    senha.send_keys(Keys.ENTER)
    #chrome.find_element(By.XPATH, "//*[@id='js_btn_login']").click()

    time.sleep(15)
    
    chrome.find_element(By.XPATH, "//*[@id='app']/div/div[1]/div/div/div[2]/div[1]/button/span").click()
    
    time.sleep(5)

    chrome.get("https://marketplace.zoom.us/develop/create")
    time.sleep(3)

    #chrome.find_element(By.XPATH, "/html/body/div[3]/div[3]/ul/li[1]").click()

    time.sleep(5)

    chrome.find_element(By.XPATH, "//*[@id='app']/div/div[2]/div[1]/div[7]/div/div[3]/button").click()

    appname = chrome.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/div/div[1]/form/div/div/div[2]/div/input")
    appname.send_keys("Balcao Virtual")
    chrome.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/div/div[2]/button[1]").click()

    time.sleep(5)

    accountid = chrome.find_element(By.XPATH, "//*[@id='app']/div[2]/div/div[2]/div[2]/div[2]/div[1]/div/div/div[3]/div/span[1]").text
    clientid = chrome.find_element(By.XPATH, "//*[@id='app']/div[2]/div/div[2]/div[2]/div[2]/div[1]/div/div/div[4]/div/span[1]").text

    chrome.find_element(By.XPATH, "//*[@id='app']/div[2]/div/div[2]/div[2]/div[2]/div[1]/div/div/label/div/div/div/span/span/i/span[1]")
    clientsecret = chrome.find_element(By.XPATH, "//*[@id='app']/div[2]/div/div[2]/div[2]/div[2]/div[1]/div/div/label/div/div/div/input").text

    time.sleep(3)

    chrome.find_element(By.XPATH, "//*[@id='app']/div[2]/div/div[3]/div/div/div/div/a/button").click()

    time.sleep(5)

    companyname = chrome.find_element(By.XPATH, "//*[@id='app']/div[2]/div/div[2]/div[2]/div[2]/div[1]/div/label[1]/div/input")
    companyname.send_keys("JFCE")

    contactcname = chrome.find_element(By.XPATH, "//*[@id='app']/div[2]/div/div[2]/div[2]/div[2]/div[1]/div/label[2]/div/input")
    contactcname.send_keys("Contato DTIC")

    contactcemail = chrome.find_element(By.XPATH, "//*[@id='app']/div[2]/div/div[2]/div[2]/div[2]/div[1]/div/label[3]/div/input")
    contactcemail.send_keys("contato.dtic@jfce.jus.br")

    chrome.find_element(By.XPATH, "//*[@id='app']/div[2]/div/div[3]/div/div/div/div/a/button").click()

    time.sleep(3)

    secrettoken = chrome.find_element(By.XPATH, "//*[@id='app']/div[2]/div/div[2]/div[2]/div[2]/div[1]/div[2]/div[2]/label/div[2]/div/div/input").text
    
    verificationtoken = chrome.find_element(By.XPATH, "//*[@id='app']/div[2]/div/div[2]/div[2]/div[2]/div[1]/div[2]/div[3]/label/div[2]/div/div/input").text

    chrome.find_element(By.XPATH, "//*[@id='app']/div[2]/div/div[3]/div/div/div/div/a/button").click()

    time.sleep(3)

    chrome.find_element(By.XPATH, "//*[@id='app']/div[2]/div/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[1]/button").click()

    time.sleep(3)

    chrome.find_element(By.XPATH, "//*[@id='tab-Meeting']/div").click()

    chrome.find_element(By.XPATH, "//*[@id='pane-Meeting']/div/div[1]/label").click()
    chrome.find_element(By.XPATH, "//*[@id='pane-Meeting']/div/div[2]/label").click()
    chrome.find_element(By.XPATH, "//*[@id='pane-Meeting']/div/div[3]/label").click()
    chrome.find_element(By.XPATH, "//*[@id='pane-Meeting']/div/div[4]/label").click()
    chrome.find_element(By.XPATH, "//*[@id='pane-Meeting']/div/div[5]/label").click()
    chrome.find_element(By.XPATH, "//*[@id='pane-Meeting']/div/div[6]/label").click()
    chrome.find_element(By.XPATH, "//*[@id='pane-Meeting']/div/div[7]").click()
    chrome.find_element(By.XPATH, "//*[@id='pane-Meeting']/div/div[8]").click()
    chrome.find_element(By.XPATH, "//*[@id='pane-Meeting']/div/div[9]").click()
    chrome.find_element(By.XPATH, "//*[@id='pane-Meeting']/div/div[10]").click()
    chrome.find_element(By.XPATH, "//*[@id='pane-Meeting']/div/div[11]").click()

    chrome.find_element(By.XPATH, "//*[@id='app']/div[2]/div/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[14]/div/div[3]/div/button").click()

    chrome.find_element(By.XPATH, "//*[@id='app']/div[2]/div/div[3]/div/div/div/div/a/button").click()

    time.sleep(3)

    chrome.find_element(By.XPATH, "//*[@id='app']/div[2]/div/div[2]/div[2]/div[2]/div[1]/div/div[4]/button").click()

    time.sleep(3)

    mail = row["EMAIL"]
    
    planilha = load_workbook("zoom.xlsx")
    aba_ativa = planilha.active
    for celula in aba_ativa["C"]:
        if celula.value == mail:
            linha = celula.row
            aba_ativa[f"E{linha}"] = accountid
            aba_ativa[f"F{linha}"] = clientid
            aba_ativa[f"G{linha}"] = clientsecret
            aba_ativa[f"H{linha}"] = secrettoken
            aba_ativa[f"I{linha}"] = verificationtoken

    planilha.save("zoom.xlsx") 

    time.sleep(3)



    chrome.quit()


#Variaveis de texto
# accountid E
# clientid F
# clientsecret G
# secrettoken H
# verificationtoken I

