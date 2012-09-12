from plone.app.layout.viewlets.common import ViewletBase
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.app.component.hooks import getSite


class footerView(ViewletBase):
    """
    Clase para el viewlet footer
    """
    render = ViewPageTemplateFile('footer.pt')

    def profiles(self):
        site = getSite()
        existing = site.contentIds()
        categorias = ['estudiantes-docentes',
                    'ciudadano',
                    'instituciones',
                    'proveedores',
                    'profesionales',
                    'ong','empresa']
        lista = []
        for item in categorias:
            if item in existing:
                lista.append(item)
        return lista