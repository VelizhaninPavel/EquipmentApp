from django.db import models

class Equipment_Type(models.Model):
    T_TYPE = models.CharField(max_length=30, primary_key=True, db_column='t_type')
    T_WEIGHT = models.DecimalField(max_digits=6, decimal_places=2, db_column='t_weight')
    T_HEIGHT = models.DecimalField(max_digits=4, decimal_places=2, db_column='t_height')
    T_LENGTH = models.DecimalField(max_digits=4, decimal_places=2, db_column='t_length')
    T_WIDTH = models.DecimalField(max_digits=4, decimal_places=2, db_column='t_width')
    T_CAPACITY = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True, db_column='t_capacity')
    T_LIFE = models.IntegerField(db_column='t_life')
    T_PRICE = models.DecimalField(max_digits=10, decimal_places=2, db_column='t_price')

    class Meta:
        db_table = 'equipment_type'

class Location(models.Model):
    L_ID = models.AutoField(primary_key=True, db_column='l_id')
    L_SHOP = models.CharField(max_length=30, db_column='l_shop')
    L_AREA = models.CharField(max_length=50, db_column='l_area')

    class Meta:
        db_table = 'location'

class Passport(models.Model):
    P_ID = models.AutoField(primary_key=True, db_column='p_id')
    E_ID = models.IntegerField(null=True, blank=True, db_column='e_id')
    T_TYPE = models.ForeignKey(Equipment_Type, on_delete=models.CASCADE, db_column='t_type')

    class Meta:
        db_table = 'passport'

class Equipment(models.Model):
    E_ID = models.AutoField(primary_key=True, db_column='e_id')
    E_NAME = models.CharField(max_length=50, db_column='e_name')
    T_TYPE = models.ForeignKey(Equipment_Type, on_delete=models.CASCADE, db_column='t_type')
    E_COUNT = models.IntegerField(db_column='e_count')
    L_ID = models.ForeignKey(Location, on_delete=models.CASCADE, db_column='l_id')
    P_ID = models.OneToOneField(Passport, on_delete=models.CASCADE, db_column='p_id')

    class Meta:
        db_table = 'equipment'

class Administrator(models.Model):
    A_ID = models.AutoField(primary_key=True, db_column='a_id')
    A_NAME = models.CharField(max_length=50, db_column='a_name')
    A_SURNAME = models.CharField(max_length=50, db_column='a_surname')
    A_PATRONYMIC = models.CharField(max_length=50, db_column='a_patronymic')
    A_EMAIL = models.CharField(max_length=50, unique=True, db_column='a_email')
    A_TEL = models.CharField(max_length=30, db_column='a_tel')
    A_DATE = models.DateField(db_column='a_date')

    class Meta:
        db_table = 'administrator'

class Management_Journal(models.Model):
    J_ID = models.AutoField(primary_key=True, db_column='j_id')
    A_ID = models.ForeignKey(Administrator, on_delete=models.CASCADE, db_column='a_id')
    E_ID = models.ForeignKey(Equipment, on_delete=models.CASCADE, db_column='e_id')
    J_DATETIME = models.DateTimeField(db_column='j_datetime')
    J_TYPE = models.CharField(max_length=30, db_column='j_type')

    class Meta:
        db_table = 'management_journal'

class Users(models.Model):
    U_ID = models.AutoField(primary_key=True, db_column='u_id')
    U_NAME = models.CharField(max_length=50, db_column='u_name')
    U_SURNAME = models.CharField(max_length=50, db_column='u_surname')
    U_PATRONYMIC = models.CharField(max_length=50, db_column='u_patronymic')
    U_EMAIL = models.CharField(max_length=50, unique=True, db_column='u_email')
    U_TEL = models.CharField(max_length=30, db_column='u_tel')

    class Meta:
        db_table = 'users'

class SearchResult(models.Model):
    R_ID = models.AutoField(primary_key=True, db_column='r_id')
    U_ID = models.ForeignKey(Users, on_delete=models.CASCADE, db_column='u_id')
    E_ID = models.ForeignKey(Equipment, on_delete=models.CASCADE, db_column='e_id')

    class Meta:
        db_table = 'search_result'