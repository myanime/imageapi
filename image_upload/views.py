from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import csrf_exempt
from django.forms import ModelForm
from models import Image
from django.http import HttpResponse, HttpResponseBadRequest

class ImageValidator(ModelForm):
    class Meta:
        model = Image
        fields = ['mypic']

@csrf_exempt
def simple_upload(request):
    if request.method == 'POST':# and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        newPic = Image()
        newPic.mypic = myfile
        newPic.save()
        return HttpResponse("DONE")
        # form = ImageValidator(request.POST, request.FILES)
        # print "FFF"
        # print form.errors
        # if form.is_valid():
        #     print "FFFSSS"
        #     form.save()
        #     return HttpResponse("DONE")
        # else:
        #     return HttpResponseBadRequest()
        # myfile = request.FILES['myfile']
        # fs = FileSystemStorage()
        # filename = fs.save(myfile.name, myfile)
        # uploaded_file_url = fs.url(filename)
        # return render(request, 'simple_upload.html', {
        #     'uploaded_file_url': uploaded_file_url
        # })
    return render(request, 'myform.html')
