


TORTOISE_ORM = {
    "connections": {
        "default": "postgres://rentdb:rentdb@localhost:5441/rent", 
    },
    "apps": {
        "models": {
            "models": ["app.database.models", "aerich.models"],  
            "default_connection": "default",
        },
    },
}
