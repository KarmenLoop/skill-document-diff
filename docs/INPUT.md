# Input and output

Supply a UTF-8 JSON object (maximum 10 MiB). Duplicate JSON keys and non-finite JSON constants are rejected. Arrays are required unless documented as optional. IDs must be stable and unique. Dates use ISO 8601; timestamps require an explicit UTC offset.

| Field | Contract |
| --- | --- |
| before/after | Strings; empty text is allowed. |
| before_label/after_label | Optional version labels. |
| max_diff_lines | Optional integer 1..10000, default 1000. |

## Example

```json
{
  "before": "Delivery in 5 days.\nPrice: 100 USD.",
  "after": "Delivery in 3 days.\nPrice: 120 USD.",
  "before_label": "v1",
  "after_label": "v2"
}
```

## Result

added_lines, removed_lines, numbers_removed, numbers_added, unified_diff, truncated, before_sha256, after_sha256.

See [the complete sample result](../examples/expected.json). Exit 0 means processing completed, not that all reported findings passed.

## Errors and side effects

The helper makes no network requests and executes no submitted commands. It reads the input and explicitly documented local paths. It writes only a requested new output file; stdout is the default. Invalid input exits 2. Existing output is preserved. An output write failure can leave a partial new file; remove that file before retrying. Installation is a separate explicit action.
