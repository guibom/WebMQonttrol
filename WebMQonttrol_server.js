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
var socket = require('socket.io');

var mqttbroker = 'localhost';
var mqttport = 1883;

var io = socket.listen(3000);
var mqttclient = mqtt.createClient(mqttport, mqttbroker);

// Reduce socket.io debug output
io.set('log level', 0)
var debug_messages = false;

//Enable debug messages from command line
if (process.argv.length >= 2)
    if (process.argv[2].toLowerCase() == "debug")
        debug_messages = true;

DEBUG_LOG('Server Started!');

// Subscribe to topic
io.sockets.on('connection', function (socket) {

    //Log subscriptions to console
    DEBUG_LOG('Client Connected: ' + socket.id);

    //Subscribe to an arbitrary number of topics
    socket.on('subscribe', function (data) {        

        //Subscribe to all the messages passed as arguments
        for (var i = 0; i < arguments.length; i++) {
            mqttclient.subscribe(arguments[i].topic);

            //Log subscriptions to console
            if (debug_messages) {
                console.log('SUB:', arguments[i].topic);
            }  
        }
    });

    //Publish to topic/message
    socket.on('publish', function (data) {

        //if (data.length < 2)
        //Log MQTT messages being sent
        if (debug_messages) {
            console.log('SENT:', data.topic, data.message);
        }

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
         'payload' : payload
        }
    );

    //Log MQTT messages being received
	if (debug_messages) {
        console.log('RECEIVED:', topic, payload);
    }        

});


//Print debug message to log, if server in debug mode
function DEBUG_LOG(msg, force=false)
{
    if (debug_messages) {
        console.log(msg);
    }
    else
    {
        if (force)
            console.log(msg);
    }
}