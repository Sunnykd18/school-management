COUNTRIES = (
    dict(
        name="India",
        country_code="91"
    ),
)

PHONE_CODE_CHOICES = list(map(
    lambda x: (x['country_code'], x['name']),
    COUNTRIES
))