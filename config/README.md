<p><img src="https://img.shields.io/badge/HA--Version-0.108.3-brightgreen.svg"/>
<img src="https://img.shields.io/badge/Supervisor-217-brightgreen.svg"/>
<img src="https://img.shields.io/badge/AppDaemon4-v0.2.3-5294E2.svg"/>
<img src="https://img.shields.io/badge/deConz-5.3.2-5294E2.svg"/>
<img src="https://img.shields.io/badge/license-MIT-yellow.svg"/>
</p>
<img align=right src="../images/ha/HAlogo.png" width="240" />

# **Dr John's Home Assistant Configuration**

As mentioned in the repo's main [README](../README.md), I run [Home Assistant Core in Docker containers](https://www.home-assistant.io/docs/installation/docker/) installed on [Raspbian Buster](https://www.raspberrypi.org/blog/buster-the-new-version-of-raspbian/) with all my add-ons and integrations also running in Docker containers.

For ease of mainteance I have divided my HA configuration into a series of packages. Essentially, [Packages](https://www.home-assistant.io/docs/configuration/packages/) in Home Assistant provide a way to bundle different elements of a component’s configuration together.  

The following Table of Contents lists where you can find the configuration of the main components.  Inside each YAML file you will find a similar Table of Contents outlining exactly what is contained therein.

**Table of Contents**
* [Humidity Controlled Fan automations](./packages/fan.yaml)
* [Logitech Harmony remote automations](./packages/harmony.yaml)
* [Drayton Wiser Heating and Hot Water automations](./packages/wiser.yaml)
* [Velux Windows and Blinds automations](./packages/velux.yaml)
* [Risco Security Alarm automations](./packages/risco.yaml)
* [Xiaomi Mi Flora configuration](./packages/miflora.yaml)
* [Phone Battery automations](./packages/battery.yaml)
* [Netgear ReadyNAS startup & shutdown automations](./packages/network.yaml)
* [Plex Media Server Configuration](./packages/plex.yaml)
* [Motion sensor automations](./packages/hall.yaml)
* [Xiaomi Aqara double light switch automations](./packages/hall.yaml)
* [GeoFencing automations](./packages/geofencing.yaml)
* [Binary Sensors](./binary_sensors.yaml)
* [Custom UI Customize](./customize.yaml)
* [Custom UI Customize Global](./customize_glob.yaml)
* [Lovelace JSON](./.storage/lovelace)
* [Lovelace Resources JSON](./.storage/lovelace_resources)

## Backup routine
I have a backup routine which I outline here as it may be useful to others to follow.  

1. At the core is taking a regular snapshot of the config using Home Assistant Supervisor. These snapshot TAR files are then downloaded to my PC and placed in a folder within my Dropbox along with screenshots of the Lovelace UI.  I find flicking through the screenshots of the Lovelace UI is a much better aide-memoire than writing copious notes.

2. As I make changes to the config, I commit them to my GitHub private repo. This allows me to roll-back individual file changes.


