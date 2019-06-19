# json2dot
A python script, which exports the JSON structure as DOT graph.

This script accepts a JSON string and returns a valid DOT graph script.
This can be used to visualize the structure of any given JSON document.

## Usage
For example will this command

`echo {\"a\":1,\"b\": { \"c\": 2}} | python3 json2dot.py | dot -Tpng -ojson.png`

create the following graph

(Image here)


`cat json.json | python3 json2dot.py | dot -Tpng -ojson.png`

This command will feed the contents of a json file into the script.

The returned DOT code can of course be combined with all graphviz utilities.
If, for example, a JSON object has many members

`cat json.json | python3 json2dot.py |  unflatten -l 5 | dot -Tpng -ojson.png`

can be used to unflatten the graph.
