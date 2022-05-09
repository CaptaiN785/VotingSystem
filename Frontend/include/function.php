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
    $sql = "SELECT * FROM VOTER WHERE VOTERID = '$voterid'";
    $result = $conn->query($sql);
    $conn->close();
    if(mysqli_num_rows($result) == 1){
        return mysqli_fetch_assoc($result);
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
    
    date_default_timezone_set('Asia/Kolkata');
    $today = date('d-m-Y');
    $list = array();
    if(mysqli_num_rows($result) > 0){
        while($row = mysqli_fetch_assoc($result)){
            $d = strtotime($row["DATE"]);
            $date = date('d-m-Y', $d);

            $array = array(
                "date" => $date,
                "name" => $row["POST"],
                "assembly" => $assembly,
                "election_name" => $row["NAME"],
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


function get_candidate_details($eid){
    $conn = get_connection();
    $sql = "SELECT C.CID, C.SYMBOL, V.NAME FROM CANDIDATE as C, VOTER as V WHERE C.VID = V.VOTERID AND C.EID = $eid ORDER BY CID";
    $result = $conn->query($sql);
    $list = array();
    if(mysqli_num_rows($result) > 0){   
        $i = 1;
        while($row = mysqli_fetch_assoc($result)){
            $array = array(
                "sl" => $i,
                "cid" => $row["CID"],
                "name" => $row["NAME"],
                "symbol" => $row["SYMBOL"]
            );
            $i++;
            array_push($list, $array);
        }
    }
    return $list;
}
// get_candidate_details(1);
function get_voter_image($voterid){
    $conn = get_connection();
    $sql = "SELECT IMAGE FROM PHOTO WHERE VOTERID = $voterid";
    $result = $conn->query($sql);
    $row = mysqli_fetch_assoc($result);
    return $row["IMAGE"];
    // file_put_contents("voter.png", $row["IMAGE"]);
    // echo $row["IMAGE"];
}
// get_voter_image(97713154);

function make_vote($voterid, $cid, $election_name){
    
    $conn = get_connection();
    $sql = "SELECT * FROM $election_name WHERE VID = $voterid";
    $result = $conn->query($sql);
    if(mysqli_num_rows($result) > 0){
        return 0;
    }
    $sql = "INSERT INTO $election_name VALUES ($voterid, $cid)";
    $result = $conn->query($sql);
    $conn->close();
    if($result){
        return 1;
    }else{
        return -1;
    }
}


?>

