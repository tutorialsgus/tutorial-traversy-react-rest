from rest_framework import serializers # biblioteca de REST
from leads.models import Lead # importar o model que queremos serializar

# Lead Serializer
class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = '__all__' # poderia colocar campo a campo (name, date, etc)