 
import os
from lxml import etree

nt_version = "nt16"
rootdir = f'/tmp/taxonomy/{nt_version}/'


#####
### Allowed namespaces according to an old list:
### https://github.com/centrumvoorstandaarden/SBR_Werkgroep_NT/blob/main/naamgeving/namespaces_prefixes.yaml
### Needs updating.
#####
allowed_namespaces = {
    "http://www.w3.org/XML/1998/namespace":"xml",
    "http://www.w3.org/2000/xmlns":"xmlns",
    "http://www.w3.org/2001/XMLSchema":"xs",
    "http://www.w3.org/2001/XMLSchema-instance":"xsi",
    "http://www.w3.org/1999/xlink":"xlink",
    "http://www.xbrl.org/2003/XLink":"xl",
    "http://www.xbrl.org/2003/linkbase":"link",
    "http://www.xbrl.org/2003/instance":"xbrli",
    "http://www.xbrl.org/2006/ref":"ref",
    "http://xbrl.org/2006/xbrldi":"xbrldi",
    "http://xbrl.org/2005/xbrldt":"xbrldt",
    "http://xbrl.org/2008/generic":"gen",
    "http://xbrl.org/2008/label":"label",
    "http://xbrl.org/2008/reference":"reference",
    "http://xbrl.org/2008/variable":"variable",
    "http://xbrl.org/2008/filter/value":"vf",
    "http://xbrl.org/2008/assertion/value":"va",
    "http://xbrl.org/2008/validation":"validation",
    "http://xbrl.org/2008/filter/unit":"uf",
    "http://xbrl.org/2008/filter/tuple":"tf",
    "http://xbrl.org/2008/filter/segment-scenario":"ssf",
    "http://xbrl.org/2008/filter/relative":"rf",
    "http://xbrl.org/2008/filter/period":"pf",
    "http://xbrl.org/2008/filter/match":"mf",
    "http://xbrl.org/2008/filter/general":"gf",
    "http://xbrl.org/2008/formula":"formula",
    "http://xbrl.org/2008/assertion/existence":"ea",
    "http://xbrl.org/2008/filter/entity":"ef",
    "http://xbrl.org/2008/assertion/consistency":"ca",
    "http://xbrl.org/2008/filter/concept":"cf",
    "http://xbrl.org/2008/filter/boolean":"bf",
    "http://xbrl.org/2010/filter/dimension":"df",
    "http://xbrl.org/2010/filter/aspect-cover":"acf",
    "http://xbrl.org/2010/filter/concept-relation":"crf",
    "http://xbrl.org/2010/custom-function":"cfi",
    "http://xbrl.org/2010/message":"msg",
    "http://xbrl.org/2010/message/validation":"valm",
}

arcroles = {}
namespaces = {}
roles = {}


domain = ""
for subdir, dirs, files in os.walk(rootdir):

    dir_delta = subdir.replace(rootdir, "")

    # Only overwrite the domain if it is a root file
    domain = dir_delta if "/" not in dir_delta else domain

    # Loop through files
    for file in files:
        f=open(subdir + "/" + file,'r').read()
        xml_file = etree.fromstring(bytes(f, encoding="utf-8"))

        for prefix, namespace in xml_file.nsmap.items():

            if domain not in namespaces.keys():
                arcroles[domain] = []
                namespaces[domain] = {}
                roles[domain] = []

            if prefix not in namespaces[domain].keys():
                namespaces[domain][prefix] = namespace

            elif namespaces[domain][prefix] != namespace:
                print(f"Prefix '{prefix}' already used, but with a different namespace! known:'{namespaces[domain][prefix]}' found: {namespace}")


            xlink_prefix = [k for k,v  in xml_file.nsmap.items() if v == 'http://www.w3.org/1999/xlink']
            if xlink_prefix:
                xlink_prefix = xlink_prefix[0]

            if xlink_prefix:
                for xml_linkbaseref in xml_file.xpath(f"//*[@{xlink_prefix}:role]", namespaces=xml_file.nsmap):
                    role = xml_linkbaseref.get('{http://www.w3.org/1999/xlink}role')
                    if role not in roles[domain]:
                        roles[domain].append(role)

                for xml_linkbaseref in xml_file.xpath(f"//*[@{xlink_prefix}:arcrole]", namespaces=xml_file.nsmap):
                    arcrole = xml_linkbaseref.get('{http://www.w3.org/1999/xlink}arcrole')
                    if arcrole not in arcroles[domain]:
                        arcroles[domain].append(arcrole)

def get_lines(header, contents, type):
    lines = header
    for domain, tag in contents.items():
        print(f"Domain: {domain}")

        if isinstance(tag, dict):
            for prefix, namespace in tag.items():
                is_sbr_nl = True if "http://www.nltaxonomie.nl" in namespace else False
                line = f"{type},{domain},{prefix},{namespace},{is_sbr_nl}\n"
                lines.append(line)
        else:
            for val in tag:
                is_sbr_nl = True if "http://www.nltaxonomie.nl" in val else False
                is_xbrl = True if "xbrl.org" in val else False
                is_local = True if val.startswith("urn:") else False
                line = f"{type},{domain},{val},{is_sbr_nl},{is_local},{is_xbrl}\n"
                lines.append(line)

    return lines


# Write arcroles
with open(f"/tmp/arcroles_{nt_version}.csv", "w") as output_file:
    header = ["Type,Domain,Prefix,sbr-nl,local,xbrl\n"]
    output_file.writelines(get_lines(header=header, contents=arcroles, type="arcroles"))

# Write namespaces
with open(f"/tmp/namespace_{nt_version}.csv", "w") as output_file:
    header = ["Type,Domain,Prefix,Namespace,sbr-nl,allowed\n"]

    lines = header
    for domain, tag in namespaces.items():
        print(f"Domain: {domain}")

        if isinstance(tag, dict):
            for prefix, namespace in tag.items():
                is_sbr_nl = True if "http://www.nltaxonomie.nl" in namespace else False
                is_allowed = True if namespace in allowed_namespaces.keys() or is_sbr_nl else False

                line = f"namespaces,{domain},{prefix},{namespace},{is_sbr_nl},{is_allowed}\n"
                lines.append(line)

    output_file.writelines(lines)

# Write roles
with open(f"/tmp/roles_{nt_version}.csv", "w") as output_file:
    header = ["Type,Domain,Prefix,sbr-nl,local,xbrl\n"]
    output_file.writelines(get_lines(header=header, contents=roles, type="roles"))

