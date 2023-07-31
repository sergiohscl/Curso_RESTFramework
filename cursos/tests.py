from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory
from cursos.models import Curso


class CursoViewSetTestCase(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        Curso.objects.create(titulo="title1", url='url1')
        Curso.objects.create(titulo="title2", url='url2')
        key_sergio = "d091ebc2df2b5c5d6af0c33ec3627a6191b54859"
        key_augusto = "4821039c20c584aa43227e0bdf606fc06cbe3b97"
        self.headers_s = f'Token {key_sergio}'
        self.headers_a = f'Token {key_augusto}'

    def test_get_cursos(self):
        url = '/api/v2/cursos/'
        self.client.credentials(HTTP_AUTHORIZATION=self.headers_s)
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
