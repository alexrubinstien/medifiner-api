import pytest
import json
import factory

from random import randint, randrange, choice

from django.utils import timezone
from django.utils.text import slugify
from django.contrib.gis.geos import GEOSGeometry
from django.db.utils import DataError, IntegrityError
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.conf import settings
from localflavor.us.us_states import STATE_CHOICES

from medications.factories import (
    OrganizationFactory,
    ProviderFactory,
    MedicationFactory,
    MedicationNDCFactory,
    ExistingMedicationFactory,
    ProviderMedicationNdcThroughFactory,
    ProviderTypeFactory,
    ProviderCategoryFactory,
    StateFactory,
    ZipCodeFactory,
    CountyFactory,
    MedicationNameFactory,
)
from medications.models import (
    Organization,
    ExistingMedication,
    ProviderMedicationNdcThrough,
    Provider,
)

pytestmark = pytest.mark.django_db()
ORGANIZATION_NAME = 'Test organization'
TEST_NDC = '0002-1433-80'
# Real address information to generate lat and lng, cannot trust in Faker
# cause sometimes it generates addresses that googlemap api cannot convert
# to real coordinates.
REAL_STREET = '2601 Mission St'
REAL_CITY = 'San Francisco'
REAL_STATE = 'CA'


@pytest.fixture()
def long_str():
    return factory.Faker(
        'pystr',
        min_chars=256,
        max_chars=256,
    ).generate({})


@pytest.fixture()
def short_str():
    return factory.Faker(
        'pystr',
        min_chars=30,
        max_chars=30,
    ).generate({})


@pytest.fixture()
def medication():
    return MedicationFactory(
        name=factory.Faker('word'),
    )


@pytest.fixture()
def medication_ndc(medication):
    return MedicationNDCFactory(
        ndc=TEST_NDC,
        medication=medication,
    )


@pytest.fixture()
def provider():
    return ProviderFactory(
        name=factory.Faker('word'),
    )


@pytest.fixture()
def provider_category():
    return ProviderCategoryFactory(
        code=f'{randrange(1, 10**2):02}', # noqa
        name=factory.Faker('word'),
    )


@pytest.fixture()
def provider_type():
    return ProviderTypeFactory(
        code=f'{randrange(1, 10**2):02}',
        name=factory.Faker('word'),
    )


@pytest.fixture()
def geographic_object():
    return GEOSGeometry(
        json.dumps(
            settings.GEOJSON_GEOGRAPHIC_CONTINENTAL_CENTER_US
        )
    )


class TestOrganization: 
    """ Test organization model """

    def test_str(self):
        organization = OrganizationFactory(
            organization_name=ORGANIZATION_NAME,
        )
        assert organization.organization_name == ORGANIZATION_NAME
        assert str(organization) == ORGANIZATION_NAME

    def test_no_organization_name(self):
        with pytest.raises(IntegrityError):
            OrganizationFactory()

    def test_user(self, django_user_model):
        organization = OrganizationFactory(
            organization_name=ORGANIZATION_NAME,
        )
        user = django_user_model.objects.create(
            email=factory.Faker('email'),
            password=factory.Faker('password'),
            organization=organization,
        )
        assert isinstance(organization.users.get(id=user.id), get_user_model())

    def test_phone(self):
        # Test that only US phone are valid
        organization_incorrect_phone = OrganizationFactory(
            organization_name=ORGANIZATION_NAME,
            phone='666-666-666'
        )
        organization_correct_phone = OrganizationFactory(
            organization_name=ORGANIZATION_NAME,
            phone='202-555-0178'
        )
        assert not organization_incorrect_phone.phone.is_valid()
        assert organization_correct_phone.phone.is_valid()

    def test_registration_date(self):
        now = timezone.now()
        organization = OrganizationFactory(
            organization_name=ORGANIZATION_NAME,
        )
        assert now <= organization.registration_date

    def test_organization_name_max_lenght(self, long_str):
        with pytest.raises(DataError):
            OrganizationFactory(
                organization_name=long_str,
            )

    def test_contact_name_max_lenght(self, long_str):
        with pytest.raises(DataError):
            OrganizationFactory(
                contact_name=long_str,
            )

    def test_website_name_max_lenght(self, long_str):
        with pytest.raises(DataError):
            OrganizationFactory(
                website=long_str,
            )


class TestProvider:
    """ Test provider model """

    def test_str_with_provider_name(self):
        name = 'test provider'
        store_number = randint(1, 100)
        provider = ProviderFactory(
            name=name,
            store_number=store_number,
        )
        obj_str = '{} - store number: {}'.format(
            name,
            store_number,
        )
        assert provider.name == name
        assert provider.store_number == store_number
        assert str(provider) == obj_str

    def test_str_with_no_provider_name(self):
        name = ''  # This is the DB default if not supplied
        store_number = randint(1, 100)
        provider = ProviderFactory(
            store_number=store_number,
        )
        obj_str = '{} - store number: {}'.format(
            name if name else 'provider',
            store_number,
        )
        assert provider.name == name
        assert provider.store_number == store_number
        assert str(provider) == obj_str

    def test_coordinates_being_generated(self):
        provider = Provider(
            address=REAL_STREET,
            city=REAL_CITY,
            state=REAL_STATE,
        )
        provider.change_coordinates = True
        provider.save()
        assert provider.lng and provider.lat

    def test_name_max_lenght(self, long_str):
        with pytest.raises(DataError):
            ProviderFactory(
                name=long_str,
            )

    def test_address_max_lenght(self, long_str):
        with pytest.raises(DataError):
            ProviderFactory(
                address=long_str,
            )

    def test_website_max_lenght(self, long_str):
        with pytest.raises(DataError):
            ProviderFactory(
                website=long_str,
            )

    def test_operating_hours_max_lenght(self, long_str):
        with pytest.raises(DataError):
            ProviderFactory(
                operating_hours=long_str,
            )

    def test_type_max_lenght(self, long_str):
        with pytest.raises(DataError):
            ProviderTypeFactory(
                name=long_str,
            )

    def test_wrong_type(self, short_str):
        with pytest.raises(ValueError):
            organization = OrganizationFactory(
                organization_name=ORGANIZATION_NAME,
            )
            state = StateFactory()
            zipcode = ZipCodeFactory(state=state)
            with pytest.raises(ValidationError):
                provider = ProviderFactory(
                    organization=organization,
                    name=short_str,
                    address=REAL_STREET,
                    city=REAL_CITY,
                    state=REAL_STATE,
                    zip=randint(10000, 99999),
                    phone='202-555-0178',
                    email=factory.Faker('email'),
                    related_zipcode=zipcode,
                    type='as',
                )
                provider.full_clean()

    def test_unique_provider_email(self):
        email = 'example@example.com'
        with pytest.raises(IntegrityError):
            for _ in range(2):
                ProviderFactory(
                    email=email,
                )

    def test_coordenates_change_in_new_address(self):
        #  Create the provider and get its coordinates
        provider = Provider(
            address=REAL_STREET,
            city=REAL_CITY,
            state=REAL_STATE,
        )
        provider.change_coordinates = True
        provider.save()
        lat, lng = provider.lat, provider.lng
        #  Change the provider address and check the change coordinates bool
        provider.address = '2802  West Fork Street'
        provider.change_coordinates = True
        provider.save()
        lat_2, lng_2 = provider.lat, provider.lng
        #  Now assert that coordinates are different and check that the flag
        # 'change_coordinates' is back to False (it should)
        assert lat != lat_2 and lng != lng_2
        assert not provider.change_coordinates

    def test_phone(self):
        # Test that only US phone are valid
        provider_incorrect_phone = ProviderFactory(
            phone='666-666-666'
        )
        provider_correct_phone = ProviderFactory(
            phone='202-555-0178'
        )
        assert not provider_incorrect_phone.phone.is_valid()
        assert provider_correct_phone.phone.is_valid()

    def test_US_wrong_state(self, provider_type, provider_category):
        states_list = [code[0] for code in STATE_CHOICES]
        fake_state = factory.Faker(
            'pystr'
        ).generate({'min_chars': 2, 'max_chars': 2})
        while fake_state in states_list:
            fake_state = factory.Faker(
                'pystr'
            ).generate({'min_chars': 2, 'max_chars': 2})
        organization = OrganizationFactory(
            organization_name=ORGANIZATION_NAME,
        )
        state = StateFactory()
        zipcode = ZipCodeFactory(state=state)
        with pytest.raises(ValidationError):
            provider = ProviderFactory(
                organization=organization,
                name=factory.Faker('name'),
                address=factory.Faker('address'),
                city=factory.Faker('city'),
                state=fake_state,
                zip=randint(10000, 99999),
                phone='202-555-0178',
                email=factory.Faker('email'),
                related_zipcode=zipcode,
                category=provider_category,
                type=provider_type,
            )
            provider.full_clean()

    def test_state_lenght(self):
        with pytest.raises(DataError):
            ProviderFactory(
                state=factory.Faker('pystr', min_chars=3),
            )

    def test_zip_code_invalid(self, provider_category, provider_type):
        organization = OrganizationFactory(
            organization_name=ORGANIZATION_NAME,
        )
        state = StateFactory()
        zipcode = ZipCodeFactory(state=state)
        with pytest.raises(ValidationError):
            provider = ProviderFactory(
                organization=organization,
                name=factory.Faker('name'),
                address=REAL_STREET,
                city=REAL_CITY,
                state=REAL_STATE,
                zip=f'{randrange(1, 10**4):04}',
                phone='202-555-0178',
                email=factory.Faker('email'),
                category=provider_category,
                type=provider_type,
                related_zipcode=zipcode,
            )
            provider.full_clean()

    def test_zip_code_valid(self, provider_category, provider_type):
        organization = OrganizationFactory(
            organization_name=ORGANIZATION_NAME,
        )
        state = StateFactory()
        zipcode = ZipCodeFactory(state=state)
        provider = ProviderFactory(
            organization=organization,
            name=factory.Faker('name'),
            address=REAL_STREET,
            city=REAL_CITY,
            state=REAL_STATE,
            zip=f'{randrange(1, 10**5):05}',
            phone='202-555-0178',
            email=factory.Faker('email'),
            category=provider_category,
            type=provider_type,
            related_zipcode=zipcode,
        )
        provider.full_clean()


class TestState:
    """ Test state model """

    def test_str(self):
        states_list = [code for code in STATE_CHOICES]
        real_state = choice(states_list)
        state_name = real_state[1]
        state_code = real_state[0]
        state = StateFactory(
            state_code=state_code,
            state_name=state_name,
        )
        assert state.state_code == state_code
        assert state.state_name == state_name
        assert str(state) == '{} - {}'.format(state_code, state_name)

    def test_US_wrong_state(self):
        states_list = [code[0] for code in STATE_CHOICES]
        fake_state = factory.Faker(
            'pystr'
        ).generate({'min_chars': 2, 'max_chars': 2})
        while fake_state in states_list:
            fake_state = factory.Faker(
                'pystr'
            ).generate({'min_chars': 2, 'max_chars': 2})
        state = StateFactory(
            state_code=fake_state,
        )
        with pytest.raises(ValidationError):
            state.full_clean()

    def test_state_lenght(self):
        with pytest.raises(DataError):
            StateFactory(
                state_code=factory.Faker('pystr', min_chars=3),
            )

    def test_geometry_invalid(self):
        with pytest.raises(TypeError):
            states_list = [code[0] for code in STATE_CHOICES]
            real_state = choice(states_list)
            state = StateFactory(
                state_code=real_state,
                geometry=[],
            )

    def test_geometry_valid(self, geographic_object):
        states_list = [code[0] for code in STATE_CHOICES]
        real_state = choice(states_list)
        state = StateFactory(
            state_code=real_state,
            geometry=geographic_object,
        )


class TestZipCode:
    """ Test ZipCode model """

    def test_str(self):
        states_list = [code for code in STATE_CHOICES]
        real_state = choice(states_list)
        state_name = real_state[1]
        state_code = real_state[0]
        state = StateFactory(
            state_code=state_code,
            state_name=state_name,
        )
        zipcode_code = f'{randrange(1, 10**5):05}'
        zipcode = ZipCodeFactory(state=state, zipcode=zipcode_code)
        assert zipcode.zipcode == zipcode_code
        assert str(zipcode) == '{} - {} - {}'.format(
            zipcode_code, state_code, state_name
        )

    def test_zip_code_invalid(self):
        state = StateFactory()
        zipcode = ZipCodeFactory(
            state=state,
            zipcode=f'{randrange(1, 10**4):04}',
        )
        with pytest.raises(ValidationError):
            zipcode.full_clean()

    def test_zip_code_valid(self, geographic_object):
        state = StateFactory()
        zipcode = ZipCodeFactory(
            state=state,
            zipcode=f'{randrange(1, 10**5):05}',
            geometry=geographic_object,
        )

    def test_geometry_invalid(self):
        with pytest.raises(TypeError):
            state = StateFactory()
            zipcode = ZipCodeFactory(
                state=state,
                zipcode=f'{randrange(1, 10**5):05}',
                geometry=[],
            )

    def test_counties_zipcodes_relation(self, geographic_object):
        state = StateFactory()
        county = CountyFactory(state=state)
        zipcode = ZipCodeFactory(
            state=state,
            zipcode=f'{randrange(1, 10**5):05}',
            geometry=geographic_object,
        )
        zipcode.counties.add(county)
        assert zipcode in county.county_zipcodes.all()


class TestCounty:
    """ Test County model """

    def test_str(self, short_str):
        state = StateFactory()
        county = CountyFactory(
            county_name=short_str,
            state=state,
        )
        assert county.county_name == short_str
        assert str(county) == short_str

    def test_state(self):
        with pytest.raises(IntegrityError):
            county = CountyFactory()

    def test_slug(self, short_str):
        state = StateFactory()
        slug = slugify(short_str)
        county = CountyFactory(
            county_name=short_str,
            state=state,
        )
        assert county.county_name_slug == slug

    def test_county_id(self, short_str):
        with pytest.raises(IntegrityError):
            state = StateFactory()
            county = CountyFactory(
                county_name=short_str,
                state=state,
                county_id=-1,
            )

    def test_geo_id(self, short_str):
        with pytest.raises(IntegrityError):
            state = StateFactory()
            county = CountyFactory(
                county_name=short_str,
                state=state,
                geo_id=-1,
            )

    def test_geometry_invalid(self, short_str):
        with pytest.raises(TypeError):
            state = StateFactory()
            county = CountyFactory(
                county_name=short_str,
                state=state,
                geometry=[],
            )

    def test_geometry_valid(self, short_str, geographic_object):
        state = StateFactory()
        county = CountyFactory(
            county_name=short_str,
            state=state,
            geometry=geographic_object,
        )


class TestMedicationName:
    """ Test medication name model """

    def test_str(self, short_str):
        medication_name = MedicationNameFactory(
            name=short_str,
        )
        assert medication_name.name == short_str
        assert str(medication_name) == short_str

    def test_no_name(self):
        medication_name = MedicationNameFactory()
        with pytest.raises(ValidationError):
            medication_name.full_clean()

    def test_too_long_name(self, long_str):
        with pytest.raises(DataError):
            MedicationNameFactory(name=long_str)


class TestMedication:
    """ Test medication model """

    def test_str(self):
        medication_name = factory.Faker('word').generate({})
        medication = MedicationFactory(
            name=medication_name,
        )
        assert medication.name == medication_name
        assert str(medication) == medication_name

    def test_name_max_lenght(self, long_str):
        with pytest.raises(DataError):
            MedicationFactory(
                name=long_str,
            )

    def test_name_exists(self, medication_ndc):
        medication = MedicationFactory()
        with pytest.raises(ValidationError):
            medication.full_clean()


class TestMedicationNdc:
    """ Test medication ndc model """

    def test_str(self, medication):
        medication = MedicationNDCFactory(
            medication=medication,
            ndc=TEST_NDC,
        )
        assert str(medication) == TEST_NDC

    def test_ndc_max_lenght(self, long_str):
        with pytest.raises(DataError):
            MedicationNDCFactory(
                ndc=long_str,
            )

    def test_ndc_exists(self):
        medication = MedicationNDCFactory()
        with pytest.raises(ValidationError):
            medication.full_clean()

    def test_ndc_unique(self):
        with pytest.raises(IntegrityError):
            for _ in range(2):
                MedicationNDCFactory(
                    ndc=TEST_NDC,
                )

    def test_ndc_exists(self, medication):
        ExistingMedicationFactory(ndc=TEST_NDC)
        medication = MedicationNDCFactory(
            ndc=TEST_NDC,
            medication=medication,
        )
        existing_ndcs = ExistingMedication.objects.values_list(
            'ndc',
            flat=True,
        )
        assert medication.ndc in existing_ndcs


class TestExistingMedication:
    """ Test existing medication model """

    def test_str(self):
        medication = ExistingMedicationFactory(
            ndc=TEST_NDC,
        )
        assert medication.ndc == TEST_NDC
        assert str(medication) == TEST_NDC

    def test_ndc_max_lenght(self, long_str):
        with pytest.raises(DataError):
            ExistingMedicationFactory(
                ndc=long_str,
            )

    def test_ndc_exists(self):
        medication = ExistingMedicationFactory()
        with pytest.raises(ValidationError):
            medication.full_clean()

    def test_import_date(self):
        now = timezone.now()
        medication = ExistingMedicationFactory(
            ndc=TEST_NDC,
        )
        assert now <= medication.import_date


class TestProviderMedicationNdcThrough:
    """
    Test ProviderMedicationNdcThrough model.
    While testing provider_medication_through == pmt for short.
    """

    def test_str(self):
        medication_name = factory.Faker('word').generate({})
        provider_name = factory.Faker('word').generate({})

        medication = MedicationFactory(
            name=medication_name,
        )
        medication_ndc = MedicationNDCFactory(
            ndc=TEST_NDC,
            medication=medication,
        )
        provider = ProviderFactory(
            name=provider_name,
        )
        pmt = ProviderMedicationNdcThroughFactory(
            provider=provider,
            medication_ndc=medication_ndc,
        )
        provider_medication_str = '{} - store number: {} - {}'.format(
            provider_name,
            provider.store_number,
            medication_name,
        )
        assert str(pmt) == provider_medication_str

    def test_level_not_editable_after_save(self, medication_ndc, provider):
        pmt = ProviderMedicationNdcThrough.objects.create(
            level=randint(1, 100),
            medication_ndc=medication_ndc,
            provider=provider,
        )
        assert pmt.level == 0

    def test_supply_level_mapping(self, medication_ndc, provider):
        supply_to_level_map = {
            '<24': 1,
            '24': 2,
            '24-48': 3,
            '>48': 4,
        }
        for supply, level in supply_to_level_map.items():
            pmt = ProviderMedicationNdcThrough.objects.create(
                supply=supply,
                medication_ndc=medication_ndc,
                provider=provider,
            )
            assert pmt.level == level

    def test_incorrect_supply_string_makes_level_0(
        self,
        medication_ndc,
        provider,
        short_str,
    ):
        pmt = ProviderMedicationNdcThrough.objects.create(
            supply=short_str,
            medication_ndc=medication_ndc,
            provider=provider,
        )
        assert pmt.level == 0

    def test_supply_max_lenght(self, provider, medication_ndc, long_str):
        with pytest.raises(DataError):
            ProviderMedicationNdcThroughFactory(
                supply=long_str,
                provider=provider,
                medication_ndc=medication_ndc,
            )

    def test_creation_date(self, provider, medication_ndc):
        now = timezone.now()
        pmt = ProviderMedicationNdcThroughFactory(
            provider=provider,
            medication_ndc=medication_ndc,
        )
        assert now <= pmt.creation_date

    def test_provider_exists(self, medication_ndc):
        with pytest.raises(IntegrityError):
            ProviderMedicationNdcThroughFactory(
                medication_ndc=medication_ndc,
            )
