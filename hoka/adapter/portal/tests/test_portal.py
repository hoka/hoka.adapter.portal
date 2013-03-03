# -*- coding: utf-8 -*-
from Products.PloneTestCase.ptc import PloneTestCase
from Products.PloneTestCase.ptc import setupPloneSite

setupPloneSite()

class TestAdapter(PloneTestCase):

    def test_portal(self):
        portal1=self.getPortal()
        portal2=portal1.getAdapter('portal')()
        if portal1!=portal2:
            self.fail()
