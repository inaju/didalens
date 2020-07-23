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
        from_email = 'mitchel@didalens.me'
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

    number=1

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
        if len(j) < 1 : partner_form=AccountabilityPartnerForm()

        else:
            return HttpResponseRedirect('/goals/partnererror/')

    return render(request, 'partner.html', context={'partner_form':partner_form, 'number':number})

@login_required(login_url="/users/account/login/")
def show_partner(request):
    partners=AccountabilityPartner.objects.filter(user=request.user)
    goal_reminder(request)
    

    return render(request, 'showpartner.html', context={'partners':partners})

@login_required(login_url="/users/account/login/")
def partner_error(request):
    partners=AccountabilityPartner.objects.filter(user=request.user)
    

    return render(request, 'partnererror.html',context={'partners':partners})


#This checks all the goals if they have been chacked for that day
#if they have not been checked for that day then mark them false
def goal_reminder(request):
    show_goal= GoalList.objects.filter()
    show_date=GoalModel.objects.filter()
    partners=AccountabilityPartner.objects.filter()
    q=GoalModel()


    #This is for the second goal
    details_list=GoalList.objects.filter(user=request.user)[1:2].get()
    for goals in show_date:
        
        for items in show_goal:
            
            if items.id == goals.datetogoal.id:
                if goals.time != datetime.now():
                    q.user=request.user
                    q.datetogoal=details_list
                    q.is_true=False
                    q.save()

    #This is for the third goal
    details_list=GoalList.objects.filter(user=request.user)[2:3].get()
    
    q=GoalModel()
    for goals in show_date:
        
        for items in show_goal:
            
            if items.id == goals.datetogoal.id:
                if goals.time != datetime.now():
                    q.user=request.user
                    q.datetogoal=details_list
                    q.is_true=False
                    q.save()
    
            
def failed_goal_report(request):
    users= CustomUser.objects.all()
    show_goal= GoalList.objects.filter()
    show_date=GoalModel.objects.filter()
  
    #print(datetime.now().time().strftime("%H:%M:%S"), str(datetime.strptime('13:48', '%H:%M').time()) )
    #print(type(datetime.now().date()))
    
    #timezone is UTC

    

    while True:
        #print(datetime.now().time().strftime("%H:%M:%S"))
        if datetime.now().time().strftime("%H:%M:%S") == str(datetime.strptime("22:30", "%H:%M").time()):
            print('k')
            
            print('one day complete')
            for goals in show_date: 
                print(str(goals.date.strftime("%Y:%m:%d")), str(datetime.now().date().strftime("%Y:%m:%d")))   
                for items in show_goal:
                    
                    if items.id == goals.datetogoal.id:
                        #if goals.date != datetime.now().date():
                        if str(goals.date.strftime("%Y:%m:%d")) == str(datetime.now().date().strftime("%Y:%m:%d")):
                            
                            for user in users:
                                
                                details_list=GoalList.objects.filter(user=user)[0:1].get()

                                b=GoalModel(user=user, datetogoal=details_list, is_true=False)
                                b.save()            

                                details_list=GoalList.objects.filter(user=user)[1:2].get()

                                b=GoalModel(user=user, datetogoal=details_list, is_true=False)
                                b.save()

                                details_list=GoalList.objects.filter(user=user)[2:3].get()

                                b=GoalModel(user=user, datetogoal=details_list, is_true=False)
                                b.save()
                break
            
            #time.sleep(10)
            print('send mail')
            send_mail(
            'Subject here',
            'Here is the message.',
            'mitchelinajuo@gmail.com',
            ['mitchelinajuo@gmail.com'],
            fail_silently=False,
            )
            for user in users:
                show_goal_user= GoalList.objects.filter(user=user)
                show_date_user=GoalModel.objects.filter(user=user)
                partners_user=AccountabilityPartner.objects.filter(user=user)

                j=[]
                for i in show_goal_user:
                    j.append(i)

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



                    subject = str(user) + ' needs your help, please check up'
                    html_message = render_to_string('help_mail_template.html', 
                    context={'goal_one':new_comb_list[0][0],'bool_one':new_comb_list[0][1], 'time_one':new_comb_list[0][2],
                            'goal_two':new_comb_list[1][0],'bool_two':new_comb_list[1][1], 'time_two':new_comb_list[1][2],
                            'goal_three':new_comb_list[2][0],'bool_three':new_comb_list[2][1], 'time_three':new_comb_list[2][2],
                            'date_now':now, 'user':user })

                    plain_message = strip_tags(html_message)
                    from_email = 'mitchelinajuo@gmail.com'
                    to = str(email_list[0])
                    to_email = str(email_list[0])

                    mail.send_mail(subject, plain_message, from_email, [to], html_message=html_message)

                            
                    

                except:
                    pass

            continue
    
def send_failed_goals_mail():
    users= CustomUser.objects.all()

    for user in users:
        show_goal_user= GoalList.objects.filter(user=user)
        show_date_user=GoalModel.objects.filter(user=user)
        partners_user=AccountabilityPartner.objects.filter(user=user)

        j=[]
        for i in show_goal_user:
            j.append(i)

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



            subject = str(user) + ' needs your help, please check up'
            html_message = render_to_string('help_mail_template.html', 
            context={'goal_one':new_comb_list[0][0],'bool_one':new_comb_list[0][1], 'time_one':new_comb_list[0][2],
                    'goal_two':new_comb_list[1][0],'bool_two':new_comb_list[1][1], 'time_two':new_comb_list[1][2],
                    'goal_three':new_comb_list[2][0],'bool_three':new_comb_list[2][1], 'time_three':new_comb_list[2][2],
                    'date_now':now, 'user':user })

            plain_message = strip_tags(html_message)
            from_email = 'mitchelinajuo@gmail.com'
            to = str(email_list[0])
            to_email = str(email_list[0])

            mail.send_mail(subject, plain_message, from_email, [to], html_message=html_message)
        except:
            pass

                    
                    

                    

        


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
                    from_email = 'mitchel@didalens.me'
                    to = str(email_list[0])
                    to_email = str(email_list[0])
                    print(to)
                    print(type(to))

                    mail.send_mail(subject, plain_message, from_email, [to], html_message=html_message)
                    mail.send_mail(subject, plain_message, from_email, [str('mitchelinaju@yahoo.com')], html_message=html_message)
                    mail.send_mail(subject, plain_message, from_email, [str('mitchelballzz@gmail.com')], html_message=html_message)
                except:
                    pass

            
        

    
        
