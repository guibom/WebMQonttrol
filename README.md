WebMQonttrol
============

Web interface and server to pub/sub MQTT messages for home automation, using Node.js and Socket.io. The `index.html` page uses a web socket to connect to the listening server `WebMQonttrol_server.js` with node.js. The server creates a connection to the MQTT broker, and passes messages from/to the client-page connected.

![alt text](https://raw2.github.com/guibom/WebMQonttrol/master/docs/screenshot.png "Screenshot")

###Structure overview

The structure and layout are very specific to my use case, and definitly won't work out of the box for other people. But hopefully this can serve as a starting point for your project. The MQTT messages I'm using are under the /docs folder. The main idea is to have actions and status messages. Actions are mostly trigger topic, where the actual message is not really important (though can be used as a 'function argument'). Status messages are usually set by whoever receiver the action message, and the messages the webpage uses to show the current status.

![alt text](https://raw2.github.com/guibom/WebMQonttrol/master/docs/WebMQonttrol_Structure.png "Structure overview")

###Dependencies
- [node.js](http://www.nodejs.org/) - Used to run a socket.io server `WebMQonttrol_server.js`, that the `index.html` page connects to.
- [socket.io](http://socket.io/) - `WebMQonttrol_server.js` runs a web socket from `index.html` to MQTT broker.
- [mqtt.js](https://github.com/adamvr/MQTT.js/) - MQTT client library for Node.js, used by the server to sub/pub messages.
- [Mosquitto](http://mosquitto.org/) - The broker I'm using, but I imagine it should work with others.

####Nice to have
- [Arduino](http://www.arduino.cc/) - Arduino with Ethernet shield, to interface with physical objects.
- [EventGhost](http://www.eventghost.org/) - Windows software used for automation of media players, peripherals, etc. Uses a MQTT plugin to talk to the broker.
- [Node-RED](http://nodered.org/) - Node.js tool to create connections between different web inputs/outputs, like MQTT/GET/POST/UDP/etc.

### Credit

The code was initially heavily based and inspired by Fabian Affolter and his [mqtt-panel](https://github.com/fabaff/mqtt-panel) project.
