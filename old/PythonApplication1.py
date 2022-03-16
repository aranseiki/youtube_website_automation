import pdb
from time import sleep
# from functions_utils import *
#from selenium_functions import *


abrir_navegador( 'chrome', url='https://youtube.com/' )

pesquisar('Aula de Chinês')

filtrar_pesquisa(tipo = 'canal')
sleep(5)
filtrar_pesquisa(ordenar_por = 'classificacao')

if expandir_menu_filtros:
    recolher_menu_filtros()


#clicar_por_texto('Aula de Chinês')


#pdb.set_trace()

#concordar_com_os_termos('sim')


#botaoLogin = '//html/body/div[1]/div[2]/div[3]/ul/li[6]/a'
