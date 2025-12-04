
![FlightTrackerExample](https://github.com/user-attachments/assets/e9e45469-f61e-45da-800c-ef822df8bdf8)


###STEPS FOR SETTING UP RASPBERRY PI

###add your own ClientID and Clientsecret to fetch.py if available

###Enable SPI interface n your pi
sudo raspi-config
    ###Choose Interfacing Options -> SPI -> Yes to enable SPI interface
sudo reboot

###Install spidev on your pi
sudo apt-get update
sudo apt-get install python3-spidev

###Set up virtual environment after installing project on pi
python3 -m venv venv
source venv/bin/activate

###Install staticmap package on venv
pip install staticmap

###allow venv access to system packages
    ###Navigate to venv folder
    ###find pyvenv.cfg
    ###change vvv
include-system-site-packages = false
    ###to vvv
include-system-site-packages = true
    ###save and exit

###navigate to PlaneTracker project and activate venv
source venv/bin/activate


###Clone the waveshare e-Paper driver repo
git clone https://github.com/waveshare/e-Paper


###Attempt to install waveshare driver (still in venv)
cd ~/e-Paper/RaspberryPi_JetsonNano/python
pip install -e .
    ###if this fails due to permission issues in lib/waveshare_epd.egg-info

    ###remove stale egg-info folder
sudo rm -rf ~/e-Paper/RaspberryPi_JetsonNano/python/lib/waveshare_epd.egg-info

###try install again if originally didnt work
cd ~/e-Paper/RaspberryPi_JetsonNano/python
pip install -e .

###install spidev into venv too
pip install spidev

