// Copyright (c) 2014, Guilherme Ramos <longinus@gmail.com>
// https://github.com/guibom/WebMQonttrol
// Released under the MIT license. See LICENSE file for details.

//Object for iTunes messages
var paneliTunes = {
    //Default values
    type: "iTunes",
    $panel: $("#Player_iTunes"),
    actionMessage: "home/player/itunes/",
    
    "home/player/itunes/status/playing": function() {
        if (msg.payload == '1') {                            
            $("#iTunes_PlayPause").html('<span class="glyphicon glyphicon-pause"></span> Pause'); 
            $("#iTunes_PlayPause").addClass('btn-warning').removeClass('btn-primary');
        } else {
            $("#iTunes_PlayPause").html('<span class="glyphicon glyphicon-play"></span> Play');
            $("#iTunes_PlayPause").addClass('btn-primary').removeClass('btn-warning');
        }
    },

    "home/player/itunes": function() {
        if (msg.payload == 'on') {                            
            $("#iTunes_OpenClose").html('<span class="glyphicon glyphicon-off"></span> Close'); 
            $("#iTunes_OpenClose").addClass('btn-warning').removeClass('btn-primary');
            //Show title text element
            $('#iTunes_Title').removeClass('hide');

            //Enable all the buttons
            $('#iTunes_Grid').find("button").each(function(index, element){
                $(this).removeClass('disabled');
            });

        } else {
            $("#iTunes_OpenClose").html('<span class="glyphicon glyphicon-off"></span> Open');
            $("#iTunes_OpenClose").addClass('btn-primary').removeClass('btn-warning');
            //Hide title text element
            $('#iTunes_Title').addClass('hide');

            //Disable all the buttons. 
            $('#iTunes_Grid').find("button").each(function(index, element){
                $(this).addClass('disabled');
            });
            //Re-enable OpenClose button, since it works without iTunes open.
            $('#iTunes_OpenClose').removeClass('disabled');
        }
    },

    "home/player/itunes/status/title": function() {
        if (msg.payload != "" && msg.payload != "0") {
            $('#iTunes_Title').html(msg.payload); 
        } else {
            $('#iTunes_Title').html('Title not found'); 
        }
    },

    Click: function(controller) {
        //Second part of MPC_xxx, lowercased is the MQTT message
        var action = controller.attr("id").split("_");
        action = action[1].toLowerCase();

        socket.emit('publish', {
            topic: this.actionMessage + action,
            message: '1'
        });
    }
}