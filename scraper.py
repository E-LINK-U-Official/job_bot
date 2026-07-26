import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

class MotorNavegacion:
    def __init__(self):
        print("[Sistema] Iniciando motor de automatización multiplataforma real...")
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-gpu")
        # Universal human masquerade headers
        chrome_options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        self.driver = webdriver.Chrome(options=chrome_options)

    def buscar_y_extraer_web(self, url_empleo):
        try:
            self.driver.get(url_empleo)
            time.sleep(7)  # Generous load time for dynamic data layers
            lista_enlaces = []

            # ENGINE 1: LINKEDIN DETAILED EXTRACTION
            if "linkedin.com" in url_empleo:
                print("[Navegador] Extrayendo estructura de datos de LinkedIn...")
                tarjetas = self.driver.find_elements(By.XPATH, "//div[contains(@class, 'base-search-card')] | //li")
                for t in tarjetas:
                    try:
                        titulo = t.find_element(By.CLASS_NAME, "base-search-card__title").text.strip()
                        empresa = t.find_element(By.CLASS_NAME, "base-search-card__subtitle").text.strip()
                        link = t.find_element(By.TAG_NAME, "a").get_attribute("href")
                        if link and titulo and empresa:
                            lista_enlaces.append({"titulo": f"{titulo} at {empresa}", "enlace": link})
                    except: continue

            # ENGINE 2: WE WORK REMOTELY EXTRACTION
            elif "weworkremotely.com" in url_empleo:
                print("[Navegador] Extrayendo estructura de datos de WeWorkRemotely...")
                elementos = self.driver.find_elements(By.TAG_NAME, "li")
                for el in elementos:
                    try:
                        texto = el.text.strip().replace("\n", " | ")
                        link = el.find_element(By.TAG_NAME, "a").get_attribute("href")
                        if link and "/remote-jobs/" in link and texto:
                            lista_enlaces.append({"titulo": texto, "enlace": link})
                    except: continue

            # ENGINE 3: REMOTE OK EXTRACTION
            elif "remoteok.com" in url_empleo:
                print("[Navegador] Extrayendo estructura de datos de RemoteOK...")
                filas = self.driver.find_elements(By.TAG_NAME, "tr")
                for f in filas:
                    try:
                        texto = f.text.strip().replace("\n", " | ")
                        link = f.find_element(By.TAG_NAME, "a").get_attribute("href")
                        if link and texto:
                            lista_enlaces.append({"titulo": texto, "enlace": link})
                    except: continue

            return lista_enlaces
            
        except Exception as e:
            print(f"[Error] Tiempo de espera agotado en red: {str(e)}")
            return []

    def cerrar_navegador(self):
        print("[Sistema] Apagando instancias activas del navegador.")
        self.driver.quit()
