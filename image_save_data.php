#!/php_dir/php
<?php

$save_string = $argv[2];

for ($i = 10; $i > 0; $i--) {
	$save_string = substr_replace($save_string, "\n", 10*$i, 0);
}

file_put_contents("image.data", $save_string);

?>
