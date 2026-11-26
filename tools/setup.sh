#!/usr/bin/env bash
# Setup-Skript für Claude-Code-Cloud-Sitzungen dieses Repos.
# Läuft (falls in der Cloud-Umgebung gespeichert) als root im Ordner ÜBER dem Repo.
# Das Repo braucht nur Python 3 (Standardbibliothek) – keine Pakete, keine Secrets.
set -e
command -v python3 >/dev/null || (apt-get update -qq && apt-get install -y -qq python3)
if [ -d gta-vi-wissensdatenbank ]; then
  python3 gta-vi-wissensdatenbank/tools/qc_check.py >/dev/null || echo "QC meldet Fehler – siehe python3 tools/qc_check.py"
fi
