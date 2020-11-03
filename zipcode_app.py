import cherrypy

from zipcode_db import ZipCodeDB
from zipcode_dto import ZipCodeDTO


@cherrypy.expose
class Root(object):
    def GET(self):
        return "Zip Code App"


@cherrypy.expose
class HealthyCheck(object):
    def GET(self):
        return "OK"


class ZipCodeApp(object):
    exposed = True

    def GET(self, zipcode=None):
        cherrypy.config.update({'request.show_tracebacks': False})

        if(zipcode is None or len(zipcode) != 8):
            message = 'Zip Code must contain 8 characters'
            raise cherrypy.HTTPError(400, message=message)

        zip_code = self.get_zip_code(zipcode)

        if zip_code:
            return zip_code
        else:
            return(f'Zip code {zipcode} does not exist.')

    def get_zip_code(self, param=''):

        db = ZipCodeDB('base/cep.db')
        zip_codes = db.select_where(f"cep = '{param}'")
        db.close()

        result = []
        for zipcode in zip_codes:
            result.append(f"{ZipCodeDTO(zipcode).to_json()}")
        return result