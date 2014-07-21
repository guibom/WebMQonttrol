// Copyright (c) 2014, Guilherme Ramos <longinus@gmail.com>
// https://github.com/guibom/WebMQonttrol
// Released under the MIT license. See LICENSE file for details.

//Object for MPC messages
var panelMPC = {
    //Default values
    type: "MPC",
    $panel: $("#Player_MPC"),
    $mpcButtons: $(".WMQ_mpc.btn"),
    actionMessage: "home/player/mpc/",
    MPCBarTotal: 0,

    //Constructor, run once at start
    __begin__: function(){
        
        //Iterate over light buttons to get ID
        this.$mpcButtons.map(function() {
            //Set state and ID based on the id of the DOM element
            $(this).data("action", getActionFromId($(this), panelMPC.type));
        });

        //Bind click events
        this.$mpcButtons.on("click", function(e) {
            e.preventDefault();
            panelMPC.Control($(this));
        });
    },

    "home/player/mpc": function() {                    
        if (msg.payload == 'online' || debug_show) {                        
            showPanel(this.$panel);
        } else {                    
            hidePanel(this.$panel);
        }
    },

    "home/player/mpc/status/total_time": function() {
        MPCBarTotal = msg.payload;                         
    },

    "home/player/mpc/status/current_time": function() {                        
        var current_time = parseInt(msg.payload);                        
        document.getElementById('MPCBar').style.width = ((current_time * 100) / MPCBarTotal) + '%';
    },

    "home/player/mpc/status/playing": function() {
        //Playing
        if (msg.payload == '1') {
            $('#MPCBar').removeClass('hide')
            $('#MPCBar_Base').addClass('active');

            $("#MPC_PlayPause").html('<span class="glyphicon glyphicon-pause"></span> Pause'); 
            $("#MPC_PlayPause").addClass('btn-warning').removeClass('btn-primary');
        //Paused
        } else if (msg.payload == "2") {
            $('#MPCBar').removeClass('hide');
            $('#MPCBar_Base').removeClass('active');

            $("#MPC_PlayPause").html('<span class="glyphicon glyphicon-play"></span> Play');
            $("#MPC_PlayPause").addClass('btn-primary').removeClass('btn-warning');
        //Stopped
        } else {
            $('#MPCBar').addClass('hide');

            $("#MPC_PlayPause").html('<span class="glyphicon glyphicon-play"></span> Play');
            $("#MPC_PlayPause").addClass('btn-primary').removeClass('btn-warning');
        }
    },
    
    "home/player/mpc/status/filename": function() {
        if (msg.payload != "" && msg.payload != "0") {
            $('#mpc_filename').html(msg.payload); 
        } else {
            $('#mpc_filename').html('Filename not found'); 
        }
    },

    Control: function($controller){
        //Publish MQTT message
        socket.emit('publish', {
            topic: topicComposer(panelMPC.actionMessage, $controller.data("action")),
            message: '1'
        });

    }

}