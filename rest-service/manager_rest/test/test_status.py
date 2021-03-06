#########
# Copyright (c) 2014 GigaSpaces Technologies Ltd. All rights reserved
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
#  * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  * See the License for the specific language governing permissions and
#  * limitations under the License.

__author__ = 'dan'


from base_test import BaseServerTestCase


class StatusTestCase(BaseServerTestCase):

    def test_get_empty(self):
        result = self.get('/status')
        self.assertEqual(result.json['status'], 'running')

    def test_get_services(self):
        result = self.get('/status')
        self.assertEqual(type(result.json['services']), list)
