from .models import Scrap
from .serializers import ScrapSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from scrap_freelancer.models import Scrap
from scrap_freelancer import freelancer_spider
    

class ScrapList(APIView):
   
    all_jobs = freelancer_spider.FreelanceSpider.jobs
    for job in all_jobs:
        Scrap.objects.create(title=job[0], description=job[1], price=job[2])

    def get(self, request, format=None):
        job_cards = Scrap.objects.all()
        serializer = ScrapSerializer(job_cards, many=True)
        return Response(serializer.data)

