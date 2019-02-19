
var http = require('http');

var mosca = require('mosca');
var MqttServer = new mosca.Server({
    http:{
        port:3000,
        bundle:true,
        static:'./'
    }
    //port: 1883
});

var login = false;
MqttServer.on('clientConnected', function(client){
    console.log('client connected', client.id);
//    if(client.id == "HUICOBUS_MQTT_CLIENTID_UIPRESENT"){
//        login = true;
//        console.log('UIPRESENT connected:', client.id);
//    }
//    if(client.id == "HUICOBUS_MQTT_CLIENTID_HCUENTRY"){
//        login = true;
//        console.log('HCUENTRY connected:', client.id);
//    }
});


MqttServer.on('published', function(packet, client) {
    var topic = packet.topic;
    console.log('message-arrived--->','topic ='+topic+',message = '+ packet.payload.toString()+'\n');


});

MqttServer.on('ready', function(){
    console.log('Xiaohui mqtt general server is running...');

    //MqttServer.authenticate = authenticate;  
});






//mqttServ.attachHttpServer(httpServ);
//httpServ.listen(3000);
