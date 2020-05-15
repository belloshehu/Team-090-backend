from django.test import TestCase
from .models import*
from django.utils import timezone
# Create your tests here.
class ModelTestCase(TestCase):
    def setUp(self):
       service = Service.objects.create(name='Tailoring', price=120)
       category= Category.objects.create(name='Fashion', services=service, document_required=True) 
       country = Country.objects.create(name='Nigeria', continent=CONTINENTS[0])
       state = State.objects.create(name='Borno', country=country)
       lga = LocalGovernmentArea.objects.create(name='Maiduguri', state=state)
       ServiceProvider.objects.create(name='Tailor1',address1='Adress1', address2='Address2',phone='080333333404',email='some@gmail.com',
       service_rendered='Tailoring', service_category=category, picture='image.jpg', description='Dress for both genders', years_of_experience=12,
       year_of_establishement=timezone.now().date(), state=state, local_government_area=lga, country=country, supporting_document='', rating=4)

    def test_valid_service_model(self):
        service = Service.objects.get(name='Tailoring')
        self.assertEquals(service.name, 'Tailoring')
        self.assertEquals(service.price, 120)

    def test_valid_category_model(self):
        category = Category.objects.get(name='Fashion')
        self.assertEquals(category.name, 'Fashion')
        self.assertEquals(category.services.name, 'Tailoring')
        self.assertIs(category.document_required, True)
    
    def test_valid_country_model(self):
        country = Country.objects.get(name='Nigeria')
        self.assertEquals(country.name, 'Nigeria')
    
    def test_invalid_country_model(self):
        country = Country.objects.get(name='Nigeria')
        self.assertNotEquals(country.name, 'Niger')
    
    def test_valid_state_model(self):
        state = State.objects.get(name='Borno')
        self.assertEquals(state.name, 'Borno')
    
    def test_valid_local_government_area_model(self):
        lga = LocalGovernmentArea.objects.get(name='Maiduguri')
        self.assertEquals(lga.name, 'Maiduguri')

    def test_valid_service_provider_model(self):
        service_provider = ServiceProvider.objects.get(name='Tailor1', address1='Adress1')
        self.assertEquals(service_provider.name, 'Tailor1')



    
