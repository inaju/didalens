from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from .models import GoalList, GoalModel
from django.contrib.auth.decorators import login_required
from .forms import GoalForm,GoalModelForm, GoalModelCheck,GoalOrdinaryForm,GoalOrdinaryFormFalse
from users.models import CustomUser
from datetime import datetime
from django.core.mail import send_mail
import itertools
from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from .forms import AccountabilityPartnerForm
from users.models import AccountabilityPartner
from django.views.generic import ListView
from django.core.paginator import Paginator
from datetime import datetime, date
import time
from django.utils import timezone
from selenium import webdriver

#create_goal is responsible for creating goals for individual users
@login_required(login_url="/users/account/login/")
def create_goal(request):
    #the whole point of this is to count the number of goals
    #if the number of goals in 3 then this would redirect them to show/
    details_list=GoalList.objects.filter(user=request.user)
    j=[]
    for i in details_list:
        j.append(i)
            

    #This gets the goals list
    #if user is authenticated and the method is post
    q=GoalList(user=request.user)
    if request.method == 'POST' and request.user.is_authenticated:
        goal = GoalForm(request.POST)
        

        #if the form is valid...continue
        # save Goallist.user to be = the connected user
        # save the current goal from the form i.e request.POST['goal']        
        if goal.is_valid():
            q.user=request.user
            q.goal=request.POST['goal']
            
            try:
                q.save()
                #goal.save()
            except :
                pass            
            
            return HttpResponseRedirect('/goals/secondgoal/')

    else:
        if len(j) <3  : goal = GoalForm() 

        else:
            return HttpResponseRedirect('/goals/goalfull/')

    return render(request, 'creategoal.html', {'goal': goal})


@login_required(login_url="/users/account/login/")
def create_goal_two(request):
    details_list=GoalList.objects.filter(user=request.user)
    j=[]
    for i in details_list:
        j.append(i)

    q=GoalList()
    if request.method == 'POST' and request.user.is_authenticated:
        goal = GoalForm(request.POST)
        
        
        if goal.is_valid():
            q.user=request.user
            q.goal=request.POST['goal']
            
            try:
                q.save()
                #goal.save()
            except :
               pass
                  
            return HttpResponseRedirect('/goals/thirdgoal/')

    else:
        goal = GoalForm()

    return render(request, 'creategoal_two.html', {'goal': goal })    

@login_required(login_url="/users/account/login/")
def create_goal_three(request):
    details_list=GoalList.objects.filter(user=request.user)
    j=[]
    for i in details_list:
        j.append(i)
    
    q=GoalList()
    if request.method == 'POST' and request.user.is_authenticated:
        goal = GoalForm(request.POST)
        
        
        
        if goal.is_valid():
            q.user=request.user
            q.goal=request.POST['goal']
            
            try:
                q.save()
                #goal.save()
            except :
                pass
            
            
            return HttpResponseRedirect('/goals/partner/')

    else:
        goal = GoalForm()
    
    return render(request, 'creategoal_three.html', { 'goal': goal})

#deaily_Details is responsible for displaying the details and saving them
@login_required(login_url="/users/account/login/")
def daily_details(request):
    try:
        details_list=GoalList.objects.filter(user=request.user)[0:1].get()
    except:
        return HttpResponse('no data')
    
    q=GoalModel()
    if request.method == 'POST' and request.user.is_authenticated:
        #details_check = GoalModelCheck(request.POST)
        goalordinaryform=GoalOrdinaryForm(request.POST)

        
        if goalordinaryform.is_valid():
            q.user=request.user
            q.datetogoal=details_list
            q.is_true=goalordinaryform.cleaned_data['is_true']
            q.save()

            return HttpResponseRedirect('/goals/details_two/')    

    else:
        goalordinaryform=GoalOrdinaryForm()
        formfalse=GoalOrdinaryFormFalse()


    return render(request, 'details.html', { 'details_list':details_list, 'goalordinaryform':goalordinaryform,'formfalse':formfalse})


@login_required(login_url="/users/account/login/")
def daily_details_two(request):

    try:
        details_list=GoalList.objects.filter(user=request.user)[1:2].get()
    except:
        return HttpResponse('no data')
    
    
    q=GoalModel()
    if request.method == 'POST' and request.user.is_authenticated:
        #details_check = GoalModelCheck(request.POST)
        goalordinaryform=GoalOrdinaryForm(request.POST)

        
        if goalordinaryform.is_valid():
            q.user=request.user
            q.datetogoal=details_list
            q.is_true=goalordinaryform.cleaned_data['is_true']
            q.save()
            
            
            #details_check.save()
            
            return HttpResponseRedirect('/goals/details_three/')    

    else:
        goalordinaryform=GoalOrdinaryForm()
        formfalse=GoalOrdinaryFormFalse()


    return render(request, 'details.html', { 'details_list':details_list, 'goalordinaryform':goalordinaryform,'formfalse':formfalse})
 
@login_required(login_url="/users/account/login/")
def daily_details_three(request):
    show_date=GoalModel.objects.filter(user=request.user)

    try:
        details_list=GoalList.objects.filter(user=request.user)[2:3].get()
    except:
        return HttpResponse('no data')
    
    
    q=GoalModel()
    if request.method == 'POST' and request.user.is_authenticated:
        #details_check = GoalModelCheck(request.POST)
        goalordinaryform=GoalOrdinaryForm(request.POST)

        
        if goalordinaryform.is_valid():
            q.user=request.user
            q.datetogoal=details_list
            q.is_true=goalordinaryform.cleaned_data['is_true']
            q.save()
            #details_check.save()

            
            
            return HttpResponseRedirect('/goals/goalfull/')    

    else:
        goalordinaryform=GoalOrdinaryForm()
        formfalse=GoalOrdinaryFormFalse()


    return render(request, 'details.html', { 'details_list':details_list, 'goalordinaryform':goalordinaryform,'formfalse':formfalse})
 
@login_required(login_url="/users/account/login/")
def show(request):
    show_goal= GoalList.objects.filter(user=request.user)
    show_date=GoalModel.objects.filter(user=request.user)
    
    show_date_page = GoalModel.objects.filter(user=request.user).order_by('-date')
    date_list=[]
    for i in show_date_page:
        date_list.append(i)
    
    
    paginator=Paginator(show_date_page,21)
    page_number = request.GET.get('page')
    posts=paginator.get_page(page_number)

    return render(request, 'show.html',
     context={'show_goal':show_goal,'show_date':posts,'items': posts})


@login_required(login_url="/users/account/login/")
def goalfull(request):
    
    show_goal= GoalList.objects.filter(user=request.user)
    show_date=GoalModel.objects.filter(user=request.user)
    partners=AccountabilityPartner.objects.filter(user=request.user)

    j=[]
    for i in show_goal:
        j.append(i)

    email_list=[]
    for emails in partners:
        email_list.append(emails)


    new_comb_list=[]
    comb_list=[]
    
    try:
        
        for goal in show_date:
            goal=[str(goal.datetogoal), goal.is_true, goal.time.strftime("%H:%M:%S")]
            comb_list.append(goal)

        for list in comb_list[-3:]:
            new_comb_list.append(list)
        now = datetime.now()



        subject = 'Goals for '+str(datetime.today().strftime('%Y-%m-%d'))
        html_message = render_to_string('mail_template.html', 
        context={'goal_one':new_comb_list[0][0],'bool_one':new_comb_list[0][1], 'time_one':new_comb_list[0][2],
                'goal_two':new_comb_list[1][0],'bool_two':new_comb_list[1][1], 'time_two':new_comb_list[1][2],
                'goal_three':new_comb_list[2][0],'bool_three':new_comb_list[2][1], 'time_three':new_comb_list[2][2],
                'date_now':now })

        plain_message = strip_tags(html_message)
        from_email = 'mitchelinajuo@gmail.com'
        to = str(email_list[0])

        to_email = str(email_list[0])

        mail.send_mail(subject, plain_message, from_email, [to], html_message=html_message)

                
        

    except:
        '''if len(j)==1:
            return HttpResponseRedirect('/goals/details_two/')
        if len(j)==2:
            return HttpResponseRedirect('/goals/details_three/')
        if len(j)==3:
            return HttpResponseRedirect('/goals/show/')
            
        else:
            return HttpResponseRedirect('/goals/create_goal/')
           '''
            
    return render(request, 'show.html',
     context={'show_goal':show_goal,'show_date':show_date })

@login_required(login_url="/users/account/login/")
def create_accountability_partners(request):
    partners=AccountabilityPartner.objects.filter(user=request.user)
    user = AccountabilityPartner.objects.filter(user=request.user)
    all_users= CustomUser.objects.all()

    link=request.META.get('HTTP_HOST')+'/goals/ask_a_friend'
    print(link)

    for current_user in all_users:
        if current_user == request.user:
            print(request.user.id)

    j=[]
    for i in partners:
        j.append(i)

    if request.method == 'POST':
        partner_form=AccountabilityPartnerForm(request.POST)

        if partner_form.is_valid:

            first_name=request.POST['first_name']
            last_name=request.POST['last_name']
            email=request.POST['email']
            phone_number=request.POST['phone_number']
            user=request.user

            partnermodel=AccountabilityPartner(first_name=first_name, last_name=last_name, email=email, phone_number=phone_number, user=request.user)
            partnermodel.save()

            

            return HttpResponseRedirect('/goals/details/')

    else:
        '''if the user has no accountability partner, return thr form to the user'''
        if len(j) < 1 : partner_form=AccountabilityPartnerForm()

        else:
            '''if the user already has an accountability user, return the partnererror page'''
            return HttpResponseRedirect('/goals/partnererror/')

    return render(request, 'partner.html', context={'partner_form':partner_form, 'number':len(j),'user_id':request.user.id, 'link':link})

@login_required(login_url="/users/account/login/")
def show_partner(request):
    partners=AccountabilityPartner.objects.filter(user=request.user)

    return render(request, 'showpartner.html', context={'partners':partners})

@login_required(login_url="/users/account/login/")
def partner_error(request):
    partners=AccountabilityPartner.objects.filter(user=request.user)
    

    return render(request, 'partnererror.html',context={'partners':partners})
    
def ask_a_friend(request, user_id):
    all_users= CustomUser.objects.all()
    for user in all_users:
        if user.id ==user_id:
            current_user_rq_send=user


    if request.method == 'POST':
        partner_form=AccountabilityPartnerForm(request.POST)

        if partner_form.is_valid:

            first_name=request.POST['first_name']
            last_name=request.POST['last_name']
            email=request.POST['email']
            phone_number=request.POST['phone_number']
            

            for user in all_users:
                

                if user.id ==user_id:
                    current_user_rq=user
                    print(user, user.id)
                    partnermodel=AccountabilityPartner(first_name=first_name, last_name=last_name, email=email, phone_number=phone_number, user=current_user_rq)
                    partnermodel.save()

            return HttpResponseRedirect('/goals/thankyou/')

    else:
        '''if the user has no accountability partner, return thr form to the user'''
        partner_form=AccountabilityPartnerForm()


    #return HttpResponse("You're looking at question %s." % user_id)
    return render(request, 'ask_a_friend.html', context={'user_id':user_id,'partner_form':partner_form,'current_user_rq_send':current_user_rq_send})

def thank_you(request):

    return False

#This checks all the goals if they have been chacked for that day
#if they have not been checked for that day then mark them false

        


def failed_goal_list(request):
    users= CustomUser.objects.all()
    
    for current_user in users:
        j=1
        date_list=[]
        
        show_goal_user= GoalList.objects.filter(user=current_user)
        show_date_user=GoalModel.objects.filter(user=current_user)
        partners_user=AccountabilityPartner.objects.filter(user=current_user)
        v=[x for x in show_date_user]
        date=[d.date for d in v]

        for i in v:
            date_list.append(i.date)
        
        for date in date_list[-3:]:
            if str(date) != datetime.now().date().strftime("%Y-%m-%d"):
                print(current_user,date , datetime.now().date().strftime("%Y-%m-%d"))

                while j < 4:
                    
                    details_list=GoalList.objects.filter(user=current_user)[j-1:j].get()
                    
                    b=GoalModel(user=current_user, datetogoal=details_list, is_true=False)
                    b.save()
                    print('saved for ',current_user)
                    j += 1

                show_goal_user= GoalList.objects.filter(user=current_user)
                show_date_user=GoalModel.objects.filter(user=current_user)
                partners_user=AccountabilityPartner.objects.filter(user=current_user)


                email_list=[]
                for emails in partners_user:
                    email_list.append(emails)


                new_comb_list=[]
                comb_list=[]
                
                try:
                    
                    for goal in show_date_user:
                        goal=[str(goal.datetogoal), goal.is_true, goal.time.strftime("%H:%M:%S")]
                        comb_list.append(goal)

                    for list in comb_list[-3:]:
                        new_comb_list.append(list)
                    now = datetime.now()



                    subject = str(current_user) + ' needs your help, please check up'
                    html_message = render_to_string('help_mail_template.html', 
                    context={'goal_one':new_comb_list[0][0],'bool_one':new_comb_list[0][1], 'time_one':new_comb_list[0][2],
                            'goal_two':new_comb_list[1][0],'bool_two':new_comb_list[1][1], 'time_two':new_comb_list[1][2],
                            'goal_three':new_comb_list[2][0],'bool_three':new_comb_list[2][1], 'time_three':new_comb_list[2][2],
                            'date_now':now, 'user':current_user })

                    plain_message = strip_tags(html_message)
                    from_email = 'mitchelinajuo@gmail.com'
                    to = str(email_list[0])
                    to_email = str(email_list[0])
                    print(to)
                    print(type(to))

                    mail.send_mail(subject, plain_message, from_email, [to], html_message=html_message)
                    mail.send_mail(subject, plain_message, from_email, [str('mitchelinaju@yahoo.com')], html_message=html_message)
                    mail.send_mail(subject, plain_message, from_email, [str('mitchelballzz@gmail.com')], html_message=html_message)
                except:
                    pass

        


def send_test_email(request):

    send_mail(
    'Subject here',
    'Here is the message.',
    'mitchelinajuo@gmail.com',
    ['mitchelinajuo@gmail.com'],
    fail_silently=False,
    )


    return HttpResponse('sent mail --done')