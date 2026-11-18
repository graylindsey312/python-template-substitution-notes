# Substitute named placeholders: implementation

## What the example does

Template.substitute requires all named values. Missing keys fail visibly rather than silently publishing unfinished placeholders; dollar signs are escaped as $$.

The public function is `solve(value)`. The JSON input contract can be seen in this concrete example:

```json
{
  "template": "Hello $name",
  "values": {
    "name": "Ada"
  }
}
```

Expected result:

```json
"Hello Ada"
```

Run `python3 example.py` for the Python representation of the result. `solution.py` contains the full implementation and can also be imported by another script.

## Scope

The function implements exactly the behavior described above. It does not perform network or filesystem access. Python exceptions indicate unsupported input; the next lesson turns them into a command-line error response. Review the limitations before reusing it in an application.
