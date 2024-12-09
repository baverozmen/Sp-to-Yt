# Spotify to YouTube Music Playlist Transfer

This project takes a Spotify playlist and transfers it to your YouTube Music account using an automated process powered by Selenium.


---

## Requirements


To run the project, the following requirements must be met:

- **Python 3.x**
- **Selenium** 
- Chromium browser and ChromeDriver
- Python libraries:
  - `selenium`

---

## Installation

1. Install the required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```
   
2. Ensure Chromium and ChromeDriver are installed on your system.
    
3. Make sure the **ChromeDriver** file is added to your system PATH.

4. Clone the project to your computer:
    
	 ```bash
	git clone https://github.com/baverozmen/Yt_to_Sp
	cd Yt_to_Sp
	python3 start.py
	```

---
## Files

### 1. `start.py`

This file is the main execution file of the program. It collects the necessary information from the user and starts the transfer process.

### 2. `spotify_playlist_push.py`

This file fetches playlist titles from Spotify and saves them to a file.

### 3. `yt_pull.py`

This file logs into YouTube Music, searches for songs from the playlist, and adds them to your account.

---
## Contribution

If you'd like to contribute, you can fork the project and make improvements. Create a pull request to submit your enhancements.




---
	
## Lisans

This project is licensed under the [MIT Lisansı](LICENSE)
