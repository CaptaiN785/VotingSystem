<?php
    $TITLE = "home";
    include('include/header.php');
    $VOTERID = $_SESSION["loggedInVoterId"];
    if(isset($_GET["eid"])){
        $_SESSION["eid"] = $_GET["eid"];
        header("Location: vote.php");
    }
    include('include/function.php');
?>
    <!-- Welcome   -->
    <section id="welcome" class="welcome-section">
        <div class="container">
            <div class="row" style="position:relative;"> 
                <!-- Below section will be displayed only when there is date of vote. -->
                <div class="col-lg-12" style="position:absolute;margin-top:25%;">
                    <h1>Online Voting Portal</h1>
					<p>&nbsp;</p>
                    <a id="vote-now-btn" class="btn btn-primary page-scroll" href="#elections">Vote Now!</a>
                </div>
            </div>
        </div>
    </section>
    <!-- About -->
    <section id="elections" class="about-section ">
        <div class="container">
            <div class="row">
                <h1 class = 'col-lg-12 my-0'>Elections</h1>
            </div>
            
            <table class="table table-hover table-bordered">
                <thead>
                    <tr class = 'bg-primary'>
                        <th scope="col">Dates</th>
                        <th scope="col">Election name</th>
                        <th scope="col">Assembly</th>
                        <th scope="col">Options</th>
                    </tr>
                </thead>
                <tbody id = "election-table-body">
                    <?php
                        $election = get_election_details($VOTERID); // Getting all election information related to this voters
                        if(count($election) > 0){
                            $_SESSION["election_name"] = $election[0]["election_name"];
                            for($i=0; $i<count($election); $i++){ // Priniting the detail in table forms
                               echo '
                                <tr>
                                    <td>'.$election[$i]["date"].'</td>
                                    <td>'.$election[$i]["name"].'</td>
                                    <td>'.$election[$i]["assembly"].'</td>';
                                
                                if($election[$i]["active"]){
                                    echo '<td><a href = "index.php?eid='.$election[$i]["eid"].'" class = "btn btn-success")>Vote now</a></td>';
                                }
                                echo '
                                </tr>
                               ';
                            }
                        }else{
                            echo '
                            <tr>    
                                <td colspan="4">There is no election in your assembly.</td>
                            </tr>
                            ';
                        }
                    ?>
                </tbody>
              </table>
        </div>

    </section>

    <!-- What we do Section -->
    <section id="whatwedo" class="whatwedo-section" style="padding-top:50px;">
        <div class="container">
            <div class="row">
                <div class="col-lg-12">
                    <h1>Results</h1>
                </div>
            </div>
            <form class="row" style="padding:10px 100px;" 
            action="<?php  echo htmlspecialchars($_SERVER['PHP_SELF']);  ?>" method="post"
            enctype="multipart/form-data"
            >
                <?php
                    $election_list = get_previous_election_details($_SESSION["loggedInVoterAid"]);
                ?>
                <div class="col-lg-12">
                    <p class = "lead text-left">Select election to view results</p>
                    <div class="input-group text-center">
                        <select class="form-control" name ="election_eid">
                            <option selected value = "0">Select election</option>
                        <?php 
                            foreach($election_list as $election){
                        ?>
                            <option value="<?php echo $election["eid"] ?>"><?php echo $election["eid"]."-".$election["post"]; ?></option>
                            <?php } ?>
                        </select> 
                    <span class="input-group-btn">
                        <button class="btn btn-primary" type="submit" name="search_result">Search</button>
                    </span>
                    </div><!-- /input-group -->
                </div><!-- /.col-lg-6 -->
            </form>
        <?php  
            if(isset($_POST["search_result"])){
                $eid = filter_input(INPUT_POST, 'election_eid', FILTER_SANITIZE_STRING);
                if($eid == 0){
                    echo "<script> alert('Invalid credential')  </script>";
                }else{
                    $election_name = "";
                    foreach($election_list as $election){
                        if($election["eid"] == $eid){
                            $election_name = $election["name"];
                            break;
                        }
                    }
                    ?>
                    <table class="table table-hover table-bordered">
                        <thead>
                            <tr class = 'bg-primary'>
                                <th scope="col">Candidate name</th>
                                <th scope="col">Votes</th>
                            </tr>
                        </thead>
                        <tbody>
                            <?php  $list = get_election_result($election_name, $eid);
                                if(count($list) > 0){
                                    foreach($list as $cand){
                                        ?>
                                            <tr>
                                                <td><?php echo $cand["name"] ?></td>
                                                <td><?php echo $cand["vote"] ?></td>
                                            </tr>
                                        <?php
                                    }
                                }else{
                                    ?>
                                        <tr><td colspan = "2">No candidates available</td></tr>
                                    <?php
                                }
                            ?>
                        </tbody>
                    </table>    
                    <?php
                }
            }
        ?>
            
            
        </div>
    </section>
    <!-- Contact Section -->
    <section id="contact" class="contact-section">
        <div class="container">
            <div class="row">
                <div class="col-lg-12">
                    <h1>Contact Section</h1>
                </div>
            </div>
        </div>
    </section>
	
	<a id="back2Top" title="Back to top" href="#">&#10148;</a>
    <!-- jQuery -->

<?php
    include('include/footer.php');
?>
