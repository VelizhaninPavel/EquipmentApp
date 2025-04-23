from rest_framework import serializers
from .models import (
    Equipment, Passport, Location, Equipment_Type,
    Administrator, Management_Journal, Users, SearchResult
)
from django.contrib.auth.models import User

# Сериализатор для пользователей (User)
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'is_staff']

# Сериализатор для Equipment_Type
class EquipmentTypeSerializer(serializers.ModelSerializer):
    t_type = serializers.CharField(source='T_TYPE')
    t_weight = serializers.DecimalField(max_digits=6, decimal_places=2, source='T_WEIGHT')
    t_height = serializers.DecimalField(max_digits=4, decimal_places=2, source='T_HEIGHT')
    t_length = serializers.DecimalField(max_digits=4, decimal_places=2, source='T_LENGTH')
    t_width = serializers.DecimalField(max_digits=4, decimal_places=2, source='T_WIDTH')
    t_capacity = serializers.DecimalField(max_digits=12, decimal_places=2, allow_null=True, source='T_CAPACITY')
    t_life = serializers.IntegerField(source='T_LIFE')
    t_price = serializers.DecimalField(max_digits=10, decimal_places=2, source='T_PRICE')

    class Meta:
        model = Equipment_Type
        fields = ['t_type', 't_weight', 't_height', 't_length', 't_width', 't_capacity', 't_life', 't_price']

# Сериализатор для Location
class LocationSerializer(serializers.ModelSerializer):
    l_id = serializers.IntegerField(source='L_ID')
    l_shop = serializers.CharField(source='L_SHOP')
    l_area = serializers.CharField(source='L_AREA')

    class Meta:
        model = Location
        fields = ['l_id', 'l_shop', 'l_area']


# Сериализатор для Passport
class PassportSerializer(serializers.ModelSerializer):
    p_id = serializers.IntegerField(source='P_ID', read_only=True, )
    e_id = serializers.IntegerField(source='E_ID')
    t_type = serializers.PrimaryKeyRelatedField(queryset=Equipment_Type.objects.all(), source='T_TYPE')  # Исправляем на PrimaryKeyRelatedField

    class Meta:
        model = Passport
        fields = ['p_id', 'e_id', 't_type']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['t_type'] = EquipmentTypeSerializer(instance.T_TYPE).data
        return representation

# Сериализатор для Equipment
class EquipmentSerializer(serializers.ModelSerializer):
    e_id = serializers.IntegerField(source='E_ID', read_only=True)  # Помечаем как read_only
    e_name = serializers.CharField(source='E_NAME')
    t_type = serializers.PrimaryKeyRelatedField(queryset=Equipment_Type.objects.all(), source='T_TYPE')  # Принимаем только t_type (строку)
    e_count = serializers.IntegerField(source='E_COUNT')
    l_id = serializers.PrimaryKeyRelatedField(queryset=Location.objects.all(), source='L_ID')  # Принимаем только l_id (целое число)
    p_id = serializers.PrimaryKeyRelatedField(queryset=Passport.objects.all(), source='P_ID')  # Принимаем только p_id (целое число)

    class Meta:
        model = Equipment
        fields = ['e_id', 'e_name', 't_type', 'e_count', 'l_id', 'p_id']

    # Добавим метод для отображения вложенных данных в ответе
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['t_type'] = EquipmentTypeSerializer(instance.T_TYPE).data
        representation['l_id'] = LocationSerializer(instance.L_ID).data
        representation['p_id'] = PassportSerializer(instance.P_ID).data
        return representation


# Сериализатор для Administrator
class AdministratorSerializer(serializers.ModelSerializer):
    a_id = serializers.IntegerField(source='A_ID', read_only=True)
    a_name = serializers.CharField(source='A_NAME')
    a_surname = serializers.CharField(source='A_SURNAME')
    a_patronymic = serializers.CharField(source='A_PATRONYMIC')
    a_email = serializers.CharField(source='A_EMAIL')
    a_tel = serializers.CharField(source='A_TEL')
    a_date = serializers.DateField(source='A_DATE')

    class Meta:
        model = Administrator
        fields = ['a_id', 'a_name', 'a_surname', 'a_patronymic', 'a_email', 'a_tel', 'a_date']

# Сериализатор для Management_Journal
class ManagementJournalSerializer(serializers.ModelSerializer):
    j_id = serializers.IntegerField(source='J_ID')
    a_id = AdministratorSerializer(source='A_ID')
    e_id = EquipmentSerializer(source='E_ID')
    j_datetime = serializers.DateTimeField(source='J_DATETIME')
    j_type = serializers.CharField(source='J_TYPE')

    class Meta:
        model = Management_Journal
        fields = ['j_id', 'a_id', 'e_id', 'j_datetime', 'j_type']

# Сериализатор для Users
class UsersSerializer(serializers.ModelSerializer):
    u_id = serializers.IntegerField(source='U_ID', read_only=True)
    u_name = serializers.CharField(source='U_NAME')
    u_surname = serializers.CharField(source='U_SURNAME')
    u_patronymic = serializers.CharField(source='U_PATRONYMIC')
    u_email = serializers.CharField(source='U_EMAIL')
    u_tel = serializers.CharField(source='U_TEL')

    class Meta:
        model = Users
        fields = ['u_id', 'u_name', 'u_surname', 'u_patronymic', 'u_email', 'u_tel']

# Сериализатор для SearchResult


# изменили т.к выводится весь словарь
class SearchResultSerializer(serializers.ModelSerializer):
    r_id = serializers.IntegerField(source='R_ID', read_only=True)  # Помечаем как read_only
    u_id = serializers.PrimaryKeyRelatedField(queryset=Users.objects.all(), source='U_ID')  # Принимаем только ID
    e_id = serializers.PrimaryKeyRelatedField(queryset=Equipment.objects.all(), source='E_ID')  # Принимаем только ID

    class Meta:
        model = SearchResult
        fields = ['r_id', 'u_id', 'e_id']

    # Добавим метод для отображения вложенных данных в ответе
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['u_id'] = UsersSerializer(instance.U_ID).data
        representation['e_id'] = EquipmentSerializer(instance.E_ID).data
        return representation