acronyms = {
    'LOL' : 'laugh out loud',
    'IDK' : "I don't know",
    'TBH' : 'to be honest'
}

definition = acronyms.get('BTW')
if (definition):
    print(definition)
else:
    print("Key doesn't exist")
