

<!DOCTYPE html>
<html>
	<head>
		<title>Registrar's Office Class Search</title>
	</head>
	<body>
		% include('header.tpl')
		<h2>Class Search</h2>
		<hr>
		<form action="search" method="get">
			<table>
				<tr>
					<td align="left">Dept: </td>
					<td align="left"><input type="text" name="dept"></td>
				</tr>
				<tr>
					<td align="left">Course Num: </td>
					<td align="left"><input type="text" name="coursenum"></td>
				</tr>
				<tr>
					<td align="left">Area:</td>
					<td align="left"><input type="text" name="area"></td>
				</tr>
				<tr>
					<td align="left">Title: </td>
					<td align="left"><input type="text" name="title"></td>
				</tr>
				<tr>
					<td align="left"> </td>
					<td align="left"><input type="submit" value="Go"></td>
				</tr>
			</table>
		</form>
		<hr>
		<br> 
    <br>
		% include('footer.tpl')
	</body>

</html>

		