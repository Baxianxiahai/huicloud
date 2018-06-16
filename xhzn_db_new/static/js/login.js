$(document).ready(function () {
    var layer=layui.layer
    $('#Login').on('click',function () {
        var username=$("#username").val()
        var password=$('#userpass').val()
        var body={
            username:username,
            password:password,
        }
        // var data={
        //     action:'Login',
        //     body:body,
        //     type:'query',
        // }
        $.ajax({
            url:'/ajax1/',
            type:'POST',
            data:{
                action:'login',
                body:body,
                type:'query',
            },
            success:function(callback){

                var callback_dict = $.parseJSON(callback);
                console.log(callback_dict)
                if (callback_dict.status==true){
                    layer.msg(callback_dict.msg);
                    window.location.href="http://127.0.0.1:8000/ajax/"
                }else{
                    // $('#status').text(callback_dict.error);
                    // $('#status').removeClass('success').addClass('error')
                    layer.msg(callback_dict.msg);
                }
            }
        })
    });
})