import falcon
import bjoern
from webprint import *

app = falcon.API()
app.add_route('/webprint', index())
app.add_route('/webprint/print', printbytes())
app.add_route('/assets/{file}', assets())

if __name__ == '__main__':
    bjoern.listen(app, '0.0.0.0', 8080)
    bjoern.run()