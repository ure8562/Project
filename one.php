<html>
      <head>
      
        <title></title>
    </head>
    <body>
<?php
        $conn= mysqli_connect("localhost","Jung","1234","music");
        
 
        $sql="select * from member where userid='".$_POST['member_id']."'";
        $pass=$_POST["password"];
         
        
        $result= mysqli_query($conn,$sql);
        $row = mysqli_fetch_array($result);
        
        if(!$row){
            echo("<script>");
            echo("window.alert('사용자 ID가 존재하지 않습니다.');");
            echo("history.go(-1)");
            echo("</script>");
        }
        else if($pass!= $row['passward']){
            echo("<script>");
            echo("window.alert('비밀번호 오류입니다.');");
            echo("history.go(-1)");;
            echo("</script>");
        }
        ?>
        <form action="two.php" method="post">
        <input type="submit" value="START" />
       </form>
    </body>
</html>

