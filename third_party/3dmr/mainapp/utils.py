import os

from django.utils.safestring import mark_safe

# Gets the key and value of an OSM tag from a string
# Note: any extra '=' chars other than the first will be included in the value.
def get_kv(string):
    return string.split('=', 2)

def update_last_page(request):
    request.session['last_page'] = request.get_full_path()

def get_last_page(request):
    return request.session['last_page']

# Checks that the user that made a request is an admin
def admin(request):
    return request.user.is_authenticated and request.user.profile.is_admin

# The avaiable licenses, to be displayed in the model upload form


#   'This 3d model is made available under the <a href="http://opendatacommons.org/licenses/odbl/1.0/">Open Database License</a>.'


LICENSES_FORM = {
    0: mark_safe('<a href="http://opendatacommons.org/licenses/odbl/1.0/">Open Database License</a>'),
}

# The same as above, for the model pages
LICENSES_DISPLAY = {
    0: mark_safe('This 3d model is made available under the <a href="http://opendatacommons.org/licenses/odbl/1.0/">Open Database License</a>.'),
}

# The possible changes users can make to the repository
CHANGES = {
    0: 'Upload',
    1: 'Revise',
}

# The directory the models will be stored in
MODEL_DIR = os.environ.get('RESERVOIR_MODEL_DIR', '/home/tdmr/models')
