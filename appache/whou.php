<!doctype html>
<html lang="en">
  <meta name="description" content="Visit to find where you're visiting from">
  <meta charset="UTF-8">
  <head>
      <link rel='stylesheet' href='css.css'>
    <title>where are you?</title>
    <div class="topnav">
      <a href="index.php">Home</a>
      <a href="2nd.php">Jokes</a>
      <a href="cheems.html">Cheems.gif</a>
      <a href="place.php">pi/place</a>
      <a class="active" href="whou.php">where are you?</a>
      <a href="games">games</a>
    </div>

  </head>
  <body>
    <h1>Hello, I know your ip!</h1>
    
    
<?php
$ipAddress = $_SERVER['REMOTE_ADDR'];
echo "Your IP address is: " . $ipAddress;


$myfile = fopen("conect.log", "a");
    
$apiKey = "6f7edfb1a7af4b2893e28267f1104d79";
$ip = $_SERVER['REMOTE_ADDR'];
//$ip="23.120.9.232";
# find location
$location = get_geolocation($apiKey, $ip);
$decodedLocation = json_decode($location, true);
//fwrite($myfile, $ip); 


# print to screen & write to log
echo "<br>";
print("You're in $decodedLocation[city], $decodedLocation[state_prov], $decodedLocation[country_name].");
echo "<br>";
if ($ip== "97.105.99.178"){
//     echo "<br>";
    echo "you're at NYOS";
    fwrite($myfile, "NYOS"); }

else if ($ip=="192.168.1.254"){
    echo "you're at home";
    fwrite($myfile, "home"); 
}
else {    
  fwrite($myfile, "idk"); 
}
fwrite($myfile, ', '); 

fwrite($myfile, $ip); 
fwrite($myfile, ", "); 

fwrite($myfile, date(DATE_RFC2822));
fwrite($myfile, ", "); 

fwrite($myfile, "You're in $decodedLocation[city], $decodedLocation[state_prov], $decodedLocation[country_name].");

fwrite($myfile, "\n"); 

fclose($myfile);




function get_geolocation($apiKey, $ip, $lang = "en", $fields = "*", $excludes = "") {
    $url = "https://api.ipgeolocation.io/ipgeo?apiKey=".$apiKey."&ip=".$ip."&lang=".$lang."&fields=".$fields."&excludes=".$excludes;
    $cURL = curl_init();

    curl_setopt($cURL, CURLOPT_URL, $url);
    curl_setopt($cURL, CURLOPT_HTTPGET, true);
    curl_setopt($cURL, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($cURL, CURLOPT_HTTPHEADER, array(
        'Content-Type: application/json',
        'Accept: application/json',
        'User-Agent: '.$_SERVER['HTTP_USER_AGENT']
    ));

    return curl_exec($cURL);
}

// Initialize cURL.
// $ch = curl_init();

//echo('https://ipgeolocation.abstractapi.com/v1/?api_key=5bd1dde4683b49888b7390019ae42b6c&ip_address='+$ipAddress);

?>
    <br><p>This likely won't work if you're on cellular<p><!--'-->
  </body>
</html>
