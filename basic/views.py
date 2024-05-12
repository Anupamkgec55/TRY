from django.shortcuts import render
from joblib import load

model=load('./Model/svc_model2.joblib')

def Home(request):
    return render(request,'index.html')

def Heart(request):
    return render(request,'heart.html')
def Liver(request):
    return render(request,'liver.html')
def Diabetes(request):
    return render(request,'diabetes.html')
def Cancer(request):
    return render(request,'cancer.html')

def About(request):
    return render(request,'about.html')

def Dept(request):
    return render(request,'departments.html')

def Cont(request):
    return render(request,'contacts.html')

def User(request):
    Age = float(request.GET['Age'])
    Gender = float(request.GET['Gender'])
    Total_Bilirubin = float(request.GET['TB'])
    Direct_Bilirubin = float(request.GET['DB'])
    Alkaline_Phosphotase = float(request.GET['Alkphos'])
    Alamine_Aminotransferase = float(request.GET['Alamine_Aminotransferase'])
    Aspartate_Aminotransferase = float(request.GET['Aspartate_Aminotransferase'])
    Total_Protiens = float(request.GET['Total_Protiens'])
    Albumin = float(request.GET['ALB'])
    Albumin_and_Globulin_Ratio = float(request.GET['A/G Ratio'])
    
    y_pred=model.predict([[Age,Gender,Total_Bilirubin,Direct_Bilirubin,Alkaline_Phosphotase,Alamine_Aminotransferase,Aspartate_Aminotransferase,Total_Protiens,Albumin,Albumin_and_Globulin_Ratio]])
    if y_pred==1:
       x= "low risk"
    else:
       x= "high risk"

    return render(request,'user.html',{'name':x})



# from Anupam.forms import ContactForm;
# from django.core.mail import send_mail;

# def contact_view(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             email = form.cleaned_data['email']
#             message = form.cleaned_data['message']
            
#             send_mail(
#                 f'Name: {name}\nEmail: {email}\n\nMessage:\n{message}',
#                 ['Anupamdasasansol@gmail.com'], 
#             )
#     else:
#         form = ContactForm()

#     return render(request, 'contacts.html', {'form': form})