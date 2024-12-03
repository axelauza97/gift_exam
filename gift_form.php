<?php
    if ($_SERVER["REQUEST_METHOD"] == "GET") {
        $indices = escapeshellarg($_GET['indices']);
        
        // Execute Python script with passed arguments
        $command = escapeshellcmd("python3 /var/www/html/gift_selector.py $indices");
        $output = shell_exec($command);

        // Display Python script output
        echo $output;
    }
?>