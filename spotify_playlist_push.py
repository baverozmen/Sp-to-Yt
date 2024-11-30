from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import os

options = Options()
options.binary_location = "/usr/bin/chromium-browser"
options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
)
options.add_argument("--ignore-certificate-errors")
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

class FirstReq:
    def __init__(self, elements=None, serch_spoti_list=None):
        self.elements = elements
        self.serch_spoti_list = serch_spoti_list

    def req_spoti(self, url):
        driver.get(url)
        print(f"spoti sayfası başlığı: {driver.title}")
        self.elements = driver.find_elements(
            By.XPATH,
            "//*[@id='main']/div/div[2]/div[4]/div/div[2]/div[2]/div/main/section/div[2]/div[3]/div/div[1]/div[2]/div[2]",
        )

        for element in self.elements:
            with open("songs.txt", "w") as new_file:
                new_file.writelines(element.text)

        with open("songs.txt", "r") as dosya:
            lines = dosya.readlines()
        song_titles = []
        son_song = []
        for i, line in enumerate(lines):
            line = line.strip()
            if ":" not in line and not any(char.isdigit() for char in line) and line != "E":
                song_titles.append(line)
            else:
                continue

        with open("sonuc-songs.txt", "w") as sonuc_dosya:
            for title in song_titles:
                sonuc_dosya.write(title + "\n")
        with open("sonuc-songs.txt", "r") as dosya:
            line2 = dosya.readlines()
        for ixs, line2 in enumerate(line2):
            line2 = line2.strip()
            if (ixs + 1) % 2 != 0:
                son_song.append(line2)
                with open("son.txt", "w") as sn:
                    for newo in son_song:
                        sn.writelines(newo + "\n")
            else:
                continue
