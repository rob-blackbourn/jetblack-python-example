# jetblack-python-example

An example python service using systemd on ubuntu.

## Installation

First create a system user to tun the service:

```bash
sudo useradd -r -G syslog jetblack
```

Install in /opt

```bash
sudo python3.8 -m venv /opt/jetblack-python-example
sudo sh -c '. /opt/jetblack-python-example/bin/activate && pip install jetblack-python-example'
```
