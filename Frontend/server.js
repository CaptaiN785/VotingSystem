var mysql = require('mysql');
var express = require('express');
var session = require('express-session');
var bodyParser = require('body-parser');
var path = require('path');

var connection = mysql.createConnection({
    host: 'localhost',//host name
    user: 'root',// username of database
    password: 'Mukesh@2001',//Password of database
    database : 'votingsystem'//Database name
});

var app = express();
app.use(session({
    secret: 'secret',
    resave: true,
    saveUninitialized: true
}));
app.use(bodyParser.urlencoded({extended : true}));
app.use(bodyParser.json());
app.use(express.static(__dirname));

// app.set("view engine", "pug");  // install pug using this command

app.get('/', function(request, response) {
    response.sendFile(path.join(__dirname + '/login.html'));
});

app.post('/auth', function(request, response) {
    var username = request.body.username;
    console.log(username)
    if (username) {
        var AID = -1;
        connection.query('SELECT * FROM voter WHERE VOTERID = ?', [username], function(error, results, fields) {
            if (results.length > 0) {
                request.session.loggedin = true;
                request.session.username = username;
                AID = results[0].AID;

                // var query = "select * from election where Date >= current_date() and AID = ?";
                // var Election_data = null;
                // connection.query(query,[AID], function(error, election_data, fields){
                //     if(error) throw err;
                //     Election_data = election_data;
                // });
                // response.render(path.join(__dirname, "home"));
                // response.redirect('home.html')
                response.render(path.join(__dirname, 'home.html'))
                console.log("home page should appear.");
            }else {
                response.send("<script language=javascript>alert('Invalid Voter ID'); history.back();</script>");
            }
            response.end();
        });
    }
});

app.listen(5000);

//    http://localhost:5000/   30876753