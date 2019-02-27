from rest_framework import filters
from rest_framework import viewsets
from contacts_backend.api.models import Contact
from contacts_backend.api.serializers import ContactSerializer


class ContactViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('first_name', 'last_name', 'phone', 'email')

