// Copyright (c) 2014, Guilherme Ramos <longinus@gmail.com>
// https://github.com/guibom/WebMQonttrol
// Released under the MIT license. See LICENSE file for details.

//Object for Light messages
var panelLight = {
    //Properties
    type: "Light",
    $panel: $("#Controller_Light"),

    //Constructor, run once at start
    __begin__: function(){
        //Set all lights to off by default
        $(".WMQ_light").html('<span class="glyphicon glyphicon-remove"></span> OFF').removeClass('btn-success').addClass('btn-danger');
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

    "home/light/1/status/brightness": function() {
        $('#Light_1_Brightness').text(msg.payload);
        $('#slider1').val(parseInt(msg.payload));
    },

    LightON: function($controller) {
        $controller.html('<span class="glyphicon glyphicon-ok"></span> ON');                        
        $controller.removeClass('btn-danger').addClass('btn-success');
    },

    LightOFF: function($controller) {       
        $controller.html('<span class="glyphicon glyphicon-remove"></span> OFF');  
        $controller.removeClass('btn-success').addClass('btn-danger'); 
    },

    //Generic Click action redirected here from the ID
    Click: function(controller) {
        //Get light number from jquery object's id
        var light_id = controller.attr("id").split("_");
        light_id = light_id[1];
        var current_status = $.trim($(controller).text().toLowerCase());
        var send_msg;

        //Toggle light status message
        if (current_status == "on") {
            send_msg = "off";                            
        } else if (current_status == "off") {
            send_msg = "on";                             
        }                            

        //Publish MQTT message
        socket.emit('publish', {
            topic: 'home/light/' + light_id + '/' + send_msg,
            message: '1'
        });
    }
}