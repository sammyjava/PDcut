import requests, sys
     
server = "https://rest.ensembl.org"

with open('Cilia_proteome.txt') as f:
    for line in f:
        symbol = line.strip()
        ext = "/xrefs/symbol/mus_musculus/"+symbol+"?"
        r = requests.get(server+ext, headers={ "Content-Type" : "application/json"})
        if not r.ok:
            r.raise_for_status()
            sys.exit()
        for item in r.json():
            if item["type"] == 'translation':
                id = item["id"]
                ext = "/sequence/id/"+id+"?type=protein"
                r = requests.get(server+ext, headers={ "Content-Type" : "text/x-fasta"})
                if not r.ok:
                    r.raise_for_status()
                    sys.exit()
                print(r.text)

