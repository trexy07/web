<!doctype html>
<html lang="en">
  <meta name="description" content="This is my server project runing on a rapberry pi">
  <meta charset="UTF-8">
  <head>
      <link rel='stylesheet' href='css.css'><!--'-->
    <title>Trevin's pi server</title>
    <div class="topnav">
      <a class="active" href="index.php">Home</a>
      <a href="2nd.php">Jokes</a>
      <a href="cheems.html">Cheems.gif</a>
      <a href="place.php">pi/place</a>
      <a href="whou.php">Where are you?</a>
      <a href="games/onu/index.html"  >ONU</a>
      <a href="timer.html">CountDown</a>
    </div>
    <style>
        html, body {
            height: 100%;
            margin: 0;
        }
        .container {
            display: flex;
            flex-direction: column;
            height: 100%;
        }
        
        .text {
            flex: 0 1 auto; /* Adjusts based on content size */
        }
        
        .video-container {
            flex: 1 1 auto; /* Takes up remaining space */
            position: relative;
        }
        
        .video-container iframe {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
        }


        
    </style>
  </head>
  <body>
    <div class="container">
    <div class="text">
    <p>Hello there, here is a dad joke:</p>
<?php

# get dad joke
$response=exec('curl -H "Accept: text/plain" https://icanhazdadjoke.com');
echo($response);
?>
    <p>LOL, now get rickrolled!</p>

    </div> 
    <div class="video-container">
    <!-- <div style="width: auto; height: 100%; position: relative; padding-bottom: 28.25%;"> -->
    <iframe title="Rick Astley's never gonna give you up" id="ifr" 
        
        src="https://www.youtube.com/embed/dQw4w9WgXcQ?autoplay=1&mute=1" frameborder="0"  allow=" autoplay" allowfullscreen></iframe>
    </div>
        
    </div>
  </body>
</html>
