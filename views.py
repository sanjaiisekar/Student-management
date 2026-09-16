from rest_framework import viewsets, filters
from rest_framework.response import Response
from rest_framework import status
from .models import Student
from .serializers import StudentSerializer


class StudentViewSet(viewsets.ModelViewSet):
    """
    Provides full CRUD (Create, Read, Update, Delete) for Student records,
    plus search/filter (SOP Section 7.4 & 8: CRUD Functional Requirements).

    Endpoints (SOP Section 7.6 REST API Implementation):
      GET    /api/students/          -> list (supports ?search=)
      POST   /api/students/          -> create
      GET    /api/students/{id}/     -> retrieve
      PUT    /api/students/{id}/     -> full update
      PATCH  /api/students/{id}/     -> partial update
      DELETE /api/students/{id}/     -> delete
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'roll_number', 'department', 'email']

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(
            {'message': 'Student deleted successfully.'},
            status=status.HTTP_200_OK
        )
