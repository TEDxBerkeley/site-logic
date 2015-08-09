# the main Flask application
import sys, os
sys.path.insert(0, os.path.join(os.getcwd()+"/logic"))

from logic import create_app
app = create_app()

if __name__ == "__main__":
	app.run(**app.config['INIT'])