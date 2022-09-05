# Owings, SDEV 400 Lab 4: Weather Station

Weather Station is a Python app that displays weather data sent to DynamoDB
and images sento to S3.

The app menu interface is executed via app.py from command line within a Cloud9 IDE instance.

## Hardware & Setup

- ESP32 CAM: https://www.amazon.com/dp/B08MJJTFN9?psc=1&ref=ppx_yo2_dt_b_product_details
- FTDI Interface: https://www.amazon.com/dp/B07XF2SLQ1?psc=1&ref=ppx_yo2_dt_b_product_details
- DHT22 Sensor: https://www.amazon.com/dp/B08TGQY64D?psc=1&ref=ppx_yo2_dt_b_product_details
- Portable power source: https://www.amazon.com/dp/B08D3MBVY8?psc=1&ref=ppx_yo2_dt_b_product_details
- Install Arduino IDE: https://www.arduino.cc/en/Guide
- Setup ESP to record weather data and send to DynamoDB: https://www.youtube.com/watch?v=FIPkU-gx_kU
- Setup ESP for timelapse photos: 
https://ksummersill.medium.com/sending-temperature-and-humidity-data-to-aws-iot-core-using-esp32-and-dht22-4506e71bde25

Note if flashing the ESP32 from windows using an FTDI interface additional drivers may be needed.
Check by navigating to your device manager and then plug in your USB cable, if the driver comes 
up unrecognized you can download it here:
  	- https://ftdichip.com/drivers/vcp-drivers/


## Required Libraries
Copy contents within "Environment" folder to a new Cloud9 IDE instance.
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install required libraries.

```bash
sudo pip install logging
sudo pip install boto3
sudo pip install imageio
sudo pip install cloudpathlib
sudo pip install pillow
```

## DynamoDB setup
While still in terminal type the following to create and populate the dynamoDB.
```bash
python populate_data.py
```
Note, this step is for testing and uses older data sent from sensors. Skip this step if making your own
weather station.

## Notes
Several of the variables within app.py are tailored to a uniqe weather station AWS setup. these will need to be 
edited if creating this from scratch.

## License
[MIT](https://choosealicense.com/licenses/mit/)