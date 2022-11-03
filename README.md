# Employee Management System

This is an employee management API using the Django framework. 

## Models

There are 5 models in this project 

### Employee

This model represents a single employee and has the following fields:
- empId: Employee ID
- name: Employee Name
- currTeam: The team that the employee refer to Team object
- rate: Hourly Rate
- workArr: Work arrangement either part time or full time 
- role: Representing the roles which are members and leaders

### Team

This model represents a Team of employees and has the following fields:
- teamId: Team ID
- name: Team Name
- leader: Team Leader refers to Employee object 

### Work Arrangement

This model represents a work arrangement of employees and has the following fields:
- waID: Arrangement ID
- name: Arrangement Name

### Role 

This model represents a role of employees and has the following fields:
- roleID: Role Id
- name: Role name 

### Payroll

This model recrods the hours of employees and has the following fields:
- empID: Employee ID refers to Employee mode
- hours: Hours worked 




## Routes

### Employee

`/employee-detail/<pk>`

GET - Returns information and monthly pay for the Employee with the specified `pk`

`/employee-list`

GET - returns all Employee objects  and monthly pay for the Employees


`/employee-create/`

POST - Creates and stores a new Employee object

Expects values for the following in the request body:
- name
- currTeam
- rate
- workArr
- role

`/employee-update/<pk>`

POST - Edits a specific Employee object

Expects values for the following in the request body:
- empId
- name
- currTeam
- rate
- workArr
- role


`/employee-delete/<pk>`

GET - Deletes the Employee object with the specified `pk`

### Team

`/team-list/`

GET - returns all Team objects

`/team-detail/<pk>`

GET - Returns information about the Team with the specified `pk`

`/team-create/`

POST - Creates and stores a new Team object

Expects values for the following in the request body:
- name
- leader

`/team-update/<pk>`

POST - Edits a specific Team object

Expects values for the following in the request body:
- teamId
- name
- leader

`/team-delete/<pk>`

GET - Deletes the Team object with the specified `pk`

### Role

`/role-list/`

GET - returns all Role objects
POST - Creates and stores a new Role object
	Expects values for the following in the request body:
	- name


`/role-detail/<pk>`

GET - Returns information about the Role with the specified `pk`
POST - Edits a specific Role object
	Expects values for the following in the request body:
	- roleID
	- name
DELETE - Deletes the Role object with the specified `pk`

### Work Arrangement

`/workArrangement-list/`

GET - returns all work arrangement objects
POST - Creates and stores a new work arrangement object
	Expects values for the following in the request body:
	- name


`/workArrangement-detail/<pk>`

GET - Returns information about the work arrangement with the specified `pk`
POST - Edits a specific work arrangement object
	Expects values for the following in the request body:
	- waID
	- name
DELETE - Deletes the work arrangement object with the specified `pk`

