from spotify_playlist_push import FirstReq, os
from yt_pull import fonk_giris_yük

url = input("spotify playlistini giriniz: ")
yt_email = input("youtube için mailinizi giriniz: ")
yt_password = input("youtube için sifrenizi giriniz: ")

fq = FirstReq()
fq.req_spoti(url=url)
os.system("rm songs.txt")
os.system("rm sonuc-songs.txt")
sarkı_list = []
with open("son.txt", "r") as sarkılar:
    sarkı_dos = sarkılar.readlines()
    for sarkı in sarkı_dos:
        sarkı_list.append(sarkı)
    for sar in sarkı_list:
        fonk_giris_yük(yt_email, yt_password, sar)
