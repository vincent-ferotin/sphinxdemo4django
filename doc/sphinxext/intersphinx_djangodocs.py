# Copied as-is from:
# https://stackoverflow.com/questions/13387125/how-to-link-with-intersphinx-to-django-specific-constructs-like-settings#13663325
def setup(app):
    app.add_crossref_type(
        directivename = "setting",
        rolename = "setting",
        indextemplate = "pair: %s; setting",
    )
