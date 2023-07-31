import requests


class TestCursos:
    headers = {
        'Authorization': 'Token d091ebc2df2b5c5d6af0c33ec3627a6191b54859'
    }
    url_base_cursos = 'http://localhost:8000/api/v2/cursos/'

    def test_get_cursos(self):
        resposta = requests.get(url=self.url_base_cursos, headers=self.headers)

        assert resposta.status_code == 200

    def test_get_curso(self):
        resposta = requests.get(
            url=f'{self.url_base_cursos}4/', headers=self.headers)

        assert resposta.status_code == 200

    def test_post_curso(self):
        novo = {
            "titulo": "Curso de Programação com Ruby 345",
            "url": "http://www.geekuniversity.com.br/cpr234"
        }
        resposta = requests.post(
            url=self.url_base_cursos, headers=self.headers, data=novo)

        assert resposta.status_code == 201
        assert resposta.json()['titulo'] == novo['titulo']

    def test_put_curso(self):
        atualizado = {
            "titulo": "Novo Curso de Ruby 35",
            "url": "http://www.geekuniversity.com.br/ncr35"
        }

        resposta = requests.put(
            url=f'{self.url_base_cursos}6/', headers=self.headers, data=atualizado)  # noqa E501

        assert resposta.status_code == 200

    def test_put_titulo_curso(self):
        atualizado = {
            "titulo": "Novo Curso de Ruby 225",
            "url": "http://www.geekuniversity.com.br/ncr225"
        }

        resposta = requests.put(
            url=f'{self.url_base_cursos}6/', headers=self.headers, data=atualizado)  # noqa E501

        assert resposta.json()['titulo'] == atualizado['titulo']

    def test_delete_curso(self):
        resposta = requests.delete(
            url=f'{self.url_base_cursos}6/', headers=self.headers)

        assert resposta.status_code == 204 and len(resposta.text) == 0
