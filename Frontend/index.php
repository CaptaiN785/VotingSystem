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
                <script>
                    // check for voting is on that date
                    if(true){
                        document.getElementById("vote-now-btn").style.display = "inline-block";
                    }else{
                        document.getElementById("vote-now-btn").style.display = "none";
                    }
                </script>
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
    <section id="whatwedo" class="whatwedo-section">
        <div class="container">
            <div class="row">
                <div class="col-lg-12">
                    <h1>What We Do</h1>
                </div>
            </div>
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
