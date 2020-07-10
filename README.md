# Open Street Map Buildings Parser
An Open Street Maps building parser. It downloads the building info from a latlon box and identifies the buildings types.

## Starting 🚀


### Requirements 📋

 - Python 3.
 - The Python requests library. See below.

### Setting it up 🔧

 - Install Pyhton requirements:

```
pip install -r requirements.txt
```

## Run it! ⚙️

Open the command line and go to the directory where the app is located. For the first time, run the app followed by the location box coordinates. For instance:

```
python main.py 37.1477 -3.6097 37.1647 -3.5875
```

It will download the map in JSON format and will generate the buildings_info.json with the coordinates and buildings info.

If you already executed it before, you can just run the app without any argument so that it will use the previously downloaded map file:

```
python main.py
```


## Built with 🛠️

* [Python 3](https://www.python.org/downloads/) - The aux langauge
* [Open Street Map API](https://wiki.openstreetmap.org/wiki/API_v0.6) - We used this API to retrieve the 3D buildings models

## Contribute 🖇️
Please, feel free to open any issue, Pull Request or to just fork this project.

## Author ✒️

* **Francisco J. Quero** - [FranciscoQuero](https://github.com/FranciscoQuero)

## License 📄

This project has been created under the GNU LGPL 3.0 license - see [LICENSE.md](LICENSE.md) for more details

