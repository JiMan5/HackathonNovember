    

    chosen1 = false;
    chosen2 = false;
    chosen3 = false;
    chosen4 = false;
    chosen5 = false;
    chosen6 = false;
    chosen7 = false;
    chosen8 = false;
    chosen9 = false;
    chosen10 = false;
    chosen11 = false;
    chosen12 = false;
    chosen13 = false;
    chosen14 = false;

    chosen = []

    var loginPressed = document.getElementById("Login")
    var registerPressed = document.getElementById("Register")
    var loginform = document.getElementById("loginForm");
    var registerform = document.getElementById("registerForm");
    var forms = document.getElementById("myMenu");
    var LoginButton = document.getElementById("LoginButton");
    var RegisterButton = document.getElementById("RegisterButton");
    var QuestionsButton = document.getElementById("QuestionsButton");
    var HobbiesButton = document.getElementById("HobbiesButton");
    var FinishButton = document.getElementById("FinishButton")

    

    ///////////////////////////////////////////////////////////////////

    loginPressed.onclick = function(){

        loginform.style.transition = "1s";
        registerform.style.transition = "1s";
        forms.style.transition = "1s";
        loginform.style.opacity = 1;
        registerform.style.opacity = 0;
        loginform.style.right = "0";
        registerform.style.left = "1000px";
        loginPressed.classList.add('active')
        registerPressed.classList.remove('active')
        forms.style.height = "430px";

    }

    registerPressed.onclick = function(){
        loginform.style.transition = "1s";
        registerform.style.transition = "1s";
        forms.style.transition = "1s";
        loginform.style.opacity = 0;
        registerform.style.opacity = 1;
        loginform.style.right = "1000px";
        registerform.style.left = "0px";
        loginPressed.classList.remove('active')
        registerPressed.classList.add('active')
        forms.style.height = "640px";
    }

    



    

    //////////////////////////////////////////////////////////

    userLogin = document.getElementById("usernameLoginID");
    passwordLogin = document.getElementById("passwordLoginID");


    document.getElementById('LoginButton').onclick = function(){
        flag = true;

        if (flag){
            var my_login_form = document.getElementById('loginForm');
            var loginFormData = new FormData(my_login_form);

            loginFormData.append('username',userLogin.value)
            loginFormData.append('password',passwordLogin.value)

            var xhr = new XMLHttpRequest();
            
            xhr.open('POST', '/login', true);

            xhr.addEventListener('load', function(e) {

                result = xhr.response;
                
                if(result[0]=='1'){
                    userLogin.style.backgroundImage = "url('static/images/right.png')";
                    userLogin.style.backgroundSize = "22px";
                    userLogin.style.backgroundPosition = "97% 50%";
                    userLogin.style.backgroundRepeat = "no-repeat";
                
                }

                else{
                    userLogin.style.backgroundImage = "url('static/images/remove.png')";
                    userLogin.style.backgroundSize = "22px";
                    userLogin.style.backgroundPosition = "97% 50%";
                    userLogin.style.backgroundRepeat = "no-repeat";

                }

                if(result[1]=='1'){
                    passwordLogin.style.backgroundImage = "url('static/images/right.png')";
                    passwordLogin.style.backgroundSize = "22px";
                    passwordLogin.style.backgroundPosition = "97% 50%";
                    passwordLogin.style.backgroundRepeat = "no-repeat";
                }

                else{
                    passwordLogin.style.backgroundImage = "url('static/images/remove.png')";
                    passwordLogin.style.backgroundSize = "22px";
                    passwordLogin.style.backgroundPosition = "97% 50%";
                    passwordLogin.style.backgroundRepeat = "no-repeat";
                }

                if(result[0]=='1' && result[1]=='1'){
                    window.location.href = 'main_page';   
                }
                
            });



            xhr.send(loginFormData);

        }


    }

    //////////////////////////////////////////////////////////







    check_username_register = function(val){
        return val!="";
    }

    check_mail_register = function(val){
        return val!="";
    }

    check_password_register = function(val){
        return val!="";
    }

    check_confirmPassword_register = function(val,otherVal){
        return val==otherVal;
        return otherVal!="";
    }


    user = document.getElementById("usernameID");
    mail = document.getElementById("emailID");
    password = document.getElementById("passwordID");
    confirmPassword = document.getElementById("confirmPasswordID");

    user.oninput = function(){

        if(check_username_register(user.value)){
            user.style.backgroundImage = "url('static/images/right.png')";
            user.style.backgroundSize = "22px";
            user.style.backgroundPosition = "97% 50%";
            user.style.backgroundRepeat = "no-repeat";
        }

        else{

            user.style.backgroundImage = "url('static/images/remove.png')";
            user.style.backgroundSize = "22px";
            user.style.backgroundPosition = "97% 50%";
            user.style.backgroundRepeat = "no-repeat";
        }



    }


    mail.oninput = function(){

            if(check_mail_register(mail.value)){
                mail.style.backgroundImage = "url('static/images/right.png')";
                mail.style.backgroundSize = "22px";
                mail.style.backgroundPosition = "97% 50%";
                mail.style.backgroundRepeat = "no-repeat";
            }

            else{

                mail.style.backgroundImage = "url('static/images/remove.png')";
                mail.style.backgroundSize = "22px";
                mail.style.backgroundPosition = "97% 50%";
                mail.style.backgroundRepeat = "no-repeat";
            }



    }


    password.oninput = function(){

            if(check_password_register(password.value)){
                password.style.backgroundImage = "url('static/images/right.png')";
                password.style.backgroundSize = "22px";
                password.style.backgroundPosition = "97% 50%";
                password.style.backgroundRepeat = "no-repeat";
            }

            else{

                password.style.backgroundImage = "url('static/images/remove.png')";
                password.style.backgroundSize = "22px";
                password.style.backgroundPosition = "97% 50%";
                password.style.backgroundRepeat = "no-repeat";
            }



    }


    confirmPassword.oninput = function(){

            if(check_confirmPassword_register(confirmPassword.value,password.value)){
                confirmPassword.style.backgroundImage = "url('static/images/right.png')";
                confirmPassword.style.backgroundSize = "22px";
                confirmPassword.style.backgroundPosition = "97% 50%";
                confirmPassword.style.backgroundRepeat = "no-repeat";
            }

            else{

                confirmPassword.style.backgroundImage = "url('static/images/remove.png')";
                confirmPassword.style.backgroundSize = "22px";
                confirmPassword.style.backgroundPosition = "97% 50%";
                confirmPassword.style.backgroundRepeat = "no-repeat";
            }



    }

     ///////////////////////////////////////////////////////////////////////////////







     document.getElementById("RegisterButton").onclick = function(event){

        flag = check_username_register(user.value) && check_mail_register(mail.value) &&
        check_password_register(password.value) &&
        check_confirmPassword_register(confirmPassword.value,password.value);

        

        if(flag){

        var my_form = document.getElementById("registerForm");
        var result = document.getElementById("result");

        var formData = new FormData(my_form);
        formData.append('username', user.value);
        formData.append('email', mail.value);
        formData.append('password',password.value);


        var xhr = new XMLHttpRequest();
        // Add any event handlers here...
        xhr.open('POST', '/upload', true);

        xhr.addEventListener('load', function(e) {
            var result = xhr.response;

            if(result[0]=='0'){
                user.style.backgroundImage = "url('static/images/remove.png')";
                user.style.backgroundSize = "22px";
                user.style.backgroundPosition = "97% 50%";
                user.style.backgroundRepeat = "no-repeat";
                document.getElementById("usernameLabel").style.transition = '0.5s';
                document.getElementById("usernameLabel").innerHTML = 'USERNAME (taken by other)';

            }

            else{
                user.style.backgroundImage = "url('static/images/right.png')";
                user.style.backgroundSize = "22px";
                user.style.backgroundPosition = "97% 50%";
                user.style.backgroundRepeat = "no-repeat";
                document.getElementById("usernameLabel").style.transition = '0.5s';
                document.getElementById("usernameLabel").innerHTML = 'USERNAME'
            }

            if(result[1]=='0'){
                mail.style.backgroundImage = "url('static/images/remove.png')";
                mail.style.backgroundSize = "22px";
                mail.style.backgroundPosition = "97% 50%";
                mail.style.backgroundRepeat = "no-repeat";
                document.getElementById("emailLabel").style.transition = '0.5s';
                document.getElementById("emailLabel").innerHTML = 'EMAIL (taken by other)'

            }

            else{
                mail.style.backgroundImage = "url('static/images/right.png')";
                mail.style.backgroundSize = "22px";
                mail.style.backgroundPosition = "97% 50%";
                mail.style.backgroundRepeat = "no-repeat";
                document.getElementById("emailLabel").style.transition = '0.5s';
                document.getElementById("emailLabel").innerHTML = 'EMAIL'
            }

            if(result[0]=='1' && result[1]=='1'){

                document.getElementById("myMenu").style.transition = "3s";
                document.getElementById("myMenu").style.marginLeft = "-500px";
                setTimeout(openQuestions = function(){
                    document.getElementById("myQuestions").style.transition = "3s";
                    document.getElementById("myQuestions").style.opacity = 1;
                    document.getElementById("myQuestions").style.marginLeft = "50px";

                    ipLookUp();

                }, 2000);
            }

        });

        xhr.send(formData);

        }
    };



    ////////////////////////////////////////////////////////////////////////////////////

    country = document.getElementById("countryID");
    city = document.getElementById("cityID");
    birth = document.getElementById("birthID");
    edu = document.getElementById("eduID");
    place = document.getElementById("addressID");

    check_country = function(val){
        return true;
    }

    check_city = function(val){
        return true;
    }

    check_place = function(val){
        return true;
    }

    check_edu = function(val){
        return true;
    }


    country.oninput = function(){

        if(check_country(country.value)){
            country.style.backgroundImage = "url('static/images/right.png')";
            country.style.backgroundSize = "22px";
            country.style.backgroundPosition = "97% 50%";
            country.style.backgroundRepeat = "no-repeat";
        }

        else{

            country.style.backgroundImage = "url('static/images/remove.png')";
            country.style.backgroundSize = "22px";
            country.style.backgroundPosition = "97% 50%";
            country.style.backgroundRepeat = "no-repeat";
        }

    }

    city.oninput = function(){

        if(check_city(city.value)){
            city.style.backgroundImage = "url('static/images/right.png')";
            city.style.backgroundSize = "22px";
            city.style.backgroundPosition = "97% 50%";
            city.style.backgroundRepeat = "no-repeat";
        }

        else{

            city.style.backgroundImage = "url('static/images/remove.png')";
            city.style.backgroundSize = "22px";
            city.style.backgroundPosition = "97% 50%";
            city.style.backgroundRepeat = "no-repeat";
        }

    }

    place.oninput = function(){

        if(check_place(place.value)){
            place.style.backgroundImage = "url('static/images/right.png')";
            place.style.backgroundSize = "22px";
            place.style.backgroundPosition = "97% 50%";
            place.style.backgroundRepeat = "no-repeat";
        }

        else{

            place.style.backgroundImage = "url('static/images/remove.png')";
            place.style.backgroundSize = "22px";
            place.style.backgroundPosition = "97% 50%";
            place.style.backgroundRepeat = "no-repeat";
        }

    }

    edu.oninput = function(){

        if(check_edu(edu.value)){
            edu.style.backgroundImage = "url('static/images/right.png')";
            edu.style.backgroundSize = "22px";
            edu.style.backgroundPosition = "97% 50%";
            edu.style.backgroundRepeat = "no-repeat";
        }

        else{

            edu.style.backgroundImage = "url('static/images/remove.png')";
            edu.style.backgroundSize = "22px";
            edu.style.backgroundPosition = "97% 50%";
            edu.style.backgroundRepeat = "no-repeat";
        }

    }



    QuestionsButton.onclick = function(){

        flag = check_city(city.value) && check_country(country.value) && check_place(place.value)
        && check_edu(edu.value);
        flag=true;

        if(flag){
            
            var my_second_form = document.getElementById("answers");
            

            var secondFormData = new FormData(my_second_form);

            secondFormData.append('country', country.value);
            secondFormData.append('city', city.value);
            secondFormData.append('dateOfBirth',birth.value);
            secondFormData.append('address',place.value);
            secondFormData.append('edu',edu.value);



            var xhr = new XMLHttpRequest();
            // Add any event handlers here...
            xhr.open('POST', '/second_upload', true);

            xhr.send(secondFormData);

            document.getElementById("myHobbies").style.transition = "2s";
            document.getElementById("myHobbies").style.opacity = 1;
            document.getElementById("myHobbies").style.marginLeft = "525px";
        }

    }

    ////////////////////////////////////////////////////////////////////////////////////////////////////

    Array.prototype.remove = function() {
        var what, a = arguments, L = a.length, ax;
        while (L && this.length) {
            what = a[--L];
            while ((ax = this.indexOf(what)) !== -1) {
                this.splice(ax, 1);
            }
        }
        return this;
    };

    ///////////////////////////////////////////////////////////////////////////////////////////////////////////


    document.getElementById("1").onclick = function(){
        if(!chosen1){
            document.getElementById("1").style.backgroundColor= "rgb(255,255,255,0.4)";
            chosen1=true;
            chosen.push('cinema')
        }

        else{
            document.getElementById("1").style.transition = "0.3s";
            document.getElementById("1").style.backgroundColor= "rgb(255,255,255,0)";
            chosen1=false;
            chosen.remove('cinema')
        }
    }

    document.getElementById("2").onclick = function(){
        if(!chosen2){
            document.getElementById("2").style.backgroundColor= "rgb(255,255,255,0.4)";
            chosen2=true;
            chosen.push('music')
        }

        else{
            document.getElementById("2").style.transition = "0.3s";
            document.getElementById("2").style.backgroundColor= "rgb(255,255,255,0)";
            chosen2=false;
            chosen.remove('music')
        }
    }

    document.getElementById("3").onclick = function(){
        if(!chosen3){
            document.getElementById("3").style.backgroundColor= "rgb(255,255,255,0.4)";
            chosen3=true;
            chosen.push('literature')
        }

        else{
            document.getElementById("3").style.transition = "0.3s";
            document.getElementById("3").style.backgroundColor= "rgb(255,255,255,0)";
            chosen3=false;
            chosen.remove('literature')
        }
    }

    document.getElementById("4").onclick = function(){
        if(!chosen4){
            document.getElementById("4").style.backgroundColor= "rgb(255,255,255,0.4)";
            chosen4=true;
            chosen.push('photos')
        }

        else{
            document.getElementById("4").style.transition = "0.3s";
            document.getElementById("4").style.backgroundColor= "rgb(255,255,255,0)";
            chosen4=false;
            chosen.remove('photos')
        }
    }

    document.getElementById("5").onclick = function(){
        if(!chosen5){
            document.getElementById("5").style.backgroundColor= "rgb(255,255,255,0.4)";
            chosen5=true;
            chosen.push('painting')
        }

        else{
            document.getElementById("5").style.transition = "0.3s";
            document.getElementById("5").style.backgroundColor= "rgb(255,255,255,0)";
            chosen5=false;
            chosen.remove('painting')
        }
    }

    document.getElementById("6").onclick = function(){
        if(!chosen6){
            document.getElementById("6").style.backgroundColor= "rgb(255,255,255,0.4)";
            chosen6=true;
            chosen.push('cooking')
        }

        else{
            document.getElementById("6").style.transition = "0.3s";
            document.getElementById("6").style.backgroundColor= "rgb(255,255,255,0)";
            chosen6=false;
            chosen.remove('cooking')
        }
    }

    document.getElementById("7").onclick = function(){
        if(!chosen7){
            document.getElementById("7").style.backgroundColor= "rgb(255,255,255,0.4)";
            chosen7=true;
            chosen.push('gaming')
        }

        else{
            document.getElementById("7").style.transition = "0.3s";
            document.getElementById("7").style.backgroundColor= "rgb(255,255,255,0)";
            chosen7=false;
            chosen.remove('gaming')
        }
    }

    document.getElementById("8").onclick = function(){
        if(!chosen8){
            document.getElementById("8").style.backgroundColor= "rgb(255,255,255,0.4)";
            chosen8=true;
            chosen.push('basket')
        }

        else{
            document.getElementById("8").style.transition = "0.3s";
            document.getElementById("8").style.backgroundColor= "rgb(255,255,255,0)";
            chosen8=false;
            chosen.remove('basket')
        }
    }

    document.getElementById("9").onclick = function(){
        if(!chosen9){
            document.getElementById("9").style.backgroundColor= "rgb(255,255,255,0.4)";
            chosen9=true;
            chosen.push('maths')
        }

        else{
            document.getElementById("9").style.transition = "0.3s";
            document.getElementById("9").style.backgroundColor= "rgb(255,255,255,0)";
            chosen9=false;
            chosen.remove('maths')
        }
    }

    document.getElementById("10").onclick = function(){
        if(!chosen10){
            document.getElementById("10").style.backgroundColor= "rgb(255,255,255,0.4)";
            chosen10=true;
            chosen.push('board games')
        }

        else{
            document.getElementById("10").style.transition = "0.3s";
            document.getElementById("10").style.backgroundColor= "rgb(255,255,255,0)";
            chosen10=false;
            chosen.remove('board games')
        }
    }

    document.getElementById("11").onclick = function(){
        if(!chosen11){
            document.getElementById("11").style.backgroundColor= "rgb(255,255,255,0.4)";
            chosen11=true;
            chosen.push('programming')
        }

        else{
            document.getElementById("11").style.transition = "0.3s";
            document.getElementById("11").style.backgroundColor= "rgb(255,255,255,0)";
            chosen11=false;
            chosen.remove('programming')
        }
    }

    document.getElementById("12").onclick = function(){
        if(!chosen12){
            document.getElementById("12").style.backgroundColor= "rgb(255,255,255,0.4)";
            chosen12=true;
            chosen.push('tennis')
        }

        else{
            document.getElementById("12").style.transition = "0.3s";
            document.getElementById("12").style.backgroundColor= "rgb(255,255,255,0)";
            chosen12=false;
            chosen.remove('tennis')
        }
    }

    document.getElementById("13").onclick = function(){
        if(!chosen13){
            document.getElementById("13").style.backgroundColor= "rgb(255,255,255,0.4)";
            chosen13=true;
            chosen.push('football')
        }

        else{
            document.getElementById("13").style.transition = "0.3s";
            document.getElementById("13").style.backgroundColor= "rgb(255,255,255,0)";
            chosen13=false;
            chosen.remove('football')
        }
    }

    document.getElementById("14").onclick = function(){
        if(!chosen14){
            document.getElementById("14").style.backgroundColor= "rgb(255,255,255,0.4)";
            chosen14=true;
            chosen.push('theater')
        }

        else{
            document.getElementById("14").style.transition = "0.3s";
            document.getElementById("14").style.backgroundColor= "rgb(255,255,255,0)";
            chosen14=false;
            chosen.remove('theater')
        }
    }

    ////////////////////////////////////////////////////////////////////////////////////////////////////////////


    HobbiesButton.onclick = function(){

        var my_third_form = document.getElementById('HobbiesAnswers')

        var thirdFormData = new FormData(my_third_form);

        hobbiesString = ""
        for(var i=0; i<chosen.length; i++){
            if(i>0){
                hobbiesString = hobbiesString.concat("+")
            }

            hobbiesString = hobbiesString.concat(chosen[i])
        }

        thirdFormData.append('hobbies', hobbiesString);

        var xhr = new XMLHttpRequest();
        // Add any event handlers here...
        xhr.open('POST', '/third_upload', true);

        xhr.addEventListener('load', function(e) {
            // HTTP status message
            //console.log(xhr.status);
            // request.response will hold the response from the server
            //console.log(xhr.response);

            alert(xhr.response);
        });

        xhr.send(thirdFormData);


        document.getElementById("myLastQuestions").style.transition = "2s";
        document.getElementById("myLastQuestions").style.opacity = 1;
        document.getElementById("myLastQuestions").style.marginLeft = "1045px";

    }

    //////////////////////////////////////////////////////////////////////////////////////////

    $("#profileImage").click(function(e) {
        $("#imageUpload").click();
    });

    function fasterPreview( uploader ) {
        if ( uploader.files && uploader.files[0] ){
              $('#profileImage').attr('src',
                 window.URL.createObjectURL(uploader.files[0]) );
        }
    }

    $("#imageUpload").change(function(){
        fasterPreview( this );
    });


    /////////////////////////////////////////////////////////////////////////////////////////

    FinishButton.onclick = function(){
        window.location.href = 'main_page';
    }



    var platform = new H.service.Platform({
      'apikey': 'jenaI9H36pkdZu4jdL3mM6zCwmkXr1ZM4IyHG447EzA'
    });

    var service = platform.getSearchService();

    function ipLookUp(){

        setTimeout(function(){
            if (navigator.geolocation) {
                navigator.geolocation.getCurrentPosition(findLocation);
            }
        },2000); 
    }

    function findLocation(position){
        
        service.reverseGeocode({
        
        at: position.coords.latitude+","+position.coords.longitude
        }, (result) => {
          result.items.forEach((item) => {
            place.value = item.address.houseNumber + " " + item.address.street;
            city.value = item.address.city;
            country.value = item.address.countryName;
          });
        }, alert);

        

        // service.geocode({
        // q: "23 Βίκτωρος Δουσμάνη, Θεσσαλονίκη, Ελλάδα"
        // }, (result) => {
        //   result.items.forEach((item) => {
        //     alert(item.position.lat)
        //     alert(item.position.lng)
        //   });
        // }, alert);

        
    }

    ////////////////////////////////////////////////////////////////////////////////////////////////