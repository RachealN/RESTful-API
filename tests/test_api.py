import unittest
from flash.api import app
from flask import json, request


class Testing(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client
        self.entry = {
            'id': 0,
            'name': 'Racheal',
            'date': 10/6/2018,
            'title': 'My quite thoughts',
            'country': 'uganda',
            'entry_added': 'Read upon my death, or just before yours'
        }

    def test_all_entries(self):
        result = self.client().get('/api/v2/resources/entries/all')
        self.assertEqual(result.status_code, 200)

    def test_single_entry(self):
        entry = {
            'id': 1,
            'name': 'Racheal',
            'date': 10/6/2018,
            'title': 'My quite thoughts',
            'country': 'uganda',
            'entry_added': 'Read upon my death, or just before yours'
        }

        result = self.client().post('/api/v2/resources/entry/',
                                    content_type='application/json',
                                    data=json.dumps(entry)
                                    )
       
        self.assertEqual(result.status_code, 201)

    def test_unavailable_fetch(self):
        result = self.client().get('/api/v2/resources/entries/')
        self.assertEqual(result.status_code, 404)

    def test_entry_posted_successfully(self):
        entry = {
            'id': 1,
            'name': 'Racheal',
            'date': 10/6/2018,
            'title': 'My quite thoughts',
            'country': 'uganda',
            'entry_added': 'Read upon my death, or just before yours'
        }

        result = self.client().post('/api/v2/resources/entry/',
                                    content_type='application/json',
                                    data=json.dumps(entry)
                                    )

        self.assertEqual(result.status_code, 201)
        self.assertIsNotNone(result)

    def test_entry_updated(self):
        entry = {
            'name': 'Racheal',
            'date': 10/6/2018,
            'title': 'My quite thoughts',
            'country': 'uganda',
            'entry_added': 'Read upon my death, or just before yours'
        }

        result = self.client().put('/api/v2/resources/entry/2',
                                   content_type='application/json',
                                   data=json.dumps(entry)
                                   )

        self.assertEqual(result.status_code, 200)
        self.assertIsNotNone(result)

    def test_invalid_update(self):
        entry_list = []
        entry = {
            'id': 1,
            'name': 'Racheal',
            'date': 10/6/2018,
            'title': 'My quite thoughts',
            'country': 'uganda',
            'entry_added': 'Read upon my death, or just before yours'
        }

        result = self.client().post('/api/v2/resources/entry/',
                                    content_type='application/json',
                                    data=json.dumps(entry)
                                    )
        
        entry_list.append(entry)
        self.assertEqual(result.status_code, 201)
        
        update = {
            'id': 1,
            'name': 'Racheal',
            'date': 10/6/2018,
            'title': 'My quite thoughts',
            'country': 'kenya',
            'entry_added': 'Read upon my death, or just before yours'
        }
        entry = [entry for entry in entry_list]
        entry[0]['title'] = update['title']
        dict_title = {'title': entry[0]['title']}
        result = self.client().put('/api/v2/resources/entry/2', content_type='application/json',
                                   data=json.dumps(dict_title))

        self.assertEqual(result.status_code, 400)

    def test_entry_deleted(self):
        delete_list = []
        delete = {
                 'id': 1,
                 'name': 'Racheal',
                 'date': 10/6/2018,
                 'title': 'My quite thoughts',
                 'country': 'uganda',
                 'entry_added': 'Read upon my death, or just before yours'
             }
        result = self.client().delete('/api/v2/resources/entry/',
                                    content_type='application/json',
                                    data=json.dumps(delete)
                                    )
       
        delete_list.append(delete)
        self.assertEqual(result.status_code, 405)
        
            
        
                


