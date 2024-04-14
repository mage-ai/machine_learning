# ML playground

Use the [no-code UI interactions](https://docs.mage.ai/interactions/overview)
in the next block to get real-time predictions.

<img 
    src="https://github.com/mage-ai/assets/blob/main/machine-learning/data%20preparation%202.png?raw=true"
    width="500" 
/>

<br />

## API request payload

### Payload

```json
{
  "run": {
    "pipeline_uuid": "ml_inference_online",
    "block_uuid": "ml/inference/online/predictions",
    "project": "machine_learning",
    "variables": {
      "probability": true,
      "user_ids": [1, 5, 100]
    },
    "record": true,
    "store_variables": true,
    "run_upstream_blocks": false,
    "incomplete_only": false
  }
}
```

### Headers

```
Content-Type: application/json
Authorization: Bearer 2ef187c9da5e41ba915f07c0f000197a
```

<br />

### Required

1. `pipeline_uuid`: The pipeline that the block you want to run belongs to.
1. `block_uuid`: Block UUID to execute a run.

### Optional

1. `project`: The project the pipeline is in; omit if you don’t have multi-project platform setup.
1. `variables`: The values in this dictionary are available in the `kwargs` throughout your pipeline and block code.
1. `record`: If true, a pipeline run and block run are created for each API request; default is `true`.
1. `store_variables`: If true, the output of the block is stored like any other block run; default is `true`.
1. `run_upstream_blocks`: If true, the targeted block will run all its upstream blocks before running itself; default is `false`.
1. `incomplete_only`: If true and `run_upstream_blocks` is true, then only the incomplete upstream blocks are run; default is `false`.

<br />

## API response

This API endpoint will return whatever data was produced by the block.

### Example 1

```json
{
  "run": {
    "output": [
      [
        [
          0.7843851447105408,
          0.21561487019062042
        ],
        [
          0.08231198787689209,
          0.9176880121231079
        ],
        [
          0.9994457960128784,
          0.0005542014841921628
        ]
      ]
    ]
  }
}
```

```json
{
  "run": {
    "output": [
      [
        0,
        1,
        0
      ]
    ]
  }
}
```