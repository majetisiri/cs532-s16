<?php
	if( $_POST["name"]) {
      if (preg_match("/[^A-Za-z'-]/",$_POST['name'] )) {
         die ("invalid name and name should be alpha");
      }
      echo "Welcome ". $_POST['name'];
	  echo "\n";
	  
	  exit();
	 }
?>
<form method ="POST" action="<?php echo $_SERVER['PHP_SELF'];?>">
	<input type="text" name="name">
	<input type="submit" name="submit" value="OK">
</form>
