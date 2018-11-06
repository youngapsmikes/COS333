<!DOCTYPE html>
<html>
   <head>
      <title>Penny.com</title>
   </head>
   <body>
      % include('header.tpl')
      <h1>Author Search Results</h1>
      <h2>Books by {{author}}:</h2>
      % if len(books) == 0:
           (None)
      % else:
      %    for book in books:
              {{book.getAuthor()}}, {{book.getTitle()}},
              ${{book.getPrice()}}<br>
      %    end
      % end
      <br>
      <br>
      Click here to do another 
      <a href="searchform">author search</a>.
      <br>
      <br>
      % include('footer.tpl')
   </body>
</html> 
