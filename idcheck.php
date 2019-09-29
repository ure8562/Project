<html>
    <body>
        <table width="230" align="center">
            <?php
                import_request_variables("GPC","");
                $mysqlid = mysqli_connect("localhost","Jung","1234","music");
        
                $sql="select * from member where userid = '$userid'";
                $result=mysqli_query($sql);
                $rows= mysqli_num_rows($result);
                if(!$rows){
            ?>
            <tr>
            <td align="center"> <font color="red" size="3"><b>사용가능</b></font>한 ID입니다.
                </td>
            </tr>
            <?php
                }
                else{
                    ?>
            <tr>
                  <td align="center"> <font color="red" size="3">이미등록</font>된 ID입니다.
                
            </tr>
            <?php
                }
                ?>
            <tr>
                <td align="center"><font size="2">
                    <input type="button" onclick="self.close();" value="닫기">
                    </font>
                </td>
            </tr>
        </table>
    </body>
</html>




/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

 <input type="submit" value="" name="회원가입" />