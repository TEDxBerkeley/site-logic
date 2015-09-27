# the main Flask application
from template_logic import create_template_app

app = create_template_app()

if __name__ == "__main__":
	app.run(**app.config['INIT'])