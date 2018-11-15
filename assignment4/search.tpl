<!DOCTYPE html>
<html>
  <head>
    <title>Registrar's Office Class Search</title>

    <meta name="viewport" content="width=device-width, initial-scale=1">

    <link rel="stylesheet"
      href="https://www.w3schools.com/w3css/4/w3.css">
  </head>

  <body onload="getResults(); 
  document.getElementById('department').focus()">
    
    <div class="w3-container w3-orange">
      <center>
        <h1>Registrar's Office: Class Search</h1>
      </center>
      <div class="w3-row">
        <div class="w3-quarter">
          <input type="text" id="department" placeholder = "Department" 
          oninput="getResults()">
        </div>
        <div class="w3-quarter">
          <input type="text" id="coursenum" placeholder = "Course Number"
          oninput="getResults()">
        </div>
        <div class="w3-quarter">
          <input type="text" id="area" placeholder = "Area" 
          oninput="getResults()">
        </div>
        <div class="w3-quarter">
          <input type="text" id="title" placeholder = "Title" 
          oninput="getResults()">
        </div>
     </div>
     <br>
    </div>

      <table class ="w3-table w3-striped w3-border">
        <tr>
          <th>ClassID</th>
          <th>Dept</th>
          <th>Num</th>
          <th>Area</th>
          <th>Title</th>
        <tbody id="data"></tbody>

      </table>

      <div class="w3-container w3-orange">
      <center>
        Created by Quinn Donohue and Michael Li
      </center>

      <script>

        function createAjaxRequest()  // From Nixon book
         {
            var req;
                       
            try  // Some browser other than Internet Explorer
            {
               req = new XMLHttpRequest();
            }
            catch (e1) 
            {    
               try  // Internet Explorer 6+
               {
                  req = new ActiveXObject("Msxml2.XMLHTTP");
               }
               catch (e2) 
               {  
                  try  // Internet Explorer 5
                  { 
                     req = new ActiveXObject("Microsoft.XMLHTTP"); 
                  }
                  catch (e3)
                  {  
                     req = false;
                  }
               }
            }
            return req;
         }

        // also taken from PennyAjax
        function processReadyStateChange()
         {
            var STATE_UNINITIALIZED = 0;
            var STATE_LOADING       = 1;
            var STATE_LOADED        = 2;
            var STATE_INTERACTIVE   = 3;
            var STATE_COMPLETED     = 4;
            
            if (this.readyState != STATE_COMPLETED)
               return;
            
            if (this.status != 200)  // Request succeeded?
            {  
               //alert(
               //   "AJAX error: Request failed: " + this.statusText);
               return;
            }
            
            if (this.responseText == null)  // Data received?
            {  
               alert("AJAX error: No data received");
               return;
            }

            var data = 
               document.getElementById("data");
            data.innerHTML = this.responseText;
         }

        var seed = date.getSeconds();
        var request = null;

        // heavily inspired by pennyajax
        function getResults() {
          var dept = document.getElementById('department').value;
          dept = encodeURIComponent(dept);
          var coursenum = document.getElementById('coursenum').value;
          coursenum = encodeURIComponent(coursenum);
          var area = document.getElementById('area').value;
          area = encodeURIComponent(area);
          var title = document.getElementById('title').value;
          title = encodeURIComponent(title);

          var messageID = Math.floor(Math.random(seed) * 1000000) + 1;

          var url = "/searchresults?dept=" + dept + "&coursenum=" +
            coursenum + "&area=" + area + "&title=" + title +
            "&messageId=" + messageID;

          if (request != null)
            request.abort();

          request = createAjaxRequest();
          if (request == null) return;
          request.onreadystatechange = processReadyStateChange;
          request.open("GET", url);
          request.send(null);
        }
      </script>

  </body>

</html>


