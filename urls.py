from datetime import date
from views import Index, About, Contacts, Examples, Page, AnotherPage


# front controller
def secret_front(request):
    request['date'] = date.today()


def other_front(request):
    request['key'] = 'key'


fronts = [secret_front, other_front]

routes = {
    '/': Index(),
    '/about/': About(),
    '/examples/': Examples(),
    '/page/': Page(),
    '/another_page/': AnotherPage(),
    '/contacts/': Contacts(),
}
