var http = require("http");

http.createServer(function(request, response) {

var sData =""

var exec = require('child_process').exec;

var child = exec('./shellExec.sh',function(err, stdout, stderr) {

sData =JSON.stringify(stdout);

sData = sData.replace(/\\"/g, '"');

sData = sData.substring(sData.lastIndexOf("%")+6,sData.lastIndexOf(","));

sData = "["+sData+"]";

console.log(sData);

response.writeHead(200, {"Content-Type": "application/json","Access-Control-Allow-Origin": "*"});

response.write(sData);
 
response.end();
  });

}).listen(8845);

