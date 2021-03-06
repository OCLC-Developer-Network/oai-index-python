from oaipmh.metadata import MetadataReader
oai_qdc_reader = MetadataReader(
    fields={
    'title':       ('textList', 'oai_qdc:qualifieddc/dc:title/text()'),
    'creator':     ('textList', 'oai_qdc:qualifieddc/dc:creator/text()'),
    'subject':     ('textList', 'oai_qdc:qualifieddc/dc:subject/text()'),
    'description': ('textList', 'oai_qdc:qualifieddc/dc:description/text()'),
    'publisher':   ('textList', 'oai_qdc:qualifieddc/dc:publisher/text()'),
    'contributor': ('textList', 'oai_qdc:qualifieddc/dc:contributor/text()'),
    'date':        ('textList', 'oai_qdc:qualifieddc/dc:date/text()'),
    'type':        ('textList', 'oai_qdc:qualifieddc/dc:type/text()'),
    'format':      ('textList', 'oai_qdc:qualifieddc/dc:format/text()'),
    'identifier':  ('textList', 'oai_qdc:qualifieddc/dc:identifier/text()'),
    'source':      ('textList', 'oai_qdc:qualifieddc/dc:source/text()'),
    'language':    ('textList', 'oai_qdc:qualifieddc/dc:language/text()'),
    'relation':    ('textList', 'oai_qdc:qualifieddc/dc:relation/text()'),
    'coverage':    ('textList', 'oai_qdc:qualifieddc/dc:coverage/text()'),
    'rights':      ('textList', 'oai_qdc:qualifieddc/dc:rights/text()'),
    'abstract':    ('textList', 'oai_qdc:qualifieddc/dcterms:abstract/text()')
    'accessRights':      ('textList', 'oai_qdc:qualifieddc/dcterms:accessRights/text()')
    'accrualMethod':      ('textList', 'oai_qdc:qualifieddc/dcterms:accrualMethod/text()')
    'accrualPeriodicity':      ('textList', 'oai_qdc:qualifieddc/dcterms:accrualPeriodicity/text()')
    'accrualPolicy':      ('textList', 'oai_qdc:qualifieddc/dcterms:accrualPolicy/text()')
    'alternative':      ('textList', 'oai_qdc:qualifieddc/dcterms:alternative/text()')
    'audience':      ('textList', 'oai_qdc:qualifieddc/dcterms:audience/text()')
    'available':      ('textList', 'oai_qdc:qualifieddc/dcterms:available/text()')
    'bibliographicCitation':      ('textList', 'oai_qdc:qualifieddc/dcterms:bibliographicCitation/text()')
    'conformsTo':      ('textList', 'oai_qdc:qualifieddc/dcterms:conformsTo/text()')
    'created':      ('textList', 'oai_qdc:qualifieddc/dcterms:created/text()')
    'dateAccepted':      ('textList', 'oai_qdc:qualifieddc/dcterms:dateAccepted/text()')
    'dateCopyrighted':      ('textList', 'oai_qdc:qualifieddc/dcterms:dateCopyrighted/text()')
    'dateSubmitted':      ('textList', 'oai_qdc:qualifieddc/dcterms:dateSubmitted/text()')
    'educationLevel':      ('textList', 'oai_qdc:qualifieddc/dcterms:educationLevel/text()')
    'extent':      ('textList', 'oai_qdc:qualifieddc/dcterms:extent/text()')
    'hasFormat':      ('textList', 'oai_qdc:qualifieddc/dcterms:hasFormat/text()')
    'hasPart':      ('textList', 'oai_qdc:qualifieddc/dcterms:hasPart/text()')
    'hasVersion':      ('textList', 'oai_qdc:qualifieddc/dcterms:hasVersion/text()')
    'instructionalMethod':      ('textList', 'oai_qdc:qualifieddc/dcterms:instructionalMethod/text()')
    'isFormatOf':      ('textList', 'oai_qdc:qualifieddc/dcterms:isFormatOf/text()')
    'isPartOf':    ('textList', 'oai_qdc:qualifieddc/dcterms:isPartOf/text()')
    'isReferencedBy':      ('textList', 'oai_qdc:qualifieddc/dcterms:isReferencedBy/text()')
    'isReplacedBy':      ('textList', 'oai_qdc:qualifieddc/dcterms:isReplacedBy/text()')
    'isRequiredBy':      ('textList', 'oai_qdc:qualifieddc/dcterms:isRequiredBy/text()')
    'issued':      ('textList', 'oai_qdc:qualifieddc/dcterms:issued/text()')
    'isVersionOf':      ('textList', 'oai_qdc:qualifieddc/dcterms:isVersionOf/text()')
    'license':      ('textList', 'oai_qdc:qualifieddc/dcterms:license/text()')
    'mediator':      ('textList', 'oai_qdc:qualifieddc/dcterms:mediator/text()')
    'medium':      ('textList', 'oai_qdc:qualifieddc/dcterms:medium/text()')
    'modified':      ('textList', 'oai_qdc:qualifieddc/dcterms:modified/text()')
    'provenance':      ('textList', 'oai_qdc:qualifieddc/dcterms:provenance/text()')
    'references':      ('textList', 'oai_qdc:qualifieddc/dcterms:references/text()')
    'replaces':      ('textList', 'oai_qdc:qualifieddc/dcterms:replaces/text()')
    'requires':      ('textList', 'oai_qdc:qualifieddc/dcterms:requires/text()')
    'rightsHolder':      ('textList', 'oai_qdc:qualifieddc/dcterms:rightsHolder/text()')
    'spatial':     ('textList', 'oai_qdc:qualifieddc/dcterms:spatial/text()')
    'tableOfContents':      ('textList', 'oai_qdc:qualifieddc/dcterms:tableOfContents/text()')
    'temporal':      ('textList', 'oai_qdc:qualifieddc/dcterms:temporal/text()')
    'valid':      ('textList', 'oai_qdc:qualifieddc/dcterms:valid/text()')
    
    
    },
    namespaces={
    'oai_qdc': 'http://worldcat.org/xmlschemas/qdc-1.0/',
    'dc' : 'http://purl.org/dc/elements/1.1/',
    'dcterms' : 'http://purl.org/dc/terms/'}
)