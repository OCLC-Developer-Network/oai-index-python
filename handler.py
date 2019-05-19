import boto3
from elasticsearch import helpers, Elasticsearch, RequestsHttpConnection
from requests_aws4auth import AWS4Auth
import yaml
from oaipmh.client import Client
from oaipmh.metadata import MetadataRegistry, oai_dc_reader

credentials = boto3.Session().get_credentials()

s3 = boto3.client('s3')
    
# read a configuration file
with open("prod_config.yml", 'r') as stream:
    config = yaml.load(stream)

awsauth = AWS4Auth(credentials.access_key, credentials.secret_key, config.get('region'), config.get('service'))
    
es = Elasticsearch(
    hosts = [{'host': config.get('eshost'), 'port': 443}],
    http_auth = awsauth,
    use_ssl = True,
    verify_certs = True,
    connection_class = RequestsHttpConnection
)

def run(event, context):
    #pull data from OAI endpoint
    registry = MetadataRegistry()
    registry.registerReader('oai_dc', oai_dc_reader)
    URL = 'http://sandbox.contentdm.oclc.org/oai/oai.php'
    client = Client(URL, registry, force_http_get=True)

    harvested_data = [];
    for record in client.listRecords(metadataPrefix='oai_dc'):
        if not record[0].isDeleted():
            fields = record[1].getMap();
            fields['set'] = record[0].setSpec()
            harvested_data.append(fields)
        
    es.indices.delete(index='digital_collection_recs', ignore=[400, 404])
    
    mapping = {
            "mappings":{
                "_doc":{
                    "properties": {
                        "title": {"type": "text"}, 
                        "creator": {"type": "text"},
                        "subject": {"type": "text"}, 
                        "description": {"type": "text"},
                        "publisher": {"type": "text"},
                        "contributor": {"type": "text"},
                        "date": {"type": "text"},
                        "type": {"type": "text", "fielddata": "true"},
                        "format": {"type": "text", "fielddata": "true"},
                        "identifier": {"type": "text"},
                        "source": {"type": "text"},
                        "language": {"type": "text", "fielddata": "true"},
                        "relation": {"type": "text"},
                        "coverage": {"type": "text"},
                        "rights": {"type": "text"}
                    }
                }
            }
        }                
    es.indices.create(index='digital_collection_recs', body=mapping)
    
    helpers.bulk(es, harvested_data, index='digital_collection_recs', doc_type='_doc')
    
    return "success"
             