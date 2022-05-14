<script src="js/jquery.js"></script>

<!-- Bootstrap Core JavaScript -->
<script src="js/bootstrap.min.js"></script>

<!-- Scrolling Nav JavaScript -->
<script src="js/jquery.easing.min.js"></script>
<script src="js/sticky-menu.js"></script>
<script src="//cdn.jsdelivr.net/npm/sweetalert2@11"></script>


    <?php
        $uri = $_SERVER['REQUEST_URI'];
        // echo $uri; // Outputs: URI
        if($uri == "/frontend/index.php"){
            ?>  
                <div class = "lead" style ="background:pink; text-align:center;padding:10px;">
                    <p>Made with <span style = "color:#f00;">&#10084;</span> by Mukesh, Ashmit and Sayan</p>
                </div>
            <?php
        }

    ?>
</body>
</html>