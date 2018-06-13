$(document).ready(function () {
    $('#Login').on('click',function () {
        var username=$("#username").val()
        var password=$('#userpass').val()
        var body={
            username:username,
            password:password,
        }
        $.ajax({
            url:'/ajax/',
            type:'POST',
            data:{
                action:'Login',
                body:body,
                type:'query',
            },
            success:function(callback){
                var callback_dict = $.parseJSON(callback);
                if (callback_dict.status==1002){
                    $('#status').text('success');
                    $('#status').removeClass('error').addClass('success');
                }else if(callback_dict.status == 1001){
                    $('#status').text(callback_dict.error);
                    $('#status').removeClass('success').addClass('error')
                }
            }
        })
    });
})