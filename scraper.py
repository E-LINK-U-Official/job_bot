import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

class MotorNavegacion:
    def __init__(self):
        print("[Sistema] Iniciando motor de extracción forzada...")
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36")
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        
        self.driver = webdriver.Chrome(options=chrome_options)

    def buscar_y_extraer_web(self, url_empleo):
        try:
            self.driver.get(url_empleo)
            time.sleep(8)  # Tiempo de carga profundo para forzar el renderizado
            
            lista_enlaces = []

            # EXTRACCIÓN ULTRA-AGRESIVA PARA LINKEDIN
            if "linkedin.com" in url_empleo:
                print("[Navegador] Ejecutando barrido de hipervínculos en LinkedIn...")
                # Hacemos un scroll rápido para forzar la aparición de datos ocultos
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight/2);")
                time.sleep(3)
                
                # Buscamos absolutamente todos los enlaces que apunten a ofertas de trabajo reales
                todos_los_enlaces = self.driver.find_elements(By.TAG_NAME, "a")
                
                for el in todos_los_enlaces:
                    try:
                        link = el.get_attribute("href")
                        texto = el.text.strip()
                        
                        # Si el enlace es de un empleo real de LinkedIn y tiene texto descriptivo, lo capturamos
                        if link and "://linkedin.com" in link and len(texto) > 10:
                            # Reconstruimos una estructura limpia de título y empresa ficticia para tu filtro
                            lista_enlaces.append({
                                "titulo": f"{texto} | Verification Required",
                                "enlace": link
                            })
                    except:
                        continue

            # MÓDULO WE WORK REMOTELY
            elif "weworkremotely.com" in url_empleo:
                elementos = self.driver.find_elements(By.TAG_NAME, "li")
                for el in elementos:
                    try:
                        texto = el.text.strip().replace("\n", " | ")
                        link = el.find_element(By.TAG_NAME, "a").get_attribute("href")
                        if link and "/remote-jobs/" in link and texto:
                            lista_enlaces.append({"titulo": texto, "enlace": link})
                    except: continue

            # MÓDULO REMOTE OK
            elif "remoteok.com" in url_empleo:
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
            print(f"[Error] Fallo en el motor de barrido: {str(e)}")
            return []

    def cerrar_navegador(self):
        print("[Sistema] Apagando instancias del navegador.")
        self.driver.quit()

