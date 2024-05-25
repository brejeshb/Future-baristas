<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Volunteer Signup</title>
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
        .signup-container {
            background: #fff;
            padding: 20px 40px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            text-align: center;
        }
        .signup-container h1 {
            margin: 0 0 20px;
            font-size: 2.5em;
            color: #333;
        }
        .signup-container form {
            display: flex;
            flex-direction: column;
        }
        .signup-container input {
            margin-bottom: 15px;
            padding: 10px;
            font-size: 1em;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
        .signup-container button {
            background-color: #28a745;
            color: white;
            border: none;
            padding: 10px;
            font-size: 1em;
            border-radius: 5px;
            cursor: pointer;
        }
        .signup-container button:hover {
            background-color: #218838;
        }
    </style>
</head>
<body>
    <div class="signup-container">
        <h1>Volunteer Signup</h1>
        <form method="post">
            {% csrf_token %}
            {{ form.as_p }}
            <button type="submit">Sign Up</button>
        </form>
    </div>
</body>
</html>
