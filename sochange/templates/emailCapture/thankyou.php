<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en"> 
<head> 
	<title>SoChange</title> 
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8" /> 
	<meta http-equiv="Content-Language" content="en" /> 
	<link href="style.css" media="screen" rel="stylesheet" type="text/css" /> 	
</head> 

<body> 
<?php
		require 'email_validator.php';

		$email = $_POST['email'];
		if ($email != '' and check_email_address($email)) {
			$file = fopen('data/emails.txt','a');
			fwrite($file, $email."\n");
			fclose($file);
		}

?>

<div class="main">
	<h1> SoChange</h1>
	<div id="about">
		<p> SoChange is fun way for groups of consumers to discuss the behavior of the companies they buy from and prove that they will reward them for making a positive impact on the world.
		</p>
	</div>
	<div style="margin-top:50px;">
		<h3 style="text-align: right; padding-right: 50px; ">Thank You!</h3>
	</div>
</div> 

</body>
</html>
