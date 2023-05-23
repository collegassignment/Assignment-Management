from assignments.models import teacherprofile, studentprofile
#from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist


def getteacher(request):
    tdetail=None
   
    if request.user.is_authenticated and request.user.is_superuser!=1:
        userid=request.user
        
        try:
            tdetail=teacherprofile.objects.get(Teacher_id_id=userid)
        except ObjectDoesNotExist:
            try:
                tdetail=studentprofile.objects.get(Student_id_id=userid)
            except ObjectDoesNotExist:
                tdetail=""
        
    return {'tdetail':tdetail}
