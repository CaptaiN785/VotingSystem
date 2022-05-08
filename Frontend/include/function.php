<!-- Database details -->
<?php
$host = "localhost";
$password = "Mukesh@2001";
$user = "root";
$database = "votingsystem";

function get_connection(){
    global $host, $user, $password, $database;
    $conn = mysqli_connect($host, $user, $password, $database);

    if(!$conn){
        echo "Database error.";
        echo "
        <script>
        Swal.fire({
            icon: 'error',
            title: 'Service Unavailable',
            text: 'Something went wrong!'
          })
        </script>
        ";
    }
    return $conn;
}

function validate_user($voterid){
    $conn = get_connection();
    $sql = "SELECT voterid FROM VOTER WHERE VOTERID = '$voterid'";
    $result = $conn->query($sql);
    $conn->close();
    if(mysqli_num_rows($result) == 1){
        return true;
    }else{
        return false;
    }
}

function get_election_details($voterid){

    $conn = get_connection();
    $sql = "SELECT AID FROM VOTER WHERE VOTERID = $voterid";
    $result = $conn->query($sql);
    $row = mysqli_fetch_assoc($result);
    $AID = $row["AID"];
    
    $result = $conn->query("SELECT NAME FROM ASSEMBLY WHERE AID = $AID");
    $assembly = mysqli_fetch_assoc($result)["NAME"];

    $sql = "SELECT * FROM  ELECTION WHERE DATE >= CURDATE() AND AID = $AID";
    $result = $conn->query($sql);
    
    $today = date('d-m-Y');

    $list = array();
    date_default_timezone_set("Asia/Kolkata");
    if(mysqli_num_rows($result) > 0){
        while($row = mysqli_fetch_assoc($result)){
            $d = strtotime($row["DATE"]);
            $date = date('d-m-Y', $d);

            $array = array(
                "date" => $date,
                "name" => $row["POST"],
                "assembly" => $assembly,
                "eid" =>$row['EID'],
                "active" => false
            );
            if($date == $today){
                $array["active"] = true;
            }
            array_push($list, $array);
        }
    }else{
        echo "No election is found";
    }  
    $conn->close();
    return $list;
}

get_election_details(29281912);

?>

