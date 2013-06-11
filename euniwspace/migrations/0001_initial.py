# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ScannerLog'
        db.create_table('euniwspace_scannerlog', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('time', self.gf('django.db.models.fields.DateTimeField')()),
            ('system', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Map.System'])),
            ('sigid', self.gf('django.db.models.fields.CharField')(max_length=7)),
            ('sig_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Map.SignatureType'], null=True)),
            ('info', self.gf('django.db.models.fields.CharField')(max_length=65, null=True)),
            ('strength', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=2)),
        ))
        db.send_create_signal('euniwspace', ['ScannerLog'])


    def backwards(self, orm):
        # Deleting model 'ScannerLog'
        db.delete_table('euniwspace_scannerlog')


    models = {
        'Map.signaturetype': {
            'Meta': {'object_name': 'SignatureType'},
            'escalatable': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'longname': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'shortname': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            'sleeprsite': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'Map.system': {
            'Meta': {'object_name': 'System', '_ormbases': ['core.SystemData']},
            'first_visited': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'info': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'last_visited': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'lastscanned': ('django.db.models.fields.DateTimeField', [], {}),
            'npckills': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'occupied': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'podkills': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'shipkills': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sysclass': ('django.db.models.fields.IntegerField', [], {}),
            'systemdata_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['core.SystemData']", 'unique': 'True', 'primary_key': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'})
        },
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'core.constellation': {
            'Meta': {'object_name': 'Constellation', 'db_table': "'mapConstellations'", 'managed': 'False'},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "'constellationID'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "'constellationName'"}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'constellations'", 'db_column': "'regionID'", 'to': "orm['core.Region']"}),
            'x': ('django.db.models.fields.FloatField', [], {}),
            'y': ('django.db.models.fields.FloatField', [], {}),
            'z': ('django.db.models.fields.FloatField', [], {})
        },
        'core.region': {
            'Meta': {'object_name': 'Region', 'db_table': "'mapRegions'", 'managed': 'False'},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "'regionID'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "'regionName'"}),
            'x': ('django.db.models.fields.FloatField', [], {}),
            'y': ('django.db.models.fields.FloatField', [], {}),
            'z': ('django.db.models.fields.FloatField', [], {})
        },
        'core.systemdata': {
            'Meta': {'object_name': 'SystemData', 'db_table': "'mapSolarSystems'", 'managed': 'False'},
            'constellation': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'systems'", 'db_column': "'constellationID'", 'to': "orm['core.Constellation']"}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "'solarSystemID'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "'solarSystemName'"}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'systems'", 'db_column': "'regionID'", 'to': "orm['core.Region']"}),
            'security': ('django.db.models.fields.FloatField', [], {}),
            'x': ('django.db.models.fields.FloatField', [], {}),
            'y': ('django.db.models.fields.FloatField', [], {}),
            'z': ('django.db.models.fields.FloatField', [], {})
        },
        'euniwspace.scannerlog': {
            'Meta': {'object_name': 'ScannerLog'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info': ('django.db.models.fields.CharField', [], {'max_length': '65', 'null': 'True'}),
            'sig_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['Map.SignatureType']", 'null': 'True'}),
            'sigid': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            'strength': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2'}),
            'system': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['Map.System']"}),
            'time': ('django.db.models.fields.DateTimeField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        }
    }

    complete_apps = ['euniwspace']