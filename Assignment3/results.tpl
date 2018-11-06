<!DOCTYPE html>
<html>
	<head>
		<title>Registrar's Office Class Search</title>
	</head>
	<body>
		% include('header.tpl')
		<hr>
		<h2><b>Class Details (class id {{classid}})</b><h2>
		<br>
		<b>Course Id: </b> {{d["courseid"][0]}} <br>
		<b>Days: </b> {{d["days"][0]}} <br>
		<b>Start time: </b> {{d["starttime"][0]}} <br>
		<b>End time: </b> {{d["endtime"][0]}} <br>
		<b>Building: </b> {{d["bldg"][0]}} <br>
		<b>Room:  </b> {{d["roomnum"][0]}} <br>

		<hr>
		<br>
		<h2><b>Course Details (course id {{d["courseid"][0]}})</b></h2>
		<br>
		% for cur in d["deptcoursenum"]:
			<b>Dept and Number: </b> {{cur}} <br>
		% end
		<b>Area: </b> {{d["area"][0]}} <br>
		<b>Title: </b> {{d["title"][0]}} <br>
		<b>Description: </b> {{d["descrip"][0]}} <br>
		<b>Prerequisites: </b> {{d["prereqs"][0]}}<br>
		% for cur in d["profname"]:
			<b>Professor(s): </b> {{cur}} <br>
		% end

		<hr>
		<br>
		Click here to do <a href="/search">another class search</a>



		<hr>
		% include('footer.tpl')
	</body>

</html>
