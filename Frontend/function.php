<!-- Database details -->
<?php
$host = "localhost";
$password = "Mukesh@2001";
$user = "root";
$database = "votingsystem";

function get_connection(){
    global $host, $user, $password, $database;
    $conn = mysqli_connect($host, $user, $password, $database);

    if($conn){
        echo "Connection is succesful";
    }else{
        echo $conn->error_log;
    }
    return $conn;
}
get_connection();
?>

