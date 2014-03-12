function updateDefinition() {
    var word = getSelectionText();
    
    $.ajax(
        {'url':'https://api.duckduckgo.com/?q=define+' + word + '&format=json',
        'type':'GET', 
        dataType:'json', 
        success: function(x) {

            var definition = x.Definition;
            var string_elem = "<div id = 'dictionary_extension_definition'>" + definition + "</div>";
            $(string_elem).appendTo('body').fadeOut(5000, function(){ $(this).remove(); });
            }
        });
    }
            
function getSelectionText() {
    var text = "";
    if (window.getSelection) {
        text = window.getSelection().toString();
        } 
    else if (document.selection && document.selection.type != "Control") {
        text = document.selection.createRange().text;
        }
    return text;
    } 
    
$(document).ready(function() {
    var a_is_pressed = false;
    var d_is_pressed = false;
    $(document.body).keydown(function (evt) {
        if (evt.keyCode == 65) { 
            a_is_pressed = true;
            }
        
        if (evt.keyCode == 68) {
            d_is_pressed = true;
            }
        
        if (a_is_pressed && d_is_pressed) {
            updateDefinition();
        }         
    });

    $(document.body).keyup(function (evt) {
        if (evt.keyCode == 65) { 
            a_is_pressed = false;
        }
        
        if (evt.keyCode == 68) {
            d_is_pressed = false;
        }
    });    
});
