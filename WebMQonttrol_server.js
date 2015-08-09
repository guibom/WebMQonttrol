#!/usr/bin/env node
/**
 * Moddified to add support for publishing messages and other tweaks
 * Copyright (c) 2014, Guilherme Ramos <longinus@gmail.com>
 * https://github.com/guibom/WebMQonttrol
 * Released under the MIT license. See LICENSE file for details.
 */
/**
 * Copyright (c) 2013, Fabian Affolter <fabian@affolter-engineering.ch>
 * Released under the MIT license. See LICENSE file for details.
 */
var mqtt = require('mqtt');
var mqttbroker = 'localhost:1883';
var mqttclient = mqtt.connect('mqtt://' + mqttbroker);

var socket = require('socket.io');
var io = socket.listen(3000);

//Internal debug
var debug_messages = false;

//Console commands
process.argv.forEach(function (val, index, array) {
    if (val) {
        if (val.toLowerCase() == "debug") {
            debug_messages = true;
        }
    }
});

//Connect to Broker
mqttclient.on('connect', function() {
  DEBUG_LOG('Server Started!');
});


// Subscribe to topic
io.sockets.on('connection', function (socket) {

    //Log subscriptions to console
    DEBUG_LOG('Client Connected: ' + socket.id);

    //Subscribe to an arbitrary number of topics
    socket.on('subscribe', function (data) {

        //Subscribe to all the messages passed as arguments
        for (var i = 0; i < arguments.length; i++) {

            try {

                //Check topic for errors
                if (typeof arguments[i].topic == 'undefined')
                {
                    DEBUG_LOG('Error, topic not valid! Ignoring function...');
                    return false;
                }

                //Topic is not null, subscribe
                mqttclient.subscribe(arguments[i].topic);
                //Log subscriptions to console
                DEBUG_LOG('SUB: ' + arguments[i].topic);
            }
            catch(err) {
                DEBUG_LOG('ERROR: ' + err, true);
            }
        }
    });

    //Publish to topic/message
    socket.on('publish', function (data) {

        //Check message
        if (typeof data.topic == 'undefined')
        {
            DEBUG_LOG('Error, topic not valid! Ignoring function...');
            return false;
        }

        //Log MQTT messages being sent
        DEBUG_LOG('SENT: ' + data.topic + " " + data.message);

        //Publish MQTT message
        try {
            mqttclient.publish(data.topic, data.message);
        }
        catch(err) {
            DEBUG_LOG('ERROR: ' + err, true);
        }
    });

    //Unsubscribe from topic
    socket.on('unsubscribe', function (data) {
	   mqttclient.unsubscribe(data.topic);
    });
});

// Push the message to socket.io
mqttclient.on('message', function(topic, payload) {
    io.sockets.emit('mqtt',
        {'topic'  : topic,
         'payload' : String(payload)
        }
    );

    //Log MQTT messages being received
    DEBUG_LOG('RECEIVED: ' + topic + " " + payload);
});

//Print debug message to log, if server in debug mode
function DEBUG_LOG(msg, force)
{
    //Default value of force
    force = typeof force !== 'undefined' ? force : false;

    if (debug_messages) {
        console.log(msg);
    }
    else
    {
        if (force)
            console.log(msg);
    }
}
