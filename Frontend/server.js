var mysql = require('mysql');
var express = require('express');
var session = require('express-session');
var bodyParser = require('body-parser');
var path = require('path');

var connection = mysql.createConnection({
    host: 'localhost',//host name
    user: 'root',// username of database
    password: '12345',//Password of database
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

app.get('/', function(request, response) {
    response.sendFile(path.join(__dirname + '/login.html'));
});

app.post('/auth', function(request, response) {
    var username = request.body.username;
    console.log(username)
    if (username) {
        connection.query('SELECT * FROM voter WHERE VOTERID = ?', [username], function(error, results, fields) {
            if (results.length > 0) {
                request.session.loggedin = true;
                request.session.username = username;
                response.redirect(path.join('/home.html'));
            } else {
                                response.send("<script language=javascript>alert('Invalid Voter ID'); history.back();</script>");
            }    

            response.end();
        });
    } 
});

app.listen(5000);

//    http://localhost:5000/   30876753