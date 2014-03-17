### Interfaces
Controller messages are set at start, and a will defined for unexpect disconnects. Gateways interface ethernet to RF/etc.
Players get the information from EventGhost running on my HTPC
```
home/gateway/mqttrf			    (online, offline) Retained
home/gateway/mqttrf/light/$ID	(online, offline) Retained
home/gateway/mqttrf/x10         (online, offline) Retained
home/gateway/mqttrf/rfswitch    (online, offline) Retained
home/x10                        (online, offline) Retained
home/rfswitch                   (online, offline) Retained

home/player/mpc					(on, off) Retained
home/player/itunes				(on, off) Retained
home/player/xbmc				(on, off) Retained

home/htpc                       (on, off) Retained
home/vault                      (on, off) Retained
```

### Action Messages
Actions are received by other clients, and are usually just a trigger event
```
home/light/$ID/action/on  			(1)
home/light/$ID/action/off  			(1)
home/light/$ID/action/fade_on		(int speed mili)
home/light/$ID/action/fade_off		(int speed mili)
home/light/$ID/action/set 			(0-100) _Brightness Value_

home/player/mpc/playpause		(1)
home/player/mpc/stop			(1)
home/player/mpc/volumeup		(1)
home/player/mpc/volumedown		(1)
home/player/mpc/fullscreen		(1)

home/player/itunes/openclose    (1)
home/player/itunes/playpause    (1)
home/player/itunes/stop         (1)
home/player/itunes/volumeup     (1)
home/player/itunes/volumedown   (1)

home/htpc/sleep                 (1)
home/htpc/wakeup                (1) WOL package from Node-Red
home/htpc/listfiles             (string pathname)

home/x10/A/UNIT_1/ON            (1) Processed by Node-RED
    |__ home/X10/action         (JSON) {"H":0,"U":2,"A":99,"T":3}

home/rfswitch/action            (JSON) {"D":123456,"B":24}

```

### Status Messages
Status updates are set by clients after actions are performed, usually persist
```
home/light/$ID/status        		(on, off) Read-only
home/light/$ID/status/brightness    (0-100)	Read-only

home/player/mpc/status/playing		(0 stopped, 1 playing, 2 paused) Retained
home/player/mpc/status/total_time	(int in seconds)
home/player/mpc/status/current_time	(int in seconds)
home/player/mpc/status/filename		(string, null or 0 for none)

home/player/itunes/status/playing   (0 stopped, 1 playing, 2 paused) Retained
home/player/itunes/status/title     (string, null or 0 for none)
```

### Configuration Messages
Configuration values are used to tweak the clients, updating their default values
```
home/light/$ID/config/min_value	    (byte)
home/light/$ID/config/max_value	    (byte)
home/light/$ID/config/fade_speed	(int in seconds)

home/web/config/debug_show      (1,0)
```

### External Messages
Messages acquired from external sources
```
weather/home/currently/temperature          (int) 5min intervals
weather/home/currently/apparenttemperature  (int) 5min intervals
weather/home/currently/summary              (string) 5min intervals
weather/home/currently/icon                 (forecast.io icons) 5min intervals
```


### Sensor Network
Short-form messages transmitted by sensor network, and how they are processed into full proper messages by Node_RED
```
S/T/$ID (int)  -->  /sensor/temperature/$ID/raw/last    (int)
S/H/$ID (int)  -->  /sensor/humidity/$ID/raw/last       (int)

C/L/10/S        Controller/
C/L/10/G
C/L/10/F/U
``` 