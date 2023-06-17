from django.shortcuts import render,redirect
from clinical_app.models import Patient,ClinicalData
from clinical_app.forms import Patient_form,ClinicalData_form

# Create your views here.
def Patient_show(request):
    obj=Patient.objects.all()
    return render(request,'clinical_app/show.html',{'obj':obj})

def Patient_add(request):
    if request.method=='POST':
        data=Patient_form(request.POST)
        if data.is_valid():
            data.save()
            return redirect('/show')

    else:
        data=Patient_form()
        return render(request,'clinical_app/add.html',{'data':data})

# delete 
def delete(request, id):
    obj= Patient.objects.get(id=id)
    if request.method == 'POST':
        obj.delete()
        return redirect('/show')
    return render(request,'clinical_app/delete.html',{'obj': obj})


# update
def update(request,id):
    obj=Patient.objects.get(id=id)
    if request.method=='POST':
        datas=Patient_form(request.POST,instance=obj)
        if datas.is_valid():
            datas.save()
            return redirect('/show')

    else:
        datas=Patient_form(instance=obj)
        return render(request,'clinical_app/update.html',{'d':datas})

# clinical data table logic
def show_clinical_data(request,id):
    obj=Patient.objects.get(id=id)
    if request.method=='POST':
        data=ClinicalData_form(request.POST)
        if data.is_valid():
            data.save()
            
            
    else:
        data=ClinicalData_form()
    return render(request,'clinical_app/showclinical.html',{'obj':obj,'data':data})

def analysis(request,**kwargs):
  
    data=ClinicalData.objects.filter(patient_id=kwargs['pk'])
    responseData=[]
    for eachEntry in data:
        if eachEntry.componentname == 'hw':
            heightAndWeight=eachEntry.componentvalue.split('/')
            if len(heightAndWeight)>1:
                feetToMeter=float(heightAndWeight[0])*0.4536
                BMI=(float(heightAndWeight[1]))/(feetToMeter*feetToMeter)
                bmiEntry=ClinicalData()
                bmiEntry.componentname='BMI'
                bmiEntry.componentvalue=BMI
                responseData.append(bmiEntry)
        responseData.append(eachEntry)
    

    return render(request,'clinical_app/analysis.html',{'data':responseData})
  

    
    
   

















