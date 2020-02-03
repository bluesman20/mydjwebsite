from django.core.management.base import BaseCommand, CommandError
from mysite.models import Page

class Command(BaseCommand):
    

    def handle(self, *args, **options):
        print('Load pages')
        # delete all records
        Page.objects.all().delete()



        page = Page()
        page.title = 'Test'
        page.alias = 'index'
        page.content = 'test test test'
        page.save()

        page = Page()
        page.title = 'Portfolio'
        page.alias = 'portfolio'
        page.content = ' Portfolio Portfolio Portfolio'
        page.save()
        
        # delete one records
        # Page.objects.get(alias="index").delete()