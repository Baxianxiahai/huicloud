$(document).ready(function () {
    close_windews();
    close_dialog()
    get_menulist();
    $('#Menu_Manage').css('display','block');
    $('#menu').on('click',function () {
        close_windews();
        $('#Menu_Manage').css('display','block');
    });
    $('#action').on('click',function () {
        close_windews();
        $('#Action_Manage').css('display','block');
    });
    $('#user').on('click',function () {
        close_windews();
        $('#User_Manage').css('display','block');
    });
    $('#user_group').on('click',function () {
        close_windews();
        $('#UserGroup').css('display','block');
    });
    $('#project_group').on('click',function () {
        close_windews();
        $('#ProjectGroup').css('display','block');
    });
    $('#project').on('click',function () {
        close_windews();
        $('#Project_Manage').css('display','block');
    });
    $('#site').on('click',function () {
        close_windews();
        $('#Site_Manage').css('display','block');
    });
    $('#Menu_add').on('click',function () {
        layer.open({
            type:1,
            title:"添加菜单",
            content:$('#Menu_New'),
            closeBtn:0,
            shade: false,
            btn:['确定','取消'],
            btn1: function(){
                close_dialog();
                layer.closeAll();
            },
            btn2: function(){
                close_dialog();
                layer.closeAll();
            },
        });
    })
});
function close_dialog() {
    $('.dialog').css('display','none');
}
function close_windews(){
    $('.Menu_windows').css('display','none');
}
function get_menulist(){
    $.ajax({
        url:"/ajax/",
        type:'POST',
        data:{
            action:'MenuList',
            type:'query',
        },
        success:function (data) {
            data=JSON.parse(data)
            var codelist=data.status.code;
            var namelist=data.status.name;
            if(data.ret==true){
                bulidmenulist(codelist,namelist);
            }
        }
    });
}
function bulidmenulist(code,name) {
    // var menulist="<option value='all' selected=''>全部菜单</option>"
    var codelist="";
    var namelist="";
    for(var i=0;i<code.length;i++){
        codelist=codelist+"<option value="+code[i]+">"+code[i]+"</option>";
        namelist=namelist+"<option value="+code[i]+">"+name[i]+"</option>";
    }
    $("#Code_select").empty();
    $("#Code_select").append(codelist);
    $("#Name_select").empty();
    $("#Name_select").append(namelist);
}