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
String.prototype.hexDecode = function(){
    var j;
    var hexes = this.match(/.{2}/g) || [];
    var back = "";
    for(j = 0; j<hexes.length; j++) {
        back += String.fromCharCode(parseInt(hexes[j], 16));
    }
    return back;
}

String.prototype.hexEncode = function(){
    var hex, i;
    var result = "";
    for (i=0; i<this.length; i++) {
        hex = this.charCodeAt(i).toString(16);
        if (hex.length < 2) {
            hex = '0'+hex
            result += (hex).slice(-4);
        }else {
            result += (hex).slice(-4);
        }
    }
    return result
}
//var output = xssfilter.filter('<div class="like" ondblclick="takeme()" onmousedown="mousedown()">something...</div>');
//-------------------- LOGIN FORM -------------------------//
function login() {
    var address = $('#email').val().trim();
    var passw = $('#password').val().trim();
    if (address && passw && address.match(/[\w\_\-\.]+\@[\w\_\-\.]+\.\w\w\w?\w?/g) !== null) {
        $.post( "login.js", { email: address, password: passw }).done(function( result ) {
            //RETURN A JSON bool value of true if the email and password is correct. false if incorrect
            if (result.bool) {
                $('#email').val('');
                $('#password').val('');
                Materialize.toast('Correct. Logging in now!', 4000);
                setTimeout(function(){
                    //redirect to home.html. This needs to be locked down by cookies!
                    window.location.href = 'account.html';
                }, 1000);
            } else {
                Materialize.toast(result.result, 4000);
            }
        }).fail(function(error) {
            Materialize.toast('Error: '+error.status + " " + error.statusText, 4000);
        })
    } else {
        Materialize.toast('You must put in a correct email and password!', 4000);
    }
}
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
$('.loginlogo').click(function(){
    window.location.href='/';
});
//------------------ Pulling User Mail ------------------//
var theinbox = {};
var thesent = {};
var theuser = '';
function inbox_msg(theid){
    var i = parseInt(theid);
    $('#from').html(filterXSS(theinbox[i].HEADERS.body.from[0].replace(/\"/g,'').split(' ')[0]));
    $('#to').html(filterXSS(theinbox[i].HEADERS.body.to[0]));
    $('#date').html(filterXSS(theinbox[i].HEADERS.body.date[0]));
    $('#subject').html(filterXSS(theinbox[i].HEADERS.body.subject[0].replace(/\*\*\*UNCHECKED\*\*\*/g,'')));
    $('#body').html('<pre>'+filterXSS(theinbox[i].BODY.body)+'</pre>');
    $('#overlay').css('display','flex');
};
function sent_msg(theid){
    var i = parseInt(theid);
    $('#from').html(filterXSS(thesent[i].HEADERS.body.from[0].replace(/\"/g,'').split(' ')[0]));
    $('#to').html(filterXSS(thesent[i].HEADERS.body.to[0]));
    $('#date').html(filterXSS(thesent[i].HEADERS.body.date[0]));
    $('#subject').html(filterXSS(thesent[i].HEADERS.body.subject[0].replace(/\*\*\*UNCHECKED\*\*\*/g,'')));
    $('#body').html('<pre>'+filterXSS(thesent[i].BODY.body)+'</pre>');
    $('#overlay').css('display','flex');
};
function retrieve_mail(){
    $.post( "api.js", { getmail: 'getmail'}).done(function( result ) {
        theinbox = result.INBOX;
        thesent = result.SENT;
        theuser = result.USER;
        $('#from_email').val(theuser);
        $('#INBOXTABLE').html('');
        $('#SENTTABLE').html('');
        for (var i=0; i < result.INBOX.length; i++) {
            var inbox_from = result.INBOX[i].HEADERS.body.from[0];
            var inbox_to = result.INBOX[i].HEADERS.body.to[0]; 
            var inbox_subject = result.INBOX[i].HEADERS.body.subject[0];
            var inbox_body = result.INBOX[i].BODY.body;
            var inbox_date = result.INBOX[i].HEADERS.body.date[0]
            $('#INBOXTABLE').append("<tr onclick='inbox_msg("+i+")'><td>"+filterXSS(inbox_from.replace(/\"/g,'').split(' ')[0])+"</td><td>"+filterXSS(inbox_to)+"</td><td>"+filterXSS(inbox_subject).replace(/\*\*\*UNCHECKED\*\*\*/g,'').substring(0, 12)+"</td><td>"+filterXSS(inbox_body).substring(0, 12)+"</td><td>"+filterXSS(inbox_date.substring(0, 25))+"</td></tr>");
        }
        for (var j=0; j < result.SENT.length; j++) {
            var sent_from = result.SENT[j].HEADERS.body.from[0];
            var sent_to = result.SENT[j].HEADERS.body.to[0]; 
            var sent_subject = result.SENT[j].HEADERS.body.subject[0];
            var sent_body = result.SENT[j].BODY.body;
            var sent_date = result.SENT[j].HEADERS.body.date[0]
            $('#SENTTABLE').append("<tr onclick='sent_msg("+j+")'><td>"+filterXSS(sent_from.replace(/\"/g,'').split(' ')[0])+"</td><td>"+filterXSS(sent_to)+"</td><td>"+filterXSS(sent_subject).replace(/\*\*\*UNCHECKED\*\*\*/g,'').substring(0, 12)+"</td><td>"+filterXSS(sent_body).substring(0, 12)+"</td><td>"+filterXSS(sent_date.substring(0, 25))+"</td></tr>");
        }
    }).fail(function(error) {
        Materialize.toast('Error: '+error.status + " " + error.statusText, 4000);
    });
};
$(document).mouseup(function(e) {
    var container = $('#innerinner');
    if (!container.is(e.target) && container.has(e.target).length === 0) {
        $('#overlay').css('display','none');
    }
});
function send_email(){
    var to = $('#to_email').val().trim();
    var subject = $('#write_subject').val().trim();
    var message = $('#textarea1').val().hexEncode();
    if (to && to.match(/[\w\_\-\.]+\@[\w\_\-\.]+\.\w\w\w?\w?/g) !== null) {
        if (subject && subject.length > 4) {
            if (message && message.length > 4) {
                $.post( "api.js", { from_email: theuser, to_email: to, subject_email: subject, message_email: message}).done(function( result ) {
                    if (result.bool) {
                        $('#to_email').val('');
                        $('#write_subject').val('');
                        $('#textarea1').val('');
                        Materialize.toast(result.result, 4000);
                    } else {
                        Materialize.toast(result.result, 4000);
                    }
                }).fail(function(error) {
                    Materialize.toast('Error: '+error.status + " " + error.statusText, 4000);
                });
            } else {
                Materialize.toast('You must put a message!', 4000);
            }
        } else {
            Materialize.toast('You must put a subject!', 4000);
        }
    } else {
        Materialize.toast('You must have a valid to email address!', 4000);
    }
};
$('#send_email').click(function(){
    send_email();
});
