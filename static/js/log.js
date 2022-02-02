function validate(){
    name1=document.getElementById('exampleInputEmail1')
    pass=document.getElementById('exampleInputPassword1')
    
    if(name1.value==""){
        document.getElementById('name2').innerHTML='enter name'
        name1.focus()
        name1.style.borderColor="red"
        document.getElementById('name2').style.color="red"
        return false
    }
    if(pass.value==""){
        document.getElementById('pass2').innerHTML='enter password'
        pass.focus()
        document.getElementById('pass2').style.color="red"
        pass.style.borderColor="red"
        return false
    }
    if(pass.value.length<=7 && pass.value!=""){
        document.getElementById('pass2').innerHTML='wrong password'
        pass.focus()
        document.getElementById('pass2').style.color="red"
        return false
    }
    
}

function toggleCheck() {
//pass=document.getElementById('exampleInputPassword1')
  // pass.type="text"
  // console.log("test");
  var pass = document.getElementById("exampleInputPassword1")

  if (pass.type == "password") {
    pass.type = "text";
  } else {
    pass.type = "password";
  }
}
