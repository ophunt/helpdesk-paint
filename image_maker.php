<?php

$img = imagecreatetruecolor(100, 100);
$black = imagecolorallocate($img, 0, 0, 0);
$white = imagecolorallocate($img, 255, 255, 255);
imagefill($img, 0, 0, $black);

$data_string = $argv[2];

for ($i = 0; $i < 100; $i++) {
	$x = 10 * ($i % 10);
	$y = $i - $x/10;
	$c = substr($data_string, $i, 1);
	if (intval($c) == 1) {
		imagefilledrectangle($img, $x, $y, $x+10, $y+10, $white);
	}
}

ob_start();
	imagepng($img);
	$img_content = ob_get_clean();
	imagedestroy($img);
ob_end_clean();

file_put_contents("static/image.png", $img_content);

?>
