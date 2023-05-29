# coding: utf-8

from lib2to3.pgen2 import driver
from tkinter import N
from urllib import response
import attrs
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from asyncio import _enter_task
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pyautogui as py
import pyperclip
navegador = webdriver.Chrome(executable_path= r"D:\Users\t_flaviomendes.JFCE\Downloads\python\chromedriver")

#utilizando o selenium para recuperar a paginaweb
#navegador = webdriver.Chrome(options=options)

sleep(3)

navegador.get('https://app2.pontomais.com.br/')

sleep(5)

login = navegador.find_element(By.XPATH, '//*[contains(concat( " ", @class, " " ), concat( " ", "col-xs-18", " " )) and (((count(preceding-sibling::*) + 1) = 1) and parent::*)]//*[contains(concat( " ", @class, " " ), concat( " ", "form-control", " " ))]')
login.send_keys('04508536328')

passwd = navegador.find_element(By.XPATH, '//*[contains(concat( " ", @class, " " ), concat( " ", "password-field", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "form-control", " " ))]')
passwd.send_keys('flavio144F!@')
sleep(3)
passwd.send_keys(Keys.ENTER)

sleep(20)

btp_editar = navegador.find_element(By.XPATH, '//*[contains(concat( " ", @class, " " ), concat( " ", "pm-secondary", " " ))]')
btp_editar.click()

sleep(10)

btp_jfce = navegador.find_element(By.XPATH, '/html/body/ngb-modal-window/div/div/pm-time-card-drawer/drawer/div[2]/div/div[2]/div[1]/div')
btp_jfce.click()

sleep(7)

btp_bater = navegador.find_element(By.XPATH, '/html/body/app-root/app-side-nav-outer-toolbar/dx-drawer/div/div[2]/dx-scroll-view/div[1]/div/div[1]/div[2]/div[1]/app-container/time-card-register/div/div[2]/div[2]/pm-time-card-register/pm-card/div/div[2]/div[1]/div[2]/div/pm-button/button')
btp_bater.click()

sleep (10)
