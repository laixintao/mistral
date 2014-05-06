# -*- coding: utf-8 -*-
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

from pecan.hooks import PecanHook

from mistral import engine
from mistral.openstack.common import log as logging


LOG = logging.getLogger(__name__)


class EngineHook(PecanHook):

    def __init__(self, transport=None):
        self.transport = engine.get_transport(transport)
        self.engine = engine.EngineClient(self.transport)

    def before(self, state):
        state.request.context['engine'] = self.engine
