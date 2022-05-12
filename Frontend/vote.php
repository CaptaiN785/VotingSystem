<?php
    $TITLE = "Vote now!";
    include('include/function.php');
    include('include/header.php');
    echo "<br><br><br><br><br>";
    // echo "election id is : ".$_SESSION["eid"];
    if(isset($_POST['submit_vote'])){
        $cid = htmlspecialchars($_POST["cid_number"]);
        $val = make_vote($_SESSION["loggedInVoterId"], $cid, $_SESSION["election_name"]);
        if($val == 0){
            // vote casted
            echo "<script>
                    alert('Vote is already casted');
                </script>";
        }elseif($val == 1){
            // success
            echo "<script>
                    alert('Vote success');
                </script>";
        }else{
            // server error.
            echo "<script>
                    alert('Server error.');
                </script>";
        }
    }
?>
<div class="container">
    <h2 class = "header text-center" >Election Candidates</h2>
    <table class="table table-hover table-bordered">
        <thead>
            <tr class = 'bg-primary'>
                <th scope="col">#</th>
                <th scope="col">Name</th>
                <th scope="col">Symbol</th>
                <th scope="col">Option</th>
            </tr>
        </thead>
        <tbody>
        <?php
            $list = get_candidate_details($_SESSION["eid"]);
            if(count($list) > 0){
                foreach($list as $row){
                    echo "<tr>";
                    echo "<td>".$row['sl']."</td>";
                    echo "<td><label class='fs-2'><strong>".$row['name']."</strong></label></td>";
                    echo '<td><label><img src = "'.$row['symbol'].'" width="50" height="40"></label></td>';
                    echo "<td><button type='button' class='btn btn-primary vote_btn' onclick='count_me(".$row['cid'].")' id='".$row['cid']."'>Vote me</button></td>";
                    echo "</tr>";
                }
            }else{
                echo "<tr><td colspan = '4'>No candidate in your area.</td></tr>";
            }
        ?>
        </tbody>
    </table>
    <div class="container" style="padding:10px 100px 100px 100px;display:none;" id="verification_container">
        <div class="row text-center">
            <label class = "lead ">Plase wait camera will turn on soon...</label>
        </div>
        <div class="row" style="width:max-content; margin:0 auto;">
            <video id = "video" autoplay muted width="300" height="300"></video>
        </div>
        <form action = <?php echo htmlspecialchars($_SERVER["PHP_SELF"]);  ?> method="POST" enctype="multipart/form-data">
            <div class="row text-center">
                <input type="number" id = "cid_number" name ="cid_number" hidden>
                <button type="submit" class= "btn btn-success text-center" id="submit_vote" name="submit_vote" style="display:none;"> Submit </button>
            </div>
        </form>
    </div>
    <!-- <textarea hidden="true" id="bufferImageArea"><?php echo $_SESSION["loggedInVoterImage"] ?></textarea> -->
    <script src = "face-api.min.js"></script>
    <script src = "server.js"></script>
<!-- Creating modals for capturing the image and verifying -->
</div>
<?php
    include('include/footer.php');
?>