from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import threading
import time

class SupremeBot(threading.Thread):

    

    def __init__(self):

        threading.Thread.__init__(self)     # per multithreading
        
        self.urlbase = 'https://www.supremenewyork.com/shop/sweatshirts/b3475hupf/k2rcjkh6o'


    def print_Cyan(self, testo): print('\033[96m {}\033[00m'.format(testo))   # per colorare testo  chiama questa funzione
    def print_Yellow(self, testo): print('\033[93m {}\033[00m'.format(testo)) 


    def configurazione(self):

        print('\nInserire il sistema operativo che si sta utilizzando (es: Windows, linux, Mac Os): \n ---> ')
        sistema_operativo = input()
        
        if 'windows' in sistema_operativo.lower():
            self.printare = print
        else :
            self.printare= self.print_Cyan
     
        if 'windows' in sistema_operativo.lower():
            self.driver = webdriver.Chrome('C:\Program Files (x86)\chromedriver.exe')
        else :
            self.driver = webdriver.Chrome('./chromedriver')


    def navigare(self):

        self.driver.get('{}'.format(self.urlbase))


    def run(self):
        
        self.printare('\nScrivere stop se si vuole interrompere: ')     # il subprocesso per stoppare il bot
        self.condizione = input().lower()

    def coppare(self):

        self.navigare()  #trova l'item

        self.condizione = 'vai'
        
        while self.condizione!='stop':          # prova a coppare

                bottone_carrello = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="add-remove-buttons"]/input')))

                if bottone_carrello.is_displayed() and bottone_carrello.is_enabled():  #verifica se il bottone è cliccabile
                    bottone_carrello.click()         # aggiunge al carrello

                bottone_checkout = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="cart"]/a[2]')))

                time.sleep(3)
                bottone_checkout.click()         # checkout
                
                bottone_accettatermini = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="cart-cc"]/fieldset/p/label/div/ins')))
                bottone_processpayment = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="pay"]/input')))
                
                time.sleep(2)
                bottone_accettatermini.click()
                bottone_processpayment.click()

                bottone_login1_pp = WebDriverWait(self.driver, 40).until(EC.presence_of_element_located((By.XPATH, '//*[@id="btnNext"]')))
                bottone_login1_pp.click()
                
                bottone_login2_pp = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="btnLogin"]')))
                bottone_login2_pp.click()

                bottone_2fa_pp = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="challenges"]/div/div[2]/button')))
                bottone_2fa_pp.click()

                # bottone_checkout_pp = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH, '')))('//*[@id="payment-submit-btn"]')
 
if __name__ == '__main__':

    ig_bot = SupremeBot()

    ig_bot.configurazione()

    ig_bot.start()

    ig_bot.coppare()