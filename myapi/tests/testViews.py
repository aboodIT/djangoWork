import json
from os import set_inheritable
from .testSetup import testSetup
import pdb
from ..models import * 
from django.urls import reverse 

class testViews(testSetup):
    def test_EmployeeCreateValid(self):
        res = self.client.post(self.employeeCreateURL, self.employeeData)
        self.assertEqual(res.status_code,200)

    def test_EmployeeCreateInvalid(self):
        team = Team.objects.create(
            name='Alpha'
        )
        self.employeeData['currTeam'] = team 
        res = self.client.post(self.employeeCreateURL, self.employeeData)
        self.assertEqual(res.status_code,404)

    def test_EmployeeDeleteValid(self):
        employee = Employee.objects.create(
            name="test",
            rate=1.00
        )
        response = self.client.delete(
            reverse('employee-delete', kwargs={'pk': employee.empId}))
        self.assertEqual(response.status_code, 200)

    def test_EmployeeDeleteInvalid(self):
        employee = Employee.objects.create(
            name="test",
            rate=1.00
        )
        response = self.client.delete(
            reverse('employee-delete', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, 404)

    
    def test_TeamCreateValid(self):
        res = self.client.post(self.teamCreateURL, self.teamData)
        self.assertEqual(res.status_code,200)

    def test_TeamCreateInvalid(self):
        self.teamData['leader'] = "Alpha"
        res = self.client.post(self.teamCreateURL, self.teamData)
        # pdb.set_trace()
        self.assertEqual(res.status_code,404)
    
    def test_TeamDeleteInvalid(self):
        team = Team.objects.create(
            name = "test",
            leader = Employee.objects.create(
                name="test",
                rate=1.00
            )
        )
        response = self.client.delete(
            reverse('employee-delete', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, 404)    
    


  