from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time

options = Options()
options.binary_location = "/usr/bin/chromium-browser"
options.add_argument(
    "user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
)
options.add_argument("--ignore-certificate-errors")
options.add_argument("--disable-web-security")
options.add_argument("--allow-running-insecure-content")
driver = webdriver.Chrome(options=options)

def fonk_giris_yük(email, password, sarkı):
    yt_giris = driver.get(
        "https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Den%26next%3Dhttps%253A%252F%252Fmusic.youtube.com%252F%26feature%3D__FEATURE__&hl=en&ifkv=AcMMx-fUscfrZM4z9DA4p-WK_RYvS_Yv9TF9OI8mz2TLOJfrvaBxMFikNsiExougP17IRnwnAMeTUA&ltmpl=music&passive=true&service=youtube&uilel=3&flowName=GlifWebSignIn&flowEntry=ServiceLogin&dsh=S-1776909017%3A1732985425711111&ddm=1"
    )

    eposta = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[2]/div/div/div[1]/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input"))
    )
    eposta.send_keys(email)

    button1 = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[3]/div/div[1]/div/div/button"))
    )
    button1.click()
    time.sleep(4)

    google_sifre = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[2]/div/div/div/form/span/section[2]/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input")
    google_sifre.send_keys(password)
    button_sifre = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[3]/div/div[1]/div/div/button")
    button_sifre.click()
    time.sleep(4)
    driver.maximize_window()

    wait = WebDriverWait(driver, 30)
    inp = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "/html/body/ytmusic-app/ytmusic-app-layout/ytmusic-nav-bar/div[2]/ytmusic-search-box/div/div[1]/input",
            )
        )
    )
    inp.send_keys(sarkı)

    wait2 = WebDriverWait(driver, 30)
    butn = wait2.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "/html/body/ytmusic-app/ytmusic-app-layout/ytmusic-nav-bar/div[2]/ytmusic-search-box/div/div[2]/ytmusic-search-suggestions-section[1]/div/ytmusic-search-suggestion[1]",
            )
        )
    )
    ActionChains(driver).move_to_element(butn).click().perform()
    save = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "/html/body/ytmusic-app/ytmusic-app-layout/div[5]/ytmusic-search-page/ytmusic-tabbed-search-results-renderer/div[2]/ytmusic-section-list-renderer/div[2]/ytmusic-card-shelf-renderer/div/div[2]/div[1]/div/div[2]/div[2]/yt-button-renderer[2]/yt-button-shape/button/yt-touch-feedback-shape/div",
            )
        )
    )
    ActionChains(driver).move_to_element(save).click().perform()

