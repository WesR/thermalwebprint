import falcon
import json
import requests
import cups

conn = cups.Connection()
# os.remove("demofile.txt")

with open('./assets/index.html', 'r') as f:
    indexHTML = f.read()


class assets(object):
    def on_get(self, req, resp, file):
        resp.status = falcon.HTTP_200

        fileType = file.split('.')[-1]
        if fileType == 'css':
            resp.content_type = 'text/css'
        elif fileType == 'html':
            resp.content_type = falcon.MEDIA_HTML
        elif fileType == 'js':
            resp.content_type = falcon.MEDIA_JS
        elif fileType == 'json':
            resp.content_type = falcon.MEDIA_JSON
        elif fileType == 'jpg':
            resp.content_type = falcon.MEDIA_JPEG

        with open('./assets/' + file, 'r') as f:
            resp.body = f.read()


class index(object):
    def on_get(self, req, resp):
        resp.content_type = falcon.MEDIA_HTML
        resp.body = indexHTML
        resp.status = falcon.HTTP_200


class printbytes(object):
    def on_post(self, req, resp):
        #content = json.loads((req.bounded_stream.read()).decode("utf-8"))
        scratchFile = open("./scratch", "wb")
        scratchFile.write(req.bounded_stream.read())
        scratchFile.close()
        jobID = conn.printFile('pi-print', './scratch', 'python print', {})
        resp.body = "{'job': "+str(jobID)+"}"
        resp.status = falcon.HTTP_200
