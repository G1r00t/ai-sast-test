const express = require('express');
const mysql = require('mysql');
const fs = require('fs');
const xml2js = require('xml2js');
const app = express();

app.use(express.urlencoded({ extended: true }));

// Dead Code Example 1: Unreachable code
function deadCode1() {
    return;
    console.log("This will never be executed"); // dead code
}

// Dead Code Example 2: Unused function
function unusedFunction() {
    let a = 1;
    let b = 2;
    return a + b;
}

// Dead Code Example 3: Unused variable
let unusedVariable = "I am not used anywhere";

app.get('/sql_injection', (req, res) => {
    let userInput = req.query.username;
    let connection = mysql.createConnection({
        host: "localhost",
        user: "root",
        password: "rootPassword@123",
        database: "test"
    });

    let query = "SELECT * FROM users WHERE username = '" + userInput + "'";
    connection.query(query, (error, results) => {
        if (error) throw error;
        res.send(results);
    });
});


app.get('/secure_sql_query', (req, res) => {
    let userInput = req.query.username;
    let connection = mysql.createConnection({
        host: "localhost",
        user: "root",
        password: "rootPassword@123",
        database: "test"
    });

    let query = "SELECT * FROM users WHERE username = ?";
    connection.query(query, [userInput], (error, results) => {
        if (error) throw error;
        res.send(results);
    });
});


app.get('/broken_auth', (req, res) => {
    let username = req.query.username;
    let password = req.query.password;

    if (username === "adminuser" && password === "xchzdhkrltu") {
        res.send("Authenticated as admin");
    } else {
        res.send("Authentication failed");
    }
});


app.get('/store_sensitive_data', (req, res) => {
    fs.writeFileSync("passwords.txt", "admin:Passwo#d@&1957");
    res.send("Password stored in plaintext");
});


app.get('/parse_xml', (req, res) => {
    let xmlData = req.query.xml;
    xml2js.parseString(xmlData, { explicitArray: false }, (err, result) => {
        if (err) {
            res.send("Error parsing XML");
        } else {
            res.send(result);
        }
    });
});


app.get('/access_control', (req, res) => {
    let role = req.query.role;
    if (role === "admin") {
        res.send("Welcome Admin!");
    } else {
        res.send("Access Denied!");
    }
});


app.get('/security_misconfig', (req, res) => {
    res.setHeader("X-Powered-By", "Express"); 
    res.send("Security Misconfiguration Example");
});

app.get('/xss_vulnerability', (req, res) => {
    let userInput = req.query.input;
    res.send("<html><body>" + userInput + "</body></html>");
});


app.post('/insecure_deserialization', express.json(), (req, res) => {
    let obj = JSON.parse(req.body.data);
    res.send("Deserialized object: " + JSON.stringify(obj));
});

// Dead Code Example 4: Conditional never true
if (false) {
    console.log("This will never run");
}

// Dead Code Example 5: Deprecated API usage (detected by some tools)
function deprecatedExample() {
    new Buffer("unsafe"); // deprecated usage
}

app.listen(3000, () => {
    console.log('Vulnerable Node.js app listening on port 3000');
});
