from pyramid.view import view_config


@view_config(route_name='home', renderer='templates/mytemplate.pt')
def my_view(request):
    return {'project': 'blueyellowapp'}


# @view_config(route_name='home', renderer='templates/albums.pt')
# def index(request):
#     albums = [
#         {'has_preview': True, 'title': 'Digital...', 'url': '/albums/123'},
#         {'has_preview': True, 'title': 'Freedom Songs', 'url': '/albums/993'},
#         {'has_preview': True, 'title': "'Makin' money", 'url': '/albums/722'},
#     ]
#     return {'albums': albums}
