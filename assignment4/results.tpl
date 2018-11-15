<!DOCTYPE html>
<html>
	<head>
		<title>Registrar's Office: Class Details</title>

		<meta name="viewport" content="width=device-width, initial-scale=1">

    	<link rel="stylesheet"
      href="https://www.w3schools.com/w3css/4/w3.css">
	</head>
	<body>
		<div class="w3-container w3-orange">
      <center>
        <h1>Registrar's Office: Class Details</h1>
      </center>
   	</div>

		<h2>Class Details (class id {{classid}})</h2>
		<br>

		<strong>Course Id: </strong> {{d["courseid"][0]}} <br>
		<strong>Days: </strong> {{d["days"][0]}} <br>
		<strong>Start time: </strong> {{d["starttime"][0]}} <br>
		<strong>End time: </strong> {{d["endtime"][0]}} <br>
		<strong>Building: </strong> {{d["bldg"][0]}} <br>
		<strong>Room:  </strong> {{d["roomnum"][0]}} <br>

		<hr>

		<h2>Course Details (course id {{d["courseid"][0]}})</h2>

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

		<div class="w3-container w3-orange">
      <center>
        Created by Quinn Donohue and Michael Li
      </center>
      </div>
	</body>

</html>
