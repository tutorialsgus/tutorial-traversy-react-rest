from leads.models import Lead
from rest_framework import viewsets, permissions
# pra que server um viewset? primeiro lembrar que views em django abrigam todo o controller
# um viewset é uma classe que agrupa views, er, controllers
from .serializers import LeadSerializer

# Lead Viewset
# na verdade o viewset vai permitir criar todas CRUD operations sem precisar ficar declarando explicitamente
class LeadViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all() # é a query que busca o set todo
    permission_classes = [
        permissions.AllowAny # por enquanto todo mundo pode tudo
    ]
    serializer_class = LeadSerializer # o serializer que foi criado