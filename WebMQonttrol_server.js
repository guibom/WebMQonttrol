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

// Subscribe to topic
io.sockets.on('connection', function (socket) {

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
    	mqttclient.publish(data.topic, data.message);

        //Log MQTT messages being sent
        if (debug_messages) {
            console.log('SENT:', data.topic, data.message);
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