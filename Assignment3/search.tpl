<!DOCTYPE html>
<html>
  <head>
    <title>Registrar's Office Class Search</title>
  </head>
  <body>
    % include('header.tpl')
    <h2>Class Search</h2>
    <hr>
    <form action="search" method="get">
      <table>
        <tr>
          <td align="left">Dept: </td>
          <td align="left"><input type="text" name="dept" value = {{"Fuck"}} ></td>
        </tr>
        <tr>
          <td align="left">Course Num: </td>
          <td align="left"><input type="text" name="coursenum" ></td>
        </tr>
        <tr>
          <td align="left">Area:</td>
          <td align="left"><input type="text" name="area" ></td>
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
    <br> 
    <br>
    <table>
      <tr>
        <td align="left"><b>ClassID</b></td>
        <td align="left"><b>Dept</b></td>
        <td align="left"><b>Num</b></td>
        <td align="left"><b>Area</b></td>
        <td align="left"><b>Title</b></td>
      </tr>

      % if len(d) == 0:
        (none)
      % else:
      % for i in range(0,len(d[d.keys()[0]])):
          <tr>
            <td align="left"><a href="results/{{d["classid"][i]}}">{{d["classid"][i]}}</a></td>
            <td align="left">{{d["dept"][i]}}</td>
            <td align="left">{{d["coursenum"][i]}}</td>
            <td align="left">{{d["area"][i]}}</td>
            <td align="left">{{d["title"][i]}}</td>
          </tr>
      %  end
      % end
</table>
    % include('footer.tpl')
  </body>

</html>


