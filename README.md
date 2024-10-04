# Solar-Battery-Meter-Scraper

Python based Web Scraper for Solar Battery Meter Using ESP32

### Steps

Steps for version `v0.0.2_ESP32`

- Clone [This Project](https://github.com/aruncs31s/Kannur-Solar-Battery-Monitoring-System) Which is a part of a core project

```bash
git clone https://github.com/aruncs31s/Kannur-Solar-Battery-Monitoring-System --recursive
```

- Goto the directory containing the sketch file

```bash
cd Kannur-Solar-Battery-Monitoring-System
cd src
```

- Compile and upload the sketch
  _For Arduino Cli_ Check [This](https://github.com/aruncs31s/Notes/blob/main/Coding/Embedded%20Programming/arduino_cli.md) for complete setup of `ESP32` board for `arduino-cli`

```bash
arduino-cli compile --fqbn esp32:esp32:esp32 sketch --log
arduino-cli upload --fqbn esp32:esp32:esp32 sketch --log -p /dev/ttyUSB0
```

> You might have different port for the `esp32`
> if you get some error like `permission denied` try `chown` the port

```bash
sudo chown <username>:<username> /path/to/port
```

#### Things to consider when using the `Scraper`

1. Change the url

```python
esp_url = "http://192.168.48.50/data"
# From this to configured ip
```

Check [this] out to know how to configure the `static ip ` for the `esp32`

### POC

![](./images/v0.0.2_ESP32.png?raw=true)
![](./images/v0.0.2_ESP32_2.png?raw=true)
