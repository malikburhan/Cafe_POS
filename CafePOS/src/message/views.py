from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from .serializers import OutBoxSerializer
from .models import OutBox, MobileMac


# Create your views here.
class ListSendMessageApiView(generics.ListAPIView):
    serializer_class = OutBoxSerializer

    def get_queryset(self):
        mac = self.request.GET.get('mac')
        mac_list = list(MobileMac.objects.filter(status=True).values_list('mac', flat=True))
        if mac not in mac_list:
            return None
        else:
            return OutBox.objects.filter(status=False)


# this api for send message using mobile app
@csrf_exempt
def update_message_api(request):
    id = request.POST.get("id")
    ob = OutBox.objects.filter(id=id).update(status=True)
    response = {'success': False}
    if ob:
        response = {'success': True}
    return JsonResponse(response)
