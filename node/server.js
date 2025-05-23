//  supervisor server.js
const hostname = '0.0.0.0';
const port = 3000;

const express = require("express")
const app = express()

const axios = require('axios');


var mysql = require('mysql2');
const fs = require('fs');
const path = require('path');

// images
// docker makes this break, because the db isn't ready in time
// var con = mysql.createConnection({
//   host: "mysql_db",
//   user: "t-rex",
//   password: "yoursql",
//   database: "mydatabase" // specify the database name
// });
var con;


function connectWithRetry() {
    console.log('Connecting to the database');
    try {
        con = mysql.createConnection({
            host: "mysql_db",
            user: "t-rex",
            password: "yoursql",
            database: "mydatabase" // specify the database name
        });
        con.connect();
        console.log('Connected to the database');
    }
    catch{
        console.log('Error connecting to the database:', err);
        setTimeout(connectWithRetry, 2000);
    }
}
// connectWithRetry();
setTimeout(connectWithRetry, 2000);


// app.get("/images", (req, res, next) => {
//     console.log("images");
//     const sql = "SELECT * FROM images";
//     con.query(sql, function (err, result) {
//         if (err) throw err;
//         console.log("Result: " + result);
//         res.send(result);

//     });
// });






app.get("/", (req, res, next) => {
    res.send("nothing here");
});

// pixel editing
app.get("/pixel", (req, res, next) => {
    
    const id = req.query.id;
    const color = req.query.color;
    console.log(color);
    const sql = `UPDATE pixels SET color = '${color}' WHERE id = ${id}`;
    con.query(sql, function (err, result) {
        if (err) throw err;
        console.log("Result: " + result);
        res.send(result);
    });
});



// reset the pixels
// for (let i = 0; i < 100; i++) {
//     const sql = `INSERT INTO pixels ( color) VALUES ( 'FFFFFF')`;
//     con.query(sql, function (err, result) {
//         if (err) throw err;
//         // console.log(`Pixel ${i} set to FFFFFF`);
//     });
// }

app.get("/pixel_data", (req, res, next) => {
    const sql = "SELECT * FROM pixels ORDER BY id";
    con.query(sql, function (err, result) {
        if (err) throw err;
        res.json(result);
    });
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
            const timestamp = new Date().toISOString().slice(0, 19).replace('T', ' '); // get the date to put it
            // console.log(ipAddress.replaceAll(".", "")); // test the ip to unsigned int

            const sql = `INSERT INTO ip_logs (ip_address, note, timestamp) VALUES ('${ipAddress.replaceAll(".", "")}', '${location + additive.slice(-5)}', '${timestamp}')`;
            
            con.query(sql, function (err, result) {
                if (err) throw err;
            });
            
        })
        .catch(error => {
            console.error(error);
            res.status(500).send('Error retrieving geolocation');
        });
        
});


// store data for a prank
var run = true
var rate = 500
var beep=false

app.get('/chirp', (req, res) => { // allow client read the remote settings
    res.send(`[${run},${rate},${beep}]`);
    beep=false
});

app.get('/activate', (req, res) => { // change the settings that the client will read
    if (req.query.run !== undefined) {
        run = req.query.run === 'true';
    }
    if (req.query.rate !== undefined) {
        rate = Math.max(parseInt(req.query.rate, 10), 0);
    }
    if (req.query.beep !== undefined) {
        beep = req.query.beep === 'true';
    }
    res.send(`[${run},${rate},${beep}]`);
});

// end prank

// mailbox
app.get('/mailbox', (req, res) => {
    const dataDir = path.join(__dirname, 'mailbox');
    fs.readdir(dataDir, (err, files) => {
        if (err) {
            console.log('Unable to scan directory: ' + err);
            res.status(500).json({ error: 'Unable to read directory' });
            return;
        }
        const result = files.map(filename => ({
            filename,
            path: path.join('mailbox', filename)
        }));
        res.json(result);
    });

});
const multer = require('multer');
// const upload = multer({ dest: 'mailbox/' }); // Set the destination for uploaded files
const storage = multer.diskStorage({
  destination: 'mailbox/',
  filename: (req, file, cb) => {
    cb(null, file.originalname); // keep original name
  }
});
const upload = multer({ storage });

app.post('/upload', upload.single('file'), (req, res) => {
    console.log('upload');
    // console.log(req.body);

    res.send('ok');
    
});

app.get('/delete/:filename', (req, res) => {
    console.log('delete');
    const filename = req.params.filename;
    const filePath = path.join(__dirname, 'mailbox', filename);

    fs.unlink(filePath, (err) => {
        if (err) {
            console.error('Error deleting file:', err);
            res.status(500).json({ error: 'Unable to delete file' });
            return;
        }
        res.json({ success: true, message: 'File deleted' });
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