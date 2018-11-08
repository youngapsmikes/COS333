<!DOCTYPE html>
<html>
   <head>
      <title>Penny.com</title>
   </head>
   <body>
      % include('header.tpl')
      <h1>Author Search</h1>
      <form action="searchresults" method="get">
         Please enter an author name:
         <input type="text" name="author" value = {{prevAuthor}}>
         <input type="submit" value="Go">
      </form>
      <br>
      <strong>{{errorMsg}}</strong>    
      <br>
      <br>
      <strong>Previous author search: {{prevAuthor}}</strong> 
      <br>
      <br>
      % include('footer.tpl')
   </body>
</html>