import intake
import os


here = os.path.abspath(os.path.dirname(__file__))

cat = intake.open_catalog(os.path.join(here, 'cat.yaml'))
data = cat.variabledefault()

