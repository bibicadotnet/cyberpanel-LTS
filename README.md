# CyberPanel-LTS

Web Hosting Control Panel that uses OpenLiteSpeed as the underlying Web Server.

This is a fork intended for LTS (Long Term Support), where the goal is to make it stable and bug-free.
New features are NOT a priority

DISCLAIMER: I am NOT affiliated with the cyberpanel team. I think they are doing a great job, yet I created this for my personal needs, as I only need stability and no new features.
This is STILL IN PROGRESS. Please use the official cyberpanel instead.


## Features & Services

* Different User Access Levels (via ACLs).
* Auto SSL.
* FTP Server.
* Light-weight DNS Server (PowerDNS).
* phpMyAdmin to manage DBs (MariaDB).
* Email Support (SnappyMail).
* File Manager.
* PHP Managment.
* Firewall (FirewallD & ConfigServer Firewall Integration).
* One-click Backups and Restores.

# Supported PHP Versions

* PHP 8.1
* PHP 8.0
* PHP 7.4
* PHP 7.3
* PHP 7.2


# Installation Instructions


```
sh <(curl https://raw.githubusercontent.com/tbaldur/cyberpanel-LTS/stable/cyberpanel.sh || wget -O - https://raw.githubusercontent.com/tbaldur/cyberpanel-LTS/stable/install.sh)
```

# Upgrading CyberPanel


```
sh <(curl https://raw.githubusercontent.com/tbaldur/cyberpanel-LTS/stable/preUpgrade.sh || wget -O - https://raw.githubusercontent.com/tbaldur-LTS/cyberpanel/stable/preUpgrade.sh)
```

