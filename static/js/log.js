function validate(){
    name1=document.getElementById('exampleInputEmail1')
    pass=document.getElementById('exampleInputPassword1')
    check=document.getElementById('exampleCheck1')
    if(name1.value==""){
        document.getElementById('name2').innerHTML='enter name'
        name1.style.borderColor="red"
        return false
    }
    if(pass.value==""){
        document.getElementById('pass2').innerHTML='enter password'
        pass.style.borderColor="red"
        return false
    }
    if(pass.value.length<=8 && pass.value!=""){
        document.getElementById('pass2').innerHTML='password must be 8 charecter'
        return false
    }
    
}
function checked(){
    pass.type="text"
}

