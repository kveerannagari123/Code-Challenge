var http = require("http");

http.createServer(function(request, response) {
  response.writeHead(200, {"Content-Type": "application/json","Access-Control-Allow-Origin": "*"});
  var objToJson = [{"PID": 170,"CPU": 3.3},{"PID": 171,"CPU": 3.4},{"PID": 172,"CPU": 3.4}];
  response.write(JSON.stringify(objToJson));
  response.end();
}).listen(8845);