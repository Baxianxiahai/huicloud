from django.shortcuts import render,HttpResponse
import json
# Create your views here.
def login(request):
    return render(request,'Login.html')
def ajax(request):
    if request.method =='POST':
        ret={'status':1001,'error':''}
        string=request.body
        # ss=json.dump(string)
        # string=urllib.parse.unquote(string)
        user='freeman'
        pwd='redhat'
        # print(ss)

        print(type(string))
        # print (user,pwd)
        if user == 'freeman' and pwd == 'redhat':
            ret['status'] = 1002
        else:
            ret['error']='Username oR password error'
        return  HttpResponse(json.dumps(ret))
    return render(request,'Login.html')
