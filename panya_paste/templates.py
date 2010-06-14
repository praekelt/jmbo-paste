from paste.script.templates import Template, var

class PanyaMinimalTemplate(Template):
    _template_dir = 'templates/panya_minimal'
    summary = 'Creates a buildout providing Django and the Panya base app only.'

class PanyaDeployTemplate(Template):
    _template_dir = 'templates/panya_deploy'
    summary = 'Creates a buildout providing 3 Django instances (production, staging and qa), NGINX and FCGI control scripts, and a selection of Panya and Django apps.'
