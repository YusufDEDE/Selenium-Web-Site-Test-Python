from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time


driver = webdriver.Firefox()
driver.get("http://www.unclesoftware.com/")

# 1.UseCase "Kayıt olma örnek parametre =>  KayitOl("JohnWick","johnwick@hotmail.com","john123","JohnWick","5553692581")"
def KayitOl(adi,mail,sifre,kadi,tel):
    # 1. aşama
    time.sleep(5)
    signup = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/ul/li[1]/a").click()
    signup = driver.find_element_by_xpath("//*[@id='i1']")
    signup.send_keys(adi)
    signup = driver.find_element_by_xpath("//*[@id='i2']")
    signup.send_keys(mail)
    signup = driver.find_element_by_xpath("//*[@id='i3']")
    signup.send_keys(sifre)
    driver.find_element_by_xpath("/html/body/div/div/div/div/div/div/form/div[3]/a").click()
    # 2. aşama
    time.sleep(5)
    singup = driver.find_element_by_xpath("//*[@id='nick']")
    singup.send_keys(kadi)
    singup = driver.find_element_by_xpath("//*[@id='phone']")
    singup.send_keys(tel)
    driver.find_element_by_xpath("/html/body/div/div/div/div/div/div/form/div[2]/a").click()

# 2.UseCase "Giriş Yap örnek parametre => GirisYap("s2ssulos@hotmail.com","sulo123")"
def GirisYap(mail,sifre):
    time.sleep(5)
    login = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/ul/li[2]/a").click()
    login = driver.find_element_by_xpath("/html/body/div/div/div/div/div/div/form/div[2]/div[1]/div/input")
    login.send_keys(mail)
    login = driver.find_element_by_xpath("/html/body/div/div/div/div/div/div/form/div[2]/div[2]/div/input");
    login.send_keys(sifre)
    driver.find_element_by_xpath("/html/body/div/div/div/div/div/div/form/div[3]/a").click()

# 3.UseCase "Çıkış Yap fonksiyon parametre almaz."
def CikisYap():
    time.sleep(3)
    logout = driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul/li[7]/a").click()
    time.sleep(3)
    logout = driver.find_element_by_xpath("//*[@id='doLogOut']").click()

# 4.UseCase "Navigasyon bar tıkla ve ara tuşuna bas fonksiyonu"
def ilanAra():
    time.sleep(3)
    driver.find_element_by_xpath("//*[@id='search-job-btn']").click()
    time.sleep(3)
    driver.find_element_by_xpath("//*[@id='search-job-form-btn']").click()

# 5. UseCase "Kurumsal Kayıt olma"
def KurumsalKayitOl(adi,mail,sifre,kadi,tel,FirmaIsmi,Ftel,Fmail,Fweb,Faciklama):
    time.sleep(4)
    singup = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/ul/li[1]/a").click()
    time.sleep(4)
    singup = driver.find_element_by_xpath("//*[@id='signupForm']/div[2]/div[4]/label[2]").click()
    signup = driver.find_element_by_xpath("//*[@id='i1']")
    signup.send_keys(adi)
    signup = driver.find_element_by_xpath("//*[@id='i2']")
    signup.send_keys(mail)
    signup = driver.find_element_by_xpath("//*[@id='i3']")
    signup.send_keys(sifre)
    driver.find_element_by_xpath("/html/body/div/div/div/div/div/div/form/div[3]/a").click()
    # 2. aşama
    time.sleep(5)
    singup = driver.find_element_by_xpath("//*[@id='nick']")
    singup.send_keys(kadi)
    singup = driver.find_element_by_xpath("//*[@id='phoneUser']")
    singup.send_keys(tel)
    singup = driver.find_element_by_xpath("//*[@id='companyName']")
    singup.send_keys(FirmaIsmi)
    singup = driver.find_element_by_xpath("//*[@id='phoneCompany']")
    singup.send_keys(Ftel)
    singup = driver.find_element_by_xpath("//*[@id='companyDate']").click()
    time.sleep(3)
    singup = driver.find_element_by_xpath("/html/body/div[2]/div[1]/table/tbody/tr[2]/td[5]/p").click()
    singup = driver.find_element_by_xpath("//*[@id='companyMail']")
    singup.send_keys(Fmail)
    singup = driver.find_element_by_xpath("//*[@id='companyWeb']")
    singup.send_keys(Fweb)
    singup = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/form/div[1]/div[6]/div/textarea")
    singup.send_keys(Faciklama)
    driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/form/div[2]/a").click()
    # 2. aşama




# Main kısmı fonksiyon çağırma :)
# 1. UseCase
# KayitOl("JohnWick","johnwwick@hotmail.com","john123","JohwnWick","5553692581")
# CikisYap()

# 2. UseCase
GirisYap("JohnWick","john123")
# 3. UseCase
ilanAra()
# 4. UseCase
CikisYap()
# 5. UseCase
#KurumsalKayitOl(adi,mail,sifre,kadi,tel,FirmaIsmi,Ftel,Fmail,Fweb,Faciklama):
KurumsalKayitOl("josshnsCons","johssrrsn@hotmail.com","johsnrs12345","const12","5442223311","JohnsTechnology","2322221144","johntessch@tech.com","johns.com","Lorem Ipsum, dizgi ve baskı endüstrisinde kullanılan mıgır metinlerdir. Lorem Ipsum, adı bilinmeyen bir matbaacının bir hurufat numune kitabı oluşturmak üzere bir yazı galerisini alarak karıştırdığı 1500'lerden beri endüstri standardı sahte metinler olarak kullanılmıştır. Beşyüz yıl boyunca varlığını sürdürmekle kalmamış, aynı zamanda pek değişmeden elektronik dizgiye de sıçramıştır. 1960'larda Lorem Ipsum pasajları da içeren Letraset yapraklarının yayınlanması ile ve yakın zamanda Aldus PageMaker gibi Lorem Ipsum sürümleri içeren masaüstü yayıncılık yazılımları ile popüler olmuştur.")
