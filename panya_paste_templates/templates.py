from paste.script.templates import Template, var

class PanyaMinimalTemplate(Template):
    _template_dir = 'templates/panya_minimal'
    summary = 'Creates a buildout providing Django and the Panya base app only.'
