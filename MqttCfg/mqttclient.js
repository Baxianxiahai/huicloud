/**
 * Created by hyj on 2017/8/7.
 */
var mqtt  = require('mqtt');
//var client  = mqtt.connect('mqtt://test.mosca.io');
//var client  = mqtt.connect('mqtt://192.168.103.237');
//var client  = mqtt.connect('mqtt://m2m.vicbang.com',{
//    username:'13800000000',
//    password:'123456',
//    clientId:'app_13800000000'
//});

var start = false;
var pause = false;
var calibration_start=false;

var client  = mqtt.connect('mqtt://127.0.0.1',{
    username:'username',
    password:'password',
    clientId:'MQTT_XH_Double_Line_Balance_HCU'
});

client.on('connect', function () {
    console.log('connected.....');
    client.subscribe('MQTT_XH_Double_Line_Balance_HCU');
    /*
     setInterval(function(){
     if(!calibration_start) return;
     client.publish('MQTT_XH_Double_Line_Balance_UI', buildcalibrationdynamicinfo());
     },6000);*/


    setInterval(function(){
        if(!start) return;
        if(pause) return;
        client.publish('MQTT_XH_Double_Line_Balance_UI', buildstatisticsinfo());
    },600);
    setInterval(function(){
        if(!start) return;
        if(pause) return;
        client.publish('MQTT_XH_Double_Line_Balance_UI', buildchamberinfo());
        /*
         var list = buildchamberinfolist();
         //console.log(list);
         for(var i=0;i<list.length;i++){
         client.publish('MQTT_XH_Double_Line_Balance_UI', JSON.stringify(list[i]));
         }*/
    },1600);
    setInterval(function(){
        if(!start) return;
        if(pause) return;
        client.publish('MQTT_XH_Double_Line_Balance_UI', buildpackageinfo());
    },600);
    /*
     setInterval(function(){
     if(!start) return;
     client.publish('MQTT_XH_Double_Line_Balance_UI', build_status_message());
     },600);*/
    setInterval(function(){
        if(!start) return;
        client.publish('MQTT_XH_Double_Line_Balance_UI', buildalarminfo());
    },60000);
    setInterval(function(){
        client.publish('MQTT_XH_Double_Line_Balance_UI', buildreportinfo());
    },30000);
    setInterval(function(){
        client.publish('MQTT_XH_Double_Line_Balance_UI', builddebuginfo());
    },600000);

    //client.publish('MQTT_TOPIC_UI_TO_HCU', 'Hello mqtt['+i+']');
});

client.on('message', function (topic, message) {
    // message is Buffer
    console.log(message.toString());
    var msg = JSON.parse(message.toString());
    /* var message = {
     action:"XH_Double_Line_Balance_config_start"
     };* */

    if(msg.action== "XH_Double_Line_Balance_config_start") {
        client.publish('MQTT_XH_Double_Line_Balance_UI', buildstatisticsinfo());

        start = true;
        pause = false;
    }else if(msg.action== "XH_Double_Line_Balance_config_stop"){
        start = false;
        pause = false;
    }else if(msg.action== "XH_Double_Line_Balance_config_pause"){
        pause = true;
    }else if(msg.action== "XH_Double_Line_Balance_config_resume"){
        pause = false;
    }else if(msg.action== "XH_Double_Line_Balance_force_flush"){
        client.publish('MQTT_XH_Double_Line_Balance_UI', build_status_info());
        client.publish('MQTT_XH_Double_Line_Balance_UI', build_status_message());
    }else if(msg.action == "XH_Double_Line_Balance_calibration_dynamic_start"){
        calibration_start = true
        buildcalibrationzeroinfo();
    }else if(msg.action == "XH_Double_Line_Balance_calibration_dynamic_stop"){
        calibration_start = false;
        buildcalibrationfullinfo();
    }else if(msg.action == "XH_Double_Line_Balance_calibration_zero_trigger"){
        client.publish('MQTT_XH_Double_Line_Balance_UI', buildcalibrationzeroinfo());
    }else if(msg.action == "XH_Double_Line_Balance_calibration_weight_trigger"){
        client.publish('MQTT_XH_Double_Line_Balance_UI', buildcalibrationweightinfo());
    }

});
/*
 function buildstatisticsinfo(){
 var biglabel= {
 title: "Test BIG Title",
 unit: "Status Report",
 value: GetRandomNum(1,3000)+"g"
 };
 var colorlist=[
 "RED",
 "ORANGE",
 "BLUE",
 "GREEN",
 "GRAY",
 "PURPLE",
 "LBLUE",
 "LGRAY",
 "DBLUE"];
 var smalllabellist=[];
 for(var i=0;i<9;i++){
 var templabel={
 title:"test title",
 unit:"note",
 color:colorlist[GetRandomNum(0,8)],
 value:GetRandomNum(0,300)+"kg"
 }
 smalllabellist.push(templabel);
 }
 var ret={
 action:"XH_Double_Line_Balance_statistics_status",
 data:{
 currentweight:biglabel,
 mainvalue:smalllabellist
 }
 }
 return JSON.stringify(ret);
 }*/
function buildversioninfo(){
    var number = GetRandomNum(1,10);
    var ret;
    if(number >7){
        ret={
            'Alarm':true,
            'Title':'New version',
            'HCU':"yyHCU-SW-R3.V243.DB11.PATCH xxHCU-SW-R3.V243.DB11.PATCH",
            'IHU':"IHU-SW-R3.V243.DB11.PATCH"
        }
    }else{
        ret={
            'Alarm':false,
            'Title':'Versoin number',
            'HCU':"yyHCU-SW-R3.V243.DB11.PATCH xxHCU-SW-R3.V243.DB11.PATCH",
            'IHU':"IHU-SW-R3.V243.DB11.PATCH"
        }
    }

    var version = {
        action:"XH_Double_Line_Balance_version_status",
        data:ret
    }
    return JSON.stringify(version);
}
function buildalarminfo(){
    var number = GetRandomNum(1,5);
    var sta='true';
    if(number == 2) sta='false';
    ret={
        'status':sta,
        'auth':'true',
        'msg':'error msg:1234567890;1234567890;1234567890'
    }


    var version = {
        action:"XH_Double_Line_Balance_alarm_status",
        data:ret
    }
    return JSON.stringify(version);
}
function buildreportinfo(){
    var number = GetRandomNum(1,50);
    var msg = "status report:";
    for(var i=0;i<number;i++){
        msg = msg+" x"+i;
    }


    var version = {
        action:"XH_Double_Line_Balance_report_status",
        data:msg
    }
    return JSON.stringify(version);
}
function builddebuginfo(){
    var number = GetRandomNum(1,50);
    var msg = "return msg:";
    for(var i=0;i<number;i++){
        msg = msg+" x"+i;
    }


    var version = {
        action:"XH_Double_Line_Balance_debug_status",
        data:msg
    }
    return JSON.stringify(version);
}
function buildcalibrationzeroinfo(){
    var balance="1";
    var ret = {
        action:"XH_Double_Line_Balance_calibration_zero_status",
        data:{
            balance:balance,
            msg:parseFloat(GetRandomNum(0,500))/1000
        }
    }
    return JSON.stringify(ret);
}
function buildcalibrationweightinfo(){
    var balance="1";
    var ret = {
        action:"XH_Double_Line_Balance_calibration_weight_status",
        data:{
            balance:balance,
            msg:parseFloat(GetRandomNum(0,5000))
        }
    }
    return JSON.stringify(ret);
}
function buildcalibrationdynamicinfo(){
    var balance="1";
    var status = false;
    var temp = GetRandomNum(0,500);
    if(temp>400) status = true;
    if(temp%2 == 0) balance="2";
    var message = "";
    for(var i=0;i<temp;i++){
        message = message+" x";
    }
    var ret = {
        action:"XH_Double_Line_Balance_calibration_dynamic_status",
        data:{
            balance:balance,
            status:status,
            value:[{
                name:'trynumber',
                value:GetRandomNum(0,50),
            },{
                name:"msg",
                value:"ret msg:"+message
            }]
        }
    }
    return JSON.stringify(ret);
}
function buildcalibrationzeroinfo(){
    var number = 6;
    var intervalhandle = setInterval(function(){
        client.publish('MQTT_XH_Double_Line_Balance_UI', buildcalibrationdynamicinfo());
        number --;
        if(number ===0){
            clearInterval(intervalhandle);
            client.publish('MQTT_XH_Double_Line_Balance_UI', JSON.stringify({
                action:"XH_Double_Line_Balance_calibration_zero_finish",
            }));
        }
    },6000);
}
function buildcalibrationfullinfo(){
    var number = 6;
    var intervalhandle = setInterval(function(){
        client.publish('MQTT_XH_Double_Line_Balance_UI', buildcalibrationdynamicinfo());
        number --;
        if(number ===0){
            clearInterval(intervalhandle);
            client.publish('MQTT_XH_Double_Line_Balance_UI', JSON.stringify({
                action:"XH_Double_Line_Balance_calibration_full_finish",
            }));
        }
    },6000);
}
function buildstatisticsinfo(){
    var biglabel1= {
        title: "Test BIG Title",
        note: "Status",
        status: GetRandomNum(1,3000)
    };
    var biglabel2= {
        title: "Test BIG Title2",
        note: "Status",
        status: GetRandomNum(1,3000)
    };
    var colorlist=[
        "RED",
        "ORANGE",
        "BLUE",
        "GREEN",
        "GRAY",
        "PURPLE",
        "LBLUE",
        "LGRAY",
        "DBLUE"];
    var smalllabellist=[];
    var tempseed= GetRandomNum(0,1);
    for(var i=0;i<6;i++){
        var templabel={
            key:'Label'+(i*2+tempseed+1),
            value:{
                title:"test title"+(i*2+tempseed+1),
                note:"note"+tempseed,
                color:colorlist[GetRandomNum(0,8)],
                value:GetRandomNum(0,300)+"kg"
            }
        }
        smalllabellist.push(templabel);
    }
    var ret={
        action:"XH_Double_Line_Balance_statistics_status",
        data:{
            //biglabel1:biglabel1,
            //biglabel2:biglabel2,
            labellist:smalllabellist
        }
    }
    return JSON.stringify(ret);
}
function buildchamberinfolist(){
    var chamberprocesslist=["0",'10','20','30','40','50','60','70','80','90','100'];
    var retlist = [];
    for(var i=0;i<11;i++){
        var chamber = {
            action:"XH_Double_Line_Balance_chamber_status",
            data:{
                process:1,
                id:(i+1),
                package:false,
                fillin:false,
                error:false,
                status:true,
                volume:i*10,
                buffer:i*10,//volume:0,
                //group:0,//reject:0,
                //basket:0,//box:0,
                basket:GetRandomNum(0,10000),
                group:GetRandomNum(0,100),
                chamberprocess:chamberprocesslist[i]
            }
        }
        retlist.push(chamber);
    }
    //console.log(retlist);
    return retlist;
}

function buildchamberinfo(){
    var number = GetRandomNum(1,32);
    var status = true;
    var error = false;
    var package = false;
    var fillin = true;
    var chamberprocesslist=["0",'10','20','30','40','50','60','70','80','90','100'];
    var volume = GetRandomNum(0,100);;

    var temp = GetRandomNum(1,10);
    if(temp>9){
        status = false;
    }
    temp = GetRandomNum(1,10);
    if(temp>8){
        error = true;
    }
    temp = GetRandomNum(1,10);
    if(temp>8){
        package = true;
        fillin=false;
    }
    temp = GetRandomNum(1,10);
    if(temp>9){
        volume = 100;
    }

    var chamber = {
        action:"XH_Double_Line_Balance_chamber_status",
        data:{
            process:GetRandomNum(1,2),
            id:number,
            package:package,
            fillin:fillin,
            error:error,
            status:status,
            volume:volume,
            buffer:volume,//volume:0,
            //group:0,//reject:0,
            //basket:0,//box:0,
            basket:GetRandomNum(0,10000),
            group:GetRandomNum(0,100),
            chamberprocess:chamberprocesslist[GetRandomNum(0,10)]
        }
    }
    //console.log(JSON.stringify(chamber));
    return JSON.stringify(chamber);
}
function buildpackageinfo(){
    var biglabel= {
        title: "Test BIG Title",
        note: "Status",
        status: GetRandomNum(1,3000)
    };
    var ret = {
        action:"XH_Double_Line_Balance_package_status",
        data:{
            biglabel:biglabel,
            process:GetRandomNum(1,2),
            weight:GetRandomNum(1,1500),
            //target:0
            target:GetRandomNum(0,32)
        }
    }
    return JSON.stringify(ret);
}
function build_status_message(){
    var list1 = [];
    var list2 = [];

    var chamberprocesslist=["0",'10','20','30','40','50','60','70','80','90','100'];
    for(var i=0;i<33;i++){
        var temp = {
            process:1,
            id:i,
            status:true,
            error:false,
            package:false,
            fillin:false,
            buffer:0,//volume:0,
            group:0,//reject:0,
            basket:0,//box:0,
            chamberprocess:'0'
        }
        list1.push(temp);
    }
    for(var i=0;i<33;i++){
        var temp = {

            process:2,
            id:i,
            status:true,
            error:false,
            package:false,
            fillin:false,
            buffer:0,//volume:0,
            group:0,//reject:0,
            basket:0,//box:0,
            chamberprocess:'0'
        }
        list2.push(temp);
    }
    var message = {
        action:"XH_Double_Line_Balance_config_status",
        data:{
            array1:list1,
            array2:list2
        }
    };
    return JSON.stringify(message);
}

function build_status_info(){
    var biglabel1= {
        title: "Initialize Big1",
        note: "Initialized",
        status: 0
    };
    var biglabel2= {
        title: "Initialize Big2",
        note: "Initialized",
        status: 0
    };
    var colorlist=[
        "RED",
        "ORANGE",
        "BLUE",
        "GREEN",
        "GRAY",
        "PURPLE",
        "LBLUE",
        "LGRAY",
        "DBLUE"];
    var smalllabellist=[];
    for(var i=0;i<12;i++){
        var templabel={
            key:'Label'+(i+1),
            value:{
                title:"init title"+(i+1),
                note:"note",
                color:colorlist[GetRandomNum(0,8)],
                value:GetRandomNum(0,300)+"kg"
            }
        }
        smalllabellist.push(templabel);
    }
    var ret={
        action:"XH_Double_Line_Balance_flash_status",
        data:{
            biglabel1:biglabel1,
            biglabel2:biglabel2,
            labellist:smalllabellist
        }
    }
    return JSON.stringify(ret);
}


function GetRandomNum(Min,Max)
{
    var Range = Max - Min;
    var Rand = Math.random();
    return(Min + Math.round(Rand * Range));
}