<?php
    $TITLE = "profile";
    include('include/header.php');
    include('include/function.php');
    echo "<br><br><br><br><br>";

    $img = get_voter_image($_SESSION["loggedInVoterId"]);
    $info = get_voter_info($_SESSION["loggedInVoterId"]);


?>
<div class="container bg-info" id ="voter_info" style ="padding:30px;width:max-content;">
    <h2 class = "display-2 text-center" style="margin:0 auto;font-size:30px;">Your profile</h2>
    <hr>
    <div class = "container" style = "width:max-content;margin:0 auto;">
        <div class="container">
            <img src = "data:image/jpg;charset=utf-8;base64,<?php echo base64_encode($img); ?>" 
            style = "width:130px;height:150px;">
        </div><hr>
        <div class="row" style="max-width:400px;">
            <table class = "table borderless ">
                <tr>
                    <th  style ="font-size:1.5rem;outline:none;border:none;">VoterID</th>
                    <td style ="font-size:1.5rem;outline:none;border:none;">
                        <label ><?php echo $info["VOTERID"];  ?></label>
                    </td>
                </tr>
                <tr>
                    <th  style ="font-size:1.5rem;outline:none;border:none;">Name</th>
                    <td style ="font-size:1.5rem;outline:none;border:none;"><label ><?php echo $info["NAME"];  ?></label></td>
                </tr>
                <tr>
                    <th  style ="font-size:1.5rem;outline:none;border:none;">Phone</th>
                    <td style ="font-size:1.5rem;outline:none;border:none;"><label ><?php echo $info["PHONE"];  ?></label></td>
                </tr>
                <tr>
                    <th  style ="font-size:1.5rem;outline:none;border:none;">Email</th>
                    <td style ="font-size:1.5rem;outline:none;border:none;"><label ><?php echo $info["EMAIL"];  ?></label></td>
                </tr>
                <tr>
                    <th  style ="font-size:1.5rem;outline:none;border:none;">DOB</th>
                    <td style ="font-size:1.5rem;outline:none;border:none;"><label ><?php echo $info["DOB"];  ?></label></td>
                </tr>
                <tr>
                    <th  style ="font-size:1.5rem;outline:none;border:none;">PIN</th>
                    <td style ="font-size:1.5rem;outline:none;border:none;"><label ><?php echo $info["PIN"];  ?></label></td>
                </tr>
                <tr>
                    <td colspan="2">
                        <button type = "button" class = "btn btn-info" 
                        style="margin-top:3rem;padding:10px 30px;"
                        onclick="printInfo()"
                        >Print</button>
                    </td>
                </tr>
            </table>
        </div>
    </div>

<script>
function printInfo() {
        var divContents = document.getElementById("voter_info").innerHTML;
        var a = window.open('', '', '');
        a.document.write('<html><body>');
        a.document.write(divContents);
        a.document.write('</body></html>');
        a.document.close();
        a.print();
    }
</script>


</div>
<?php
    include('include/footer.php');
?>