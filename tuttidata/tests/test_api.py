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

ad_delete_query = '''
mutation($id: Int!){
  deleteAd(id: $id) {
    ok
  }
}
'''

aduser_delete_query = '''
mutation($id: Int!){
  deleteAduser(id: $id) {
    ok
  }
}
'''

ad_update_query = '''
mutation($id: Int!,$newtitle: String!) {
  updateAd(id: $id,title: $newtitle) {
    id
    title
    description
    url
  }
}
'''

aduser_update_query = '''
mutation($id: Int!,$newname: String!) {
  updateAduser(id: $id,name: $newname) {
    id
    name
  }
}
'''


@pytest.mark.django_db
class TestTuttigraphQLSchema(TestCase):

    def setUp(self):
        self.client = Client(schema)
        self.ad = mixer.blend(Ad)
        self.aduser = mixer.blend(AdUser)

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
        response = self.client.execute(ad_create_query, variables=payload)
        response_api = response.get('data').get('createAd')
        assert response_api['title'] == payload['title']

    # create aduser
    def test_createaduser_query(self):
        payload = {
            "name": "a_new_user"
        }
        response = self.client.execute(aduser_create_query, variables=payload)
        response_api = response.get('data').get('createAduser')
        assert response_api['name'] == payload['name']

    # check if search for title is returned
    def test_search_query(self):
        response = self.client.execute(ad_search_query, variables={
                                       "search": self.ad.title})
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
        response = self.client.execute(ad_create_query, variables=payload)
        response_api = response.get('errors')[0]
        assert response_api['message'] == 'Invalid User!'

    # delete ad
    def test_deletead_query(self):
        response = self.client.execute(
            ad_delete_query, variables={"id": self.ad.id})
        response_api = response.get('data').get('deleteAd')
        assert response_api['ok'] == True

    # delete aduser
    def test_deleteaduser_query(self):
        user = mixer.blend(AdUser)
        response = self.client.execute(
            aduser_delete_query, variables={"id": user.id})
        response_api = response.get('data').get('deleteAduser')
        assert response_api['ok'] == True

    # update ad
    def test_updatead_query(self):
        newtitle = "some new title"
        response = self.client.execute(ad_update_query, variables={
                                       "id": self.ad.id, "newtitle": newtitle})
        response_api = response.get('data').get('updateAd')
        assert response_api.get('title') == newtitle
        assert response_api.get('description') == self.ad.description
        assert response_api.get('url') == self.ad.url

    # update aduser
    def test_updateaduser_query(self):
        newname = "new username"
        response = self.client.execute(aduser_update_query, variables={
                                       "id": self.aduser.id, "newname": newname})
        response_api = response.get('data').get('updateAduser')
        assert response_api.get('name') == newname


'''
code als kommentar: was noch offen ist...

'''
