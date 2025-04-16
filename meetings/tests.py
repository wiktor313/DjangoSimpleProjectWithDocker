from django.test import TestCase
from django.urls import reverse
from meetings.models import Meeting, Room
from django.contrib.auth import get_user_model
from datetime import datetime, time

class MeetingDetailViewTest(TestCase):
    def setUp(self):
        self.room = Room.objects.create(name="Test Room", floor_number=1, room_number=101)

        self.user = get_user_model().objects.create_user(username="testuser", password="password")

        self.meeting = Meeting.objects.create(
            title="Test Meeting",
            date=datetime(2025, 4, 15, 10, 0),
            start_time=time(10, 0),
            duration=2,
            room=self.room
        )
        
        self.client.login(username="testuser", password="password")

    def test_user_detail(self):
        response = self.client.get(reverse('detail', args=[self.user.id]))
        
        self.assertEqual(response.status_code, 200)

        self.assertContains(response, "testuser")
        
        self.assertTemplateUsed(response, 'meetings/detail.html')

    def test_meeting_detail_meeting(self):
        response = self.client.get(reverse('detail', args=[self.meeting.id]))
        
        self.assertEqual(response.status_code, 200)

        self.assertContains(response, "Test Meeting")

        self.assertContains(response, "Test Room")
        
        self.assertContains(response, "101")
        
        self.assertTemplateUsed(response, 'meetings/detail.html')
        
        

    def test_meeting_detail_view_not_found(self):
        response = self.client.get(reverse('detail', args=[999]))
        
        self.assertEqual(response.status_code, 404)