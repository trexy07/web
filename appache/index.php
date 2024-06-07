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
      <a href="whou.php">where are you?</a>
      <a href="games">games</a>
    </div>
    
  </head>
  <body>
    <p>Hello there, here is a dad joke:</p>
<?php

# get dad joke
$response=exec('curl -H "Accept: text/plain" https://icanhazdadjoke.com');
echo($response);
?>
    <p>LOL, now get rickrolled!</p>
      <br><br><br><br>
    <iframe title="Rick Astley's never gonna give you up" id="ifr" width=50% height=50% src="https://www.youtube.com/embed/dQw4w9WgXcQ?autoplay=1&mute=1" frameborder="0"  allow=" autoplay" allowfullscreen></iframe>
    <p></p>
    <!--<iframe width="410" height="460"src="https://academy.cs.cmu.edu/sharing/oldLaceDeer1547/embed"> </iframe>-->
    <p></p>
    <p style="font-size: 20px; color:#1F9AFE;">
    
    
    </p>
  </body>
</html>
