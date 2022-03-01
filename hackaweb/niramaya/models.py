from datetime import datetime
from email.policy import default
from pyexpat import model
from sre_parse import State
from urllib import request
from django import forms
from django.db import models
from django.contrib.auth.models import User
import os

class hospital(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    sno = models.AutoField(primary_key=True)
    hospital_name = models.CharField(max_length=100)
    serial = models.CharField(max_length=10,unique=True)
    Level = models.IntegerField(default=0)
    address = models.CharField(max_length=100)
    State = models.CharField(max_length=50)
    district = models.CharField(max_length=10)
    phone = models.CharField(max_length=15)
    head = models.CharField(max_length=50)
    doctor_nos = models.IntegerField(default=0)
    skilled_nos = models.IntegerField(default=0)
    non_skilled_nos = models.IntegerField(default=0)
    gen_bed = models.IntegerField(default=0)
    spec_bed = models.IntegerField(default=0)
    surg_bed = models.IntegerField(default=0)
    av_gen_bed = models.BooleanField(default=False,null=True)
    av_spec_bed = models.BooleanField(default=False,null=True)
    av_surg_bed = models.BooleanField(default=False,null=True)
    ICU_units = models.BooleanField(default=False,null=True)
    CIC_units = models.BooleanField(default=False,null=True)
    BIC_units = models.BooleanField(default=False,null=True)
    SIC_units = models.BooleanField(default=False,null=True)
    PsIC_units = models.BooleanField(default=False,null=True)
    PeIC_units = models.BooleanField(default=False,null=True)
    NIC_units = models.BooleanField(default=False,null=True)
    TIC_units = models.BooleanField(default=False,null=True)
    DIC_units = models.BooleanField(default=False,null=True)
    PrIC_units = models.BooleanField(default=False,null=True)
    Nursery_units = models.BooleanField(default=False,null=True)

    Lab_chem = models.BooleanField(default=False,null=True)
    Lab_hemo = models.BooleanField(default=False,null=True)
    Lab_microB = models.BooleanField(default=False,null=True)
    Lab_trans = models.BooleanField(default=False,null=True)
    Lab_immuno = models.BooleanField(default=False,null=True)
    Lab_surg_path = models.BooleanField(default=False,null=True)
    Lab_cyto = models.BooleanField(default=False,null=True)

    C_cath = models.BooleanField(default=False,null=True)
    C_rehab = models.BooleanField(default=False,null=True)
    C_surgery = models.BooleanField(default=False,null=True)
    C_stenting = models.BooleanField(default=False,null=True)
    C_intervene = models.BooleanField(default=False,null=True)
    C_electro = models.BooleanField(default=False,null=True)
    C_vas_interv = models.BooleanField(default=False,null=True)
    C_vas_surg  = models.BooleanField(default=False,null=True)

    R_com_T  = models.BooleanField(default=False,null=True)
    R_com_TA  = models.BooleanField(default=False,null=True)
    R_dig_mamo  = models.BooleanField(default=False,null=True)
    R_dig_IMRT  = models.BooleanField(default=False,null=True)
    R_dig_MRA  = models.BooleanField(default=False,null=True)
    R_dig_MRI  = models.BooleanField(default=False,null=True)
    R_dig_PET  = models.BooleanField(default=False,null=True)
    R_dig_SPECT  = models.BooleanField(default=False,null=True)

    Re_phy  = models.BooleanField(default=False,null=True)
    Re_sp  = models.BooleanField(default=False,null=True)

    EME_dept  = models.BooleanField(default=False,null=True)
    EME_ped_TC  = models.BooleanField(default=False,null=True)
    EME_TC  = models.BooleanField(default=False,null=True)

    N_EEG  = models.BooleanField(default=False,null=True)
    N_sleep  = models.BooleanField(default=False,null=True)
    Sp_BICU  = models.BooleanField(default=False,null=True)
    Sp_CCU  = models.BooleanField(default=False,null=True)
    Sp_det  = models.BooleanField(default=False,null=True)
    Sp_ICU  = models.BooleanField(default=False,null=True)
    Sp_NIC  = models.BooleanField(default=False,null=True)
    Sp_PeIC  = models.BooleanField(default=False,null=True)
    Sp_PrIC  = models.BooleanField(default=False,null=True)
    Sp_PsIC  = models.BooleanField(default=False,null=True)
    Sp_SICU  = models.BooleanField(default=False,null=True)
    Sp_TCU  = models.BooleanField(default=False,null=True)

    On_chemo  = models.BooleanField(default=False,null=True)
    On_rad  = models.BooleanField(default=False,null=True)

    Or_heart  = models.BooleanField(default=False,null=True)
    Or_intestinal  = models.BooleanField(default=False,null=True)
    Or_kidney  = models.BooleanField(default=False,null=True)
    Or_liver  = models.BooleanField(default=False,null=True)
    Or_lung  = models.BooleanField(default=False,null=True)
    Or_pancreas  = models.BooleanField(default=False,null=True)

    ortho_Arth  = models.BooleanField(default=False,null=True)
    ortho_JR  = models.BooleanField(default=False,null=True)
    ortho_spine  = models.BooleanField(default=False,null=True)

    def __str__(self):
        return   self.hospital_name +  ' @ ' + ' | ' + self.district + ' | ' + self.State 
    


def get_path(instance, filename):
    return os.path.join("static/bucket/", filename)

class refernce(models.Model):
    refernce_sno = models.AutoField(primary_key=True)
    refernce_date = models.DateTimeField(default=datetime.now,blank=True)
    refernce_hospital = models.ForeignKey(hospital,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    patientName = models.CharField(max_length=50,default='default')
    patientID = models.CharField(max_length=20)
    patientInfo = models.FileField(upload_to="info/pdfs/",null=True, blank=True)
    message = models.CharField(max_length=500)
    acceptance_choices =[
    ("1", "Waiting"),
    ("2", "Accepted"),
    ("3", "Rejected"),
]
    acceptance = models.CharField(choices=acceptance_choices ,default=1, max_length=2)

    def __str__(self):
        return ' from ' + self.user.username + ' for '  + self.patientName +'|  message:  ' + self.message

# Create your models here.
