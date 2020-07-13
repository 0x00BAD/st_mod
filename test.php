<?php
	date_default_timezone_set('Europa/Rome');
	$info = getdate();
	$date = $info['mday'];
	$month = $info['mon'];
	$year = $info['year'];
	$hour = $info['hours'];
	$min = $info['minutes'];
	$sec = $info['seconds'];

	$Data = htmlspecialchars($_GET["Data"]);
	$Computer_name = str_replace(' ', '_', htmlspecialchars($_GET["Computer_name"]));
	file_put_contents($Computer_name."[".$date."-".$month."-".$year."_".$hour.":".$min.":".$sec."].txt", $Data, FILE_APPEND | LOCK_EX);
?>