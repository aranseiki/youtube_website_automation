from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common import desired_capabilities
from selenium.webdriver.firefox import options
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.action_chains import ActionChains
# from os import error

def Firefox():
    firefox = webdriver.Firefox( keep_alive = True, desired_capabilities = {"platformName": "windows"} )
    return firefox


def Edge():
    edge = webdriver.Edge( keep_alive = True, desired_capabilities = {"platformName": "windows"} )
    return edge


def Chrome():
    options = webdriver.ChromeOptions
    options.binary_location = "C:\Program Files\Google\Chrome\Application\chrome.exe"
    chrome = webdriver.Chrome( keep_alive = True, desired_capabilities = {"platformName" : "windows"})
    return chrome


def abrir_navegador( nome_navegador, url ):
    global navegador
    if nome_navegador.upper() == 'CHROME':
        navegador = Chrome
    if nome_navegador.upper() == 'EDGE':
        navegador = Edge()
    elif nome_navegador.upper() == 'FIREFOX':
        navegador = Firefox()
    else:
        print (f' {nome_navegador} não disponível. Escolha uma das seguintes opções: Chrome, Edge, Firefox.')
        print ('Como padrão será aberto o Edge. ')
        navegador = Chrome()
    
    navegador.get (url)
    return navegador
    

def pesquisar(texto_pesquisa):
    input_pesquisa = navegador.find_element_by_xpath('//input[contains(@id, "search")]')
    input_pesquisa.clear()
    input_pesquisa.send_keys(texto_pesquisa)
    button_pesquisa = navegador.find_element_by_xpath('//ytd-masthead/div[3]/div[2]/ytd-searchbox/button/yt-icon')
    button_pesquisa.click()


def clicar_por_texto(texto):
    elemento = navegador.find_element_by_xpath('div < yt-formatted-string[contains(text(), texto)]')
    elemento.click()

abrir_navegador( 'chrome', url='https://youtube.com/' )

sleep(5)

pesquisar('Aula de Chinês')

filtrar_pesquisa(tipo = 'canal')
sleep(5)
filtrar_pesquisa(ordenar_por = 'classificacao')