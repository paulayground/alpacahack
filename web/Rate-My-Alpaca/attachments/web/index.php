<?php

$message = '';

if (isset($_FILES['file'])) {
    $filename = $_FILES['file']['full_path'];
    $uploaddir = '/var/www/uploads/';
    $uploadfile = $uploaddir . $filename;
    $uploadurl = '/uploads/' . $filename;
    move_uploaded_file($_FILES['file']['tmp_name'], $uploadfile);

    $message = "File uploaded to <a href=\"" . $uploadurl . "\">" . $uploadurl . "</a>. Please wait 15~20 business days until we rate your alpaca image.";
}
?><!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <title>Rate My Alpaca</title>
</head>
<body>
    <h1>Rate My Alpaca</h1>
    <?php 
        if ($message !== '') {
            echo $message;
        }
    ?>
    
    <form method="POST" enctype="multipart/form-data">
        <label for="file">Upload your Alpaca image</label>
        <input type="file" name="file">
        <br>
        <button type="submit">Upload</button>
    </form>
</body>
</html>
