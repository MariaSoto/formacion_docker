from server import create_app, settings

# Update settings from environment
settings.update()

# quart application
app = create_app(settings)