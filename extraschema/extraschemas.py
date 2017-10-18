from os import listdir

extraschemas = {}

try:
    myfile = globals()['__file__']
    mydir = myfile[:myfile.rfind('/')]

    for f in listdir(mydir):
        if f.find('_extraschema') > -1:
            t = f[:f.find('_')]
            extraschema = getattr(__import__('%s_extraschema' % t, globals(), locals(), ['%s_extraschema' % t]), 'extraschema')
            if extraschema:
                extraschemas[t] = extraschema.copy()
except:
    print "FAILED TO GENERATE EXTRASCHEMAS DICT"

def add_extraschema(meta_type, schema):
    extraschema = extraschemas.get(meta_type)

    if extraschema:
        schema = schema + extraschema

    return schema

def get_extraschemata(meta_type, schema):
    extraschemata = []
    extraschema = extraschemas.get(meta_type)

    if extraschema:
        for f in extraschema.fields():
            if f.schemata not in extraschemata:
                extraschemata.append(f.schemata)

    return extraschemata

def gen_extraschema(meta_type, schema):
    schema = add_extraschema(meta_type, schema)
    extraschemata = get_extraschemata(meta_type, schema)
    return schema, extraschemata
