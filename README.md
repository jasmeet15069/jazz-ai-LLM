# Jazz AI V1.0 LLM Bundle

This folder contains the files currently available for the `jazz-ai-testing` model work.

The internal compatibility ID remains `jazz-ai-testing`, but the user-facing display name is now `Jazz AI V1.0`.

Primary runtime is the from-scratch GPT-style checkpoint under `from_scratch_checkpoint_on_jazz_server/model`. Qwen is only a separate backup/runtime artifact and must not be described as Jazz AI V1.0.

## Included

- `from_scratch_checkpoint_on_jazz_server/`
  - Exported scratch checkpoint copied from `root@45.79.124.28:/opt/texting-coding-model/model`
  - Jazz AI V1.0 FastAPI serving app for the from-scratch checkpoint
- `current_jazz_ai_testing_runtime/`
  - Qwen-backed backup runtime app from the earlier deployment
  - Azure systemd service and private tunnel service
- `knowledge/`
  - Curated coach knowledge from `Advait AI Knowledge.pdf`
  - `advait_ai_knowledge.raw.md`
  - `advait_ai_knowledge.coach.json`
- `scripts/`
  - PDF rendering helper
  - Runtime smoke tests
- `jazz_backend_integration/`
  - Current `server14.py` backend snapshot with the `jazz-ai-testing` adapter, math guard, display rename, and coach router

## Azure Source Project

The original training project path is:

```text
azureuser@74.225.235.134:/home/azureuser/llm-0_5b-from-scratch
```

Azure SSH was timing out during this copy, so the full training source folder could not be pulled yet. Use `fetch_full_azure_training_project.ps1` from this folder when SSH is responding again.

## Current Live Wiring

- Jazz backend: `root@45.79.124.28:/root/jazzai/server14.py`
- Backend port: `8000`
- Primary scratch model service on Jazz server: `127.0.0.1:18080`
- Scratch service: `texting-coding-llm.service`
- Qwen backup tunnel on Jazz server: `127.0.0.1:18081`
- Qwen backup Azure service: `jazz-ai-testing-llm.service`

## Behavior Targets

- `hindi mai bol` -> Hindi/Hinglish acknowledgement.
- `ladki ko first message kya bheju` -> ready-to-send bold/flirty but respectful Hinglish options.
- `she replied haha nice` -> practical reply options.
- `she said she is not interested` -> respectful close; no pressure.
- `bonjour parle francais` -> French response.
- `1+1` -> `1+1 = 2`.

## Git Note

Large model weights are ignored by git (`*.safetensors`, `*.bin`, `*.pt`, `*.pth`) so the GitHub repo can push cleanly. Keep weights on the server/runtime host, not in regular git.
