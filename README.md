# ieee-118-bus-blocks

Python script computing IEEE 118 bus block ranges and aggregate totals.

## Overview

This project includes a Python implementation that analyzes contiguous connection blocks ranging from 10201 to 11800 and computes both:

- individual block metrics
- combined aggregate totals for the unified range

## Main script

```python
# Fast computation for IEEE 118 Bus connection blocks and aggregate totals

blocks = [
    (10201, 10600),
    (10601, 11000),
    (11001, 11400),
    (11401, 11800),
]

# Individual block computations
results = []
for start, end in blocks:
    count = end - start + 1
    block_sum = count * (start + end) // 2
    total_sum = end * (end + 1) // 2
    results.append(
        {
            "block": (start, end),
            "count": count,
            "block_sum": block_sum,
            "cumulative_sum": total_sum,
        }
    )

# Combined range computation across all contiguous blocks
overall_start = blocks[0][0]
overall_end = blocks[-1][1]
overall_count = overall_end - overall_start + 1
overall_block_sum = overall_count * (overall_start + overall_end) // 2
overall_total_sum = overall_end * (overall_end + 1) // 2

combined_summary = {
    "overall_range": (overall_start, overall_end),
    "total_elements": overall_count,
    "combined_block_sum": overall_block_sum,
    "total_cumulative_sum": overall_total_sum,
    "block_details": results,
}

print(combined_summary)

# Optional pretty print
print("\nCombined Output Summary")
print(f"Overall Range: ({overall_start}, {overall_end})")
print(f"Total Elements: {overall_count:,}")
print(f"Combined Block Sum: {overall_block_sum:,}")
print(f"Total Cumulative Sum (1 to {overall_end}): {overall_total_sum:,}")
```

## Expected output

```text
Overall Range: (10201, 11800)
Total Elements: 1,600
Combined Block Sum: 17,600,800
Total Cumulative Sum (1 to 11800): 69,625,900
```

## Run it

```bash
python main.py
```

## Files

- `main.py` — core computation
