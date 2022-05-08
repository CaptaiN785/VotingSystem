<?php

function compare($a, $b)
{

    $output = shell_exec('docker run -it -d macgyvertechnology/face-comparison-model:2');
    $output = preg_replace('/[^0-9a-z]/', '', $output);

// write images to container
    exec('docker cp ' . $a . ' ' . $output . ':/macgyver/temp/known.jpg');
    exec('docker cp ' . $b . ' ' . $output . ':/macgyver/temp/test.jpg');

// Run main file
    $probability = shell_exec("docker exec -t " . $output . " /bin/bash -c 'python3 /macgyver/main'");

// Stop the Container
    exec("docker stop " . $output);

// Delete the Container
    exec("docker rm " . $output);

    return $probability;
}

compare('./elon1.jpg', './elon2.jpg');