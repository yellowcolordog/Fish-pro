
match=[1,1,1,1,1,1] //几个登录条件,有不满足的就不能登录

function login_match(num,re){
    var login_element = '#login input:eq('+num+')'
    $(login_element).blur(function(){
        // console.log(num)
        var data =  this.value
        // 匹配相应的正则表达式,检查字符串是否合规
        var reg = re.test(data)
        if (reg){
            $(this).next().css('display','none')
            match[num] = 0 // 合规
        }else{
            $(this).next().css('display','inline')
            match[num] = 1 // 不合规
        }    
        //是手机号的话专门去数据库检查是否已存在
        if (num == 0 && reg){
            var xhr = createXhr()
            //请求地址/login_phone?login_phone=%s      
            var url = '/login_phone?login_phone='+$('#login_phone').val()
            xhr.open('get',url,false)
            
            xhr.onreadystatechange = function(){
                if (xhr.readyState == 4 && xhr.status == 200){
                    // 服务器端响应回: 手机号称已存在或通过
                    if (xhr.responseText=='1'){
                        $('#login_phone').next().html('手机号已存在')
                        $('#login_phone').next().css('display','inline')
                        match[num] = 1        
                    }else{
                        $('#login_phone').next().html('手机号格式不正确')
                        $('#login_phone').next().css('display','none')
                        match[num] = 0
                    }
                }
            } 
            xhr.send(null)
        }  
        //检查是否全部通过    
    })
}

//建立异步核心对象
function createXhr(){
    if (XMLHttpRequest){
        var xhr = new XMLHttpRequest()
        return xhr
    }else{
        return new ActiveXObject('Microsoft.XMLHTTP')
    }
}


// 重复输入密码限制:
function login_repeat_pwd(){
    $('#login input:eq(3)').blur(function(){
        var pwd = $('#login input:eq(2)').val()
        var pwd2 = $('#login input:eq(3)').val()
        if (pwd == pwd2){
            // console.log('=')
            $('#login input:eq(3)').next().css('display','none')
            match[3] = 0 
        }else{
            // console.log('!')
            $('#login input:eq(3)').next().css('display','inline')
            match[3] = 1 
        }
    })
}

//注册按钮判断:
function register(){
    if(match.indexOf(1) == -1 && $('#login input:eq(3)').val()){  
        return true;    
    }else{ 
        console.log(match)
        return false;
    }
}
function print_match(){
    console.log(match)
    console.log(match.indexOf(1))
    return false;
}