// Copyright (c) 2014, Guilherme Ramos <longinus@gmail.com>
// https://github.com/guibom/WebMQonttrol
// Released under the MIT license. See LICENSE file for details.

//File selection to start a video in MPC
var panelMPCSelection = {
    //Default values
    type: "MPCSelection",
    requestMessage: "home/htpc",
    playFileMessage: "home/player/mpc/open",
    extFilter: ["mkv", "mp4", "avi", "wmv"],
    currentPath: "",
    pathHistory: [],

    //Constructor, run once at start
    __begin__: function(){

        //Set event handler for file selection buttons
        $("#MPCSelection_BackFolder").on("click", function(e) {
            e.preventDefault();
            panelMPCSelection.BackFolder();
        });

        $("#MPCSelection_ListFiles_1").on("click", function(e) {
            e.preventDefault();                        
            panelMPCSelection.OpenFolder("c:/users/longinus/downloads");
        });

        $("#MPCSelection_ListFiles_2").on("click", function(e) {
            e.preventDefault();
            panelMPCSelection.OpenFolder("E:/MOVE/_WATCH");
        });        
    },

    "home/htpc/listfiles/result": function() {
        if (msg.payload) {
            var obj = $.parseJSON(msg.payload);
            var extFilter = this.extFilter;                        
            var $myList = $("#MPC_File_List");
            
            //Clear file list
            $myList.empty();

            //Iterate over the JSON object, finding files to add
            $.each( obj.files, function( key, value ) {
                //Check if the file matches the filtered extensions
                $.each(extFilter, function(keyF, valueFilter) {
                    if (valueFilter == value.split('.').pop()) {                                    
                        
                        //Create element
                        var $myNewElement = $('<a href="#" class="list-group-item"><i class="fa fa-file-o fa-fw"></i> ' + value + '</a>');

                        //Attach click event, with proper path to be used
                        $myNewElement.on( "click", function(e) {
                            e.preventDefault();
                            //Remove active from other list items
                            $(".list-group-item").removeClass('active');
                            //Add active on the clicked one
                            $(this).addClass('active');                                        
                            panelMPCSelection.OpenFile(obj.root + "/" + value);
                        });

                        //Append to list
                        $myNewElement.appendTo($myList);

                        //Return earlier since we found a valid one already
                        return false;
                    }
                });                        
            });
            

            //Iterate over the folders to add.
            $.each( obj.folders, function( key, value ) {  

                //Create element
                var $myNewElement = $('<a href="#" class="list-group-item"><i class="fa fa-folder fa-fw"></i> ' + value + '</a>');

                //Attach click event
                $myNewElement.on( "click", function(e) {
                    e.preventDefault();
                    panelMPCSelection.OpenFolder(obj.root + "/" + value);
                    $myNewElement.addClass('active');
                });

                //Append to list
                $myNewElement.appendTo($myList);

            });

            //Path that was used on json query
            this.currentPath = obj.root;
            this.pathHistory.push(this.currentPath);
            
            //Enable the button if there are folders to go back to
            $("#MPCSelection_BackFolder").toggleClass("disabled", !(this.pathHistory.length > 1));

            //Toggle proper status text
            $("#MPCSelection_FolderText").html("<strong><i class='fa fa-folder-open fa-lg'></i> " + this.currentPath + "</strong>");
            
        }                       
    },

    OpenFile: function(path) {
        if(path){
            //Publish MQTT message
            socket.emit('publish', {
                topic: this.playFileMessage,
                message: path
            });                        
        }                
    },

    OpenFolder: function(path){
        if(path){
            //Publish MQTT message
            socket.emit('publish', {                            
                topic: topicComposer(this.requestMessage, "listfiles"),
                message: path
            });                        
        }   
    },

    BackFolder: function(){
        if (this.pathHistory.length > 1){
            this.pathHistory.pop() //First get rid of the current folder
            this.OpenFolder(this.pathHistory.pop()); //Now pass the right one
        }
    }
}