# Git Commit 1: Made the Login System

Implemented Django's built-in authentication system using:

```python
urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
]
```

## Authentication URLs

This single `include()` provides several built-in authentication URLs:

```text
/accounts/login/
/accounts/logout/
/accounts/password_change/
/accounts/password_change/done/
/accounts/password_reset/
/accounts/password_reset/done/
/accounts/reset/<uidb64>/<token>/
/accounts/reset/done/
```

## Login Template

By default, Django looks for the login template at:

```text
templates/
└── registration/
    └── login.html
```

Create the `templates` directory and the `registration` folder inside it.

## Update `settings.py`

Tell Django where the project-level templates directory is located.

Update the `TEMPLATES` configuration in `settings.py`:

```python
TEMPLATES = [
    {
        ...
        "DIRS": [BASE_DIR / "templates"],
        ...
    },
]
```

This allows Django to find templates stored inside the project's `templates/` directory.