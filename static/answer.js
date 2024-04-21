//get the text that is highlighted by the user
//print out the text that they highlighted in a text box

document.addEventListener("DOMContentLoaded", function() {
    var num = 0;
    function getSelectedText() {
        if(num%2!=0){ // for some reason it runs the mouse up twice so we divide each click 
        var selectedText = '';
        if (window.getSelection) {
            selectedText = window.getSelection().toString();
        }
        const div = document.querySelector("div");
        $.ajax({
            url: '/further/' + selectedText, // getting the definitions from flask
            success: function(response) {
                div.innerHTML = "";
                console.log('Result:', response); // trubleshooting
                for (var i = 0; i < response.length; i++) {
                    div.innerHTML = div.innerHTML + "\n" + response[i]; // easier to read formatting
                }
            }
        });
    }
    num++;
        
    }
    
    $(document).mouseup(getSelectedText); // listening for mouseup input


});


