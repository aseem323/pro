
function toggleCheck(){
    pass = document.getElementById("pass")

 if (pass.type == "password") {
   pass.type = "text";
 } else {
   pass.type = "password";
 }
}



function validation(){

    var sname1 = document.getElementById('name')
    var smail = document.getElementById('mail')
    var suname = document.getElementById('uname')
    var spass = document.getElementById('pass')
    var spass2 = document.getElementById('pass2')
    if(sname1.value==""){
        document.getElementById('name2').innerHTML="please enter name"
        sname1.focus()
        sname1.style.borderColor="red"
        document.getElementById('name2').style.color="red"
        return false

    }
    if(smail.value==""){
        document.getElementById('mail2').innerHTML="please enter email"
        smail.focus()
        smail.style.borderColor="red"
        document.getElementById('mail2').style.color="red"
        return false    
    }
    if(suname.value==""){
        document.getElementById('uname2').innerHTML="enter user name"
        suname.focus()
        suname.style.borderColor="red"
        document.getElementById('uname2').style.color="red"
        return false
    }
    if(spass.value==""){
        document.getElementById('pass_error').innerHTML="enter password"
        spass.focus()
        spass.style.borderColor="red"
        document.getElementById('pass_error').style.color="red"
        return false
    }
    if(spass.value.length<=7 && spass.value!=""){
        document.getElementById('pass_error').innerHTML="password must be 8 charecter"
        spass.focus()
        spass.style.borderColor="red"
        document.getElementById('pass_error').style.color="red"
        return false
    }
    if(spass2.value!=spass.value){
        document.getElementById('pass2_error').innerHTML="incorrect password"
        spass2.focus()
        spass2.style.borderColor="red"
        document.getElementById('pass2_error').style.color="red"
        return false
    }
}



