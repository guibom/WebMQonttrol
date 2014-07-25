// Copyright (c) 2014, Guilherme Ramos <longinus@gmail.com>
// https://github.com/guibom/WebMQonttrol
// Released under the MIT license. See LICENSE file for details.

//Global variables
var debug_show = false;  //If it's on, no panels will be hidden          
var msg; //global msg variable       

//Socket server and port
var port = 3000;
var host = (window.location.hostname) ? "http://" + window.location.hostname + ":" + port : "http://192.168.0.175:" + port

//Connect to socket and MQTT broker
var socket = io.connect(host);

//Special tweaks for different page sizes
function tweakPageForEnvironment(env) {
    switch (env) {

        case "ExtraSmall":
            //Remove icons from tab menu
            $.each($("#topTab").find("a").contents(), function(key, obj) {                                        
                if ($(obj)[0].nodeName == "#text")
                    obj.data = "";
            });
            //Remove justified from tab menu
            $("#topTab").removeClass("nav-justified");
            //Remove every button
            // $(".btn").contents().filter(function(){
            //     return this.nodeType === 3;                    
            // }).remove();
    }
}

//Tweak page based on the screen resolution
function findBootstrapEnvironment() {
    var envs = ["ExtraSmall", "Small", "Medium", "Large"];
    var envValues = ["xs", "sm", "md", "lg"];

    $el = $('<div>');
    $el.appendTo($('body'));

    for (var i = envValues.length - 1; i >= 0; i--) {
        var envVal = envValues[i];

        $el.addClass('hidden-'+envVal);
        if ($el.is(':hidden')) {
            $el.remove();
            return envs[i]
        }
    };
}

//Takes an arbritary number of arguments and sanitize the topic with proper '/'.
//IMPORTANT: Always set it to lowercase too!
function topicComposer(arg){                  
    var finalTopic = "";

    for (var i = 0; i < arguments.length; i++) {
        explodedTopic = arguments[i].split("/");

        $.each(explodedTopic, function(key, topicPart) {
            if (topicPart){
                finalTopic += topicPart + "/";
            }
        });
    }

    //Clears out the final /
    return finalTopic.substr(0,finalTopic.length-1).toLowerCase();
}

//Return the Action message from DOM id in the format <Type>_<Action>
function getActionFromId($obj, panel_type){

    return $obj.attr('id').split(panel_type + "_").pop();
}

//Return the Action message from DOM id in the format <Type>_<ID>_<Action>
function getActionFromId($obj){
    
    return $obj.attr('id').split("_").pop();
}

function getNameFromId($obj) {

    return $obj.attr('id').split("_").splice(-2, 1).pop();
}

//Assign hide class
function hidePanel($panel) {
    $panel.addClass('hide');
}

//Remove hide class
function showPanel($panel) {
    $panel.removeClass('hide');
}

//Display an alert message, log to console
function logError(error){
    console.log(error);
    $("#alertWindow").html('<div class="alert alert-danger">' + error + '</div>');
}

// $(window).resize(function () {
//     //console.log($(document).width());
//     console.log(findBootstrapEnvironment());
// });