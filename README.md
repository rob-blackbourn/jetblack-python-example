# python-example

An example python service using systemd on ubuntu.

## Installation

First create a system user to tun the service:

```bash
sudo useradd --system jetblack
```

Install in /opt

```bash
sudo python3.8 -m venv /opt/python-example
sudo chown -R $(id -un).$(id -gn) /opt/python-example
. /opt/python-example/bin/activate
pip install python-example
sudo chown -R $(id -un).$(id -gn) /opt/python-example
sudo sh -c '. /opt/python-example/bin/activate && pip install jetblack-python-example'