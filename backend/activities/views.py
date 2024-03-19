from django.http.response import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http.response import JsonResponse
from .models import Activity
from .serializers import ActivitySerializer


# Create your views here.
class ActivityView(APIView):

    def post(self, request):
        data = request.data
        serializer = ActivitySerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Aktivitas Berhasil Ditambahkan", safe=False)

        return JsonResponse("Aktivitas Gagal", safe=False)
    

    def get_activity(self, pk):
        try:
            activity = Activity.objects.get(activityId=pk)
            return activity
        except Activity.DoesNotExist:
            raise Http404

    def get(self, request, pk=None):
        if pk:
            data = self.get_activity(pk)
            serializer = ActivitySerializer(data)
        else:
            data = Activity.objects.all()
            serializer = ActivitySerializer(data, many=True)
        return Response(serializer.data)
    
    def put(self, request, pk=None):
        activity_to_update = Activity.objects.get(activityId=pk)
        serializer = ActivitySerializer(instance=activity_to_update, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Berhasil Diupdate", safe=False)
        return JsonResponse("Failed To Update ")

    def delete(self, request, pk):
        activity_to_delete = Activity.objects.get(activityId=pk)
        activity_to_delete.delete()
        return JsonResponse("Data Berhasil Dihapus", safe=False)