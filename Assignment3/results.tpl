<!DOCTYPE html>
<html>
	<head>
		<title>Registrar's Office Class Search</title>
	</head>
	<body>
		% include('header.tpl')
		<hr>
		<h2><strong>Class Details (class id {{classid}})</strong></h2>
		<br>

		<strong>Course Id: </strong> {{d["courseid"][0]}} <br>
		<strong>Days: </strong> {{d["days"][0]}} <br>
		<strong>Start time: </strong> {{d["starttime"][0]}} <br>
		<strong>End time: </strong> {{d["endtime"][0]}} <br>
		<strong>Building: </strong> {{d["bldg"][0]}} <br>
		<strong>Room:  </strong> {{d["roomnum"][0]}} <br>

		<hr>

		<br>

		<h2><strong>Course Details (course id {{d["courseid"][0]}})</strong></h2>

		<br>
		% for cur in d["deptcoursenum"]:
			<strong>Dept and Number: </strong> {{cur}} <br>
		% end
		<strong>Area: </strong> {{d["area"][0]}} <br>
		<strong>Title: </strong> {{d["title"][0]}} <br>
		<strong>Description: </strong> {{d["descrip"][0]}} <br>
		<strong>Prerequisites: </strong> {{d["prereqs"][0]}}<br>
		% for cur in d["profname"]:
			<strong>Professor(s): </strong> {{cur}} <br>
		% end

		<hr>
		<br>
		Click here to do <a href="/search">another class search</a>



		<hr>
		% include('footer.tpl')
	</body>

</html>
