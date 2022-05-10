<?php
    $TITLE = "profile";
    include('include/header.php');
    echo "<br><br><br><br><br>";

    $image = get_voter_image($_SESSION["loggedInVoterId"]);
    $info = get_voter_info($_SESSION["loggedInVoterId"]);

    
?>
<div class="container">
    <h2 class = "display-2 text-center" style="font-size:30px;">Your profile</h2>
    <hr>
    <div class = "row">
        <div class="col-lg-9">
            <label></label>
        </div>
        <div class="col-lg-3">
            
        </div>

    </div>

    


</div>
<?php
    include('include/footer.php');
?>