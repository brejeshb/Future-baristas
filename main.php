<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Welcome Page</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        .welcome-container {
            background: #fff;
            padding: 20px 40px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            text-align: center;
        }
        .welcome-container h1 {
            margin: 0 0 20px;
            font-size: 2em;
            color: #333;
        }
        .welcome-container p {
            margin: 0 0 20px;
            font-size: 1.2em;
            color: #666;
        }
        .buttons {
            margin-top: 20px;
        }
        .buttons button {
            background-color: #007bff;
            color: white;
            border: none;
            padding: 10px 20px;
            font-size: 1em;
            border-radius: 5px;
            cursor: pointer;
            margin: 0 10px;
        }
        .buttons button:hover {
            background-color: #0056b3;
        }
    </style>
</head>
<body>
    <div class="welcome-container">
        <?php
        // Set the welcome message
        $welcomeMessage = "Welcome to My Website!";
        
        // Display the welcome message
        echo "<h1>$welcomeMessage</h1>";
        
        // Optionally, display the current date and time
        echo "<p>Today's date is " . date("l, F j, Y") . ".</p>";
        ?>
        <div class="buttons">
            <button onclick="location.href='userlogin.php'">User Log In</button>
            <button onclick="location.href='orglogin.php'">Organisation Log In</button>
        </div>
    </div>
</body>
</html>

