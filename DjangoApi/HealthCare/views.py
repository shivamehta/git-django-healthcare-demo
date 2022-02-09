import uuid
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.contrib.auth.models import User
from HealthCare.models import MEntityType,TblUserDetail
from HealthCare.serializers import EntityTypeSerializer,TblUserDetailSerializer


from django.core.files.storage import default_storage



@csrf_exempt
def m_entity_typeApi(request,id=0):
    #current_user = User.objects.create_user('sonu','sonu@xyz.com','sn@pswrd')
    #addedby=uuid()
    if request.method=='GET':
        m_entity_types = MEntityType.objects.all()
        m_entity_type_serializer=EntityTypeSerializer(m_entity_types,many=True)
        return JsonResponse(m_entity_type_serializer.data,safe=False)
    elif request.method=='POST':
        m_entity_type_data=JSONParser().parse(request)
        m_entity_type_serializer=EntityTypeSerializer(data=m_entity_type_data)
        if m_entity_type_serializer.is_valid():
            #addedby.save()
            m_entity_type_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        m_entity_type_data=JSONParser().parse(request)
        m_entity_type=MEntityType.objects.get(pk_entity_typeid=m_entity_type_data['pk_entity_typeid'])
        m_entity_type_serializer=EntityTypeSerializer(m_entity_type,data=m_entity_type_data)
        if m_entity_type_serializer.is_valid():
            m_entity_type_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        m_entity_type=MEntityType.objects.get(pk_entity_typeid=id)
        m_entity_type.delete()
        return JsonResponse("Deleted Successfully",safe=False)


@csrf_exempt
def tbl_user_detailApi(request,id=0):
    #current_user = User.objects.create_user('sonu','sonu@xyz.com','sn@pswrd')
    #addedby=uuid()
    if request.method=='GET':
        tbl_user_details = TblUserDetail.objects.all()
        tbl_user_detail_serializer=TblUserDetailSerializer(tbl_user_details,many=True)
        return JsonResponse(tbl_user_detail_serializer.data,safe=False)
    elif request.method=='POST':
        tbl_user_detail_data=JSONParser().parse(request)
        tbl_user_detail_serializer=TblUserDetailSerializer(data=tbl_user_detail_data)
        if tbl_user_detail_serializer.is_valid():
            #addedby.save()
            tbl_user_detail_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        tbl_user_detail_data=JSONParser().parse(request)
        tbl_user_detail=TblUserDetail.objects.get(pk_userid=tbl_user_detail_data['pk_userid'])
        tbl_user_detail_serializer=TblUserDetailSerializer(tbl_user_detail,data=tbl_user_detail_data)
        if tbl_user_detail_serializer.is_valid():
            tbl_user_detail_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        tbl_user_detail=TblUserDetail.objects.get(pk_userid=id)
        tbl_user_detail.delete()
        return JsonResponse("Deleted Successfully",safe=False)

'''
# Create your views here.
@csrf_exempt
def m_doctor_detailApi(request,id=1):
    if request.method=='GET':
        m_entity_types = MDoctorDetail.objects.all()
        m_doctor_Detail_serializer=DoctorDetailSerializer(m_entity_types,many=True)
        return JsonResponse(m_doctor_Detail_serializer.data,safe=False)
    elif request.method=='POST':
        m_doctor_Detail_data=JSONParser().parse(request)
        m_doctor_Detail_serializer=DoctorDetailSerializer(data=m_doctor_Detail_data)
        if m_doctor_Detail_serializer.is_valid():
            m_doctor_Detail_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        m_doctor_Detail_data=JSONParser().parse(request)
        m_doctor_Detail=MDoctorDetail.objects.get(dr_id_autoincrement=m_doctor_Detail_data['dr_id_autoincrement'])
        m_doctor_Detail_serializer=DoctorDetailSerializer(m_doctor_Detail,data=m_doctor_Detail_data)
        if m_doctor_Detail_serializer.is_valid():
            m_doctor_Detail_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        m_doctor_Detail=MDoctorDetail.objects.get(dr_id_autoincrement=id)
        m_doctor_Detail.delete()
        return JsonResponse("Deleted Successfully",safe=False)
'''