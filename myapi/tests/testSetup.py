from rest_framework.test import APITestCase
from django.urls import reverse 

class testSetup(APITestCase):
    
    def setUp(self):
        
        self.employeeListURL = reverse('employee-list')
        # self.employeeDetailURL = reverse('employee-detail')
        self.employeeCreateURL = reverse('employee-create')
        self.teamCreateURL = reverse('team-create')

        
        self.employeeData = {
            "empId": 1,
            "name": "Test",
            "currTeam": "",
            "workArr": "",
            "role": "",
            "rate": "1.35"
        }
        self.teamData = {
            "name":"Alpha",
            "leader":""
        }

        return super().setUp()
        
    def tearDown(self):

        return super().tearDown()


