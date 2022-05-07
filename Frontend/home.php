
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta http-equiv="x-ua-compatible" content="ie=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="canonical" href="https://html5-templates.com/" />
    <title></title>
    <meta name="description" content="Simplified Bootstrap template with sticky menu">
    <link href="css/bootstrap.min.css" rel="stylesheet">
    <link href="css/sticky-menu.css" rel="stylesheet">
</head>
<body id="page-top" data-spy="scroll" data-target=".navbar-fixed-top">
    <nav class="navbar navbar-default navbar-fixed-top" role="navigation">
        <div class="container">
            <div class="navbar-header page-scroll">
                <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-ex1-collapse">
                    <span class="sr-only">Toggle menu</span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                </button>
                <a class="navbar-brand page-scroll" href="#page-top">Home</a>
            </div>

            <div class="collapse navbar-collapse navbar-ex1-collapse">
                <ul class="nav navbar-nav">
                    <li class="hidden">
                        <a class="page-scroll" href="#page-top"></a>
                    </li>
                    <li>
                        <a class="page-scroll" href="#elections">Elections</a>
                    </li>
                    <li>
                        <a class="page-scroll" href="#whatwedo">What We Do</a>
                    </li>
                    <li>
                        <a class="page-scroll" href="#contact">Contact us</a>
                    </li>
                </ul>
            </div>	<!-- .navbar-collapse -->
        </div>		<!-- .container -->
    </nav>
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
    <?php
    include('function.php');
?>
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
    <script src="js/jquery.js"></script>

    <!-- Bootstrap Core JavaScript -->
    <script src="js/bootstrap.min.js"></script>

    <!-- Scrolling Nav JavaScript -->
    <script src="js/jquery.easing.min.js"></script>
    <script src="js/sticky-menu.js"></script>
    <script src ='server.js'></script>

</body>

</html>
