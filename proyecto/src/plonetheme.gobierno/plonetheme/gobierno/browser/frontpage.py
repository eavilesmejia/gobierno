from Products.Five import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.app.component.hooks import getSite
from Products.CMFCore.utils import getToolByName

from DateTime.DateTime import DateTime
import datetime

class frontPageView(BrowserView):
    template = ViewPageTemplateFile('frontpage.pt')

    def events_show(self):
         portal = getSite()
         catalog = getToolByName(portal, 'portal_catalog')
         existing = portal.contentIds()
         limit = 4
         if 'proximos-eventos' in existing:
             eventLimit = getattr(portal,'proximos-eventos')
             limit = eventLimit.getItemCount()

         return catalog(portal_type='Event',
                        end={'query': DateTime(),
                             'range': 'min'},
                        sort_on='start',
                        sort_limit=limit)[:limit]

    def Fecha(self):
        fecha = datetime.date.today()
        fecha_actual = fecha.strftime("%Y/%m/%d")
        return fecha_actual

