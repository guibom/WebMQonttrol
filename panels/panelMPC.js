// Copyright (c) 2014, Guilherme Ramos <longinus@gmail.com>
// https://github.com/guibom/WebMQonttrol
// Released under the MIT license. See LICENSE file for details.

//Object for MPC messages
var panelMPC = {
    //Default values
    type: "MPC",
    $panel: $("#Player_MPC"),
    actionMessage: "home/player/mpc/",
    MPCBarTotal: 0,

    "home/player/mpc": function() {                    
        if (msg.payload == 'on' || debug_show) {                        
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