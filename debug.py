from ExperienceSampling.App import App
import sys, os

try:
    with open("timer.txt", 'r') as file:
        timer = file.read()
    timer = int(timer)
    app = App(pollTime=timer, postponeTime=5, debug=True)
except:
    app = App(pollTime=2, postponeTime=5, debug=True)

sys.exit(app.exec_())