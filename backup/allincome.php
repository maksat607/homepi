<?php
include('session.php');



?>
   <div class="jumbotron">
      <div class="container">
<?php

						$db_host = 'localhost';
						$db_user = 'root';
						$db_pwd = 'maksat';

						$database = 'my_db';
						$table = 'income';
//substr('abcdef', 0, 4); 
						if (!mysql_connect($db_host, $db_user, $db_pwd))
							die("Can't connect to database");

						if (!mysql_select_db($database))
							die("Can't select database");

						// sending query
						$query="SELECT SUM(fare) as total FROM income where type='cash' AND (date BETWEEN '$startd "."00:00:00' AND '".$endd." 00:00:00')";
						$result = mysql_query("SELECT * FROM {$table}");
						if (!$result) {
							die("Query to show fields from table failed");
						}

						$fields_num = mysql_num_fields($result);

						echo "<h1>Table: {$table}</h1>";
						echo "<table border='1'><tr>";
						// printing table headers
						for($i=0; $i<$fields_num; $i++)
						{
							$field = mysql_fetch_field($result);
							echo "<td>{$field->name}</td>";
						}
						echo "</tr>\n";
						// printing table rows
						while($row = mysql_fetch_row($result))
						{
							echo "<tr>";

							// $row is array... foreach( .. ) puts every element
							// of $row to $cell variable
							foreach($row as $cell)
								echo "<td>$cell</td>";

							echo "</tr>\n";
						}
						echo '</table>';
						mysql_free_result($result);

						?>
</div>
</div>