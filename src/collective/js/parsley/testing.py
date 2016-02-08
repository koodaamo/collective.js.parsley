# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import collective.js.parsley


class CollectiveJsParsleyLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        self.loadZCML(package=collective.js.parsley)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'collective.js.parsley:default')


COLLECTIVE_JS_PARSLEY_FIXTURE = CollectiveJsParsleyLayer()


COLLECTIVE_JS_PARSLEY_INTEGRATION_TESTING = IntegrationTesting(
    bases=(COLLECTIVE_JS_PARSLEY_FIXTURE,),
    name='CollectiveJsParsleyLayer:IntegrationTesting'
)


COLLECTIVE_JS_PARSLEY_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(COLLECTIVE_JS_PARSLEY_FIXTURE,),
    name='CollectiveJsParsleyLayer:FunctionalTesting'
)


COLLECTIVE_JS_PARSLEY_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        COLLECTIVE_JS_PARSLEY_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='CollectiveJsParsleyLayer:AcceptanceTesting'
)
