# Spotify to YouTube Music Playlist Transfer

Bu proje, bir Spotify çalma listesini alıp YouTube Music hesabınıza aktarır. Selenium kütüphanesini kullanarak otomatikleştirilmiş bir süreç ile çalışır.

---

## Gereksinimler

Projenin çalışabilmesi için aşağıdaki gereksinimlerin karşılanması gerekir:

- **Python 3.x**
- **Selenium** 
- Chromium tarayıcısı ve ChromeDriver
- Python kütüphaneleri:
  - `selenium`

---

## Kurulum

1. Gerekli Python kütüphanelerini yükleyin:
   ```bash
   pip install -r requirements.txt
   ```
   
2. Chromium ve ChromeDriver'ın yüklü olduğundan emin olun.
    
3. **ChromeDriver** dosyasının sistem PATH'ine ekli olduğundan emin olun.
    
4. Projeyi bilgisayarınıza klonlayın:
    
	 ```bash
	git clone https://github.com/baverozmen/Yt_to_Sp
	cd Yt_to_Sp
	python3 start.py
	```

---
## Dosyalar

### 1. `start.py`

Bu dosya, programın ana yürütme dosyasıdır. Kullanıcıdan gerekli bilgileri alır ve aktarım sürecini başlatır.

### 2. `spotify_playlist_push.py`

Spotify'dan çalma listesi başlıklarını çeker ve bu verileri bir dosyada saklar.

### 3. `yt_pull.py`

YouTube Music'e giriş yapar ve çalma listesindeki şarkıları arayıp hesabınıza ekler.

---
## Katkıda Bulunma

Katkıda bulunmak isterseniz, projeyi fork edip geliştirmeler yapabilirsiniz. Geliştirmelerinizi göndermek için bir pull request oluşturun.



---
	
## Lisans

Bu proje, [MIT Lisansı](LICENSE) altında lisanslanmıştır.
