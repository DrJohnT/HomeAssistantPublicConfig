<style type="text/css">
.tg
.tg td{font-size:14px;padding:10px 5px;overflow:hidden;word-break:normal;}
.tg th{font-size:30px;font-weight:bold;}
.tg .tg-la{text-align:left;vertical-align:bottom}
.tg .tg-ra{text-align:right;vertical-align:bottom}
</style>
<table width="100%" class="tg">
  <tr>
    <th class="tg-la">Dr John's Home Assistant Configuration</th>
    <th class="tg-ra"><img src="./images/ha/HAlogo.png" width="240" /></th>
  </tr>
</table>

Home Assistant has made numerous improvements to the way we live, making our lives easier in many ways.  This repo is dedicated to the hard work of those who have put their heart and sole into this product and this community.

Below I list the components, how they are used and why.  However, all that is a little cold if you don't know the benefits Home Assistant can bring.  So in each section I try to highlight the key problems, the solutions and key benefits.

# Climate Control
| Velux Windows | Velux Blinds | Velux Active CO<sub>2</sub> Sensor | Velux Active Gateway |   
| --- | --- | --- | --- |
| <img src="./images/velux/velux_integra.png" width="200"/> | <img src="./images/velux/velux_integra_blind.jpg" width="200"/> | <img src="./images/velux/velux-active-netatmo-indoor-climate-sensor.jpg" width="200"/>  | <img src="./images/velux/veluxGateway.jfif" width="200"/> |

When I extended the apartment some years ago, I had five [Velux Integra](https://www.velux.co.uk/products/roof-windows/integra) roof windows installed, each with their own blackout blind.  Although Velux provide a remote control device, they use the [IO-Homecontrol](http://www.io-homecontrol.com/) protocol for which there is no direct interface.  After doing much research, I found an integration root: [Velux Active](https://www.velux.co.uk/products/smart-home/velux-active) works with Apple HomeKit which is a [zeroconf Home Assistant](https://www.home-assistant.io/integrations/zeroconf/) integration!  Now all five windows and five blinds can be controlled by Home Assistant along with the  [Velux Active](https://www.velux.co.uk/products/smart-home/velux-active) temperature / CO<sub>2</sub> sensors.

Note that [Velux Active](https://www.velux.co.uk/products/smart-home/velux-active) is touted as indoor climate control system which will keep your home fresh by period ventilation.  This marketing speak equates to the system opening and closing your windows at random throughout the day, regardless of the outdoor temperature.  Very unwelcome in the winter!  The first thing I did was switch off all automations in the Velux app and implemented proper automations in Home Assistant.

One benefit of [Velux Active](https://www.velux.co.uk/products/smart-home/velux-active) is that it comes with a CO<sub>2</sub> sensor which also operates as a remote control for the windows in the same room.  I now have an automation which opens the kitchen window when the CO<sub>2</sub> level reaches over 1250ppm or if either gets to hot, both of which often occur during cooking.

| Drayton Wiser Multiroom Kit 2 | Drayton Wiser TRVs | Drayton Wiser Roomstat | Central Heating & Hot Water System (2-Channel) |
| --- | --- | --- | --- | 
| <img src="./images/wiser/wiser_kit2.jpg" width="200"/> | <img src="./images/wiser/drayton-wiser-trv.png" width="200"/> | <img src="./images/wiser/drayton_wiser_roomstat.jpg" width="200"/> | <img src="./images/wiser/electric-boilers-for-heating-and-hot-water.jpg" width="200"/> |

Like most homes the heating was either all or nothing. That is, once the boiler is on, then all the radiators get hot regardless.  Obviously thermostatic radiator valves can reduce the temperature in certain rooms, but that does not cater for the following senarios: 
<ul>
<li>When working from home, I want to switch off all the radiators in the rest of the home.</li>
<li>When my partner is home alone, only the bedroom needs heating, so switch off all the radiators in the rest of the home</li>
<li>When the family is about, I want the whole home heated</li>
</ul>

I found that I was constantly walking around the flat turning the radiator valves on and off manually.  Clearly I neede remote controlled thermostatic values on each radiator which would allow me to set the temperature of each room individually.

I posted my requirements on the [community forum](https://community.home-assistant.io/t/167409/) so others could make suggestions.  Fortunately I came across the excellent Wiser Heat Hub integration for Home Assistant by @Angelo_Santagata and team is available on HACS as the *Wiser Heating Component for Home Assistant*

I now have heating which adapts to where we are and what we are doing
Room by room heating control

# Audio / Visual
Years ago, I was a serious Hi-Fi buff and this reflects in my choise of audio components found around the apartment.  Originally, I had a Logitech Squeezebox Touch in every room streaming music from a central Logitech Music Server (LMS).  Unfortunately, these units were discontinued by Logitech years ago and with the advent of high-quality streaming services such as Tidal, I was in dire need of a technology refresh. So I purchased a couple of Chromecast Audio devices and was amazed to find just how good they were!  Firstly, they have a *full dynamic range* mode so that they are able to drive my stereo system to an acceptable level.  Also, to my surprise they have a *group* mode so that the same music can be streamed to several rooms (i.e. multiroom).  After a few months of running both systems in parallel I found I hardly used Logitech system anymore as streaming Tidal to Chromecast Audio was so, so convenient.  So the Logitech units were sold and my use of Plex expanded to encompass my own music collection.  I always had a love/hate relationship with the Logitech Music Server (LMS), so I was very glad to see it go!
 
## Lounge AV
| EPOS M16i Speakers | Audiolab CDQ / Amp | Chromecast Audio | Logitech Harmony Hub | 
| --- | --- | --- | --- |
| <img src="./images/av/epos_m16i.jpg" width="200"/> | <img src="./images/av/audiolab_8200cdq.jpg" width="200"/> | <img src="./images/google/google_chromecast_audio.png" width="200"/> | <img src="./images/av/harmony-companion-remote-hub.png" width="200"/> |  

| Samsung 55" Smart TV |  Streaming Services | Humax 1100S Freesat PVR | Samsung Blu-Ray Player |
| --- | --- | --- | --- |
| <img src="./images/av/Samsung_Smart_TV_F8000.jpg" width="200"/> | <img src="./images/av/streaming_services.png" width="200"/> | <img src="./images/av/humax_hdr-1100s.png" width="200"/> |  <img src="./images/av/samsung-blu-ray-player-bd-h6500.webp" width="200"/> |  

My lounge AV is built around my aging stereo system.  Fortunately the Audiolab CDQ has multiple digital inputs which allow it to be my *AV receiver*.  Although the Audiolab units do have a IR remote control they only have a manual power button.  The Logitech Harmony Hub Companion was a godsend, but it only solved some of the problems.  Obviously it did not power on the Audiolab units, but worse did not change the TV input correctly when changing source.  

## Multiroom Audio
| Q Acoustic 2020i Speakers | Pro-Ject Stereo Box S2 | Google Chromecast Audio | Logitech Harmony Hub |
| --- | --- | --- | --- |
| <img src="./images/av/q_acoustic-qa2020i.jpg" width="200"/> | <img src="./images/av/Pro-Ject_Stereo-Box-S_02.jpg" width="200"/> | <img src="./images/google/google_chromecast_audio.png" width="200"/> |  <img src="./images/av/logitech-harmony-hub.jpg" width="200"/> |  

In addition to the lounge, all other rooms have a set-up built around the dimunuative Pro-Ject Audio Stereo Box S2, a pair of Q Acoustic 2020i speakers and a Google Chromecast Audio.  Each have a Logitech Harmony Hub which allow me (via Home Assistant) to control the multiroom audio throughout the home.  So guests can stream their own music to the room they are in, or I can stream the same music to every room.  All very convenient.

The master bedroom has the above setup plus another Samsung Smart TV and Google Chromecast device for video streaming.  The guest room simply has a LG TV with Google Chromecast.


## Network Infrastructure
| Netgear ReadyNAS | Netgear Wireless AP | Netgear 16-Port Switch | Netgear 5-port Switch | Virgin Hub 3.0 | 
| --- | --- | --- | --- | --- |
| <img src="./images/netgear/Netgear_ReadyNAS_RN212.jpg" width="200"/> | <img src="./images/netgear/netgear-wndr3700v4.png" height="200"/>  | <img src="./images/netgear/Netgear-ProSafe-Switch-16-port.jpg" width="200"/> | <img src="./images/netgear/netgear-gs105e.png" width="200"/> |  <img src="./images/netgear/virgin-hub3.jpg" width="200"/> |

I had Cat6 cabling installed throughout the apartment when I had it renovated and extended.  The network cupboard nestles under the eaves of the building and contains a 16-port Ethernet switch, the Netgear ReadyNAS which runs [Plex media server](https://www.plex.tv/), the [Velux Active](https://www.velux.co.uk/products/smart-home/velux-active) gateway and the unused [HD HomeRun](https://www.silicondust.com/).  Fortunately, I had the foresight to have both standard telephone cable and three coaxial cables run into the network cupboard from the outside.  This proved very useful when I switched broadband providers as it gave me the option to use Virgin Media cable modem service.  The Virgin Hub 3.0 is not the best, but it is provided free of charge and gave me the chance to repurpose my old Netgear router as a wireless access point in the kitchen.

## Lighting
| LED Strip Light Controllers | SmartThings Smart Plugs | Xiaomi Aqara Wall Switch | Xiaomi Smart Button |
| --- | --- | --- | --- |
| <img src="./images/switches/GLEDOPTO-Smart-LED-Strip-Controller-RGBW.png" width="200"/> | <img src="./images/switches/SmartThingsSmartPlug.jpg" width="200"/> | <img src="./images/switches/xiaomi-aqara-wall-switch.jpg" width="200"/> | <img src="./images/switches/Xiaomi_smart_button.png" width="200"/> |

## Voice Interaction
| Google Nest Mini | Google Assistant | Google Pixel Phone |
| --- | --- | --- |
| <img src="./images/google/google_nest_mini.jpg" width="200"/> | <img src="./images/google/google_assistant.jpg" width="200"/> | <img src="./images/google/google_pixel.jpg" width="200"/> | 

Having had Android phones for many years, Google Assistant seemed the natural choice for voice interaction with Home Assistant.  John Legend

## Home Assistant Hardware

| [Raspberry Pi 4 Model B 4GB](https://thepihut.com/products/raspberry-pi-4-model-b) | [Raspberry Pi 4 Enclosure](https://www.ebay.co.uk/itm/Raspberry-Pi-4-Pi4-Case-Cooling-Kit-inc-Fan-Heatsink-35-C-lower-temps/) | [SanDisk Extreme 64GB MicroSD]() | [Raspberry Pi 4 Power Supply](https://thepihut.com/products/raspberry-pi-psu-uk) |
| --- | --- | --- | --- |
| <img src="./images/ha/Raspberry_Pi_4_Model_B.jpg" width="250"/> | <img src="./images/ha/Raspberry_Pi_4_enclosure.jpg" width="250"/> | <img src="./images/ha/SandDiskExtreme64GBMicroSDCard.jfif" width="150"/> | <img src="./images/ha/UK_PSU_BLACK_TRANS_400x.jpg" width="200"/> |

<img src="./images/conbee/conbee2_colours.jfif" width="200"/>
<img src="./images/ha/Nabu_Casa.jpg" width="200"/>

## Home Assistant Software


<img src="./images/ha/docker_logo.png" width="200"/>
<img src="./images/ha/ha_logo.png" width="200"/>
<img src="./images/ha/Mosquitto_MQTT_Logo.png" width="200"/>

<img src="./images/plex/plex_vector_logo.png" width="200"/>
<img src="./images/plex/Plex-Media-Server.png" width="200"/>

| Risco Security Alarm |
| --- |
| <img src="./images/risco/risco_lightsys2_main.png" width="200"/>  |

Backup routine


<table class="fpsb">
  <tr>
    <td class="fpsb-la">Feature:</th>
    <td class="fpsb-ra">Humidity controlled fans</th>
  </tr>
  <tr>
    <td class="fpsb-la">Problem:</th>
    <td class="fpsb-ra">The fan used go on and off with the light switch. This was particularly annoying as the fan is noisy, especially at night. Often we would disable the fan with the tri-pole switch, but this meant people had to proactively remember to flick on the switch before having a shower - which they never did! Also, after having a shower, the fan goes off with the light switch, thus leaving behind a steamy bathroom.</th>
  </tr>
  <tr>
    <td class="fpsb-la">Solution:</th>
    <td class="fpsb-ra">Now Home Assistant switches on the bathroom fan when the humidity goes over 75% and off again when it drops below this point. The result is that the fan only comes on when it is needed. No more, no less.
    </th>
  </tr>    
  <tr>
    <td class="fpsb-la">Benefit:</th>
    <td class="fpsb-benefit">No more noisy fans or steamy bathrooms!</th>
  </tr>      
</table>

## Acknowledgements
This repo is inspired by the excellent work of others listed on the [Awesome Home Assistant](https://www.awesome-ha.com/) page, especially [James McCarthy of Kingia Castle](https://github.com/JamesMcCarthy79/Home-Assistant-Config).