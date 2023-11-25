# from rest_framework import status
# from rest_framework.test import APITestCase
# from .models import Request
# from .serializers import RequestSerializer
# from django.contrib.auth.models import User
#
#
# class RequestAPITestCase(APITestCase):
#     def setUp(self):
#         self.user = User.objects.create_user(username="testuser", password="testpassword")
#         self.request1 = Request.objects.create(cadastre_number="45:87:9865432:1234", latitude=55.7558, longitude=37.6173, result=True)
#         self.request2 = Request.objects.create(cadastre_number="66:66:9996666:6996", latitude=48.8566, longitude=2.3522, result=False)
#         self.request1_serializer = RequestSerializer(self.request1)
#         self.request2_serializer = RequestSerializer(self.request2)
#
#     def test_get_all_requests(self):
#         response = self.client.get("/history")
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data, [self.request1_serializer.data, self.request2_serializer.data])
#
#     def test_create_request(self):
#         data = {"cadastre_number": "1357924680", "latitude": 40.7128, "longitude": -74.0060}
#         response = self.client.post("/query", data)
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(response.data["cadastre_number"], data["cadastre_number"])
#         self.assertEqual(response.data["latitude"], data["latitude"])
#         self.assertEqual(response.data["longitude"], data["longitude"])
#         self.assertTrue("id" in response.data)
#         self.assertTrue("result" in response.data)
#
#     def test_get_request_by_id(self):
#         response = self.client.get(f"/result/{self.request1.id}")
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data, self.request1_serializer.data)
#
#     def test_ping_server(self):
#         response = self.client.get("/ping")
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertContains(response, "Server is running", status_code=status.HTTP_200_OK)
