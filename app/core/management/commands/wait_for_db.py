from django.core.management.base import BaseCommand

"""_summary_
    
    Django command to pause execution until database is available
    
"""

class command(BaseCommand):
    """_summary_
        
        Django Command to wait for database
        
    """
    def handle(self, *args, **options):
        
        pass
        
        
        # """_summary_
            
        #     Handle the command
            
        # """
        # self.stdout.write('Waiting for database...')
        # db_conn = None
        # while not db_conn:
        #     try:
        #         db_conn = connections['default']
        #     except OperationalError:
        #         self.stdout.write('Database unavailable, waiting 1 second...')
        #         time.sleep(1)
        # self.stdout.write(self.style.SUCCESS('Database available!'))    
    