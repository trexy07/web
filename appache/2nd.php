<!DOCTYPE html>
<html lang="en">
  <meta name="description" content="A page of dad jokes">
  <meta charset="UTF-8">
  <head>
    <link rel='stylesheet' href='css.css'>
    <title>joke page</title>
    <div class="topnav">
      <a href="index.php">Home</a>
      <a class="active" href="2nd.php">Jokes</a>
      <a href="cheems.html">Cheems.gif</a>
      <a href="place.php">pi/place</a>
      <a href="whou.php">Where are you?</a>
      <a href="games"  >ONU</a>
      <a href="timer.html">CountDown</a>
    
    </div>
  </head>
  <body>
    <h1>This is a test to make a second page of dad jokes</h1>
  </body>
</html>
<?php
$response=exec('curl https://official-joke-api.appspot.com/random_joke');
$new=json_decode($response,true);
echo($new['setup']);
echo("<br>");
echo($new['punchline']);
echo("<br><br>");

#dad jokes
$response=exec('curl -H "Accept: text/plain" https://icanhazdadjoke.com');
echo($response);
echo("<br><br>");

#sv443 jokeAPI 
$curl=curl_init();
curl_setopt_array($curl, [
  CURLOPT_URL => "https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,religious,political,racist,sexist,explicit&format=txt",
]);
$res2=curl_exec($curl);

curl_close($curl);

echo $res2;


?>

