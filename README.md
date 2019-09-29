# Apple DevOps Coding Challenge
## Robin Peter <robin.peter@gmail.com>


## Requirements
This application requires bash, make and Docker for intended execution.


## Coding Challenge Information
### 01
This tool will takes a path to the folder as an argument, 
and prints the highest build number.

### O2
A tool for finding the network interfaces on a system with
the corresponding IP addresses in CIDR format. 

### 03
1. Identify every earthquake in California from past week
2. List them chronologically (ascending)
3. Display the output in a specified format.


## Program Execution
I chose Python v3.6 as the language for this application. To ensure portability,
the application resides within a Docker container. Please run 'make' for
additional instructions regarding how to assemble and invoke the container.

### Eg:-
```
:➜  make

usage: make [command] [args...]

build  Dev image build.
push   Dev image push.
clean  Clean dangling images.
test   Create the container for testing.
run    Create the container for running the tools.
help   Display this help.
```

## Sample Build & Run Output
```
:➜  make build
docker image build -t rpeets/rpeter-apple:latest .
Sending build context to Docker daemon  53.76kB
Step 1/8 : FROM python:3.6.9-alpine3.10
 ---> 95a9e476c634
....
....
....



:➜  make run
Coding Challenge 01 : Build Number
----------------------------------

Highest Build Number: 21.10


Coding Challenge 02 : IP in CIDR Format
---------------------------------------

      lo : 127.0.0.1/8
      lo : ::1/128
  ens160 : 192.168.8.62/24
  ens160 : fe80::250:56ff:febe:95bb/64
 docker0 : 192.168.4.1/24
 docker0 : fe80::42:c2ff:fec2:8871/64


Coding Challenge 03 : Earthquakes Report
----------------------------------------

2019-09-22T13:55:42+00:00 | 11km NW of Parkfield, California | Magnitude: 1.35
2019-09-22T14:05:31+00:00 | 2km WNW of The Geysers, California | Magnitude: 0.51
2019-09-22T14:08:31+00:00 | 12km SW of Searles Valley, California | Magnitude: -0.17
2019-09-22T14:19:18+00:00 | 8km ENE of Coso Junction, California | Magnitude: 0.96
2019-09-22T14:20:53+00:00 | 27km S of Trona, California | Magnitude: 2.05
2019-09-22T14:41:34+00:00 | 19km E of Little Lake, California | Magnitude: 0.89
2019-09-22T14:48:50+00:00 | 13km ENE of Little Lake, California | Magnitude: 1.59
2019-09-22T15:01:17+00:00 | 13km ENE of Little Lake, California | Magnitude: 1.65
2019-09-22T15:04:09+00:00 | 13km W of Searles Valley, California | Magnitude: 0.98
2019-09-22T15:17:08+00:00 | 8km E of Alum Rock, California | Magnitude: 0.81
2019-09-22T15:23:04+00:00 | 2km NW of Anza, California | Magnitude: 0.06
2019-09-22T15:23:21+00:00 | 7km S of Yucca Valley, California | Magnitude: 0.44
2019-09-22T15:43:54+00:00 | 26km S of Trona, California | Magnitude: 1.35
2019-09-22T15:57:20+00:00 | 4km SW of Petrolia, California | Magnitude: 1.76
2019-09-22T15:58:00+00:00 | 18km E of Little Lake, California | Magnitude: 0.76
2019-09-22T16:18:05+00:00 | 12km SW of Searles Valley, California | Magnitude: 1.05
2019-09-22T16:48:36+00:00 | 7km NE of Coso Junction, California | Magnitude: 1.36
....
....
....
```
