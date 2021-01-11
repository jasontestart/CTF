//------------------- Common Initializations -------------------//
$(document).ready(function(){
    $('.slider').slider();
});
$(document).ready(function(){
    $('.tooltipped').tooltip({delay: 50});
});
$(document).ready(function() {
    $('select').material_select();
});
$(document).ready(function(){
    $('.collapsible').collapsible();
});
//-------------------- LOGIN FORM -------------------------//
function login() {
    var uname = $('#username').val().trim();
    var passw = $('#password').val().trim();
    if (uname && passw) {
        $.post( "/login", { username: uname, password: passw }).done(function( result ) {
            if (result.bool) {
                Materialize.toast(result.message, 4000);
                localStorage.setItem('np-auth',result.token)
                setTimeout(function(){
                    window.location.href = result.link;
                }, 1000);
            } else {
                Materialize.toast(result.message, 4000);
            }
        }).fail(function(error) {
            Materialize.toast('Error: ' + error.status + " " + error.statusText, 4000);
        })
    } else {
        Materialize.toast('You must input a valid username and password!', 4000);
    }
}
// -------------------- All the clicks ---------------------------//
$('#login_button').click(function(){
    login();
});
$('#password').keyup(function(e){
    if ( e.which == 13) {
        login();
    }
});
$('#email').keyup(function(e){
    if ( e.which == 13) {
        login();
    }
});
$(document).keyup(function(e) {
    if (e.keyCode == 27) {
        $('.overlay').css('display','none');
    }
});
$(document).on( 'click', '#exit_overlay',function(){
    $('.overlay').css('display','none');
});
$('#help').click(function(e) {
    e.preventDefault();
    $('.overlay').css('display','flex');
});
$('#logout').click(function(e){
    if (confirm('Are you sure you would like to logout?')) {
        e.preventDefault();
        localStorage.removeItem('np-auth')
        window.location.href = '/index.html'
    }
});
// --------------------------Customer Service Request -----------------------------/
$('#help_button').click(function(e){
    e.preventDefault();
    var help_uid = $('#help_uid').val();
    var help_email = $('#help_email').val();
    var help_message = $('#help_message').val();
    if (help_uid.match(/^\w+\.\w+$/g) != null){
        if (help_email.match(/^[\w\_\-\.]+\@[\w\_\-\.]+\.\w\w\w?\w?$/g) !== null){
            if (help_message.match(/^.+$/g) != null) {
                if (help_message.match(/[sS][cC][rR][iI][pP][tT]/g) == null) {
                    $.post( "/service", { uid: help_uid, email: help_email, message: help_message }).done(function( result ) {
                        Materialize.toast('Submitting... Please Wait.', 4000);
                        if (result.bool) {
                            Materialize.toast(result.message, 4000);
                            setTimeout(function(){
                                window.location.href = result.link;
                            }, 1000);
                        } else {
                            Materialize.toast(result.message, 4000);
                        }
                    }).fail(function(error) {
                        Materialize.toast('Error: '+error.status + " " + error.statusText, 4000);
                    })
                } else {
                    Materialize.toast('Alert, Hacker!', 4000);
                }
            } else {
                Materialize.toast('You must enter a message!', 4000);
            }                   
        } else {
            Materialize.toast('Invalid email format!', 4000);
        }
    } else {
        Materialize.toast('Invalid User Id Format! ex- first.last', 4000);
    }
});

