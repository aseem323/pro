function validate(){
    var name = document.getElementById("name")
    var email = document.getElementById("mail")
    var username = document.getElementById("user_name")

    if(name.value==""){
        document.getElementById('name2').innerHTML='enter name'
        name.focus()
        document.getElementById('name2').style.color="red"
        return false
    }
    if(email.value==""){
        document.getElementById("mail2").innerHTML='enter a valid email'
        email.focus()
        document.getElementById('mail2').style.color="red"
        return false
    }
    if(username.value==""){
        document.getElementById('user_name2').innerHTML='enter username'
        username.focus()
        document.getElementById('user_name2').style.color="red"
        return false
    }


}