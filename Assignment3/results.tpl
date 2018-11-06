<!DOCTYPE html>
<html>
	<head>
		<title>Registrar's Office Class Search</title>
	</head>
	<body>
		% include('header.tpl')
		<hr>
		<h2><b>Class Details (class id {{result.getclassID()}})</b><h2>
		<br>
		<b>Course Id: </b> {{result.getcourseID()}} 
		<b>Days: </b> {{result.getDays()}}
		<b>Start time: </b> {{result.getStart()}}
		<b>End time: </b> {{result.getEnd()}}
		<b>Building </b> {{result.getBuilding()}}
		<b>Room </b> {{result.getRoom()}}

		<hr>
		<br>
		<h2><b>Course Details (course id {{result.getcourseID()}})</b></h2>
		<br>
		<b>Dept and Number: </b> % NEED TO FIGURE OUT HOW TO DO THESE PROBABLY A LOOP
		<b>Area: </b> {{result.getArea()}}
		<b>Title: </b> {{result.getTitle()}}
		<b>Description: </b> {{result.getDescription()}}
		<b>Prerequisites: </b> {{result.getPreReq()}}
		<b>Professor(s): </b> % NEED TO FIGURE OUT HOW TO GET THESE

		<hr>
		<br>

		Click here to do <a href="IDK WHAT URL TO DO HERE PLZ HELP">another class search</a>



		<hr>
		% include('footer.tpl')
	</body>

</html>
