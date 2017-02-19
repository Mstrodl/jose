import sys
import json

def main(args):
    basefile = args[1]
    langfile = args[2]

    basejson, langjson = None, None
    with open(basefile, 'r') as f:
        basejson = json.load(f)

    with open(langfile, 'r') as f:
        langjson = json.load(f)

    # best merge ever!!!
    for entry in basejson:
        if entry not in langjson:
            langjson[entry] = basejson[entry]

    i = 0
    print('{')
    for key in langjson:
        val = langjson[key]
        if i == len(langjson)-1:
            print("\t%s: \"%s\"" % (json.dumps(key), val))
        else:
            print("\t%s: \"%s\"," % (json.dumps(key), val))
        i += 1
    print('}')


if __name__ == '__main__':
    sys.exit(main(sys.argv))
