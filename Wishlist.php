<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title></title>
    </head>
<?php
    $conn= mysqli_connect_errno("localhost","Jung","1234","Pet");
    
    if(mysqli_connect_errno_connect_errno($conn)){
        echo "실패";
    }
    else
    {
        echo "성공";
    }
    
?>

        </body>
</html>