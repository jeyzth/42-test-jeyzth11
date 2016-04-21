# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Requests'
        db.create_table(u'hello_requests', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('query_dt', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('remote_ip', self.gf('django.db.models.fields.IPAddressField')(max_length=15)),
            ('query_string', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'hello', ['Requests'])


    def backwards(self, orm):
        # Deleting model 'Requests'
        db.delete_table(u'hello_requests')


    models = {
        u'hello.applicant': {
            'Meta': {'object_name': 'Applicant'},
            'bio': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'dateofbird': ('django.db.models.fields.DateField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '40'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jabber': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '40'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'others': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'skype': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '40', 'blank': 'True'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        u'hello.requests': {
            'Meta': {'object_name': 'Requests'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'query_dt': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'query_string': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'remote_ip': ('django.db.models.fields.IPAddressField', [], {'max_length': '15'})
        }
    }

    complete_apps = ['hello']