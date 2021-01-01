# My top 100 movies

### MyTop100Movies - API,Database,CRUD - Application which lets users set their top 100 movies. Movies could come from an API like The Movie Database (http://tmdb.org). Should allow for users to add a movie, list and rank their movie selections. Start with basic CRUD for movies and add features.

# Api

`api/v1/ ^users/$ [name='user-list']`

`api/v1/ ^users\.(?P<format>[a-z0-9]+)/?$ [name='user-list']`

`api/v1/ ^users/activation/$ [name='user-activation']`

`api/v1/ ^users/activation\.(?P<format>[a-z0-9]+)/?$ [name='user-activation']`

`api/v1/ ^users/me/$ [name='user-me']`

`api/v1/ ^users/me\.(?P<format>[a-z0-9]+)/?$ [name='user-me']`

`api/v1/ ^users/resend_activation/$ [name='user-resend-activation']`

`api/v1/ ^users/resend_activation\.(?P<format>[a-z0-9]+)/?$ [name='user-resend-activation']`

`api/v1/ ^users/reset_password/$ [name='user-reset-password']`

`api/v1/ ^users/reset_password\.(?P<format>[a-z0-9]+)/?$ [name='user-reset-password']`

`api/v1/ ^users/reset_password_confirm/$ [name='user-reset-password-confirm']`

`api/v1/ ^users/reset_password_confirm\.(?P<format>[a-z0-9]+)/?$ [name='user-reset-password-confirm']`

`api/v1/ ^users/reset_username/$ [name='user-reset-username']`

`api/v1/ ^users/reset_username\.(?P<format>[a-z0-9]+)/?$ [name='user-reset-username']`

`api/v1/ ^users/reset_username_confirm/$ [name='user-reset-username-confirm']`

`api/v1/ ^users/reset_username_confirm\.(?P<format>[a-z0-9]+)/?$ [name='user-reset-username-confirm']`

`api/v1/ ^users/set_password/$ [name='user-set-password']`

`api/v1/ ^users/set_password\.(?P<format>[a-z0-9]+)/?$ [name='user-set-password']`

`api/v1/ ^users/set_username/$ [name='user-set-username']`

`api/v1/ ^users/set_username\.(?P<format>[a-z0-9]+)/?$ [name='user-set-username']`

`api/v1/ ^users/(?P<id>[^/.]+)/$ [name='user-detail']`

`api/v1/ ^users/(?P<id>[^/.]+)\.(?P<format>[a-z0-9]+)/?$ [name='user-detail']`

`api/v1/ ^$ [name='api-root']`

`api/v1/ ^\.(?P<format>[a-z0-9]+)/?$ [name='api-root']`

`api/v1/ films/`

`api/v1/ create-film/`

`api/v1/auth/`
