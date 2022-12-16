# Importar Bibliotecas
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import openpyxl
import time

# Criação da Lista de URLs e Palavras-Chave
urls = ["https://www.ofertaesperta.com/", "http://www.globo.com", "https://autoesporte.globo.com/", "https://www.escolavirtual.gov.br/curso/213", "https://www.mg.superesportes.com.br/", "https://medium.com/data-hackers/web-scraping-com-python-para-pregui%C3%A7osos-unindo-", "https://filmow.com/listas/200-filmes-obrigatorios-para-cinefilos-l56792/"]

keywords = ["carro", "política", "tecnologia", "globo", "verdade", "python", "web scraping", "auto", "sonho", "luta", "esportes", "busca"]

# Importar Bibliotecas
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import openpyxl
import time

# Criação da Lista de URLs e Palavras-Chave
urls = ["https://www.ofertaesperta.com/", "http://www.globo.com", "https://autoesporte.globo.com/", "https://www.escolavirtual.gov.br/curso/213", "https://www.mg.superesportes.com.br/", "https://medium.com/data-hackers/web-scraping-com-python-para-pregui%C3%A7osos-unindo-", "https://filmow.com/listas/200-filmes-obrigatorios-para-cinefilos-l56792/"]

keywords = ["carro", "política", "tecnologia", "globo", "verdade", "python", "web scraping", "auto", "sonho", "luta", "esportes", "busca"]

# lista vazia para Armazenamento de resultados
results = []

# Configuração da Automatização com o Selenium para abrir o Navegador
opt = webdriver.ChromeOptions()
opt.add_argument('--ignore-certificate-errors')
opt.add_argument('--ignore-ssl-errors')
opt.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=opt)

# Iterar sobre a lista de URLs
for url in urls:
    try: # Utilização de try except como boa prática para evitar que o programa falhe em caso de problemas de conexão ou outros erros inesperados
        driver.get(url) # Abrir a URL com o Selenium
        time.sleep(1) # Boa Prática adicionar um pequeno tempo de espera antes de acessar cada URL, para evitar sobrecarregar os servidores do site.

    # Obter o conteúdo da página com o Beautiful Soup
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        text = soup.get_text()

    # Buscar as Palavras-Chave na página
        for keyword in keywords:
            if keyword in text:
                results.append((url, keyword))
    except:
        print("Erro de Handshake")

driver.quit() # Fechar o Navegador

# Criar um Dataframe com os Resultados
df = pd.DataFrame(results, columns=['URL', 'Palavras-Chave'])
df.to_excel("Tabela.xlsx", index=False)
print(df)
