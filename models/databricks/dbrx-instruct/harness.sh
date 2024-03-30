MODEL_ARGS="pretrained=databricks/dbrx-instruct,use_accelerate=True,trust_remote_code=True"
TASK="jsquad-1.1-0.3,jcommonsenseqa-1.1-0.3,jnli-1.3-0.3,marc_ja-1.1-0.3"
python scripts/main_eval.py \
    --model hf-causal-experimental \
    --model_args $MODEL_ARGS \
    --tasks $TASK \
    --num_fewshot "2,3,3,3" \
    --device "cuda" \
    --output_path "./result.json"
