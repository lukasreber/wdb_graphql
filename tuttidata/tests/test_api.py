import pytest
from django.test import TestCase
from mixer.backend.django import mixer
from graphene.test import Client

from tuttigraphql.models import *
from tuttidata.schema import schema

ad_search_query = '''
    query{
    ads(search: "second") {
        id
        title
        user {
        name
        }
    }
    }
'''

@pytest.mark.django_db
class TestTittigraphQLSchema(TestCase):

    def setUp(self):
        self.client = Client(schema)
        self.tuttigraphql = mixer.blend(Ad)

    def test_query(self):
        response = self.client.execute(ad_search_query)
        response_api = response.get("data").get("ads")
        assert len(response)

#   def test_search_query(self):
#       response = self.client.execute(ad_search_query, variables={"search": "second"})
#       response_api = response.get("data").get("ads")
#       assert response_api['id'] == '2'