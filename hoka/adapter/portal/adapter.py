from hoka.adapter.base import *
from zope.component.hooks import getSite

class IPortal(Interface):
    pass

class Adapter(BaseAdapter):

    def __call__(self):
        """Return plone site root"""
        return getSite()