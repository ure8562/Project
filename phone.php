<?php


    
    $conn= mysqli_connect("localhost","Jung","1234","pet");
 
 
    if(mysqli_connect_errno($conn)){
         echo "fail";
    } 
    else
    {
     
        $query = "select * from generated_events";
        $result= mysqli_query($conn, $query);
       
        
        while ($row = mysqli_fetch_array($result)){
            echo "<br>Event count  ".$row['generatedEventId']."<br>\n";
            echo "level  ".$row['level']."<br>\n";
            echo "category  ".$row['event_category']."<br>\n";
            echo "event  ".$row['event']."<br>\n";
            echo "time  ".$row['date_time']."<br>\n";
            echo "<br>-------------------";
            echo "-------------------<br>";
           
        }
        



    }
    
?>