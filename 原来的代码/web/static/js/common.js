
//建立异步核心对象
function createXhr(){
    if (XMLHttpRequest){
        var xhr = new XMLHttpRequest()
        return xhr
    }else{
        return new ActiveXObject('Microsoft.XMLHTTP')
    }
}
