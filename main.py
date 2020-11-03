import cherrypy

from zipcode_app import Root, HealthyCheck, ZipCodeApp

cherrypy.config.update({
    'server.socket_host': '0.0.0.0',
    'server.socket_port': 8080,
})

root_conf = \
    {'/': {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}}
cherrypy.tree.mount(Root(), '/', root_conf)

health_check_conf = \
    {'/': {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}}
cherrypy.tree.mount(HealthyCheck(), '/hc', health_check_conf)

zip_code_conf = \
    {'/': {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}}
cherrypy.tree.mount(ZipCodeApp(), '/zipcode', zip_code_conf)

cherrypy.engine.start()
cherrypy.engine.block()