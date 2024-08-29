//  supervisor server.js
const hostname = '0.0.0.0';
const port = 3000;


const express = require("express")
const app = express()



app.use(express.static("static/"));

// Handling GET /hello request
app.get("/hello", (req, res, next) => {
    res.send("This is an endpoint");
})

app.get('*', function(req, res){
  res.status(404).send('u got a 404');
  // res.status(404).sendFile('static/404.html', { root : __dirname});
  

});

// Server setup
app.listen(3000, () => {
    console.log(`Server running at http://${hostname}:${port}/`);

})