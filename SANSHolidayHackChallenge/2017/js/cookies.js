//FOUND THESE FOR creating and validating cookies. Going to use this in node js
var aes256 = require('aes256');
    function cookie_maker(username){
        var key = 'A';
        //randomly generates a string of 5 characters
        var plaintext = ''
        //makes the string into cipher text .... in base64. When decoded this 21 bytes in total length. 16 bytes for IV and 5 byte of random characters
        //Removes equals from output so as not to mess up cookie. decrypt function can account for this without erroring out.
        //var ciphertext = aes256.encrypt(key, plaintext).replace(/\=/g,'');
	var ciphertext = 'AAAAAAAAAAAAAAAAAAAAAA';
        //Setting the values of the cookie.
        var json_string = JSON.stringify({"name":username, "plaintext":plaintext,  "ciphertext":ciphertext})
        return json_string;
    };
    function cookie_checker(json_string){
        try{
            var key = 'dgfdgfg';
            //Retrieving the cookie from the request headers and parsing it as JSON
     	    // var thecookie = JSON.parse(req.cookies.IOTECHWEBMAIL);
            var thecookie = JSON.parse(json_string);
            //Retrieving the cipher text 
            var ciphertext = thecookie.ciphertext;
            //Retrievingin the username
            var username = thecookie.name
            //retrieving the plaintext
            var plaintext = aes256.decrypt(key, ciphertext);
            //If the plaintext and ciphertext are the same, then it means the data was encrypted with the same key
            if (plaintext === thecookie.plaintext) {
                console.log(username);
            } else {
                console.log('false');
            }
        } catch (e) {
            console.log(e);
        }
    };
var mystring = '';
console.log('Here is the created cookie...')
mystring = cookie_maker('gdpr@northpolechristmastown.com');
console.log(mystring);
console.log('\n Cookie checker is next...')
cookie_checker(mystring);
