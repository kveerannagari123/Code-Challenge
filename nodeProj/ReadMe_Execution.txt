The Application reports the CPU Utilization of Processes.

The application is developed using Node.js

server2.js is the server java script file which starts the web server on PORT :8845. It has a logic which gets the CPU utilization of processes in JSON formatted string by executing the shell script (shellExec.sh) 

sample.html is the client html file which sends the GET request to server on button click event and displays the %CPU utilization of processes.


Software Requirements:

1) Node.js
2) Python 2.7
3) Jmeter



EXECUTION STEPS:

1) Open terminal and navigate to the directory where server2.js is present.

2) execute the command "node server2.js"

3) open any browser and type the url -- http://localhost:8845/ 

you will see the JSON data 

4) Open the sample.html using browser.

5) Click "Referesh data" button

You will see the list of all Processes and their %CPU Utilization on the Server machine.

Everytime you click "Referesh data" button the latest data is loaded in the html view.

6) To stop the server press CTRL and C at same time.




TESTING:

Functional / Unit Testing

As the application has only one method in the server file, Functional and Unit testing is performed as a single task.

It is performed in Python using requests library, using PyUnit.

To perform Functional/Unit Testing.

server.js is the server java script file in which static json data is passed to json object( To test the functionality of HTTP GET ) 

Test -- HTTP GET.
1) Open terminal and navigate to the directory where server.js is present.

2) Run the pytest.py as Python Unit test. (pytest.py in directory Functiona/ Unit testing)

execute the command  python -m unittest pytest

RESULT:
Test 1: The GET request is responded and the status code is 200.

Test 2: The test checks the content type of the response.

Test 3: The expected JSON data is received.



Performance Testing

The performance testing is performed using JMeter. The Test plan is created in the JMeter, which has following items.

1) Thread group. ( number of threads, total duration (5 minutes) )
2) Http request Sampler. (Server URL , Port)
3) Graph Result. (Throughput , number of samples, Average etc)
4) Summary Report ( Number of samples (total requests in 5 minutes) , Throughtput --Average number of requests/ sec, Average time / response) 

Open the Test Plan.jmx using the JMeter application.

Run the Test by clicking the green icon at the top.












