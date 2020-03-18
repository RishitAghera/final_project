$(document).ready(function(){

    function username_validation(){
        $('#error_id_username').remove()
        input=$('#id_username').val()
            var pattern= /^[a-zA-Z]+[_]*[a-zA-Z0-9]*$/

            if(!pattern.test(input)){
                $('#id_username').after("<p id='error_id_username' class='text-danger'>*Username should contain first atleast one alphabet</p>")
                return false
            }else{
                return true
            }
    }

    function name_validation(){
        len=$('#id_name').val()
        var con= /^[a-zA-Z ]*$/
        $('#error_id_name').remove()
        if(!con.test(len)){
            $('#id_name').after("<p id='error_id_name' class='text-danger'>*Contains only alphabets</p>")
            return false
        }else{
            $('#error_id_name').remove()
            return true
        }
    }

    function contact_validation(){
            len=$('#id_contact').val()
            var con= /^[0-9]*$/
            $('#error_id_contact').remove()
            if((len.length>10 || len.length<10) || (!con.test(len))){
                $('#id_contact').after("<p id='error_id_contact' class='text-danger'>* Numbers only Length Must be 10 digit.</p>")
                return false
            }else{
                $('#error_id_first_name').remove()
                return true
            }
    }

    function email_validation(){
        len=$('#id_email').val()
        var con= /^[a-zA-Z_.0-9]+@[a-zA-Z]+[.]{1}[a-zA-Z]+$/
        $('#error_id_email').remove()

        if(!con.test(len)){
            $('#id_email').after("<p id='error_id_email' class='text-danger'>*Email should contains '.' after '@'</p>")
            return false
        }else{
            $('#error_id_email').remove()
            return true
        }
    }

    function password1_validation(){

        $('#error_id_password1').remove()
        len=$('#id_password1').length
        input=$('#id_password1').val()
        var pass_pat= /^[a-zA-z._@#$%&()0-9]*$/
        if((!pass_pat.test(input)) || input.length < 6 ){
            $('#id_password1').after("<p id='error_id_password1' class='text-danger'>*Length should be 6 and contain special character,number.</p>")
            return false
        }else{
            return true
        }
    }

    function password2_validation(){
        $('#error_id_password2').remove()
        pass1=$('#id_password1').val()
        pass2=$('#id_password2').val()
        if(pass2!=pass1){
            $('#id_password2').after("<p id='error_id_password2' class='text-danger'>*password does not match</p>")
        return false
        }else{
        return true
        }
    }


    function search_city(){
    //          var contact = $(this).val();
//            $('#valid').remove()
            var cityinput=$('#myInput').val()
            var countries;
              $.ajax({
                url: '/ajax/search/',
                data: {
                  'cityinput': cityinput
                },
                dataType: 'json',
                success: function (data) {
                    countries = JSON.parse(data);
                    autocomplete(document.getElementById("myInput"), countries)
                }
              });

        }


    $('#id_contact').blur(function(){
                contact_validation()
        });


    $('#id_username').blur(function(){
        username_validation()
    }   );

    $('#id_name').blur(function(){
           name_validation()
        });

    $('#id_password1').blur(function(){
            password1_validation()
         });

    $('#id_password2').blur(function(){
           password2_validation()
        });


    $('#id_email').blur(function(){
            email_validation()
        });

    $('#registration').submit(function(e){
        if(!(username_validation() && name_validation() && contact_validation() && email_validation() && password1_validation() && password2_validation())){
            e.preventDefault()
        }
        });

//    $('#myInput').blur(function(){
//        search_city()
//        });


    });

