from datasets import load_dataset
ds = load_dataset("SWE-bench/SWE-bench_Lite", split="test")
print(ds.column_names)