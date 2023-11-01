from selenium import webdriver

# Configurar o WebDriver (no caso do Chrome)
driver = webdriver.Chrome()

# Abrir a página da web
url = "https://echweb.autoglass.com.br/cmswebreports/Report/LayoutDinamico.aspx"
driver.get(url)

# Localizar e preencher o campo de login
driver.find_element('xpath','//*[@id="ctl00_ContentPlaceHolder1_UserNameTextBox"]').send_keys('joao.mmelo')

# Localizar e preencher o campo de senha (se necessário)
driver.find_element('xpath','//*[@id="ctl00_ContentPlaceHolder1_PasswordTextBox"]').send_keys('1234')

driver.find_element('xpath', '//*[@id="ctl00_ContentPlaceHolder1_LoginImageButton"]').click().send_keys("\n").send_keys("\n").send_keys("\n")

# Fechar o navegador quando terminar.quit()
