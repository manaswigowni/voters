from django.shortcuts import render,redirect
# Create your views here.
from django.contrib import messages


from django.shortcuts import render, redirect
from django.contrib import messages
from .models import distrcred, constcred

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import distrcred  # Import your distrcred model
from .models import info,voterinfo,distrcred,constcred,votercred

def home(request):
    return render(request,"home.html")

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        vot_list = votercred.objects.all()
        for i in vot_list:
            if i.voterid == username and i.voterpass == password:
                request.session['username'] = username  # Store username in the session
                return redirect("/voterview")
        else:
            messages.info(request, 'Invalid username or password')
            return redirect('/login')
    else:
        return render(request, 'login.html')


from django.shortcuts import render, redirect
from django.contrib import messages
from .models import distrcred

def distr_login(request):
    if request.method == 'POST':
        username = request.POST['distr_id']
        password = request.POST['distr_pass']
        district_name = request.POST['dist_name']  # Use the correct key 'dist_name'

        try:
            district = distrcred.objects.get(dist_name=district_name)
            if district.distr_id == username and district.distr_pass == password:
                request.session['district_id'] = district.distr_id  # Store district_id in session
                return redirect('/districtview')  # Redirect after successful login
            else:
                messages.error(request, 'Invalid username, password, or district')
        except distrcred.DoesNotExist:
            messages.error(request, 'Invalid district')

    return render(request, 'distr_login.html')


def consti_login(request) :
    if request.method=='POST' :
        global username
        username=request.POST['voterid']
        password=request.POST['voterpass']
        vot_list=votercred.objects.all()
        for i in vot_list :
            if i.voterid==username and i.voterpass==password:
                return redirect("/voterview")
        else :
            messages.info(request,'Invalid username or password')
            return redirect('/consti_login')
    else  :
        return render(request,'consti_login.html')

def voterview(request):
    username = request.session.get('username')
    print(voterinfo.objects.filter(vid=username).query)

    if username:
        user_details = voterinfo.objects.filter(vid=username).first()

        if user_details:
            context = {'user_details': user_details}
            return render(request, 'voterview.html', context)
        else:
            messages.error(request, 'User details not found')
            return redirect('/login')
    else:
        messages.error(request, 'Please log in first')
        return redirect('/login')

def districtview(request):
    district_id = request.session.get('district_id')

    if district_id:
        constituencies = constcred.objects.filter(district__distr_id=district_id)
        return render(request, 'districtview.html', {'constituencies': constituencies})
    else:
        messages.error(request, 'Please log in first')
        return redirect('/distr_login')



from django.shortcuts import render
from .models import constcred, votercred

def voters_list(request):
    if request.method == 'POST':
        const_id = request.POST.get('const_id')

        try:
            constituency = constcred.objects.get(const_id=const_id)
            voters = votercred.objects.filter(constituency=constituency)

            return render(request, 'voterslist.html', {'voters': voters, 'constituency': constituency})
        except constcred.DoesNotExist:
            # Handle invalid constituency
            pass

    return redirect('/districtview')  
    

from django.shortcuts import render, get_object_or_404
from .models import voterinfo

def view_voter_details(request, voter_id):
    voter = get_object_or_404(voterinfo, vid=voter_id)
    return render(request, 'voters_details.html', {'voter': voter})



from django.shortcuts import render, get_object_or_404, redirect
from .models import voterinfo
from .forms import VoterForm

def create_voter(request, constituency_id):
    if request.method == 'POST':
        form = VoterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('voters_list', constituency_id)
    else:
        form = VoterForm()
    return render(request, 'create_voter.html', {'form': form})

def delete_voter(request, id):
    record_to_delete = voterinfo.objects.get(id=id)
    record_to_delete.delete()
    return redirect('voters_list', constituency_id=record_to_delete.part_no)  # Redirect back to voters_list



def edit(request, voter_identifier):
    research = voterinfo.objects.get(voter_identifier=voter_identifier)
    return render(request, 'edit.html', {'research': research})

def update_voter(request, voter_id):
    voter = voterinfo.objects.get(vid=voter_id)
    form = VoterForm(request.POST or None, instance=voter)
    
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/voterslist/',constituency_id=voter.part_n0)
    
    return render(request, 'edit.html', {'form': form, 'voter': voter})