# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Applicant.jabber'
        db.alter_column(u'hello_applicant', 'jabber', self.gf('django.db.models.fields.EmailField')(unique=True, max_length=40))

    def backwards(self, orm):

        # Changing field 'Applicant.jabber'
        db.alter_column(u'hello_applicant', 'jabber', self.gf('django.db.models.fields.CharField')(max_length=40, unique=True))

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
        }
    }

    complete_apps = ['hello']