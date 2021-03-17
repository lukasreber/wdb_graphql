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

# all tests follow the same format: 
# 1. data is added directory to the database using the mixer extension
# 2. query is performed to the api
# 3. the response is checked for consistency

@pytest.mark.django_db
class TestTuttigraphQLSchema(TestCase):

    def setUp(self):
        self.client = Client(schema)
        self.ad = mixer.blend(Ad)
        self.aduser = mixer.blend(AdUser)

    # check if any data for ad table is returned
    # a simple test just to see if data is returned, content of data is not checked
    def test_ads_query(self):
        response = self.client.execute(ad_all_query)
        res = response.get("data").get("ads")
        assert len(response)

    # check if any data for aduser table is returned
    # a simple test just to see if data is returned, content of data is not checked
    def test_adusers_query(self):
        response = self.client.execute(ad_all_user_query)
        res = response.get("data").get("adusers")
        assert len(response)

    # create ad over the api and check if all attributes are returned correctly
    def test_createad_query(self):
        user = mixer.blend(AdUser)
        payload = {
            "title": "test title",
            "description": "this is a description test",
            "url": "https://thisisaurl.com",
            "user": user.name
        }
        response = self.client.execute(ad_create_query, variables=payload)
        res = response.get('data').get('createAd')
        assert res['title'] == payload['title']
        assert res['description'] == payload['description']
        assert res['url'] == payload['url']
        assert res.get('user')['id'] == str(user.id)

    # create user over the api and check if all attributes are returned correctly
    def test_createaduser_query(self):
        payload = {
            "name": "a_new_user"
        }
        response = self.client.execute(aduser_create_query, variables=payload)
        res = response.get('data').get('createAduser')
        assert res['name'] == payload['name']

    # check if search for title is returned
    def test_search_query(self):
        response = self.client.execute(ad_search_query, variables={
                                       "search": self.ad.title})
        res = response.get('data').get('ads')
        assert res[0]['title'] == str(self.ad.title)

    # check if only existing users can be added to an ad
    def test_false_user_query(self):
        payload = {
            "title": "test title",
            "description": "this is a description test",
            "url": "https://thisisaurl.com",
            "user": "doesnotexist"
        }
        response = self.client.execute(ad_create_query, variables=payload)
        res = response.get('errors')[0]
        assert res['message'] == 'Invalid User!'

    # check if deleting an ad works
    def test_deletead_query(self):
        response = self.client.execute(
            ad_delete_query, variables={"id": self.ad.id})
        res = response.get('data').get('deleteAd')
        assert res['ok'] == True

    # check if deleting an user works
    def test_deleteaduser_query(self):
        user = mixer.blend(AdUser)
        response = self.client.execute(
            aduser_delete_query, variables={"id": user.id})
        res = response.get('data').get('deleteAduser')
        assert res['ok'] == True

    # check if updating an ad works and if the other untouched attributes stay the same
    def test_updatead_query(self):
        newtitle = "some new title"
        response = self.client.execute(ad_update_query, variables={
                                       "id": self.ad.id, "newtitle": newtitle})
        res = response.get('data').get('updateAd')
        assert res.get('title') == newtitle
        assert res.get('description') == self.ad.description
        assert res.get('url') == self.ad.url

    # check if updating an user works
    def test_updateaduser_query(self):
        newname = "new username"
        response = self.client.execute(aduser_update_query, variables={
                                       "id": self.aduser.id, "newname": newname})
        res = response.get('data').get('updateAduser')
        assert res.get('name') == newname
