<!DOCTYPE html>
<html>
	<head>
		<title>Registrar's Office Class Search</title>
	</head>
	<body>
		% include('header.tpl')
		<hr>
		<h2><em>Class Details (class id {{classid}})</em><h2>
		<br>
		<em>Course Id: </em> {{d["courseid"][0]}} <br>
		<em>Days: </em> {{d["days"][0]}} <br>
		<em>Start time: </em> {{d["starttime"][0]}} <br>
		<em>End time: </em> {{d["endtime"][0]}} <br>
		<em>Building: </em> {{d["bldg"][0]}} <br>
		<em>Room:  </em> {{d["roomnum"][0]}} <br>

		<hr>
		<br>
		<h2><em>Course Details (course id {{d["courseid"][0]}})</em></h2>
		<br>
		% for cur in d["deptcoursenum"]:
			<em>Dept and Number: </em> {{cur}} <br>
		% end
		<em>Area: </em> {{d["area"][0]}} <br>
		<em>Title: </em> {{d["title"][0]}} <br>
		<em>Description: </em> {{d["descrip"][0]}} <br>
		<em>Prerequisites: </em> {{d["prereqs"][0]}}<br>
		% for cur in d["profname"]:
			<em>Professor(s): </em> {{cur}} <br>
		% end

		<hr>
		<br>
		Click here to do <a href="/search">another class search</a>



		<hr>
		% include('footer.tpl')
	</body>

</html>
