import pytest
from django.test import TestCase
from mixer.backend.django import mixer
from graphene.test import Client

from tuttigraphql.models import *
from tuttidata.schema import schema

ad_all_query = '''
query{
ads {
    id
    title
    user {
    name
    }
}
}
'''

ad_search_query = '''
query($search: String!){
ads(search: $search) {
    id
    title
}
}
'''

@pytest.mark.django_db
class TestTittigraphQLSchema(TestCase):

    def setUp(self):
        self.client = Client(schema)
        self.ad = mixer.blend(Ad)

    # check if any data is returned
    def test_query(self):
        response = self.client.execute(ad_all_query)
        response_api = response.get("data").get("ads")
        assert len(response)

    # check if search for title is returned
    def test_search_query(self):
        response = self.client.execute(ad_search_query,variables={"search": self.ad.title})
        response_api = response.get('data').get('ads')
        assert response_api[0]['title'] == str(self.ad.title)

    # create ad
    