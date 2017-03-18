import urllib2
import sys
from flask import Flask


app = Flask(__name__)

try:
    repository = sys.argv[1].split("/", 3)[3]

except IndexError:
    print "Invalid or No config repository URL provided!"
    sys.exit()

@app.route("/")
def hello():
    return "Hello from Dockerized Flask App!!"

@app.route("/v1/<environment>-config.yml")
def configYml(environment):
    file_ext = ".yml"
    try:
        response = fileContent(environment,file_ext)
        return response
    except IndexError:
        return "Config file not found!"


@app.route("/v1/<environment>-config.json")
def configJson(environment):
    file_ext = ".json"
    try:
        response = fileContent(environment,file_ext)
        return response
    except IndexError:
        return "Config file not found!"

def fileContent(environment,file_ext):
    try:
        request = urllib2.Request("https://api.github.com/repos/" + repository + "/contents/" + environment + "-config" + file_ext)
        request.add_header('Accept' , 'application/vnd.github.VERSION.raw')
        return urllib2.urlopen(request).read().strip()
    except:
        return "Config file not found!"

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')

