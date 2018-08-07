from rest_framework import serializers

from medications.models import ProviderMedicationThrough, Provider
from medications.utils import get_supplies


class ProviderMedicationSimpleSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='medication.name')
    supply = serializers.SerializerMethodField()

    class Meta:
        model = ProviderMedicationThrough
        fields = ('name', 'supply')

    def get_supply(self, obj):
        return get_supplies([obj.level])[1]


class FindProviderSerializer(serializers.ModelSerializer):
    distance = serializers.SerializerMethodField()
    supply = serializers.SerializerMethodField()
    all_other_medications_provider = serializers.SerializerMethodField()

    class Meta:
        model = Provider
        fields = (
            'id',
            'name',
            'all_other_medications_provider',
            'supply',
            'distance',
        )

    def get_distance(self, obj):
        # return distance in miles
        return obj.distance.mi

    def get_supply(self, obj):
        # Take only the verbose supply for this serializer
        return get_supplies(obj.medication_levels)[1]

    def get_all_other_medications_provider(self, obj):
        return ProviderMedicationSimpleSerializer(
            obj.provider_medication.all(),
            many=True,
        ).data
