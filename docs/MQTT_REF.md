### Interfaces
Controller messages are set at start, and a will defined for unexpect disconnects.
Players get the information from EventGhost running on my HTPC
```
home/controller/MQTTRF			(on, off) Retained
home/controller/MQTTRF/light/#	(string) _ID of light_ Retained

home/player/mpc					(on, off) Retained		
home/player/itunes				(on, off) Retained
home/player/xbmc				(on, off) Retained

home/pc                         (on, off) Retained
home/vault                      (on, off) Retained
```

### Action Messages
Actions are received by other clients, and are usually just a trigger event
```
home/light/#/on  				(1)
home/light/#/off  				(1)
home/light/#/fade_on			(int speed mili)
home/light/#/fade_off			(int speed mili)
home/light/#/set 				(0-100) _Brightness Value_

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

home/pc/sleep                   (1)
home/pc/wakeup                  (1) WOL package from Node-Red
```

### Status Messages
Status updates are set by clients after actions are performed, usually persist
```
home/light/#/status        		    (on, off) Read-only
home/light/#/status/brightness      (0-100)	Read-only

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
home/light/#/config/min_value	(byte)
home/light/#/config/max_value	(byte)
home/light/#/config/fade_speed	(int in seconds)

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