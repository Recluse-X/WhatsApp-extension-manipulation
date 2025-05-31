# WhatsApp-extension-manipulation

This is a modified version of the original project by [0x6rss](https://github.com/0x6rss/WhatsApp-extension-manipulation-PoC), licensed under the MIT License.<br>

Android malware (.apk) can be spread through a fake PDF document by manipulating the file extension in the WhatsApp application. PoC is available in this repo


https://github.com/Recluse-X/WhatsApp-extension-manipulation/.resources/Wa_P-O-C.mp4

### Step 1: First, create a free account at [ultramsg](https://user.ultramsg.com/signup.php). We will use this to manage the API

### Step 2: Click the "Add Instance" button and create a new instance. <br>
<img src=".resources/R001.jpg "/> <br>


### Step 3: Log in to your WhatsApp application using the QR code found under the instance information. <br>
<img src=".resources/R002.jpg "/> <br>

### Step 4: Configuration token and API URL
```sh
python3 wa.py -t <token> -u <api url>
```
#### Show this help message
```sh
python3 wa.py -h 
```
###  To manually input one by one, type wa.py and run.
```sh
python3 wa.py
```
```sh
python3 wa.py -n <victim number> -d <payload, script link> -f <File name you want display>
```
## Disclaimer

This software is provided "as is", without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose, and noninfringement. In no event shall the authors or copyright holders be liable for any claim, damages, or other liability, whether in an action of contract, tort, or otherwise, arising from, out of, or in connection with the software or the use or other dealings in the software.


## License

This project continues to be licensed under the [MIT License](https://github.com/0x6rss/WhatsApp-extension-manipulation-PoC/blob/main/LICENSE).

Original copyright:
© 2024 0x6rss

Modifications:
© 2025 Recluse-X

