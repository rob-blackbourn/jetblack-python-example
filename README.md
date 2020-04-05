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

Setup the service

```bash
sudo cp -r etc /lib/systemd/system
sudo systemctl daemon-reload
```

Check the status:

```bash
systemctl status jetblack-python-example
```

Start the service

```bash
sudo systemctl start jetblack-python-example
```

Check syslog

```bash
journalctl -u jetblack-python-example
```
