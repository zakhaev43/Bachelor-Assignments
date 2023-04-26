<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>

<!DOCTYPE html>
<html>

<head>
	<title>Student Tracker App</title>
	
	<link type="text/css" rel="stylesheet" href="css/style.css">
</head>

<body>

	<div id="wrapper">
		<div id="header">
			<h2>Student Tracker </h2>
		</div>
	</div>

	<div id="container">
	
		<div id="content">
		
		
		<!--  add a search box -->
			<form action="StudentControllerServlet" method="GET">
		
				<input type="hidden" name="command" value="SEARCH" />
			
                 <input type="text" name="theSearchName" />
                
                <input type="submit" value="Search" class="add-student-button" />
            
            </form>
		<br/>
			<!-- put new button: Add Student -->
			
			<input type="button" value="Add Student" 
				   onclick="window.location.href='add-student-form.jsp'; return false;"
				   class="add-student-button"
			/>
			
			<br/><br/>
            
            

			<input type="button" value="View Students" 
				   onclick="window.location.href='StudentControllerServlet'; return false;"
				   class="add-student-button"
			/>
		   <br/><br/>
		   <!-- put new button: Edit Student -->
			
			<input type="button" value="Edit Student" 
				   onclick="window.location.href='add-student-form.jsp'; return false;"
				   class="add-student-button"
			/>
			
			<br/><br/>
			
			<!-- put new button: Add Student -->
			
			<input type="button" value="Delete Student" 
				   onclick="window.location.href='add-student-form.jsp'; return false;"
				   class="add-student-button"
			/>
			
			<br/><br/>
		</div>
	
	</div>
</body>


</html>








