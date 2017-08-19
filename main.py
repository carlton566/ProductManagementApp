#!usr/bin/python
import webapp2
from google.appengine.ext import ndb
   
   
html = """ 
            <html>
<head>
<script type="text/javascript">
//auto expand textarea
function adjust_textarea(h) {
    h.style.height = "50px";
    h.style.height = (h.scrollHeight)+"px";
}
<!--

var speed = 5000

// Specify the image files
var Pic = new Array() // don't touch this
// to add more images, just continue
// the pattern, adding to the array below

Pic[0] = 'download.jpg'
Pic[1] = 'download1.jpg'
Pic[2] = 'images.jpg'
Pic[3] = 'images1.jpg'

// =======================================
// do not edit anything below this line
// =======================================

var t
var j = 0
var p = Pic.length

var preLoad = new Array()
for (i = 0; i < p; i++){
   preLoad[i] = new Image()
   preLoad[i].src = Pic[i]
}

function runBGSlideShow(){
   if (document.body){
       document.body.style.backgroundSize =  "cover";
   document.body.background = Pic[j];
   document.body.style.backgroundRepeat = "no-repeat";
   j = j + 1
   if (j > (p-1)) j=0
   t = setTimeout('runBGSlideShow()', speed)
   }
}

//-->
</script>
<style type="text/css">
body{
font-family: "Algerian";
}
.form-style-4{
    width: 550px;
    font-size: 30px;
	background: #c94c4c;
    padding: 30px 30px 30px 30px;
    border: 10px solid #53687E;
}
.form-style-4 h1
{
font-size: 40px;
color: #A8BACE;
}
.form-style-4 input[type=submit],
.form-style-4 input[type=button],
.form-style-4 input[type=text],
.form-style-4 input[type=email],
.form-style-4 input[type=number],
.form-style-4 textarea,
.form-style-4 label
{
    
    font-size: 30px;
    color: #A8BACE;

}
.form-style-4 label {
    display:block;
    margin-bottom: 50px;
}
.form-style-4 label > span{
    display: inline-block;
    float: center;
    width: 450px;
}
.form-style-4 input[type=text],
.form-style-4 input[type=email],
.form-style-4 input[type=number] 
{
    background: transparent;
    border: none;
    border-bottom: 1px dashed #83A4C5;
    width: 300px;
    outline: none;
    padding: 0px 0px 0px 0px;
    font-style: italic,bold;
}
.form-style-4 textarea{
    font-style: italic;
    padding: 0px 0px 0px 0px;
    background: transparent;
    outline: none;
    border: none;
    border-bottom: 1px dashed #83A4C5;
    width: 275px;
    overflow: hidden;
    resize:none;
    height:30px;
}

.form-style-4 textarea:focus, 
.form-style-4 input[type=text]:focus,
.form-style-4 input[type=email]:focus,
.form-style-4 input[type=number] :focus,
{
    border-bottom: 1px dashed #D9FFA9;
}

.form-style-4 input[type=submit],
.form-style-4 input[type=button]{
    background: red;
	font-family: "Algerian";
    border: none;
    padding: 8px 10px 8px 10px;
    border-radius: 5px;
    color: #A8BACE;
}
.form-style-4 input[type=submit]:hover,
.form-style-4 input[type=button]:hover{
background: green;
}
</style>
</head>
<body onload="runBGSlideShow()">
<center>
<form class="form-style-4" action = "/confirm"  method="post">
<h1><b><u>Product Order Sheet</u></b></h1>
<label for="names">
<span>Client  Name</span><input type="text" name="names" required="true" />
</label>
<label for="emailid">
<span>Client Email Address</span><input type="email" name="emailid" required="true" />
</label>
<label for="pname">
<span>Product Name</span><input type="text" name="pname" required="true" />
</label>
<label for="descriptions">
<span>Product Description</span><textarea name="descriptions" onkeyup="adjust_textarea(this)" required="true"></textarea>
</label>
<label for="quantity">
<span>Quantity</span><input type="number" name="quantity" required="true" />
</label>
<label>
<span>&nbsp;</span><input type="submit" value="Submit Form" />
</label>
</form>
</center>
</body>
</html>  
 """  
   
   
class Product(ndb.Model):
     Clientname = ndb.StringProperty(indexed=True)
     emailid = ndb.StringProperty(indexed=True)
     productname = ndb.StringProperty(indexed=True)
     descriptions = ndb.TextProperty(indexed=True)
     quantity = ndb.IntegerProperty(indexed=True)	 
     when = ndb.DateTimeProperty(auto_now_add=True)
	 
	 
	 
class MyHandler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write(html)
		
		
		
		
class MainHandler(webapp2.RequestHandler):
   def post(self):
     Clientname = self.request.get('names')
     emailid = self.request.get('emailid')
     productname = self.request.get('pname')
     descriptions = self.request.get('descriptions')
     quantity = int(self.request.get('quantity'))
     products = Product()
     products.Clientname=Clientname
     products.emailid=emailid
     products.productname=productname
     products.descriptions=descriptions
     products.quantity=quantity
     products.put()
     self.redirect('/')
	 
app = webapp2.WSGIApplication([('/', MyHandler),('/confirm', MainHandler)], 
 debug=True)
