from django.conf import settings
from rest_framework import serializers

from feed.models import Feed


class FeedSerializer(serializers.ModelSerializer):
    # If your <field_name> is declared on your serializer with the parameter required=False
    # then this validation step will not take place if the field is not included.

    # last_modify_date = serializers.DateTimeField(format=settings.DATETIME_FORMAT, required=False)
    # created = serializers.DateTimeField(format=settings.DATE_FORMAT, required=False)

    class Meta:
        model = Feed
        # fields = '__all__'
        fields = ('id', 'fname', 'fitem', 'fusage1', 'flegalname', 'master_feed')
