window.onload = function()

{
    var root = document.forms[0].elements;
    var elementNumber;
    //text boxes
    for (elementNumber = 0; elementNumber < root.length; elementNumber++) {
        if (root[elementNumber].type == "text") {
            root[elementNumber].onfocus = function() {
                myFocus(this);
            }
            root[elementNumber].onkeyup = function() {
                text(this);
            }
        }


        //password  
        if (root[elementNumber].type == "password") {
            root[elementNumber].onfocus = function() {
                myFocus(this);
            }
            root[elementNumber].onkeyup = function() {
                password(this);
            }
        }
        // email validation
        if (root[elementNumber].type == "email") {
            root[elementNumber].onfocus = function() {
                myFocus(this);
            }
            root[elementNumber].onkeyup = function() {
                email(this);
            }
        } else if (root[elementNumber].type == "submit") {
            root[elementNumber].onclick = function() {
                return validation(root[elementNumber]);
            }
        }
    }

}



//onfocus function

function myFocus(a)

{



    var err = a.name + "error";

    if (a.value.length == 0 && !document.getElementById(err))

    {

        var errorMsg = document.createElement('span');

        errorMsg.id = err;

        errorMsg.textContent = "This is the required field";
        errorMsg.style.color = "red";

        a.parentNode.appendChild(errorMsg);

    }

}







//text boxes validation







function text(b)

{

    var type = b.getAttribute("type")

    var show = b.name + "error";

    var minLength = b.getAttribute("min");

    var maxLength = b.getAttribute("max");

    if (minLength == null) minLength = 2;

    if (maxLength == null) maxLength = 50;



    if (type == "text")

    {



        var l = b.value.length;

        if (l == 0)

        {

            document.getElementById(show).innerHTML = "&#10008; minimum 2 chars";

            document.getElementById(show).style.color = "red";

            return false;

        } else if

        (l >= minLength && l <= maxLength)

        {

            document.getElementById(show).innerHTML = "&#10004; ok";

            document.getElementById(show).style.color = "green";

            return true;

        }

    }



}







//password validation







function password(c)

{

    var type = c.getAttribute("type");

    var typ = c.getAttribute("id")

    var show = c.name + "error";

    var minLength = c.getAttribute("min");

    var maxLength = c.getAttribute("max");

    var todo = document.getElementById("password");

    var todo2 = document.getElementById("conformpassword");

    if (minLength == null) minLength = 6;

    if (maxLength == null) maxLength = 12;

    if (typ == "conformpassword")

    {

        // atleast 2 digits,letters,special chars

        var l = c.value.length;

        if (l == 0)

        {

            document.getElementById(show).innerHTML = "&#10008; enter minimum 6 chars";



            return false;

        } else if (todo.value !== todo2.value) {

            document.getElementById(show).innerHTML = "&#10008; Password Not Matched";

            document.getElementById(show).style.color = "red";

            return false;

        } else if (todo.value == todo2.value) {

            document.getElementById(show).innerHTML = "&#10004; Password matched";

            document.getElementById(show).style.color = "green";

            return true;

        }

    } else {

        var l = c.value.length;

        if (l == 0)

        {

            document.getElementById(show).innerHTML = "&#10008; enter minimum 6 chars";

            document.getElementById(show).style.color = "red";

            return false;

        } else if (l >= minLength && l <= maxLength)

        {

            document.getElementById(show).innerHTML = "&#10004; ok";

            document.getElementById(show).style.color = "green";

            return true;

        }



    }

}









//Email validation









function email(e)

{

    var type = e.getAttribute("type");

    var show = e.name + "error";

    if (type == "email")

    {

        var match = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;

        var l = e.value.length;

        if (l == 0)

        {

            document.getElementById(show).innerHTML = "&#10008; Not Empty";

            document.getElementById(show).style.color = "red";

            return false;

        }

        if (l > 0 && match.test(e.value) == false)

        {

            document.getElementById(show).innerHTML = "&#10008; Enter a valid email address";

            document.getElementById(show).style.color = "red";

            return false;

        }

        if (l > 0 && match.test(e.value) == true)

        {

            document.getElementById(show).innerHTML = "&#10004; ok";

            document.getElementById(show).style.color = "green";

            return true;

        }

    }

}







//Form Validation







function validation(form)

{

    var x = document.forms[0].elements;


    for (var i = 0; i < x.length; i++)

    {

        var funRegex = /^[A-Za-z0-9 ]/;

        var match = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;

        var type = x[i].type;

        var minLength = x[i].getAttribute("min");

        var maxLength = x[i].getAttribute("max");



        if (type == "text")

        {

            if (minLength == null) minLength = 2;

            if (maxLength == null) maxLength = 50;

            if (x[i].value.length < minLength || x[i].value.length > maxLength)

            {

                x[i].focus();

                x[i].style.border = "1px solid #990033";

                return false;

            } else if (x[i].value.length > minLength && x[i].value.length < maxLength && funRegex.test(x[i]).value == false)

            {

                x[i].focus();

                x[i].style.border = "1px solid #990033";

                return false;

            }

        } else if (type == "email")

        {



            if (x[i].value.length == 0)

            {

                x[i].focus();

                x[i].style.border = "1px solid #990033";

                return false;

            }



            if (match.test(x[i].value) != true)

            {

                x[i].focus();

                x[i].style.border = "1px solid #990033";

                return false;

            }



        } else if (type == "password")

        {

            if (minLength == null) minLength = 6;

            if (maxLength == null) maxLength = 12;

            if (x[i].value.length < minLength || x[i].value.length > maxLength || x[i].value.length == 0)

            {

                x[i].focus();

                x[i].style.border = "1px solid pink";

                return true;

            } else if (x[i].value.length > minLength && x[i].value.length < maxLength)

            {

                x[i].focus();

                x[i].style.border = "1px solid yellow";

                return true;

            }

        }



    }


}
