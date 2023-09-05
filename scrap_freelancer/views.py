from .models import Scrap
from .serializers import ScrapSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from scrap_freelancer.models import Scrap
import freelancer_spider
import subprocess

class ScrapList(APIView):
    def get(self, request, format=None):
        #running the scrapy script
        cmd_command = "python freelancer_spider.py"

        try:
            completed_process = subprocess.run(cmd_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

            if completed_process.returncode == 0:
                print("Scrapy script got executed successfully.")
                all_jobs = freelancer_spider.FreelanceSpider.jobs
                for job in all_jobs:
                    Scrap.objects.create(title=job[0], description=job[1], price=job[2])
            else:
                print("Scrapy script failed to run!!")
                print("Error Output:")
                print(completed_process.stderr)
        except Exception as e:
            print(f"An error occurred: {str(e)}")
        
        #Fetching all the scrapped data from the database
        job_cards = Scrap.objects.all()
        serializer = ScrapSerializer(job_cards, many=True)
        return Response(serializer.data)
