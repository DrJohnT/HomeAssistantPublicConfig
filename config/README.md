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
* [WFH and Power Everything Off](./packages/power.yaml)
* [GeoFencing automations](./packages/geofencing.yaml)
* [Binary Sensors](./binary_sensors.yaml)
* [Custom UI Customize](./customize.yaml)
* [Custom UI Customize Global](./customize_glob.yaml)
* [Lovelace JSON](./.storage/lovelace)
* [Lovelace Resources JSON](./.storage/lovelace_resources)

## Backup routine
I have a backup routine which I outline here as it may be useful to others to follow.  

1. Take regular snapshots of the config using Home Assistant Supervisor. These snapshot TAR files are then downloaded to my desktop PC and placed in a folder within my Dropbox along with screenshots of the Lovelace UI.  I find flicking through the screenshots of the Lovelace UI is a much better aide-memoire than writing copious notes.

2. As I make changes to the config, I commit them to my GitHub private repo. This allows me to roll-back individual file changes.

3. I have a spare 64GB MicroSD card which is a replica of the live card.  So if the live card fails, I can simply swap out the broken card, put in the replica card and restore the latest snapshot and I will have a working Home Assistant installation again.  However, if this happens, I would be considering getting a solid state drive! 

