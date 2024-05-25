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
            flex-direction: column;
            align-items: center;
        }
        .welcome-container {
            background: #fff;
            padding: 20px 40px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            text-align: center;
            margin-top: 50px;
        }
        .welcome-container h1 {
            margin: 0 0 20px;
            font-size: 2.5em;
            color: #333;
        }
        .welcome-container p {
            margin: 0 0 20px;
            font-size: 1.2em;
            color: #666;
        }
        .welcome-container .quote {
            font-style: italic;
            color: #555;
            margin: 20px 0;
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
        .volunteer-section {
            background: #e9f5f9;
            padding: 40px;
            border-radius: 10px;
            text-align: center;
            margin: 20px 0;
        }
        .volunteer-section img {
            max-width: 100%;
            height: auto;
            border-radius: 10px;
        }
        .volunteer-section h2 {
            font-size: 2em;
            margin: 20px 0;
            color: #007bff;
        }
        .volunteer-section p {
            font-size: 1.2em;
            color: #333;
        }
        .volunteer-section .cta-button {
            background-color: #28a745;
            color: white;
            border: none;
            padding: 10px 20px;
            font-size: 1em;
            border-radius: 5px;
            cursor: pointer;
            margin-top: 20px;
        }
        .volunteer-section .cta-button:hover {
            background-color: #218838;
        }
    </style>
</head>
<body>
    <div class="welcome-container">
        <?php
        // Set the welcome message
        $welcomeMessage = "Welcome to Valueteer!";
        
        // Display the welcome message
        echo "<h1>$welcomeMessage</h1>";
        
        // Optionally, display the current date and time
        ?>
        <div class="quote">
            "The best way to find yourself is to lose yourself in the service of others." - Mahatma Gandhi
        </div>
        <div class="buttons">
            <button onclick="location.href='user_login.php'">User Log In</button>
            <button onclick="location.href='organisation_login.php'">Organisation Log In</button>
        </div>
    </div>

    <div class="volunteer-section">
        <img src="volunteer.jpg" alt="Volunteers in action">
        <h2>Join Us in Making a Difference!</h2>
        <p>Volunteering is a great way to give back to your community, learn new skills, and meet new people. Whether you have a lot of time to give or just a little, your contributions can make a significant impact.</p>
        <button class="cta-button" onclick="location.href='volunteer_signup.php'">Become a Volunteer</button>
    </div>
</body>
</html>
