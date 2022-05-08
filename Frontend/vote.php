<?php
    $TITLE = "Vote now!";
    include('include/header.php');
    include('include/function.php');
    echo "<br><br><br><br><br>";
    // echo "election id is : ".$_SESSION["eid"];
?>
<div class="container">
    <h2 class = "header text-center" >Election post : </h2>
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
                    echo '<td><label><img src = "../symbol/1.png"></label></td>';
                    echo "<td><button type='button' class='btn btn-primary vote_btn' onclick='count_me(".$row['cid'].")' id='".$row['cid']."'>Vote me</button></td>";
                    echo "</tr>";
                }
            }else{
                echo "<tr><td colspan = '4'>No candidate in your area.</td></tr>";
            }



        ?>
        </tbody>
    </table>
    <script>
        // function count_me(cid){
        //     alert(cid);
        // }
    </script>
    <div class="container" style="padding:10px 100px 100px 100px;display:none;" id="verification_container">
        <div class="row text-center">
            <label class = "lead ">Capture and submit to make a vote count.</label>
        </div>
        <div class="row" style="width:max-content; margin:0 auto;">
            <video id = "video" autoplay muted width="300" height="300"></video>
            <canvas id="canvas" width="300" height="300"></canvas>
        </div>
        <form action = <?php echo htmlspecialchars($_SERVER["PHP_SELF"]);  ?> method="post" enctype="multipart/form-data">
            <div class="row text-center">
                <input type="number" id = "cid_number" name ="cid_number" hidden>
                <button type="button"  class="btn btn-info" id = "snap"> Capture </button>
                <button type="submit" class= "btn btn-success" id="submit_vote" name="submit_vote" style="display:none;"> Submit </button>
            </div>
        </form>
    </div>
    <script src = "server.js"></script>
<!-- Creating modals for capturing the image and verifying -->
</div>
<?php
    include('include/footer.php');
?>