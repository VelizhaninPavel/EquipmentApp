from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny

from .models import (
    Equipment, Equipment_Type, Passport, Location,
    Administrator, Management_Journal, Users, SearchResult
)
from .serializers import (
    UserSerializer, EquipmentSerializer, EquipmentTypeSerializer,
    PassportSerializer, LocationSerializer, ManagementJournalSerializer,
    SearchResultSerializer, UsersSerializer, AdministratorSerializer
)

# Пользователи
class UsersList(generics.ListCreateAPIView):  # Поддерживает GET и POST
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    permission_classes = [permissions.AllowAny]

class UsersDetail(generics.RetrieveAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    lookup_field = 'u_id'
    permission_classes = [permissions.AllowAny]

class UsersUpdate(generics.UpdateAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    lookup_field = 'u_id'
    permission_classes = [permissions.AllowAny]

class UsersDelete(generics.DestroyAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    lookup_field = 'u_id'
    permission_classes = [permissions.AllowAny]

# Оборудование
class EquipmentList(generics.ListAPIView):  # Изменяем на ListAPIView (только GET)
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
    permission_classes = [permissions.AllowAny]

class EquipmentCreate(generics.CreateAPIView):  # Добавляем отдельное представление для создания
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
    permission_classes = [permissions.AllowAny]

class EquipmentDetail(generics.RetrieveAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
    lookup_field = 'E_ID'
    permission_classes = [permissions.AllowAny]  # GET доступен всем

class EquipmentUpdate(generics.UpdateAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = 'E_ID'

    def get_permissions(self):
        if self.request.user.is_staff:
            return [permissions.AllowAny()]
        return [permissions.AllowAny()]  # PATCH для Admin и Users

class EquipmentDelete(generics.DestroyAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
    lookup_field = 'E_ID'

    def get_permissions(self):
        if self.request.user.is_staff:
            return [permissions.AllowAny()]
        return [permissions.AllowAny()]  # DELETE для Admin и Users

# Типы оборудования
class EquipmentTypeList(generics.ListCreateAPIView):
    queryset = Equipment_Type.objects.all()
    serializer_class = EquipmentTypeSerializer
    permission_classes = [permissions.AllowAny]  # GET доступен всем

    def get_permissions(self):
        if self.request.method == 'POST':
            return [permissions.AllowAny()]  # POST для Admin и Users
        return [permissions.AllowAny()]

class EquipmentTypeDetail(generics.RetrieveAPIView):
    queryset = Equipment_Type.objects.all()
    serializer_class = EquipmentTypeSerializer
    lookup_field = 'T_TYPE'
    permission_classes = [permissions.AllowAny]  # GET доступен всем

class EquipmentTypeUpdate(generics.UpdateAPIView):
    queryset = Equipment_Type.objects.all()
    serializer_class = EquipmentTypeSerializer
    lookup_field = 'T_TYPE'
    permission_classes = [permissions.AllowAny]  # PATCH только для Admin

class EquipmentTypeDelete(generics.DestroyAPIView):
    queryset = Equipment_Type.objects.all()
    serializer_class = EquipmentTypeSerializer
    lookup_field = 'T_TYPE'
    permission_classes = [permissions.AllowAny]  # DELETE только для Admin


# Паспорта (Passport)
class PassportList(generics.ListCreateAPIView):  # Поддерживает GET и POST
    queryset = Passport.objects.all()
    serializer_class = PassportSerializer
    permission_classes = [permissions.AllowAny]

class PassportDetail(generics.RetrieveAPIView):
    queryset = Passport.objects.all()
    serializer_class = PassportSerializer
    lookup_field = 'P_ID'
    permission_classes = [permissions.AllowAny]  # GET доступен всем

class PassportUpdate(generics.UpdateAPIView):
    queryset = Passport.objects.all()
    serializer_class = PassportSerializer
    lookup_field = 'P_ID'

    def get_permissions(self):
        if self.request.user.is_staff:
            return [permissions.AllowAny()]
        return [permissions.AllowAny()]  # PATCH для Admin и Users

class PassportDelete(generics.DestroyAPIView):
    queryset = Passport.objects.all()
    serializer_class = PassportSerializer
    lookup_field = 'P_ID'

    def get_permissions(self):
        if self.request.user.is_staff:
            return [permissions.AllowAny()]
        return [permissions.AllowAny()]  # DELETE для Admin и Users

# Журнал управления
class ManagementJournalList(generics.ListAPIView):
    queryset = Management_Journal.objects.all()
    serializer_class = ManagementJournalSerializer
    permission_classes = [permissions.AllowAny]  # Только для Admin

# Результаты поиска (SearchResult)
class SearchResultList(generics.ListAPIView):  # Добавляем класс SearchResultList
    queryset = SearchResult.objects.all()
    serializer_class = SearchResultSerializer
    permission_classes = [permissions.AllowAny]

class SearchResultCreate(generics.CreateAPIView):
    queryset = SearchResult.objects.all()
    serializer_class = SearchResultSerializer
    permission_classes = [permissions.AllowAny]

class SearchResultUpdate(generics.UpdateAPIView):
    queryset = SearchResult.objects.all()
    serializer_class = SearchResultSerializer
    lookup_field = 'r_id'
    permission_classes = [permissions.AllowAny]

# Местоположения
class LocationList(generics.ListAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [permissions.AllowAny]  # GET доступен всем


# Представления для Administrator
class AdministratorList(generics.ListCreateAPIView):
    queryset = Administrator.objects.all()
    serializer_class = AdministratorSerializer
    permission_classes = [permissions.AllowAny]  # Доступ только для администраторов

class AdministratorDetail(generics.RetrieveAPIView):
    queryset = Administrator.objects.all()
    serializer_class = AdministratorSerializer
    lookup_field = 'a_id'
    permission_classes = [permissions.AllowAny]  # Доступ только для администраторов

class AdministratorUpdate(generics.UpdateAPIView):
    queryset = Administrator.objects.all()
    serializer_class = AdministratorSerializer
    lookup_field = 'a_id'
    permission_classes = [permissions.AllowAny]  # Доступ только для администраторов

class AdministratorDelete(generics.DestroyAPIView):
    queryset = Administrator.objects.all()
    serializer_class = AdministratorSerializer
    lookup_field = 'a_id'
    permission_classes = [permissions.AllowAny]  # Доступ только для администраторов


class LocationCreate(generics.CreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [permissions.AllowAny]

class LocationUpdate(generics.UpdateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    lookup_field = 'l_id'
    permission_classes = [permissions.AllowAny]

class LocationDelete(generics.DestroyAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    lookup_field = 'l_id'
    permission_classes = [permissions.AllowAny]