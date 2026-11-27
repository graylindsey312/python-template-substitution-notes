# Ordered batch processing for Substitute named placeholders

`batch.py` accepts an outer JSON array containing separate inputs. This is an extra level of nesting when `solve` itself accepts a list. It produces one result envelope per item, preserving input order and zero-based position.

```sh
python3 batch.py < samples/batch.json
```

The batch covers these three input/output pairs:

## Case 1

Input:
```json
{
  "template": "Hello $name",
  "values": {
    "name": "Ada"
  }
}
```

Result:
```json
"Hello Ada"
```

## Case 2

Input:
```json
{
  "template": "$$${amount}",
  "values": {
    "amount": 12
  }
}
```

Result:
```json
"$12"
```

## Case 3

Input:
```json
{
  "template": "${x}/${x}",
  "values": {
    "x": "a"
  }
}
```

Result:
```json
"a/a"
```

## Partial failures

Each successful item has `ok: true` and `result`. A failed item has `ok: false` and an exception type; later items still run. Exit status 1 means at least one item failed, while status 2 means the batch envelope itself was invalid. An empty outer array is a valid empty batch.

Template.substitute requires all named values. Missing keys fail visibly rather than silently publishing unfinished placeholders; dollar signs are escaped as $$.

The implementation processes sequentially, avoiding shared-state concurrency and keeping output order predictable. Input is limited to one MiB and 1000 items; this version materializes all results in memory. The next lesson removes that whole-batch memory requirement with line-oriented processing.
