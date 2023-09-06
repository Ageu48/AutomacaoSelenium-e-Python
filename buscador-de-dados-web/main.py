from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# Inicializar o webdriver
webdriver_instance = webdriver.Chrome()
webdriver_instance.implicitly_wait(10)  # Aguardar até 10 segundos por elementos

# Acessar a página de login
webdriver_instance.get('https://site/para/fazer/login')
sleep(2)

# Preencher o formulário de login
usuario = webdriver_instance.find_element(By.NAME, 'j_username')
usuario.send_keys('usuario-para-login')
senha = webdriver_instance.find_element(By.NAME, 'j_password')
senha.send_keys('senha-do-usuario')
button_login = webdriver_instance.find_element(By.CSS_SELECTOR, 'input.btn.btn-lg.btn-primary.btn-block')
button_login.click()
sleep(2)

# Ler os itens do arquivo input.txt e construir URLs
with open('input.txt', 'r') as file:
    items = file.read().splitlines()

base_url = 'https://base/da/url/do/site='
for item in items:
    target_url = base_url + item
    webdriver_instance.get(target_url)

    # Salvar o HTML da página em um arquivo de texto
    filename = f'html_{item}.txt'
    with open(filename, 'w', encoding='utf-8') as html_file:
        html_file.write(webdriver_instance.page_source)

    # Realize as operações necessárias na página
    # ...
    sleep(2)

# Fechar o navegador ao final
webdriver_instance.quit()
