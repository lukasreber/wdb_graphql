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

ad_all_user_query = '''
query{
adusers {
    name
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

ad_create_query = '''
mutation($title: String!,$description: String!, $url: String!, $user: String!) {
  createAd(
      title: $title,
      description: $description,
      url: $url,
      userName: $user
  ) {
    id
    title
    description
    url
    user {
      id
    }
  }  
}
'''

aduser_create_query = '''
mutation($name: String!) {
  createAduser(
      name: $name
  ) {
    name
  }  
}
'''

@pytest.mark.django_db
class TestTuttigraphQLSchema(TestCase):

    def setUp(self):
        self.client = Client(schema)
        self.ad = mixer.blend(Ad)

    # check if any data for ad table is returned
    def test_ads_query(self):
        response = self.client.execute(ad_all_query)
        response_api = response.get("data").get("ads")
        assert len(response)

    # check if any data for aduser table is returned
    def test_adusers_query(self):
        response = self.client.execute(ad_all_user_query)
        response_api = response.get("data").get("adusers")
        assert len(response)

    # create ad    
    def test_createad_query(self):
        user = mixer.blend(AdUser)
        payload = {
            "title": "test title",
            "description": "this is a description test",
            "url": "https://thisisaurl.com",
            "user": user.name
        }
        response = self.client.execute(ad_create_query,variables=payload)
        response_api = response.get('data').get('createAd')
        assert response_api['title'] == payload['title']

    # create aduser   
    def test_createaduser_query(self):
        payload = {
            "name": "a_new_user"
        }
        response = self.client.execute(aduser_create_query,variables=payload)
        response_api = response.get('data').get('createAduser')
        print(response.get('data'))
        assert response_api['name'] == payload['name']

    # check if search for title is returned
    def test_search_query(self):
        response = self.client.execute(ad_search_query,variables={"search": self.ad.title})
        response_api = response.get('data').get('ads')
        assert response_api[0]['title'] == str(self.ad.title)

    # insert false user
    def test_false_user_query(self):
        payload = {
            "title": "test title",
            "description": "this is a description test",
            "url": "https://thisisaurl.com",
            "user": "doesnotexist"
        }
        response = self.client.execute(ad_create_query,variables=payload)
        response_api = response.get('errors')[0]
        assert response_api['message'] == 'Invalid User!'    

    