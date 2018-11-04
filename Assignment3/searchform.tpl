<!DOCTYPE html>
<html>
	<head>
		<title>Registrar's Office Class Search</title>
	</head>
	<body>
		% include('header.tpl')
		<h2>Class Search</h2>
		<hr>
		<form action="searchresults" method="get">
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

		<table>
			<tr>
				<td align="left"><b>ClassID</b></td>
				<td align="left"><b>Dept</b></td>
				<td align="left"><b>Num</b></td>
				<td align="left"><b>Area</b></td>
				<td align="left"><b>Title</b></td>
			</tr>

			% if len(classes) == 0:
				(none)
			% else:
			%	for class in classes:
					<tr>
						<td align="left">{{class.getID()}}</td>
						<td align="left">{{class.getDept()}}</td>
						<td align="left">{{class.getNum()}}</td>
						<td align="left">{{class.getArea()}}</td>
						<td align="left">{{class.getTitle()}}</td>
					</tr>
			%  end
			% end

		</table>



		% include('footer.tpl')
	</body>

</html>
