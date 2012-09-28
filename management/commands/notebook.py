from optparse import make_option

from django.core.management.base import BaseCommand, CommandError

from IPython.frontend.html.notebook.notebookapp import NotebookApp


class Command(BaseCommand):
    """
    A Django management command to load up a IPython notebook with Django
    settings loaded.
    """
    args = '[optional port number, or ipaddr:port]'
    option_list = BaseCommand.option_list + (
        make_option('--no-mathjax',
            action='store_true',
            dest='no_mathjax',
            default=False,
            help='Don\'t load MathJax JS, in case there is no network.'),
    )
    help = "Runs the IPython notebook."
    requires_model_validation = False

    def handle(self, addrport=None, *args, **options):
        if args:
            raise CommandError('Usage is notebook %s' % self.args)

        if addrport:
            if ':' in addrport:
                ip_addr, port = addrport.split(':')
            else:
                ip_addr = '127.0.0.1'
                port = addrport

        app = NotebookApp.instance()

        if 'ip_addr' in locals() and 'port' in locals():
            app.ip = ip_addr
            app.port = int(port)

        if options.get('no_mathjax', False):
            app.enable_mathjax = False
            del options['no_mathjax']

        app.initialize()
        app.start()
