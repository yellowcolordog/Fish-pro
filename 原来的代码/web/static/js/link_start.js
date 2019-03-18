$(function(){
    
})


function link_check(){
    var phone = $('#link_start [name="link_phone"]').val()
    var pwd = $('#link_start [name="link_pwd"]').val()
    // console.log(phone,pwd)
    if (/^\d{11}$/.test(phone) && /^\w{6,16}$/.test(pwd)){ //账号和密码符合格式
        var xhr = createXhr()
        // console.log($('#auto_login').prop('checked'))
        //请求地址 /login_phone?login_phone=
        var url = '/login_phone'
        xhr.open('post',url,false)
        xhr.setRequestHeader('Content-Type','application/x-www-form-urlencoded')        
        xhr.onreadystatechange = function(){
            if (xhr.readyState == 4 && xhr.status == 200){
                var data = xhr.responseText
                if (data =='0'){
                    $('#link_tip').html('账号或密码错误')
                }else{
                    $('#link_tip').html('登录成功,3秒后跳转<a href="http://www.baidu.com">主页</a>')
                }
            }
        }
        var data = 'login_phone='+phone+'&login_pwd='+pwd+'&auto_login='+$('#auto_login').prop('checked')
        xhr.send(data)
    }else{
        $('#link_tip').html('数据格式不正确')
    }

}