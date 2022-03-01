import imp
from multiprocessing import context
from pickle import NONE
from django import http
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,  login, logout
from .models import hospital , refernce
from django.core.files import File
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy

# Create your views here.


def index(request):
    return render(request, 'niramaya/index.html')


def handelLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        User = authenticate(username=username, password=password)

        if User is not None:
            login(request, User)
            print('user logged in successfully')
            if hospital.objects.filter(user = request.user):
                return render(request, 'niramaya/ref1.html')
            return redirect('createHospital')
        else:
            print("something went wrong")
            return render(request, 'niramaya/login.html', {})
    return HttpResponse("404 not found: Not authorised please follow the inWebFrame to navigate through pages only")


def handelLogout(request):
    logout(request)
    print('you have been loged out of account successfully')
    return redirect('login')


def createHospital(request):
    if request.user.is_anonymous:
        return HttpResponse('404 unauthorised, Login to access')
    if hospital.objects.filter(user = request.user):
        return HttpResponse('unauthorised Access to url: please contact the admin to change the values')
    if request.method == 'POST':
        user = request.user
        hospital_name = request.POST.get('hospital_name')
        serial = request.POST.get('brach_serial')
        Level = request.POST.get('hospital_level')
        address = request.POST.get('branc_add')
        State = request.POST.get('brach_state')
        district = request.POST.get('brach_district')
        phone = request.POST.get('brach_phone')
        head = request.POST.get('brach_head')
        doctor_nos = request.POST.get('brach_doctors')
        skilled_nos = request.POST.get('brach_skilled')
        non_skilled_nos = request.POST.get('brach_NonSkilled')
        gen_bed = request.POST.get('brach_gen_bed')
        spec_bed = request.POST.get('brach_special_bed')
        surg_bed = request.POST.get('brach_srg_bed')
        av_gen_bed = request.POST.get('branch_available_gen_beds')
        av_spec_bed = request.POST.get('branch_available_spec_beds')
        av_surg_bed = request.POST.get('branch_available_srg_beds')

        ICU_units = request.POST.get('branch_ICU')
        CIC_units = request.POST.get('branch_CIC')
        BIC_units = request.POST.get('branch_BIC')
        SIC_units = request.POST.get('branch_SIC')
        PsIC_units = request.POST.get('branch_PsIC')
        PeIC_units = request.POST.get('branch_PeIC')
        NIC_units = request.POST.get('branch_NIC')
        TIC_units = request.POST.get('branch_TIC')
        DIC_units = request.POST.get('branch_DIC')
        PrIC_units = request.POST.get('branch_PrIC')
        Nursery_units = request.POST.get('branch_Nursery')

        Lab_chem = request.POST.get('Lab_chem')
        Lab_hemo = request.POST.get('Lab_hemo')
        Lab_microB = request.POST.get('Lab_microB')
        Lab_trans = request.POST.get('Lab_trans')
        Lab_immuno = request.POST.get('Lab_immuno')
        Lab_surg_path = request.POST.get('Lab_surg_path')
        Lab_cyto = request.POST.get('Lab_cyto')

        C_cath = request.POST.get('C_cath')
        C_rehab = request.POST.get('C_rehab')
        C_surgery = request.POST.get('C_surgery')
        C_stenting = request.POST.get('C_stenting')
        C_intervene = request.POST.get('C_interve')
        C_electro = request.POST.get('C_electro')
        C_vas_interv = request.POST.get('C_vas_interv')
        C_vas_surg = request.POST.get('C_vas_sur')

        R_com_T = request.POST.get('R_com_T')
        R_com_TA = request.POST.get('R_com_TA')
        R_dig_mamo = request.POST.get('R_dig_mamo')
        R_dig_IMRT = request.POST.get('R_IMRT')
        R_dig_MRA = request.POST.get('R_MRA')
        R_dig_MRI = request.POST.get('R_MRI')
        R_dig_PET = request.POST.get('R_PET')
        R_dig_SPECT = request.POST.get('R_SPECT')

        Re_phy = request.POST.get('Re_phy')
        Re_sp = request.POST.get('Re_sp')

        EME_dept = request.POST.get('EME_dept')
        EME_ped_TC = request.POST.get('EME_ped_TC')
        EME_TC = request.POST.get('EME_TC')

        N_EEG = request.POST.get('N_sleep')
        N_sleep = request.POST.get('N_EEG')

        Sp_BICU = request.POST.get('Sp_BICU')
        Sp_CCU = request.POST.get('Sp_CCU')
        Sp_det = request.POST.get('Sp_det')
        Sp_ICU = request.POST.get('Sp_ICU')
        Sp_NIC = request.POST.get('Sp_NIC')
        Sp_PeIC = request.POST.get('Sp_PeIC')
        Sp_PrIC = request.POST.get('Sp_PrIC')
        Sp_PsIC = request.POST.get('Sp_PsIC')
        Sp_SICU = request.POST.get('Sp_SICU')
        Sp_TCU = request.POST.get('Sp_TCU')

        On_chemo = request.POST.get('On_chemo')
        On_rad = request.POST.get('On_rad')

        Or_heart = request.POST.get('Or_heart')
        Or_intestinal = request.POST.get('Or_intestinal')
        Or_kidney = request.POST.get('Or_kidney')
        Or_liver = request.POST.get('Or_liver')
        Or_lung = request.POST.get('Or_lung')
        Or_pancreas = request.POST.get('Or_pancreas')

        ortho_Arth = request.POST.get('Ortho_Arth')
        ortho_JR = request.POST.get('Ortho_JR')
        ortho_spine = request.POST.get('Ortho_spine')

        new_hospital = hospital(user=user, hospital_name=hospital_name, serial=serial, Level=Level, address=address, State=State, district=district, phone=phone, head=head, doctor_nos=doctor_nos, skilled_nos=skilled_nos, non_skilled_nos=non_skilled_nos, gen_bed=gen_bed, spec_bed=spec_bed, surg_bed=surg_bed, av_gen_bed=av_gen_bed, av_spec_bed=av_spec_bed, av_surg_bed=av_surg_bed, ICU_units=ICU_units, CIC_units=CIC_units, BIC_units=BIC_units, SIC_units=SIC_units, PsIC_units=PsIC_units, PeIC_units=PeIC_units, NIC_units=NIC_units, TIC_units=TIC_units, DIC_units=DIC_units, PrIC_units=PrIC_units, Nursery_units=Nursery_units, Lab_chem=Lab_chem, Lab_hemo=Lab_hemo, Lab_microB=Lab_microB, Lab_trans=Lab_trans, Lab_immuno=Lab_immuno, Lab_surg_path=Lab_surg_path, Lab_cyto=Lab_cyto, C_cath=C_cath, C_rehab=C_rehab, C_surgery=C_surgery,
                            C_stenting=C_stenting, C_intervene=C_intervene, C_electro=C_electro, C_vas_interv=C_vas_interv, C_vas_surg=C_vas_surg, R_com_T=R_com_T, R_com_TA=R_com_TA, R_dig_mamo=R_dig_mamo, R_dig_IMRT=R_dig_IMRT, R_dig_MRA=R_dig_MRA, R_dig_MRI=R_dig_MRI, R_dig_PET=R_dig_PET, R_dig_SPECT=R_dig_SPECT, Re_phy=Re_phy, Re_sp=Re_sp, EME_dept=EME_dept, EME_ped_TC=EME_ped_TC, EME_TC=EME_TC, N_EEG=N_EEG, N_sleep=N_sleep, Sp_BICU=Sp_BICU, Sp_CCU=Sp_CCU, Sp_det=Sp_det, Sp_ICU=Sp_ICU, Sp_NIC=Sp_NIC, Sp_PeIC=Sp_PeIC, Sp_PrIC=Sp_PrIC, Sp_PsIC=Sp_PsIC, Sp_SICU=Sp_SICU, Sp_TCU=Sp_TCU, On_chemo=On_chemo, On_rad=On_rad, Or_heart=Or_heart, Or_intestinal=Or_intestinal, Or_kidney=Or_kidney, Or_liver=Or_liver, Or_lung=Or_lung, Or_pancreas=Or_pancreas, ortho_Arth=ortho_Arth, ortho_JR=ortho_JR, ortho_spine=ortho_spine)

        new_hospital.save()
        return redirect('refer_to')
    # return HttpResponse('something went wrong')
    return render(request, 'niramaya/register.html')


def refer(request):
    if request.user.is_anonymous:
        return HttpResponse('404 unauthorised, Login to access')

    if request.method == 'POST':
        paitent_name = request.POST['paitent_name']
        paitent_id = request.POST['paitent_id']
        # paitentInfo = request.POST['paitent_summary']
        paitentInfo = request.FILES['paitent_summary']
        request_message = request.POST['request_message']
        refernce_hospital_serial = request.POST.get('referal_hospital')
        refernce_hospital = hospital.objects.filter(serial = refernce_hospital_serial).first()
        user = request.user
        fs = FileSystemStorage()
        filename = fs.save( paitentInfo.name,paitentInfo)
        uploaded_file_url = fs.url(filename)

        context = {
            'uploaded_file_url': uploaded_file_url
        }

        referance = refernce(patientName=paitent_name, patientID=paitent_id,patientInfo=paitentInfo,message=request_message,refernce_hospital = refernce_hospital,user=user)

        referance.save()

    return render(request, 'niramaya/ref1.html')


def search(request):
    if request.method == 'POST':
        Q_av_gen_bed = request.POST.get('Q_branch_available_gen_beds', False)
        Q_av_spec_bed = request.POST.get('Q_branch_available_spec_beds', False)
        Q_av_surg_bed = request.POST.get('Q_branch_available_srg_beds', False)

        Q_ICU_units = request.POST.get('Q_branch_ICU', False)
        Q_CIC_units = request.POST.get('Q_branch_CIC', False)
        Q_BIC_units = request.POST.get('Q_branch_BIC', False)
        Q_SIC_units = request.POST.get('Q_branch_SIC', False)
        Q_PsIC_units = request.POST.get('Q_branch_PsIC', False)
        Q_PeIC_units = request.POST.get('Q_branch_PeIC', False)
        Q_NIC_units = request.POST.get('Q_branch_NIC', False)
        Q_TIC_units = request.POST.get('Q_branch_TIC', False)
        Q_DIC_units = request.POST.get('Q_branch_DIC', False)
        Q_PrIC_units = request.POST.get('Q_branch_PrIC', False)
        Q_Nursery_units = request.POST.get('Q_branch_Nursery', False)

        Q_Lab_chem = request.POST.get('Q_Lab_chem', False)
        Q_Lab_hemo = request.POST.get('Q_Lab_hemo', False)
        Q_Lab_microB = request.POST.get('Q_Lab_microB', False)
        Q_Lab_trans = request.POST.get('Q_Lab_trans', False)
        Q_Lab_immuno = request.POST.get('Q_Lab_immuno', False)
        Q_Lab_surg_path = request.POST.get('Q_Lab_surg_path', False)
        Q_Lab_cyto = request.POST.get('Q_Lab_cyto', False)

        Q_C_cath = request.POST.get('Q_C_cath', False)
        Q_C_rehab = request.POST.get('Q_C_rehab', False)
        Q_C_surgery = request.POST.get('Q_C_surgery', False)
        Q_C_stenting = request.POST.get('Q_C_stenting', False)
        Q_C_intervene = request.POST.get('Q_C_interve', False)
        Q_C_electro = request.POST.get('Q_C_electro', False)
        Q_C_vas_interv = request.POST.get('Q_C_vas_interv', False)
        Q_C_vas_surg = request.POST.get('Q_C_vas_sur', False)

        Q_R_com_T = request.POST.get('Q_R_com_T', False)
        Q_R_com_TA = request.POST.get('Q_R_com_TA', False)
        Q_R_dig_mamo = request.POST.get('Q_R_dig_mamo', False)
        Q_R_dig_IMRT = request.POST.get('Q_R_IMRT', False)
        Q_R_dig_MRA = request.POST.get('Q_R_MRA', False)
        Q_R_dig_MRI = request.POST.get('Q_R_MRI', False)
        Q_R_dig_PET = request.POST.get('Q_R_PET', False)
        Q_R_dig_SPECT = request.POST.get('Q_R_SPECT', False)

        Q_Re_phy = request.POST.get('Q_Re_phy', False)
        Q_Re_sp = request.POST.get('Q_Re_sp', False)

        Q_EME_dept = request.POST.get('Q_EME_dept', False)
        Q_EME_ped_TC = request.POST.get('Q_EME_ped_TC', False)
        Q_EME_TC = request.POST.get('Q_EME_TC', False)

        Q_N_EEG = request.POST.get('Q_N_sleep', False)
        Q_N_sleep = request.POST.get('Q_N_EEG', False)

        Q_Sp_BICU = request.POST.get('Q_Sp_BICU', False)
        Q_Sp_CCU = request.POST.get('Q_Sp_CCU', False)
        Q_Sp_det = request.POST.get('Q_Sp_det', False)
        Q_Sp_ICU = request.POST.get('Q_Sp_ICU', False)
        Q_Sp_NIC = request.POST.get('Q_Sp_NIC', False)
        Q_Sp_PeIC = request.POST.get('Q_Sp_PeIC', False)
        Q_Sp_PrIC = request.POST.get('Q_Sp_PrIC', False)
        Q_Sp_PsIC = request.POST.get('Q_Sp_PsIC', False)
        Q_Sp_SICU = request.POST.get('Q_Sp_SICU', False)
        Q_Sp_TCU = request.POST.get('Q_Sp_TCU', False)

        Q_On_chemo = request.POST.get('Q_On_chemo', False)
        Q_On_rad = request.POST.get('Q_On_rad', False)

        Q_Or_heart = request.POST.get('Q_Or_heart', False)
        Q_Or_intestinal = request.POST.get('Q_Or_intestinal', False)
        Q_Or_kidney = request.POST.get('Q_Or_kidney', False)
        Q_Or_liver = request.POST.get('Q_Or_liver', False)
        Q_Or_lung = request.POST.get('Q_Or_lung', False)
        Q_Or_pancreas = request.POST.get('Q_Or_pancreas', False)

        Q_ortho_Arth = request.POST.get('Q_Ortho_Arth', False)
        Q_ortho_JR = request.POST.get('Q_Ortho_JR', False)
        Q_ortho_spine = request.POST.get('Q_Ortho_spine', False)

        raw_query_set = {
        "av_gen_bed": Q_av_gen_bed,
        "av_spec_bed": Q_av_spec_bed,
        "av_surg_bed": Q_av_surg_bed,
        "ICU_units": Q_ICU_units,
        "CIC_units": Q_CIC_units,
        "BIC_units": Q_BIC_units,
        "SIC_units": Q_SIC_units,
        "PsIC_units": Q_PsIC_units,
        "PeIC_units": Q_PeIC_units,
        "NIC_units": Q_NIC_units,
        "TIC_units": Q_TIC_units,
        "DIC_units": Q_DIC_units,
        "PrIC_units": Q_PrIC_units,
        "Nursery_units": Q_Nursery_units,
        "Lab_chem": Q_Lab_chem,
        "Lab_hemo": Q_Lab_hemo,
        "Lab_microB": Q_Lab_microB,
        "Lab_trans": Q_Lab_trans,
        "Lab_immuno": Q_Lab_immuno,
        "Lab_surg_path": Q_Lab_surg_path,
        "Lab_cyto": Q_Lab_cyto,
        "C_cath": Q_C_cath,
        "C_rehab": Q_C_rehab,
        "C_surgery": Q_C_surgery,
        "C_stenting": Q_C_stenting,
        "C_intervene": Q_C_intervene,
        "C_electro": Q_C_electro,
        "C_vas_interv": Q_C_vas_interv,
        "C_vas_surg": Q_C_vas_surg,
        "R_com_T": Q_R_com_T,
        "R_com_TA": Q_R_com_TA,
        "R_dig_mamo": Q_R_dig_mamo,
        "R_dig_IMRT": Q_R_dig_IMRT,
        "R_dig_MRA": Q_R_dig_MRA,
        "R_dig_MRI": Q_R_dig_MRI,
        "R_dig_PET": Q_R_dig_PET,
        "R_dig_SPECT": Q_R_dig_SPECT,
        "Re_phy": Q_Re_phy,
        "Re_sp": Q_Re_sp,
        "EME_dept": Q_EME_dept,
        "EME_ped_TC": Q_EME_ped_TC,
        "EME_TC": Q_EME_TC,
        "N_EEG": Q_N_EEG,
        "N_sleep": Q_N_sleep,
        "Sp_BICU": Q_Sp_BICU,
        "Sp_CCU": Q_Sp_CCU,
        "Sp_det": Q_Sp_det,
        "Sp_ICU": Q_Sp_ICU,
        "Sp_NIC": Q_Sp_NIC,
        "Sp_PeIC": Q_Sp_PeIC,
        "Sp_PrIC": Q_Sp_PrIC,
        "Sp_PsIC": Q_Sp_PsIC,
        "Sp_SICU": Q_Sp_SICU,
        "Sp_TCU": Q_Sp_TCU,
        "On_chemo": Q_On_chemo,
        "On_rad": Q_On_rad,
        "Or_heart": Q_Or_heart,
        "Or_intestinal": Q_Or_intestinal,
        "Or_kidney": Q_Or_kidney,
        "Or_liver": Q_Or_liver,
        "Or_lung": Q_Or_lung,
        "Or_pancreas": Q_Or_pancreas,
        "ortho_Arth": Q_ortho_Arth,
        "ortho_JR": Q_ortho_JR,
        "ortho_spine": Q_ortho_spine,
    }

        query_set = {}
        for items in raw_query_set:
            if raw_query_set[items]:
                query_set[items] = raw_query_set[items]

        searched_hospitals = hospital.objects.all()
        searched_hospitals = searched_hospitals.exclude(user=request.user)
        searched_hospitals = searched_hospitals.filter(**query_set)

        if len(searched_hospitals) == 0:
            print('XXXXX NO result found')
            return render(request, 'niramaya/ref1.html')

        context = {
            'searched_hospitals': searched_hospitals,
            'query_sets': raw_query_set
        }
        return render(request, 'niramaya/ref1.html', context)

    return render(request, 'niramaya/ref1.html')

def request(request):
    if request.user.is_anonymous:
        return HttpResponse('404 unauthorised, Login to access')
    
    user_hospital = hospital.objects.filter(user = request.user).first()
    hospital_referal_requests = refernce.objects.filter(acceptance = '1',refernce_hospital = user_hospital).exclude(user = request.user)
    print(hospital_referal_requests.first())
    
    context={        
        'hospital_referal_requests' : hospital_referal_requests
    }
    return render(request, 'niramaya/request.html',context)

def request_acceptance(request):
    if request.user.is_anonymous:
        return HttpResponse('404 unauthorised, Login to access')
    
    if request.method == 'POST':
        acceptance = request.POST.get('referal_acceptance')
        request_code = request.POST.get('referal_code')

        extract_request = refernce.objects.filter(refernce_sno = request_code).first()

        extract_request.acceptance = acceptance

        extract_request.save()
    return render(request, 'niramaya/request.html')


def history(request):
    if request.user.is_anonymous:
        return HttpResponse('404 unauthorised, Login to access')
    
    user_hospital = hospital.objects.filter(user = request.user).first()
    incoming_hospital_referal_requests = refernce.objects.exclude(acceptance = '1',user = request.user).filter(refernce_hospital = user_hospital)


    outgoing_hospital_referal_requests = refernce.objects.filter(user = request.user)

    context = {
        'incoming_hospital_referal_requests' : incoming_hospital_referal_requests,
        'outgoing_hospital_referal_requests' : outgoing_hospital_referal_requests
    }
    return render(request,'niramaya/history.html',context)


def account(request):
    if request.user.is_anonymous:
        return HttpResponse('404 unauthorised, Login to access')
    return render(request, 'niramaya/register.html', {'username': request.user})




def Login(request):
    return render(request, 'niramaya./login.html')
