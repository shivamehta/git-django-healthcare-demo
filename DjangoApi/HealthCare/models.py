from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class MEntityType(models.Model):
    pk_entity_typeid = models.CharField(db_column='Pk_entity_typeID', primary_key=True, max_length=36)  # Field name made lowercase.
    entity_type = models.CharField(max_length=50)
    #description = models.CharField(db_column='entitydescription',max_length=255, blank=True, null=True)
    fk_addedby = models.CharField(db_column='Fk_addedby', blank=True, null=True,max_length=36)  # Field name made lowercase.
    #fk_updatedby = models.ForeignKey('TblUserDetail', models.DO_NOTHING, db_column='Fk_updatedby', blank=True, null=True)  # Field name made lowercase.
    #addedon = models.DateTimeField()
    #updatedon = models.DateTimeField(blank=True, null=True)
    active = models.BooleanField()
    #rv = models.TextField(db_column='RV')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'm_entity_type'

#comit amend2
class TblUserDetail(models.Model):
    pk_userid = models.CharField(db_column='Pk_userID', primary_key=True, max_length=36)  # Field name made lowercase.
    username = models.CharField(max_length=255)
    user_contact = models.BigIntegerField(blank=True, null=True)
    user_dob = models.DateField(blank=True, null=True)
    fk_height = models.CharField(db_column='Fk_height', max_length=36, blank=True, null=True)  # Field name made lowercase.
    fk_weight = models.CharField(db_column='Fk_weight', max_length=36, blank=True, null=True)  # Field name made lowercase.
    fk_bmi = models.CharField(db_column='Fk_bmi', max_length=36, blank=True, null=True)  # Field name made lowercase.
    fk_blood_group = models.CharField(db_column='Fk_blood_group', max_length=36, blank=True, null=True)  # Field name made lowercase.
    user_password = models.BinaryField(max_length=100,blank=True, null=False)  # This field type is a guess.
    user_email = models.CharField(max_length=100, blank=True, null=True)
    addedby = models.CharField(max_length=36, blank=True, null=True)
    updatedby = models.CharField(max_length=36, blank=True, null=True)
    updatedon = models.DateTimeField(blank=True, null=True)
    active = models.BooleanField()
    
    class Meta:
        managed = False
        db_table = 'tbl_user_detail'
'''
class MEntityType(models.Model):
    pk_entity_typeid = models.CharField(db_column='Pk_entity_typeID', primary_key=True, max_length=32)  # Field name made lowercase.
    entity_type = models.CharField(max_length=50)
    entitydescription = models.CharField(max_length=255, blank=True, null=True)
    fk_addedby = models.CharField(db_column='Fk_addedby', max_length=36, blank=True, null=True)  # Field name made lowercase.
    #fk_updatedby = models.CharField(db_column='Fk_updatedby', max_length=36, blank=True, null=True)  
# Field name made lowercase.
    addedon = models.DateTimeField(blank=True, null=True)
    #updatedon = models.DateTimeField(blank=True, null=True)
    active = models.BooleanField()
    #rv = models.TextField(db_column='RV')  # Field name made lowercase. This field type is a guess.  

    class Meta:
        managed = False
        db_table = 'm_entity_type'
'''