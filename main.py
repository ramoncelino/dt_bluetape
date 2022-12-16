# Importar bibliotecas
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import openpyxl
import time

# Criar lista de URLs e palavras-chave
urls = ["https://www.ofertaesperta.com/", "http://www.globo.com", "https://autoesporte.globo.com/", "https://www.escolavirtual.gov.br/curso/213", "https://www.mg.superesportes.com.br/", "https://medium.com/data-hackers/web-scraping-com-python-para-pregui%C3%A7osos-unindo-", "https://filmow.com/listas/200-filmes-obrigatorios-para-cinefilos-l56792/"]

keywords = ["carro", "política", "tecnologia", "globo", "verdade", "python", "web scraping", "auto", "sonho", "luta", "esportes", "busca"]

# Criar lista vazia para armazenar os resultados
results = []

# Configurar o Selenium para abrir o navegador
opt = webdriver.ChromeOptions()
opt.add_argument('--ignore-certificate-errors')
opt.add_argument('--ignore-ssl-errors')
opt.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=opt)


# Iterar sobre a lista de URLs
for url in urls:
    try:
        # Abrir a URL com o Selenium
        driver.get(url)
        print(url) # Apenas para Debug
        time.sleep(1) # Boa Prática

    # Obter o conteúdo da página com o Beautiful Soup
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        text = soup.get_text()
        print(1) # Apenas para Debug

    # Procurar as palavras-chave na página
        for keyword in keywords:
            if keyword in text:
                results.append((url, keyword))
        print(2) # Apenas para Debug
    except:
        print("Erro de Handshake")

# Fechar o navegador
driver.quit()

# Criar um dataframe com os resultados
df = pd.DataFrame(results, columns=['URL', 'Palavras-Chave'])
df.to_excel("Tabela.xlsx", index=False)

# Exibir o dataframe
print(df)
