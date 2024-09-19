<?php
    $servername = 'localhost';
    $username = 'liiga';
    $password = 'J@mi1414';
    $dbname = 'liiga';

    $conn = new mysqli($servername, $username, $password, $dbname);
    if ($conn->connect_error) {
        echo 'connection failed';
        die('Database connection failed'. $conn->connect_error);
    }
    echo'Connected successfully!';
?>

<html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Liigatesti</title>
    </head>
    <body>
        <h1>Liigatesti</h1>
    </body>
    </html>
</html>