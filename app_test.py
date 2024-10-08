import pytest

from app import app


@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client


def test_index_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert (b'<!DOCTYPE html>\n<html lang="en">\n<head>\n    <title>BuyAdvisor - Home</ti'
            b'tle>\n    <link rel="stylesheet" href="../static/css/homepage.css">\n    <'
            b'link rel="stylesheet" href="../static/css/logo.css">\n    <style type="te'
            b'xt/css">\n        .content{\n            float: left;\n        }\n    </styl'
            b'e>\n</head>\n<body>\n    <div class="main">\n        <div class="navbar"'
            b'>\n            <img id="icon" src="../static/img/Icon.png" onclick="locat'
            b'ion.href=\'/\'" alt="Logo">\n            <div class="btn">\n                '
            b'<button class="loginBtn" onclick="location.href=\'/signIn\'">Log in / Regi'
            b'ster</button>\n            </div>\n        </div>\n\n        <div class="con'
            b'tent">\n            <p class= "par" style = "background-color: rgba(0, 0,'
            b' 0, 0.4); padding: 0.5%">\n                <span> <!--BuyAdvisor: </span>'
            b' --> Your Ultimate Shopping Assistant!</span> Sifting through overwhelmi'
            b'ng,\n                     prejudiced, and untrustworthy product reviews i'
            b's a hard   undertaking in the age of internet buying.\n                  '
            b'   We recognize the time and effort required to make intelligent choices. Th'
            b"at's why our website uses\n                     cutting-edge technologies"
            b' to evaluate  product reviews, assigning a score to each product to make'
            b'\n                     your purchasing decisions easier. Bid farewell to '
            b'uncertainty and hello to  efficient, effective purchasing!\n             '
            b'        Trust BuyAdvisor to save time and make better decisions.<br>\n   '
            b'         </p>\n        </div>\n    </div>\n</body>\n</html>') in response.data


def test_login_page(client):
    response = client.get('/signIn')
    assert response.status_code == 200
    assert (b'<!DOCTYPE html>\n<html lang="en">\n<head>\n    <title>Login</title>\n    <li'
            b'nk rel="stylesheet" href="../static/css/login.css">\n    <link rel="style'
            b'sheet" href="../static/css/logo.css">\n    \n</head>\n<body>\n    <div class'
            b'="main">\n        <div class="navbar">\n            <img id="icon" src="..'
            b'/static/img/Icon.png" onclick="location.href=\'/\'" alt="Logo">\n    \n     '
            b'       <div class="hero">\n                <div class="form-box">\n       '
            b'             <div class="button-box">\n                        <div id="b'
            b'tn"></div>\n                        <button type="button" class="toggle-b'
            b'utton" onclick="login()">Log In</button>\n                        <button'
            b' type="button" class="toggle-button" onclick="register()">Register</butt'
            b'on>\n                    </div>\n                    <p style="color: red;'
            b' font-style: italic; text-align: center" id="messageValidation">\n       '
            b'                 \n                            \n                        \n'
            b'                    </p>\n                    <form id="login" class="inp'
            b'ut-group" action="/signIn" method="post">\n                        <input'
            b' type="email" class="input-field" placeholder="Email" name="email" required>'
            b'\n                        <input type="password" class="input-field" plac'
            b'eholder="Password" name="password" required>\n                        <bu'
            b'tton type="submit" class="submit-btn">Log In</button>\n                  '
            b'  </form>\n                </div>\n            </div>\n        </div>\n    <'
            b'/div>\n\n    <script>\n\n        var x = document.getElementById("login"'
            b');\n        var y = document.getElementById("register");\n        var z = '
            b'document.getElementById("btn");\n\n        x.style.left = "50px";\n        '
            b'//y.style.left = "450px";\n        z.style.left = "0";\n\n        function '
            b'register() {\n            x.style.left = "-400px";\n            //y.style.'
            b'left = "50px";\n            z.style.left = "110px";\n            location.'
            b'href="/register"\n\n        }\n\n        function login() {\n            '
            b'x.style.left = "50px";\n            //y.style.left = "450px";\n           '
            b' z.style.left = "0";\n            location.href="/signIn"\n        }\n    <'
            b'/script>\n</body>\n</html>') in response.data


def test_register_page(client):
    response = client.get('/register')
    assert response.status_code == 200
    assert (b'<!DOCTYPE html>\n<html>\n<head>\n    <title>Register</title>\n    <link rel='
            b'"stylesheet" href="../static/css/login.css">\n    <link rel="stylesheet" '
            b'href="../static/css/logo.css">\n\n</head>\n<body>\n    <div class="main"'
            b'>\n        <div class="navbar">\n            <img id="icon" src="../static'
            b'/img/Icon.png" onclick="location.href=\'/\'" alt="Logo">\n            <div '
            b'id="Modal" class="modal">\n            <!-- Modal content -->\n           '
            b'     <div class="modal-content">\n                    <span class="close"'
            b'>&times;</span>\n                    <p id="msg">\n                    </p'
            b'>\n                </div>\n            </div>\n            <div class="hero'
            b'">\n                <div class="form-box">\n                    <div class'
            b'="button-box">\n                        <div id="btn"></div>\n            '
            b'            <button type="button" class="toggle-button" onclick="login()">Lo'
            b'g In</button>\n                        <button type="button" class="toggl'
            b'e-button" onclick="register()">Register</button>\n                    </d'
            b'iv>\n                    <div>\n                        <p style="color: r'
            b'ed; font-style: italic; text-align: center" id="messageValidation">\n    '
            b'                        \n                                \n              '
            b'              \n                        </p>\n                    </div>\n '
            b'                   <form id="register" class="input-group" action="/register'
            b'" method="post">\n                        <input type="text" class="input'
            b'-field" placeholder="First Name" name="firstName" required>\n            '
            b'            <input type="text" class="input-field" placeholder="Last Name" n'
            b'ame="lastName" required>\n                        <input type="email" cla'
            b'ss="input-field" placeholder="Email" name="email" required>\n            '
            b'            <input type="password" class="input-field" placeholder="Password'
            b'" name="password" id="password" required>\n                        <input'
            b' type="password" class="input-field" placeholder="Confirm Password" name="co'
            b'nfirm_password" id="confirm_password" required>\n\n                       '
            b' <button type="submit" class="submit-btn" id="register-btn">Register</button'
            b'>\n                    </form>\n                </div>\n            </div>\n'
            b'        </div>\n    </div>\n\n    <script>\n\n        //var x = document.'
            b'getElementById("login");\n        var y = document.getElementById("regist'
            b'er");\n        var z = document.getElementById("btn");\n\n        var passw'
            b'ord = document.getElementById("password"), confirm_password = document.getEl'
            b'ementById("confirm_password");\n\n        function validatePassword(){\n   '
            b'         if(password.value !== confirm_password.value) {\n               '
            b' confirm_password.setCustomValidity("Passwords Don\'t Match");\n          '
            b"  } else {\n                confirm_password.setCustomValidity('');\n     "
            b'       }\n        }\n\n        //x.style.left = "-400px";\n        y.style.l'
            b'eft = "50px";\n        z.style.left = "110px";\n\n        function register'
            b'() {\n            //x.style.left = "-400px";\n            y.style.left = "'
            b'50px";\n            z.style.left = "110px";\n            location.href="/r'
            b'egister"\n\n        }\n\n        function login() {\n            //x.styl'
            b'e.left = "50px";\n            y.style.left = "450px";\n            z.style'
            b'.left = "0";\n            location.href="/signIn"\n        }\n\n        pass'
            b'word.onchange = validatePassword;\n        confirm_password.onkeyup = val'
            b'idatePassword;\n\n        var modal = document.getElementById("Modal");\n  '
            b'      var btn = document.getElementById("register-btn");\n        var spa'
            b'n = document.getElementsByClassName("close")[0];\n        var flag;\n\n\n   '
            b'     var message = document.getElementById("messageValidation").innerHTM'
            b'L;\n        document.getElementById("messageValidation").style.visibility'
            b' = "hidden";\n\n        if(message.includes("This email login already exis'
            b'ts. Please register using a different email address")){\n            docu'
            b'ment.getElementById("messageValidation").style.visibility = "visible";\n '
            b'           flag = 0;\n            setTimeout(function(){\n                '
            b'redirectPage();\n            },2000);\n        }\n        else if(message.i'
            b'ncludes("Error while registering the account. Please try again")){\n     '
            b'       document.getElementById("messageValidation").style.visibility = "visi'
            b'ble";\n            flag = 0;\n            setTimeout(function(){\n         '
            b'       redirectPage();\n            },2000);\n        }\n        else if(me'
            b'ssage.includes("Successfully registered. Please log in to use our services."'
            b')){\n            document.getElementById("msg").innerHTML = message;\n    '
            b'        document.getElementById("messageValidation").style.visibility = "hid'
            b'den";\n            modal.style.display = "block";\n            flag = 1;\n '
            b'           setTimeout(function(){\n                redirectPage();\n      '
            b'      },2000);\n        }\n\n        // When the user clicks on <span> (x),'
            b' close the modal\n        span.onclick = function() {\n          modal.sty'
            b'le.display = "none";\n          redirectPage();\n        }\n\n        // Whe'
            b'n the user clicks anywhere outside the modal, close it\n        window.on'
            b'click = function(event) {\n          if (event.target === modal) {\n      '
            b'      modal.style.display = "none";\n            redirectPage();\n        '
            b'  }\n        }\n\n        function redirectPage(){\n            if (flag ==='
            b' 1)\n                location.href = "/signIn"\n        }\n\n    </scrip'
            b't>\n</body>\n</html>') in response.data


def test_dashboard_page(client):
    response = client.get('/dashboard')
    assert response.status_code == 200
    assert (b'<!DOCTYPE html>\n<html lang="en">\n<head>\n    \n    <link rel="stylesheet" '
            b'href="../static/css/reviewProduct.css">\n    <link rel="stylesheet" href='
            b'"https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.'
            b'min.css">\n    <link rel="stylesheet" href="https://www.w3schools.com/w3c'
            b'ss/4/w3.css">\n\n    <link rel="stylesheet" href="../static/css/dashboard.'
            b'css">\n    <link rel="stylesheet" href="../static/css/logo.css">\n    <lin'
            b'k rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">\n    '
            b'<link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Materi'
            b'al+Icons">\n    <link rel="stylesheet" href="https://cdnjs.cloudflare.com'
            b'/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">\n</head>\n<body>\n'
            b'    <div class="main">\n        <div class="navigationBar">\n            <'
            b'img id="icon" src="../static/img/Icon.png" onclick="location.href=\'/dash'
            b'board\'" alt="Logo">\n            <div class="dropdown">\n                <'
            b'i class=\'w3-xlarge fa fa-user\' id="user" style="color:white"></i>\n      '
            b'          <p id="nameOfUser"></p>\n                <div class="dropdown-c'
            b'ontent">\n                    <a href="/editProfile">Edit Profile</a>\n   '
            b'                 <a href="/searchHistory">Search History</a>\n           '
            b'         <a href="/signOut">Log Out</a>\n                </div>\n         '
            b'   </div>\n            <a id="home" href="/dashboard" style=""><i class="'
            b'fa fa-home" style="font-size:36px;color:white"></i></a>\n        </div>\n '
            b'       <div id="Modal" class="modal">\n            <!-- Modal content -->'
            b'\n            <div class="modal-content">\n                <span class="cl'
            b'ose" id="closeModal">&times;</span>\n                <i class="material-i'
            b'cons" style="font-size:36px;" id="error_icon">error_outline</i><p id="msg" s'
            b'tyle="font-weight: bold"></p>\n            </div>\n        </div>\n        '
            b'<!-- Modal block for analyzed products -->\n        <div id="Modal2" clas'
            b's="modal">\n            <div class="modal-content">\n                <span'
            b' class="close" id="closeModal2">&times;</span>\n                <p id="ms'
            b'g2" style="font-weight: bold"></p>\n                <br>\n                '
            b'<div id="Positive" class="w3-container w3-padding-large w3-green w3-center w'
            b'3-text-black" style="width:0%; font-weight: bold;">0% Positive</div>\n   '
            b'             <br>\n                <div id="Negative" class="w3-container'
            b' w3-padding-large w3-red w3-center w3-text-black" style="width:0%; font-weig'
            b'ht: bold;">0% Negative</div>\n                <br>\n            </div>\n   '
            b'     </div>\n        <!-- Modal block for Search History -->\n        <div'
            b' id="Modal3" class="modal">\n            <!-- Modal content -->\n         '
            b'   <div class="modal-content">\n                <span class="close" id="c'
            b'loseModal3">&times;</span>\n                <br>\n                <p id="m'
            b'sg3" style="font-weight: bold"></p>\n                <br>\n               '
            b' <a onclick="copyToClipboard()"><i class="w3-xlarge w3-display-bottommiddle '
            b'fa fa-clipboard" id="displayClipboard" style="visibility: hidden; padding-bo'
            b'ttom: 3%;"></i></a>\n                <p id="copiedMsg" style="text-align:'
            b' center; visibility: hidden">Copied to Clipboard!</p>\n            </div>'
            b'\n        </div>\n        <div>\n            \n    <div>\n        <p styl'
            b'e="color: red; font-style: italic; text-align: center; visibility: hidden" i'
            b'd="messageValidation">\n            \n                \n            \n      '
            b'  </p>\n        <p id="messageValidation2">\n            \n                '
            b'\n            \n        </p>\n        <p id="messageValidation3">\n         '
            b'   \n                \n            \n        </p>\n    </div>\n    <div c'
            b'lass="wrap">\n        <div class="search">\n            <form action="/rev'
            b'iewProduct" method="get">\n                <input type="text" class="sear'
            b'chTerm" name="url" placeholder="Product URL"><button type="submit" class="se'
            b'archButton"><i class="fa fa-search"></i>\n                </button>\n     '
            b'       </form>\n        </div>\n    </div>\n    <script>\n        var modal '
            b'= document.getElementById("Modal");\n        var modal2 = document.getEle'
            b'mentById("Modal2");\n        var span1 = document.getElementsByClassName('
            b'"close")[0];\n        var span2 = document.getElementsByClassName("close"'
            b')[1];\n        var flag = 0;\n        document.getElementById("messageVali'
            b'dation").style.visibility = "hidden";\n        document.getElementById("m'
            b'essageValidation2").style.visibility = "hidden";\n        document.getEle'
            b'mentById("messageValidation3").style.visibility = "hidden";\n\n        // '
            b'When the user clicks on <span> (x), close the modal\n        span1.onclic'
            b'k = function() {\n          modal.style.display = "none";\n          redir'
            b'ectPage();\n        }\n        // When the user clicks on <span> (x), clos'
            b'e the modal\n        span2.onclick = function() {\n          modal2.style.'
            b'display = "none";\n          redirectPage();\n        }\n\n        // When t'
            b'he user clicks anywhere outside the modal, close it\n        window.oncli'
            b'ck = function(event) {\n            if (event.target === modal) {\n       '
            b'         modal.style.display = "none";\n                redirectPage();\n '
            b'           }\n            else if (event.target === modal2) {\n           '
            b'     modal2.style.display = "none";\n                redirectPage();\n    '
            b'        }\n        }\n\n        var message = document.getElementById("mess'
            b'ageValidation").innerHTML;\n        var message2 = document.getElementByI'
            b'd("messageValidation2").innerHTML;\n\n        if(message.includes("This is'
            b' not a product from the US store. Please paste a URL from the US store")'
            b'){\n            document.getElementById("msg").innerHTML = message;\n     '
            b'       document.getElementById("msg").style.color = "darkred";\n         '
            b'   document.getElementById("error_icon").style.color = "darkred";\n      '
            b'      modal.style.display = "block";\n            flag = 1;\n        }\n   '
            b'     else if(message.includes("The number of reviews are not sufficient for '
            b'analysis")){\n            document.getElementById("msg").innerHTML = mess'
            b'age;\n            document.getElementById("msg").style.color = "darkred";'
            b'\n            document.getElementById("error_icon").style.color = "darkre'
            b'd";\n            modal.style.display = "block";\n            flag = 1;\n   '
            b'     }\n        else if(message.includes("This is not a valid amazon.com '
            b'URL. Please paste a valid URL from amazon.com")){\n            document.g'
            b'etElementById("msg").innerHTML = message;\n            document.getElemen'
            b'tById("msg").style.color = "darkred";\n            document.getElementByI'
            b'd("error_icon").style.color = "darkred";\n            modal.style.display'
            b' = "block";\n            flag = 1;\n        }\n        else if(message.incl'
            b'udes("Product not found with the URL pasted. Try again with the proper URL")'
            b'){\n            document.getElementById("msg").innerHTML = message;\n     '
            b'       document.getElementById("msg").style.color = "darkred";\n         '
            b'   document.getElementById("error_icon").style.color = "darkred";\n      '
            b'      modal.style.display = "block";\n            flag = 1;\n        }\n   '
            b'     else if(message.includes("The analysis was found to be non-conclusive."'
            b')){\n            document.getElementById("msg").innerHTML = message + " &'
            b'#128521;";\n            document.getElementById("msg").style.color = "dar'
            b'kgreen";\n            document.getElementById("msg").style.color = "darkg'
            b'reen";\n            document.getElementById("error_icon").style.color = "'
            b'darkgreen";\n            modal.style.display = "block";\n            flag '
            b'= 1;\n        }\n        else if(message.includes("The analysis was could '
            b'not be processed. Uncaught Exception. Try analyzing another")){\n        '
            b'    document.getElementById("msg").innerHTML = message;\n            docu'
            b'ment.getElementById("msg").style.color = "darkred";\n            document'
            b'.getElementById("msg").style.color = "darkred";\n            document.get'
            b'ElementById("error_icon").style.color = "darkred";\n            modal.sty'
            b'le.display = "block";\n            flag = 1;\n        }\n        if (messag'
            b'e2.includes("The product was found to be")){\n            var message3 = '
            b'document.getElementById("messageValidation3").innerHTML;\n            mes'
            b"sage3 = message3.replace(' ','');\n            var arr = message3.spl"
            b'it(",");\n            document.getElementById("msg2").innerHTML = message'
            b'2;\n            if (message2.includes("Positive"))\n                docume'
            b'nt.getElementById("msg2").style.color = "darkgreen";\n            else if'
            b' (message2.includes("Negative"))\n                document.getElementById'
            b'("msg2").style.color = "darkred";\n            modal2.style.display = "bl'
            b'ock";\n            flag = 1;\n            movePos(parseInt(arr[0]));\n     '
            b'       moveNeg(parseInt(arr[1]));\n        }\n\n        function redirectPa'
            b'ge(){\n            if (flag === 1)\n                location.href = "/dash'
            b'board"\n        }\n\n        function movePos(maxWidth) {\n            var e'
            b'lem = document.getElementById("Positive");\n            var width = 0;\n  '
            b'          var id = setInterval(frame, 10);\n            function frame() '
            b'{\n                if (width >= maxWidth) {\n                    elem.inne'
            b"rHTML = maxWidth  + '% Negative';\n                    clearInterval(id);"
            b'\n                } else {\n                    width++;\n                 '
            b"   elem.style.width = width + '%';\n                    elem.innerHTML = "
            b"width * 1  + '% Positive';\n                }\n            }\n        }"
            b'\n\n        function moveNeg(maxWidth) {\n            var elem = document.g'
            b'etElementById("Negative");\n            var width = 0;\n            var id'
            b' = setInterval(frame, 10);\n            function frame() {\n              '
            b'  if (width >= maxWidth) {\n                    elem.innerHTML = maxWidth'
            b"  + '% Negative';\n                    clearInterval(id);\n               "
            b' } else {\n                    width++;\n                    elem.style.wi'
            b"dth = width + '%';\n                    elem.innerHTML = width * 1  + '% "
            b"Negative';\n                }\n            }\n        }\n\n    </script>\n"
            b'\n        </div>\n    </div>\n</body>\n<script>\n    //Can add in respect'
            b'ive pages, the messages to be displayed in the modal box\n</script>\n</htm'
            b'l>') in response.data


def test_admin_dashboard_page(client):
    response = client.get('/adminDashboard')
    assert response.status_code == 200
    assert (b'<!DOCTYPE html>\n<html lang="en">\n<head>\n    \n    <link rel="stylesheet" '
            b'href="../static/css/viewUsers.css">\n    <link rel="stylesheet" href="htt'
            b'ps://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.'
            b'css">\n    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/b'
            b'ootstrap/3.3.7/css/bootstrap.min.css">\n\n    <link rel="stylesheet" href='
            b'"../static/css/dashboard.css">\n    <link rel="stylesheet" href="../stati'
            b'c/css/logo.css">\n    <link rel="stylesheet" href="https://www.w3schools.'
            b'com/w3css/4/w3.css">\n    <link rel="stylesheet" href="https://fonts.goog'
            b'leapis.com/icon?family=Material+Icons">\n    <link rel="stylesheet" href='
            b'"https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.'
            b'min.css">\n    <style type="text/css">\n        .content{\n            floa'
            b't: left;\n        }\n    </style>\n</head>\n<body>\n    <div class="main"'
            b'>\n        <div class="navigationBar">\n            <img id="icon" src="..'
            b'/static/img/Icon.png" onclick="location.href=\'/adminDashboard\'" alt="Log'
            b'o">\n            <div class="dropdown">\n                <i class=\'w3-xlar'
            b'ge fa fa-user\' id="user" style="color:white"></i>\n                <p id='
            b'"nameOfUser">Administrator</p>\n                <div class="dropdown-cont'
            b'ent">\n                    <a href="/signOut">Log Out</a>\n               '
            b' </div>\n            </div>\n            <a id="home" href="/adminDashboar'
            b'd" style=""><i class="fa fa-home" style="font-size:36px;color:white"></i></a'
            b'>\n        </div>\n        <div id="Modal" class="modal">\n            <!--'
            b' Modal content -->\n            <div class="modal-content">\n             '
            b'   <span class="close" id="closeModal">&times;</span>\n                <i'
            b' class="material-icons" style="font-size:36px;" id="error_icon">error_outlin'
            b'e</i><p id="msg" style="font-weight: bold"></p>\n            </div>\n     '
            b'   </div>\n        <!-- Modal block for analyzed products -->\n        <di'
            b'v id="Modal2" class="modal">\n            <div class="modal-content">\n   '
            b'             <span class="close" id="closeModal2">&times;</span>\n       '
            b'         <p id="msg2" style="font-weight: bold"></p>\n                <br'
            b'>\n                <div id="Positive" class="w3-container w3-padding-larg'
            b'e w3-green w3-center w3-text-black" style="width:0%; font-weight: bold;">0% '
            b'Positive</div>\n                <br>\n                <div id="Negative" c'
            b'lass="w3-container w3-padding-large w3-red w3-center w3-text-black" style="w'
            b'idth:0%; font-weight: bold;">0% Negative</div>\n                <br>\n    '
            b'        </div>\n        </div>\n        <!-- Modal block for Deleting User'
            b' -->\n        <div id="Modal3" class="modal">\n            <!-- Modal cont'
            b'ent -->\n            <div class="modal-content">\n                <span cl'
            b'ass="close" id="closeModal3">&times;</span>\n                <i class="ma'
            b'terial-icons" style="font-size:36px;" id="error_icon">error_outline</i><p id'
            b'="msg" style="font-weight: bold">Are you sure you want to delete user?</'
            b'p>\n                <button type="button" class="confirm-btn" onclick="co'
            b'nfirmDeleteUser()">Yes</button>\n                <button type="button" cl'
            b'ass="cancel-btn" onclick="location.href=\'/adminDashboard\'">No</button>\n '
            b'               <br>\n            </div>\n        </div>\n        <!-- Modal'
            b' Block for Search History -->\n        <div id="Modal4" class="modal">\n  '
            b'          <!-- Modal content -->\n            <div class="modal-content">'
            b'\n                <span class="close" id="closeModal4">&times;</span>\n   '
            b'             <br>\n                <p id="msg4" style="font-weight: bold"'
            b'></p>\n                <br>\n                <a onclick="copyToClipboard()'
            b'"><i class="w3-xlarge w3-display-bottommiddle fa fa-clipboard" id="displayCl'
            b'ipboard" style="visibility: hidden; padding-bottom: 3%;"></i></a>\n      '
            b'          <p id="copiedMsg" style="text-align: center; visibility: hidden">C'
            b'opied to Clipboard!</p>\n            </div>\n        </div>\n        \n    <'
            b'div class="view-users" id="viewUserDiv">\n        <h2 id="viewUsersHeadin'
            b'g">Users Registered to our Services</h2>\n        <table id="viewUser">\n '
            b'           <thead>\n                <tr>\n                    <th style="t'
            b'ext-align:center;">Full Name</th>\n                    <th style="text-al'
            b'ign:center;">Email</th>\n                    <th style="text-align:center'
            b';">Edit</th>\n                    <th style="text-align:center;">Delete</'
            b'th>\n                    <th style="text-align:center;">Search History</t'
            b'h>\n                </tr>\n            </thead>\n            <tbody id="tab'
            b'leBody">\n            </tbody>\n        </table>\n    </div>\n    <div>\n'
            b'        <p id="tableContents" style="visibility: hidden">\n            \n '
            b'               \n                        &lt;tr&gt;&lt;td&gt;Iona Thomas&'
            b'lt;/td&gt;&lt;td&gt;iona@gmail.com&lt;/td&gt;&lt;td&gt;&lt;a onclick=&#34;ed'
            b'itEmail(&#39;iona@gmail.com&#39;)&#34;&gt;&lt;i class=&#34;fa fa-edit&#34; s'
            b'tyle=&#34;font-size:24px&#34;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;&lt;td&gt;&l'
            b't;a onclick=&#34;deleteUser(&#39;iona@gmail.com&#39;)&#34;&gt;&lt;i class=&#'
            b'34;fa fa-trash&#34; style=&#34;font-size:24px&#34;&gt;&lt;/i&gt;&lt;/a&gt;&l'
            b't;/td&gt;&lt;td&gt;&lt;a onclick=&#34;userSearchHistory(&#39;iona@gmail.com&'
            b'#39;)&#34;&gt;&lt;i class=&#34;fa fa-search&#34; style=&#34;font-size:24px&#'
            b'34;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;&lt;/tr&gt;\n                    \n '
            b'                       &lt;tr&gt;&lt;td&gt;Shefali Upadhyaya&lt;/td&gt;&lt;t'
            b'd&gt;shefali@gmail.com&lt;/td&gt;&lt;td&gt;&lt;a onclick=&#34;editEmail(&#39'
            b';shefali@gmail.com&#39;)&#34;&gt;&lt;i class=&#34;fa fa-edit&#34; style=&#34'
            b';font-size:24px&#34;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;&lt;td&gt;&lt;a oncli'
            b'ck=&#34;deleteUser(&#39;shefali@gmail.com&#39;)&#34;&gt;&lt;i class=&#34;fa '
            b'fa-trash&#34; style=&#34;font-size:24px&#34;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&'
            b'gt;&lt;td&gt;&lt;a onclick=&#34;userSearchHistory(&#39;shefali@gmail.com&#39'
            b';)&#34;&gt;&lt;i class=&#34;fa fa-search&#34; style=&#34;font-size:24px&#34;'
            b'&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;&lt;/tr&gt;\n                    \n    '
            b'                    &lt;tr&gt;&lt;td&gt;Isaac Thomas&lt;/td&gt;&lt;td&gt;isa'
            b'ac@gmail.com&lt;/td&gt;&lt;td&gt;&lt;a onclick=&#34;editEmail(&#39;isaac@gma'
            b'il.com&#39;)&#34;&gt;&lt;i class=&#34;fa fa-edit&#34; style=&#34;font-size:2'
            b'4px&#34;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;&lt;td&gt;&lt;a onclick=&#34;dele'
            b'teUser(&#39;isaac@gmail.com&#39;)&#34;&gt;&lt;i class=&#34;fa fa-trash&#34; '
            b'style=&#34;font-size:24px&#34;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;&lt;td&gt;&'
            b'lt;a onclick=&#34;userSearchHistory(&#39;isaac@gmail.com&#39;)&#34;&gt;&lt;i'
            b' class=&#34;fa fa-search&#34; style=&#34;font-size:24px&#34;&gt;&lt;/i&gt;&l'
            b't;/a&gt;&lt;/td&gt;&lt;/tr&gt;\n                    \n                    '
            b'    &lt;tr&gt;&lt;td&gt;Test User&lt;/td&gt;&lt;td&gt;test@buyadvisor.com&lt'
            b';/td&gt;&lt;td&gt;&lt;a onclick=&#34;editEmail(&#39;test@buyadvisor.com&#39;'
            b')&#34;&gt;&lt;i class=&#34;fa fa-edit&#34; style=&#34;font-size:24px&#34;&gt'
            b';&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;&lt;td&gt;&lt;a onclick=&#34;deleteUser(&#39'
            b';test@buyadvisor.com&#39;)&#34;&gt;&lt;i class=&#34;fa fa-trash&#34; style=&'
            b'#34;font-size:24px&#34;&gt;&lt;/i&gt;&lt;/a&gt;&lt;/td&gt;&lt;td&gt;&lt;a on'
            b'click=&#34;userSearchHistory(&#39;test@buyadvisor.com&#39;)&#34;&gt;&lt;i cl'
            b'ass=&#34;fa fa-search&#34; style=&#34;font-size:24px&#34;&gt;&lt;/i&gt;&lt;/'
            b'a&gt;&lt;/td&gt;&lt;/tr&gt;\n                    \n            \n        </'
            b'p>\n    </div>\n    <p style="color: red; font-style: italic; text-align: '
            b'center; visibility: hidden" id="messageValidation">\n        \n           '
            b' \n        \n    </p>\n    <form id="UserEmailForm">\n        <input type="h'
            b'idden" name="email" id="userEmail">\n    </form>\n    <script>\n        var'
            b' modal = document.getElementById("Modal");\n        var modal3 = document'
            b'.getElementById("Modal3");\n        var span1 = document.getElementsByCla'
            b'ssName("close")[0];\n        var span3 = document.getElementsByClassName('
            b'"close")[2];\n        var flag = 0;\n        document.getElementById("mess'
            b'ageValidation").style.visibility = "hidden";\n\n        // When the user c'
            b'licks on <span> (x), close the modal\n        span1.onclick = function() '
            b'{\n          modal.style.display = "none";\n          document.getElementB'
            b'yId("viewUserDiv").style.display = "block";\n          redirectPage();\n  '
            b'      }\n\n        span3.onclick = function() {\n          modal3.style.dis'
            b'play = "none";\n          document.getElementById("viewUserDiv").style.di'
            b'splay = "block";\n          redirectPage();\n        }\n\n        // When th'
            b'e user clicks anywhere outside the modal, close it\n        window.onclic'
            b'k = function(event) {\n            if (event.target === modal) {\n        '
            b'        modal.style.display = "none";\n                document.getElemen'
            b'tById("viewUserDiv").style.display = "block";\n                redirectPa'
            b'ge();\n            }\n            else if (event.target === modal3) {\n    '
            b'            modal3.style.display = "none";\n                document.getE'
            b'lementById("viewUserDiv").style.display = "block";\n                redir'
            b'ectPage();\n            }\n        }\n\n        var message = document.getEl'
            b'ementById("messageValidation").innerHTML;\n        var message2 = documen'
            b't.getElementById("tableContents").innerHTML;\n\n        if(message.include'
            b's("No Registered Users")){\n            document.getElementById("msg").in'
            b'nerHTML = message+"...";\n            document.getElementById("msg").styl'
            b'e.color = "darkgreen";\n            document.getElementById("error_icon")'
            b'.style.color = "darkgreen";\n            document.getElementById("viewUse'
            b'rDiv").style.display = "none";\n            modal.style.display = "block"'
            b';\n            flag = 1;\n        }\n        else if(message.includes("Reco'
            b'rd Successfully Deleted")){\n            document.getElementById("msg").i'
            b'nnerHTML = message;\n            document.getElementById("msg").style.col'
            b'or = "darkgreen";\n            document.getElementById("error_icon").styl'
            b'e.color = "darkgreen";\n            document.getElementById("viewUserDiv"'
            b').style.display = "none";\n            modal.style.display = "block";\n   '
            b'         setTimeout(function(){\n                modal.style.display = "n'
            b'one";\n                document.getElementById("viewUserDiv").style.displ'
            b'ay = "block";\n                redirectPage();\n            },2000);\n     '
            b'       flag = 1;\n        }\n\n        if(message2.includes("fa fa-edit")){'
            b'\n            var len = message2.length;\n            message2 = message2.'
            b'substring(1,len-1);\n            message2 = message2.replaceAll("&lt;","<'
            b'");\n            message2 = message2.replaceAll("&gt;",">");\n            '
            b'message2 = message2.replaceAll("&quote;","\\"");\n            document.get'
            b'ElementById("tableBody").innerHTML = message2;\n            flag = 0;\n   '
            b'     }\n\n        function redirectPage(){\n            if (flag === 1)\n   '
            b'             location.href = "/adminDashboard"\n        }\n\n        functi'
            b'on deleteUser(email){\n            document.getElementById("userEmail").v'
            b'alue = email;\n            document.getElementById("UserEmailForm").actio'
            b'n = "/deleteUser";\n            document.getElementById("UserEmailForm").'
            b'method = "post";\n            modal3.style.display = "block";\n        }\n\n'
            b'        function confirmDeleteUser(){\n            document.getElementByI'
            b'd("UserEmailForm").submit();\n        }\n\n        function editEmail(email'
            b'){\n            document.getElementById("userEmail").value = email;\n     '
            b'       document.getElementById("UserEmailForm").action = "/editEmail";\n '
            b'           document.getElementById("UserEmailForm").method = "get";\n    '
            b'        document.getElementById("UserEmailForm").submit();\n        }\n\n  '
            b'      function userSearchHistory(email){\n            document.getElement'
            b'ById("userEmail").value = email;\n            document.getElementById("Us'
            b'erEmailForm").action = "/userSearchHistory";\n            document.getEle'
            b'mentById("UserEmailForm").method = "post";\n            document.getEleme'
            b'ntById("UserEmailForm").submit();\n        }\n    </script>\n\n\n    </di'
            b'v>\n</body>\n<script>\n    //Can add in respective pages, the messages to b'
            b'e displayed in the modal box\n</script>\n</html>') in response.data
