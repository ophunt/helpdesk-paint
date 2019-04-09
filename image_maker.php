<?php

$img = imagecreatetruecolor(100, 100);
$black = imagecolorallocate($img, 0, 0, 0);
$white = imagecolorallocate($img, 255, 255, 255);
imagefill($img, 0, 0, $black);

$test_string = $argv[2];

for ($i = 0; $i < 100; $i++) {
	$x = 10 * ($i % 10);
	$y = $i - $x/10;
	$c = substr($test_string, $i, 1);
	if (intval($c) == 1) {
		imagefilledrectangle($img, $x, $y, $x+10, $y+10, $white);
	}
}

imagepng($img, "static/image.png");
imagedestroy($img);

// $img_content = ob_get_clean();

// file_put_contents("image.png", $img_content);

?>
