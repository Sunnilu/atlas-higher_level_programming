<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>jQuery Example</title>
    <!-- Include jQuery library -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    <style>
        .red {
            background-color: red;
        }
    </style>
</head>
<body>

<div id="red_header">Click me to change header color</div>
<header>This is a header</header>

<script>
    $(document).ready(function(){
        $('#red_header').click(function(){
            $('header').toggleClass('red'); // Use toggleClass to add/remove 'red' class
        });
    });
</script>

</body>
</html>

