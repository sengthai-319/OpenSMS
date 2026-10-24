<p align="center"><img width="20%" src="app/data/images/favicont512.png" /></p>

# 📨 OpenSMS
An open-source solution to host a `SMS` API server locally.

### 🤔 Why would you choose our app? (Features)
👉 Turns your `Android` phone into a SMS API server. <br>
👉 Works with an `iPhone` too, through a Mac (see [Using an iPhone](#-using-an-iphone-via-a-mac)). <br>
👉 Open-source, No advertisements and privacy focused.

## 💰 Sponsor Me
You can buy me a coffee via [this link](https://www.paypal.com/paypalme/soomnathsdas) or tap on below image. Thank you 🙏. <br>
<a href="https://www.paypal.com/paypalme/soomnathsdas"><img src="./docs/images/donate.svg" height="40"></a>

## 📽️ Demo
You can click on the below Image or this [Youtube Link](https://www.youtube.com/watch?v=wNXH_3onjfg) to see the demo. Please let me know in the comments, how do you feel about this App. <br>

<a href="https://www.youtube.com/watch?v=wNXH_3onjfg"><img src="docs/images/OpenSmsThumb.webp" width="70%"></a>

## 🧑‍💻 Quickstart Guide

### 📱 Download & Run the Android App
1. You can check the [Releases](https://github.com/daslearning-org/OpenSMS/releases) and downlaod the latest version of the android app on your phone.
2. You may need to disable (temporarily) `Play Protect` from your `Play Store` settings.
3. Install the App & launch.
4. Grant the permissions.
5. Android might block `sms` permission. Go to `Settings` > `Apps` > `OpenSMS` > Tap on three vertical-dots at top-right corner > `Allow restricted access`.
6. Then grant `SMS` permission from the settings window.
7. Relaunch the app. 
8. Click `Start Server`. It will then prompt you to generate an API Key for the first time. Generate and store it securely.

### 🍎 Using an iPhone (via a Mac)
iOS does not let apps send SMS silently or keep a server running in the background, so OpenSMS can't run on the iPhone itself. Instead, run OpenSMS on a Mac: it sends each message through the `Messages` app, and your iPhone delivers it as a regular SMS using `Text Message Forwarding`.

1. Sign in to the same Apple Account on your iPhone and Mac, in `Messages` on both.
2. On the iPhone, go to `Settings` > `Apps` > `Messages` > `Text Message Forwarding` and turn on your Mac. (On older iOS: `Settings` > `Messages` > `Text Message Forwarding`.)
3. On the Mac, open `Messages` and send one SMS by hand to make sure forwarding works.
4. Install and run the app on the Mac:
    ```bash
    git clone https://github.com/daslearning-org/OpenSMS.git
    cd OpenSMS/app
    python3 -m venv .env
    source .env/bin/activate
    pip install -r requirements.txt
    python main.py
    ```
5. Click `Start Server` and generate an API key.
6. When you send the first SMS, macOS will ask to let `Terminal` (or Python) control `Messages`. Click `Allow`. If you dismissed the prompt, enable it under `System Settings` > `Privacy & Security` > `Automation`.
7. Keep the Mac awake (for example `caffeinate -i python main.py`), and keep the iPhone on the same Apple Account with a cellular signal.

> Note: `"stat": true` means `Messages` accepted the message. Delivery is then handled by the iPhone. If the iPhone is off or out of range, the message waits in `Messages` on the Mac.

### 🧪 Test API endpoint
Find the network address of your device and you may test out the API. Sample given below.

```bash
curl -i -X POST 'http://127.0.0.1:9292/sms/' \
    -H 'Content-Type: application/json' \
    -H 'Authorization: Bearer my-secret-api-key' \
    -d '{"number": "+1234567890", "text": "Hello from OpenSMS API!"}'
```

## 📚 Tech Stack Used

### Python stack
It works on `Android` and will bring this to `Linux` & `Windows` too.
- [FastAPI](https://github.com/fastapi/fastapi) for the API layer.
- [KivyMD](https://github.com/kivymd/kivymd) and few [Kivy](https://github.com/kivy) components for the UI and building the app.

### 📋 Future plans

1. Bring this SMS API option to Desktop platforms. We will leverage [Quectel EC200U](https://www.quectel.com/product/lte-ec200u-series/) based USB development boards to send SMS.

-----

## 🧩 Building your app from code

### 📱 Build Android App
A Linux environment is recommended for the app development. If you are on Windows, you may use `WSL` or any `Virtual Machine`.

```bash
# add the python repository (Optional: if you want some other versions)
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update

# install all dependencies.
sudo apt install -y ant autoconf automake ccache cmake g++ gcc lbzip2 libffi-dev libltdl-dev libtool libssl-dev make openjdk-17-jdk patch patchelf pkg-config unzip wget zip git python3 python3-venv python3-dev libcairo2-dev pkg-config libjpeg-dev zlib1g-dev

# optionally you may check the java installation with below commands
java -version
javac -version

# install python modules
git clone https://github.com/daslearning-org/OpenSMS.git
cd OpenSMS/app
python3 -m venv .env # create python virtual environment
source .env/bin/activate
pip install -r req_android.txt

# build the android apk
buildozer android debug # this may take a good amount of time for the first time & will generate the apk in the bin directory
```

-----

### Linux Dependencies for build
```bash
sudo apt install libcairo2-dev pkg-config python3-dev
sudo apt-get install libjpeg-dev zlib1g-dev
```
