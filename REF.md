Controller messages are set at start, and a Will defined for unexpect disconnects
```
home/controller/MQTTRF			(on, off) _Persistent_
home/controller/MQTTRF/light/#	(string) _ID of light_ _Persistent_
```

Actions are received by controller
```
home/light/#/on  				(1,0) _Action_
home/light/#/off  				(1,0) _Action_
home/light/#/fade_on			(int speed mili) _Action_
home/light/#/fade_off			(int speed mili) _Action_
home/light/#/set 				(0-100) _Brightness Value_
```

Status updates are set by controller after actions are performed
```
home/light/#/status        		(on, off) _Read-only_
home/light/#/status/brightness 	(0-100)	_Read-only_
```

Configuration values are read by the controller
```
home/light/#/config/min_value	(byte)
home/light/#/config/max_value	(byte)
home/light/#/config/fade_speed	(int in seconds)
```