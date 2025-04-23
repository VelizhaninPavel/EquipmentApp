from django.urls import path
from .views import (
    UsersList, UsersDetail, UsersUpdate, UsersDelete,
    EquipmentList, EquipmentCreate, EquipmentDetail, EquipmentUpdate, EquipmentDelete,
    EquipmentTypeList, EquipmentTypeDetail, EquipmentTypeUpdate, EquipmentTypeDelete,
    PassportList, PassportDetail, PassportUpdate, PassportDelete,
    ManagementJournalList, SearchResultList, SearchResultCreate, LocationList, LocationCreate, LocationUpdate, LocationDelete,
    AdministratorList, AdministratorDetail, AdministratorUpdate, AdministratorDelete
)

urlpatterns = [
    # Пользователи
    path('users/', UsersList.as_view(), name='user-list'),
    path('users/<int:u_id>/', UsersDetail.as_view(), name='user-detail'),
    path('users/<int:u_id>/update/', UsersUpdate.as_view(), name='user-update'),
    path('users/<int:u_id>/delete/', UsersDelete.as_view(), name='user-delete'),

    # Оборудование
    path('equipment/', EquipmentList.as_view(), name='equipment-list'),
    path('equipment/create/', EquipmentCreate.as_view(), name='equipment-create'),
    path('equipment/<int:e_id>/', EquipmentDetail.as_view(), name='equipment-detail'),
    path('equipment/<int:e_id>/update/', EquipmentUpdate.as_view(), name='equipment-update'),
    path('equipment/<int:e_id>/delete/', EquipmentDelete.as_view(), name='equipment-delete'),
    # Типы оборудования
    path('equipment_type/', EquipmentTypeList.as_view(), name='equipment-type-list'),
    path('equipment_type/<str:t_type>/', EquipmentTypeDetail.as_view(), name='equipment-type-detail'),
    path('equipment_type/<str:t_type>/update/', EquipmentTypeUpdate.as_view(), name='equipment-type-update'),
    path('equipment_type/<str:t_type>/delete/', EquipmentTypeDelete.as_view(), name='equipment-type-delete'),

    # Паспорта
    path('passport/', PassportList.as_view(), name='passport-list'),
    path('passport/<int:p_id>/', PassportDetail.as_view(), name='passport-detail'),
    path('passport/<int:p_id>/update/', PassportUpdate.as_view(), name='passport-update'),
    path('passport/<int:p_id>/delete/', PassportDelete.as_view(), name='passport-delete'),

    # Журнал управления
    path('management_journal/', ManagementJournalList.as_view(), name='management-journal-list'),

    # Результаты поиска
    path('search_result/', SearchResultList.as_view(), name='search-result-list'),
    path('search_result/create/', SearchResultCreate.as_view(), name='search-result-create'),

    # Местоположения
    path('location/', LocationList.as_view(), name='location-list'),
    path('location/create/', LocationCreate.as_view(), name='location-create'),
    path('location/<int:l_id>/update/', LocationUpdate.as_view(), name='location-update'),
    path('location/<int:l_id>/delete/', LocationDelete.as_view(), name='location-delete'),

    # Администраторы (новые маршруты)
    path('administrator/', AdministratorList.as_view(), name='administrator-list'),
    path('administrator/<int:a_id>/', AdministratorDetail.as_view(), name='administrator-detail'),
    path('administrator/<int:a_id>/update/', AdministratorUpdate.as_view(), name='administrator-update'),
    path('administrator/<int:a_id>/delete/', AdministratorDelete.as_view(), name='administrator-delete'),
]