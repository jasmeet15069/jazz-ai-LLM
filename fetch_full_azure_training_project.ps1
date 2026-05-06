$ErrorActionPreference = "Stop"

$target = "C:\Users\ACXIOM\Desktop\jazz_ai_llm\azure_training_project_full"
$archive = "/tmp/llm-0_5b-from-scratch.tar.gz"
$sshKey = "$env:USERPROFILE\.ssh\id_rsa"
$remote = "azureuser@74.225.235.134"

New-Item -ItemType Directory -Force -Path $target | Out-Null

ssh -i $sshKey $remote "cd /home/azureuser && tar --exclude='llm-0_5b-from-scratch/.venv' --exclude='llm-0_5b-from-scratch/__pycache__' -czf $archive llm-0_5b-from-scratch"
scp -i $sshKey "${remote}:$archive" "$target\llm-0_5b-from-scratch.tar.gz"

Push-Location $target
tar -xzf .\llm-0_5b-from-scratch.tar.gz
Pop-Location

Write-Host "Copied Azure training project to $target"
