<?php
session_start();
if(!isset($_SESSION["loggedInVoterId"])){ // Checking if user is logged in
    header("Location:login.php");
}
?>


<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta http-equiv="x-ua-compatible" content="ie=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="canonical" href="https://html5-templates.com/" />
    <title><?php echo $TITLE ?></title>
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
                <a class="navbar-brand page-scroll" href="../">Home</a>
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