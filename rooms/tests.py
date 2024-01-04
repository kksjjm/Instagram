# from django.test import TestCase

from rest_framework.test import APITestCase
from . import models

class TestAmenities(APITestCase):
    NAME = "Amenity Test"
    DESC = "Amenity Description"
    URL = "/api/v1/rooms/amenities/"
    
    def setUp(self):
        models.Amenity.objects.create(
            name=self.NAME,
            descriptions=self.DESC,
        )
    
    #naming rule : 앞에 "test_" 를 붙여야함
    def test_all_amenities(self):
        
        #client가 요청을 보내는 것을 시뮬레이션 해볼 수 있음
        response = self.client.get(self.URL)
        data = response.json()
        
        #로그인을 안해도 접근이 가능한지
        self.assertEqual(
            response.status_code, 
            200,
            "통신 실패 Status isn't 200",
        )
        
        self.assertIsInstance(data, list)
        
        # 들어있는 데이터 숫자 확인
        self.assertEqual(
            len(data),
            1,
        )
        
        self.assertEqual(
            data[0]["name"],
            self.NAME,
        )
        
        self.assertEqual(
            data[0]["descriptions"],
            self.DESC,
        )
    
    def test_creat_amenities(self):
        
        new_amenityName = "New Amenity"
        new_amenityDecriptions = "New Amenity descriptions"
        
        response = self.client.post(
            self.URL,
            data={
                "name": new_amenityName,
                "descriptions": new_amenityDecriptions,
            }
        )
        
        data = response.json()
        
        self.assertEqual(
            response.status_code,
            200,
            "통신 실패 Status isn't 200",
        )
        
        self.assertEqual(
            data["name"],
            new_amenityName,
        )
        
        self.assertEqual(
            data["descriptions"],
            new_amenityDecriptions,
        )
        
        response_part = self.client.post(self.URL)

        self.assertEqual(
            response_part.status_code,
            400,
            "필수항목 체크가 잘 작동하지 않는 듯 합니다.",
        )
        
        self.assertIn("name", data)
        self.assertIn("descriptions", data)