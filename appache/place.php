<!doctype html>
<?php
// Initialize the color variable
// $selectedColor = isset($_POST['color']) ? $_POST['color'] : '#000000'; // Default to black if no color is selected

$fill=  $_GET['fill'] ?? '';
echo $fill;
?>
<html lang="en">
  <meta name="description" content="Color the grid for anyone to see">
  <meta charset="UTF-8">
  <head>
      <link rel='stylesheet' href='css.css'>
    <title>The Pi/Place</title>
    <div class="topnav">
      <a href="index.html">Home</a>
      <a href="2nd.html">Jokes</a>
      <a href="cheems.html">Cheems.gif</a>
      <a class="active" href="place.php">pi/place</a>
      <a href="whou.php">Where are you?</a>
      <a href="games/onu/index.html"  >ONU</a>
      <a href="timer.html">CountDown</a>
    </div>
	<style>
		.container {
            display: flex;
            align-items: center; /* Center vertically */
        }
        .pixel {
            width:  min(2.2vh,2.2vw);
            height: min(2.2vh,2.2vw);
            
            display: inline-block;
            cursor: pointer;
        }
        /* Style for the container of the grid */
        
		.grid-container {
            display: grid;
            grid-template-columns: repeat(9, min(3vw,3vh)); /* 4 columns of 50px each */
            grid-template-rows: repeat(2, min(3vw,3vh)); /* 2 rows of 50px each */
            grid-gap: 10px; /* Gap between grid items */
        }
        /* Style for the individual grid items (squares) */
        .grid-item {
            width:min(3vw,3vh);
            height: min(3vw,3vh);
            background-color: #ccc; /* Default background color */
            cursor: pointer;
            border: 2px solid white;
        }
		/* Define styles for each button */
        #blackButton {
            background-color:Black;
        }

        #blueButton {
            background-color: Blue;
        }

        #limeButton {
            background-color: Lime;
        }

        #redButton {
            background-color:Red ;
        }

        #whiteButton {
            background-color: White;
        }

        #yellowButton {
            background-color: Yellow;
        }

        #cyanButton {
            background-color: Cyan ;
        }

        #magentaButton {
            background-color: Magenta;
        }

        #greenButton {
            background-color: Green ;
        }

        #grayButton {
            background-color: Gray;
        }

        #silverButton {
            background-color:Silver;
        }

        #maroonButton {
            background-color: Maroon;
        }

        #purpleButton {
            background-color: Purple;
        }

        #orangeButton {
            background-color:darkOrange;
        }

        #siennaButton {
            background-color: sienna;
        }

        #tealButton {
            background-color: teal;
        }

        #brightMaroonButton {
            background-color: #C51A4A; /* Bright Maroon */
        }

        #appleButton {
            background-color: #6CC04A; /* Apple */
        }

        
	</style>
  </head>
  <body>
	<h1>The place of pixels</h1>
    <p>
		Select a color from the top, then hit a pixel to color it.
        
	</p>
	<div class="container">
		<input type="color" id="colorPicker" style="display: inline-block;;margin-bottom: 10px;margin-right: 5px;" value="#ffffff">
	  
	  <!--<button id="submitButton" style="display: none;">Submit Color Change</button>
	   -->
	   <button id="submitButton" style="display: none;">
		<span class="circle1"></span>
		<span class="circle2"></span>
		<span class="circle3"></span>
		<span class="circle4"></span>
		<span class="circle5"></span>
		<span class="text">Submit</span>
		</button>
		<div class="grid-container" style="margin-bottom: 5px;" >
			<!-- Black button -->
            <div id="blackButton" class="grid-item" onclick="changeColor('#000000')"></div>

            <!-- Blue button -->
            <div id="blueButton" class="grid-item" onclick="changeColor('#0000FF')"></div>

            <!-- Lime button -->
            <div id="limeButton" class="grid-item" onclick="changeColor('#00FF00')"></div>

            <!-- Red button -->
            <div id="redButton" class="grid-item" onclick="changeColor('#FF0000')"></div>

            <!-- White button -->
            <div id="whiteButton" class="grid-item" onclick="changeColor('#FFFFFF')"></div>

            <!-- Yellow button -->
            <div id="yellowButton" class="grid-item" onclick="changeColor('#FFFF00')"></div>

            <!-- Cyan button -->
            <div id="cyanButton" class="grid-item" onclick="changeColor('#00FFFF')"></div>

            <!-- Magenta button -->
            <div id="magentaButton" class="grid-item" onclick="changeColor('#FF00FF')"></div>

            <!-- Green button -->
            <div id="greenButton" class="grid-item" onclick="changeColor('#008000')"></div>

            <!-- Gray button -->
            <div id="grayButton" class="grid-item" onclick="changeColor('#808080')"></div>

            <!-- Silver button -->
            <div id="silverButton" class="grid-item" onclick="changeColor('#C0C0C0')"></div>

            <!-- Maroon button -->
            <div id="maroonButton" class="grid-item" onclick="changeColor('#800000')"></div>

            <!-- Purple button -->
            <div id="purpleButton" class="grid-item" onclick="changeColor('#800080')"></div>

            <!-- Orange button -->
            <div id="orangeButton" class="grid-item" onclick="changeColor('#FF8C00')"></div>

            <!-- Sienna button -->
            <div id="siennaButton" class="grid-item" onclick="changeColor('#A0522D')"></div>

            <!-- Teal button -->
            <div id="tealButton" class="grid-item" onclick="changeColor('#008080')"></div>

            <!-- Bright Maroon button -->
            <div id="brightMaroonButton" class="grid-item" onclick="changeColor('#C51A4A')"></div>
			
			<!-- Apple button -->
            <div id="appleButton" class="grid-item" onclick="changeColor('#6CC04A')"></div>

		</div>
	</div>
<?php

// Connect to the database (Replace with your own database credentials)
$host = 'localhost';
include('config.php');
$database = 'web';

$conn = mysqli_connect($host, $username, $password, $database);

if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}


// Retrieve pixel data from the database
    $query = "SELECT x, y, color FROM pixels";
    $result = mysqli_query($conn, $query);

    if (!$result) {
        die("Query failed: " . mysqli_error($conn));
    }

    $grid = array_fill(0, 20, array_fill(0, 20, '#FFFFFF')); // Initialize with white pixels

    while ($row = mysqli_fetch_assoc($result)) {
        $x = $row['x'];
        $y = $row['y'];
        $color = $row['color'];

        $grid[$y][$x] = $color;
    }

    // Handle pixel editing
    if (isset($_POST['x']) && isset($_POST['y']) && isset($_POST['newColor'])) {
        $x = $_POST['x'];
        $y = $_POST['y'];
        $newColor = $_POST['newColor'];

        // Update the database with the new color
        $updateQuery = "UPDATE pixels SET color = '$newColor' WHERE x = $x AND y = $y";
        $updateResult = mysqli_query($conn, $updateQuery);

        if (!$updateResult) {
            die("Update query failed: " . mysqli_error($conn));
        }

        // Update the grid
        $grid[$y][$x] = $newColor;
    }

    // Display the pixel grid
    for ($y = 0; $y < 20; $y++) {
        echo '<div style="line-height: 0;">';
        for ($x = 0; $x < 20; $x++) {
            $color = $grid[$y][$x];
            //echo "<div id='$x,$y' class='pixel' style='background-color: $color;' onclick='editPixel($x, $y)'></div>";
            echo "<div id='$x,$y' class='pixel' style='background-color: $color; border: 2px solid $color;' onmousedown='editPixel($x, $y);' onmouseover='document.getElementById(\"$x,$y\").style.border=\"2px solid gray\"' onmouseout= ' document.getElementById(\"$x,$y\").style.border=\"2px solid $color\" ' ></div>";
        }
        // echo '<br>';
        echo '</div>';
    }
?>



	
   
  <script>
	  
	  // Function to change the color input value
        function changeColor(color) {
            // Get the color input element
            const colorPicker = document.getElementById('colorPicker');
            
            // Set the value of the color input to the specified color
            colorPicker.value = color;
        }

	  
        // Define the grid variable here to make it accessible to JavaScript
        const grid = <?php echo json_encode($grid); ?>;
        let selectedPixel = null;
        //let lastSelectedColor = '#FFFFFF'; // Initialize with white
		
		//let lastSelectedColor= lastSelectedColor
		
        function editPixel(x, y) {
            // Show the color picker input and submit button
            const colorPicker = document.getElementById('colorPicker');
            const submitButton = document.getElementById('submitButton');

            colorPicker.style.display = 'inline-block';
            //submitButton.style.display = 'inline-block';

            // Set the color picker's current value to the last selected color
            //colorPicker.value = lastSelectedColor;

            // Store the selected pixel's coordinates
            
            //const pix= document.getElementById(x+','+y);
            //border: 2px solid white;
            //pix.style.border='2px solid gray';
            
            selectedPixel = { x, y };
            if (selectedPixel) {
                const x = selectedPixel.x;
                const y = selectedPixel.y;
                const newColor = document.getElementById('colorPicker').value;

                // Send an AJAX request to update the pixel color in the database
                const xhr = new XMLHttpRequest();
                xhr.onreadystatechange = function () {
                    if (xhr.readyState === 4 && xhr.status === 200) {
                        // Update the last selected color
                        //lastSelectedColor = newColor;

                        // Reload the page to reflect the updated pixel color
                        location.reload();
                    }
                };
                xhr.open("POST", "", true); // Use the same URL to handle the POST request
                xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
                xhr.send(`x=${x}&y=${y}&newColor=${newColor}`);
            }
        }

        // When the user clicks the submit button
        const submitButton = document.getElementById('submitButton');
        submitButton.addEventListener('click', function () {
            if (selectedPixel) {
                const x = selectedPixel.x;
                const y = selectedPixel.y;
                const newColor = document.getElementById('colorPicker').value;

                // Send an AJAX request to update the pixel color in the database
                const xhr = new XMLHttpRequest();
                xhr.onreadystatechange = function () {
                    if (xhr.readyState === 4 && xhr.status === 200) {
                        // Update the last selected color
                        //lastSelectedColor = newColor;

                        // Reload the page to reflect the updated pixel color
                        location.reload();
                    }
                };
                xhr.open("POST", "", true); // Use the same URL to handle the POST request
                xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
                xhr.send(`x=${x}&y=${y}&newColor=${newColor}`);
            }
        });
    </script>
  
</body>
</html>
