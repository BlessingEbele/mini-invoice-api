from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Invoice

class InvoiceAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.invoice_data = {
            "client_name": "Jane Doe",
            "description": "Website redesign project",
            "amount": 500.00,
            "status": "Pending"
        }

    def test_create_invoice(self):
        response = self.client.post('/api/invoices/', self.invoice_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Invoice.objects.count(), 1)
        self.assertEqual(Invoice.objects.get().client_name, "Jane Doe")

    def test_list_invoices(self):
        Invoice.objects.create(**self.invoice_data)
        response = self.client.get('/api/invoices/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
