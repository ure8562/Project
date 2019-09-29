<!DOCTYPE html>
<!--
To change this license header, choose License Headers in Project Properties.
To change this template file, choose Tools | Templates
and open the template in the editor.
-->
<html>
    <head>
      <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title></title>
    
    <style>
    body{
        background-image:url('back5.png');
        background-attachment:fixed;
        background-repeat: no-repeat;
         background-size: cover;
    }
         .div_block {
      width: 150px;
      height: 150px;
      border-style: solid;
      border-width: thin;
      border-color: transparent;
      position: absolute;
     }

     .div_block:nth-child(2) {
      background-image:url('dog2.jpg');
     
        background-repeat: no-repeat;
      
      left: 230px;
      top: 60px;
     }
     .div_block:nth-child(3) {
         background-image: url('log3.png');
         background-repeat: no-repeat;
         left: 380px;
         top: 60px;
     }
      .div_block:nth-child(4) {
         background-image: url('log4.png');
         background-repeat: no-repeat;
         left: 530px;
         top: 60px;
     }
     
        .div_block1 {
      width: 150px;
      height: 150px;
      border-style: solid;
      border-width: thin;
      border-color: transparent;
      position: absolute;
     }
     .div_block1:nth-child(5) {
         background-image: url('run.png');
         background-repeat: no-repeat;
         left: 70px;
         top: 200px;
     }

    </style>
    </head>
        
        <body>
            
       <form action="wishlist.php" method="GET" name="wishList">
          
           <a href=http://localhost/wishlist.php><img src="log1.png" hspace="70px" vspace="50px"  alt="test"/></a>
       </form>
              
               
    
     <div class="div_block"></div>
      <div class="div_block"></div> 
        <div class="div_block"></div>
        <div class="div_block1"></div>   
           <a href="http://localhost/index2">
               <img src="stop.png" width="200px" height="200px"hspace="-10px" vspace="170"></a>
        <?php
        // put your code here
        ?>
    </body>
</html>
