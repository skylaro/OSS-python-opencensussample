import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    INSTRUMENTATION_KEY = os.environ.get('APPINSIGHTS_INSTRUMENTATIONKEY') or \
       'e68b4afd-0d26-44ce-a1ae-b0707eb83c64'
    CONNECTION_STRING = 'InstrumentationKey=' + INSTRUMENTATION_KEY
    sampler = 'opencensus.trace.samplers.ProbabilitySampler(rate=1.0)'
    OPENCENSUS = {
        'TRACE': {
            'SAMPLER': sampler,
            'EXPORTER': 'opencensus.ext.azure.trace_exporter.AzureExporter(connection_string="'
            + CONNECTION_STRING + '")',
            'BLACKLIST_PATHS': ['blacklist'],
        }
    }
