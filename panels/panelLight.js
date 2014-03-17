// Copyright (c) 2014, Guilherme Ramos <longinus@gmail.com>
// https://github.com/guibom/WebMQonttrol
// Released under the MIT license. See LICENSE file for details.

//Object for Light messages
var panelLight = {
    //Properties
    type: "Light",
    controlMessage: "home/light/%ID%/action",  //%ID% is replaced with Light ID
    $panel: $("#Controller_Light"),
    $lightButtons: $(".WMQ_light.btn"),

    //Constructor, run once at start
    __begin__: function(){
        
        //Iterate over light buttons to get ID
        this.$lightButtons.map(function() {
            //Set light button default values. Off by default (no MQTT msg received yet)
            $(this).html('<span class="glyphicon glyphicon-remove"></span> OFF').removeClass('btn-success').addClass('btn-danger');

            //Set state and ID based on the id of the DOM element            
            $(this).data("id", getActionFromId($(this), panelLight.type));
            $(this).data("isOn", false);
        });

        //Bind click events
        this.$lightButtons.on("click", function(e) {
            e.preventDefault();
            panelLight.LightControl($(this));
        });
    },

    "home/light/1/status": function() {
        if (msg.payload == 'on') {
            this.LightON($('#Light_1')); 
        } else {
            this.LightOFF($('#Light_1'));            
        }        
    },

    "home/light/2/status": function() {
        if (msg.payload == 'on') {
            this.LightON($('#Light_2'));
        } else {
            this.LightOFF($('#Light_2'));
        }
    },

    "home/light/5/status": function() {
        if (msg.payload == 'on') {
            this.LightON($('#Light_5'));
        } else {
            this.LightOFF($('#Light_5'));
        }
    },

    "home/light/1/status/brightness": function() {
        $('#Light_1_Brightness').text(msg.payload);
        $('#slider1').val(parseInt(msg.payload));
    },

    LightON: function($controller) {
        $controller.html('<span class="glyphicon glyphicon-ok"></span> ON');                        
        $controller.removeClass('btn-danger').addClass('btn-success');
        $controller.data("isOn", true);
    },

    LightOFF: function($controller) {       
        $controller.html('<span class="glyphicon glyphicon-remove"></span> OFF');  
        $controller.removeClass('btn-success').addClass('btn-danger'); 
        $controller.data("isOn", false);
    },

    //ON/OFF based Control messages
    LightControl: function($controller) {                
        //Toggle light status message
        var send_msg;
        if ($controller.data("isOn")) {
            send_msg = "off";
        } else {
            send_msg = "on";
        }

        //Publish MQTT message
        socket.emit('publish', {
            topic: topicComposer(panelLight.controlMessage.replace("%ID%", $controller.data("id")), send_msg),
            message: '1'
        });
    }
}