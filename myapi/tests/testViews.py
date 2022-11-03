import json
from os import set_inheritable
from .testSetup import testSetup
import pdb
from ..models import * 

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
    
    def test_TeamCreateValid(self):
        res = self.client.post(
            self.teamCreateURL, 
            data=json.dumps(self.teamData),
            content_type='application/json'
        )
        self.assertEqual(res.status_code,200)

    def test_TeamCreateInvalid(self):
        self.teamData['leader'] = "Alpha"
        res = self.client.post(self.teamCreateURL, self.teamData)
        pdb.set_trace()
        self.assertEqual(res.status_code,404)
    
    

  