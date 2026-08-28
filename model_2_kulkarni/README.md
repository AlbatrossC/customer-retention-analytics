# Model 2 Kulkarni

Simple steps to run the fine-tuned 0.5B retention model locally.

## 1. Go to the model folder

```powershell
cd D:\customer-retention-analytics\model_2_kulkarni
```

## 2. Create and activate a uv environment

```powershell
uv venv
.venv\Scripts\activate
```

## 3. Install dependencies

CPU install:

```powershell
$env:UV_LINK_MODE="copy"
uv pip install -r "model 2 demo\requirements.txt"
```

Optional CUDA install:

```powershell
$env:UV_LINK_MODE="copy"
uv pip install llama-cpp-python==0.3.35 --extra-index-url https://abetlen.github.io/llama-cpp-python/whl/cu124
```

If CUDA gives DLL errors, use the CPU install.

## 4. Run the demo

```powershell
python "model 2 demo\model_demo.py"
```

The demo loads:

```text
model 2 demo\model2_retention_0.5b.gguf
```

This is the quantized fine-tuned model.

