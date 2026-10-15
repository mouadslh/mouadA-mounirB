# Script de configuration de l'environnement Windows PowerShell
# Utilise Python 3.11

Write-Host "====================================" -ForegroundColor Cyan
Write-Host "Configuration de sentiment-app" -ForegroundColor Cyan
Write-Host "====================================" -ForegroundColor Cyan

# Vérifier Python 3.11
Write-Host "`n1. Vérification de Python 3.11..." -ForegroundColor Yellow
$pythonVersion = py -3.11 --version 2>&1
if ($LASTEXITCODE -eq 0) {
    Write-Host "✓ $pythonVersion" -ForegroundColor Green
} else {
    Write-Host "✗ Python 3.11 non trouvé" -ForegroundColor Red
    Write-Host "Installez Python 3.11 depuis https://www.python.org/downloads/" -ForegroundColor Red
    exit 1
}

# Créer l'environnement virtuel
Write-Host "`n2. Création de l'environnement virtuel..." -ForegroundColor Yellow
if (Test-Path ".venv") {
    Write-Host "✓ .venv existe déjà" -ForegroundColor Green
} else {
    py -3.11 -m venv .venv
    Write-Host "✓ .venv créé" -ForegroundColor Green
}

# Activer l'environnement
Write-Host "`n3. Activation de l'environnement..." -ForegroundColor Yellow
& ".\.venv\Scripts\Activate.ps1"
Write-Host "✓ Environnement activé" -ForegroundColor Green

# Installer les dépendances
Write-Host "`n4. Installation des dépendances..." -ForegroundColor Yellow
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
Write-Host "✓ Dépendances installées" -ForegroundColor Green

# Créer la structure des dossiers
Write-Host "`n5. Création de la structure..." -ForegroundColor Yellow
$dossiers = @("data", "models", "src", "ui", "tests", "docs", "docs/cadrage", "docs/images", "scripts", "notebooks")
foreach ($dossier in $dossiers) {
    if (-not (Test-Path $dossier)) {
        New-Item -ItemType Directory -Path $dossier -Force | Out-Null
        Write-Host "✓ $dossier/ créé" -ForegroundColor Green
    } else {
        Write-Host "✓ $dossier/ existe" -ForegroundColor Green
    }
}

# Vérifier l'installation
Write-Host "`n6. Vérification finale..." -ForegroundColor Yellow
python scripts/check_setup.py

Write-Host "`n====================================" -ForegroundColor Cyan
Write-Host "Configuration terminée !" -ForegroundColor Cyan
Write-Host "====================================" -ForegroundColor Cyan
