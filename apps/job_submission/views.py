from rest_framework import permissions

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer

from apps.job_submission.models import JobSubmission
from apps.job_submission.serializers import JobSubmissionSerializer


class JobSubmissionListOrCreateView(APIView):
    """
    JobSubmissionListOrCreateView will return a list of all of the objects on GET
    and allow the creation of a job-script on POST.
    
    /job-scripts GET - Returns the list of job-scripts.
                 POST - Allows to create a job-script.
    """

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = JobSubmissionSerializer
    queryset = JobSubmission.objects.all()

    def get(self, request):
        # user = request.user
        # job_scripts = JobSubmission.objects.get(user=user)
        # serializer = JobSubmissionSerializer(data=job_scripts, many=True)
        #
        # print(serializer.__dict__)
        # return Response(JSONRenderer().render(serializer.data))
        pass


    def post(self, request):
        pass


class JobSubmissionDetailView(APIView):
    """Job script get, post, update, delete operations.

    * Requires token authentication.

    endpoint: job-scripts/<pk>/
    """

    def get(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass
