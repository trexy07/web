//  supervisor server.js
const hostname = '0.0.0.0';
const port = 3000;


const express = require("express")
const app = express()

const axios = require('axios');




var mysql = require('mysql2');

// images

var con = mysql.createConnection({
  host: "mysql_db",
  user: "root",
  password: "rootpassword",
  database: "images" // Ensure you specify the database name
});

con.connect(function(err) {
  if (err) throw err;

  console.log("Connected!");
});
app.get("/images", (req, res, next) => {
    console.log("images");
    const sql = "SELECT * FROM images";
    con.query(sql, function (err, result) {
        if (err) throw err;
        console.log("Result: " + result);
        res.send(result);

    });
});




app.get("/joke1", (req, res, next) => {
    res.send("Why did the chicken cross the road?");
});


app.get("/", (req, res, next) => {
    res.send("nothing here");
});



// Handling GET /hello request
app.get("/hello", (req, res, next) => {
    res.send("This is an endpoint!!!!!!");
})
const apiKey = "6f7edfb1a7af4b2893e28267f1104d79";

app.get('/iplog', (req, res) => {
    const ipAddress = req.headers['x-forwarded-for'];

    var additive = '';
    if (ipAddress === "12.9.54.246") {
        additive="<br>  you're at NYOS";
        // myfile.write("NYOS");
    } else if (ipAddress === "192.168.1.254") {
        additive="<br> you're at home";
        // myfile.write("home");
    } //else {
       // myfile.write("idk");
    //}

    // check db log for chaching first, otherwise call the api

    axios.get(`https://api.ipgeolocation.io/ipgeo?apiKey=${apiKey}&ip=${ipAddress}`)
        .then(response => {
            const { city, state_prov, country_name } = response.data;
            const location = `${city}, ${state_prov}, ${country_name}`;
            res.send(`Your IP address is: ${ipAddress}. <br> Your location is: ${location} ${additive}`);
            // add row to the db
            
        })
        .catch(error => {
            console.error(error);
            res.status(500).send('Error retrieving geolocation');
        });
});


app.get('*', function (req, res) {
    res.status(404).send('node dont know this path :(' + req.url);

    // res.status(404).sendFile('static/404.html', { root : __dirname});
});





// Server setup
app.listen(3000, () => {
    console.log(`Server running at http://${hostname}:${port}/`);

})