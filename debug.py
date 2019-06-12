from ExperienceSampling.App import App
import sys

app = App(pollTime=2, postponeTime=5, debug=True)
sys.exit(app.exec_())