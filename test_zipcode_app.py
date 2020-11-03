import cherrypy

from cherrypy.test import helper

from zipcode_app import ZipCodeApp, Root, HealthyCheck

class SimpleCPTest(helper.CPWebCase):
    @staticmethod
    def setup_server():
        root_conf = \
            {'/': {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}}
        cherrypy.tree.mount(Root(), '/', root_conf)

        health_check_conf = \
            {'/': {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}}
        cherrypy.tree.mount(HealthyCheck(), '/hc', health_check_conf)

        zip_code_conf = \
            {'/': {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}}
        cherrypy.tree.mount(ZipCodeApp(), '/zipcode', zip_code_conf)

    def test_index(self):
        self.getPage("/")
        self.assertStatus('200 OK')
        self.assertBody('Zip Code App')

    def test_empty_cep(self):
        self.getPage("/zipcode")
        self.assertStatus('400 Bad Request')

    def test_invalid_cep(self):
        self.getPage("/zipcode/12345")
        self.assertStatus('400 Bad Request')

    def test_unexistent_cep(self):
        self.getPage("/zipcode/12345678")
        self.assertStatus('200 OK')

    def test_existent_cep(self):
        self.getPage("/zipcode/89035300")
        self.assertStatus('200 OK')
        self.assertBody('{"id": 89035300, "zipcode": "89035300", "city": "Blumenau", "state": "SC", "neighborhood": "Vila Nova", "public_place": "Rua Theodoro Holtrup", "description": ""}')
        
    def test_healthy(self):
        self.getPage("/hc/")
        self.assertStatus('200 OK')
        self.assertBody('OK')
