from django.shortcuts import render
import pickle
# Create your views here.
def index(request):
    return render(request,'index.html')


def spam_check(request):
    try:

        spam='spam_model.sdv'
        model=pickle.load(open(spam,'rb'))
        info=request.GET['search']
        result=model.predict([info])
        if result==[0]:
            result='HAM'
        elif result==[1]:
            result='SPAM'
    except:
        pass
    
    
    return render(request,'index.html',{'value':result})

