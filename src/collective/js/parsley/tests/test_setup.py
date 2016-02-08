# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from collective.js.parsley.testing import COLLECTIVE_JS_PARSLEY_INTEGRATION_TESTING  # noqa
from plone import api

import unittest2 as unittest


class TestSetup(unittest.TestCase):
    """Test that collective.js.parsley is properly installed."""

    layer = COLLECTIVE_JS_PARSLEY_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if collective.js.parsley is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('collective.js.parsley'))

    def test_browserlayer(self):
        """Test that ICollectiveJsParsleyLayer is registered."""
        from collective.js.parsley.interfaces import ICollectiveJsParsleyLayer
        from plone.browserlayer import utils
        self.assertIn(ICollectiveJsParsleyLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = COLLECTIVE_JS_PARSLEY_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['collective.js.parsley'])

    def test_product_uninstalled(self):
        """Test if collective.js.parsley is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled('collective.js.parsley'))
