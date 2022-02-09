from rest_framework import serializers
from HealthCare.models import *
"""
class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Departments 
        fields=('DepartmentId','DepartmentName')

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employees 
        fields=('EmployeeId','EmployeeName','Department','DateOfJoining','PhotoFileName')

class MDoctorDetail(models.Model):
    pk_dr_id = models.CharField(db_column='Pk_dr_ID', primary_key=True, max_length=36)  # Field name made lowercase. 
    fk_entity_specialityid = models.ForeignKey('MEntitySpeciality', models.DO_NOTHING, db_column='Fk_entity_specialityID', blank=True, null=True)  # Field name made lowercase.
    dr_name = models.CharField(max_length=255)
    frequency = models.TimeField(blank=True, null=True)
    fk_addedby = models.ForeignKey('TblUserDetail', models.DO_NOTHING, db_column='Fk_addedby', blank=True, null=True)  # Field name made lowercase.
    fk_updatedby = models.ForeignKey('TblUserDetail', models.DO_NOTHING, db_column='Fk_updatedby', blank=True, null=True)  # Field name made lowercase.
    addedon = models.DateTimeField()
    updatedon = models.DateTimeField(blank=True, null=True)
    active = models.BooleanField()
    rv = models.TextField(db_column='RV')  # Field name made lowercase. This field type is a guess.


class DoctorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=MDoctorDetail 
        fields=('dr_id_autoincrement','pk_dr_id','dr_name','frequency','addedon','updatedon','active','rv')
"""
class EntityTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model=MEntityType
        #fields=()        
        fields=('pk_entity_typeid','entity_type','fk_addedby','active')

        

class TblUserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=TblUserDetail
        #fields=()        
        fields=('pk_userid','username','user_contact','user_dob',
        'fk_height','fk_weight','fk_bmi','fk_blood_group','addedby',
        'user_password','updatedby','updatedon','user_email','active')