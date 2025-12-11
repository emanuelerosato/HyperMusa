# 🚗 HyperMusa - Digital Cluster per Lancia Musa 2009

Sistema di quadro strumenti digitale open-source basato su Raspberry Pi per Lancia Musa (2007-2012).
Progetto derivato da [Cyberpandino](https://github.com/cyberpandino/cluster).

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Platform](https://img.shields.io/badge/platform-Raspberry%20Pi%204B%2F5-red.svg)](https://www.raspberrypi.com/)
[![Status](https://img.shields.io/badge/status-in%20development-yellow.svg)]()

---

## ✨ Features

- **Quadro strumenti digitale 3D** con interfaccia moderna
- **Lettura dati CAN-Bus nativo** ISO 15765-4 in tempo reale
- **Display touch screen** ad alta risoluzione
- **Integrazione con sensori originali** del veicolo via CAN
- **Interfaccia diretta OBD2** senza adattatori analogici
- **Modalità demo** per test senza veicolo
- **Completamente personalizzabile** e open-source

---

## 🎯 Obiettivo del Progetto

HyperMusa adatta il sistema Cyberpandino (originariamente per Fiat Panda 141) alla **Lancia Musa 2009**, un veicolo più moderno con:

- **CAN-Bus nativo** (vs sensori analogici della Panda 141)
- **Body Computer integrato** con diagnostica avanzata
- **Protocollo ISO 15765-4** standard
- **Sistema elettrico più complesso** e digitalizzato

---

## 🛠️ Hardware Necessario

### Componenti Principali

- **Raspberry Pi 4B** (4GB RAM minimo) o **Raspberry Pi 5**
- **Display touch screen** 7-10 pollici (IPS consigliato)
- **Interfaccia CAN-Bus** (MCP2515 o ELM327 compatibile CAN)
- **Convertitore DC-DC** 12V → 5V (3A per Pi 4B, 5A per Pi 5)
- **Cavi e connettori** automotive

### Sensori Opzionali

- GPS per navigazione
- Sensori temperatura esterni
- Telecamera retromarcia

📋 **Guida Hardware Completa**: [HARDWARE.md](HARDWARE.md) *(in sviluppo)*

---

## 📚 Documentazione

- [**Guida Hardware**](HARDWARE.md) - Lista componenti e schema di montaggio *(in sviluppo)*
- [**Guida Installazione**](INSTALLATION.md) - Setup passo-passo *(in sviluppo)*
- [**Architettura Sistema**](ARCHITECTURE.md) - Stack tecnologico e design *(in sviluppo)*
- [**Roadmap Sviluppo**](ROADMAP.md) - Piano di sviluppo e milestone *(in sviluppo)*
- [**Note Migrazione**](docs/migration-notes.md) - Adattamenti da Cyberpandino *(in sviluppo)*
- [**Specifiche Musa**](docs/musa-specs.md) - Specifiche tecniche Lancia Musa 2009 *(in sviluppo)*
- [**Mappatura CAN-Bus**](docs/can-bus-mapping.md) - PID e protocolli Musa *(in sviluppo)*

---

## 🚀 Quick Start

> ⚠️ **NOTA**: Il progetto è attualmente in fase di sviluppo iniziale. Le istruzioni di installazione saranno disponibili nelle prossime milestone.

### Setup Sviluppo (Modalità Demo)

```bash
# Clona il repository
git clone https://github.com/emanuelerosato/HyperMusa.git
cd HyperMusa

# Installa dipendenze (da implementare)
npm run install:all

# Avvia in modalità demo (da implementare)
npm run dev:mock
```

### Installazione su Raspberry Pi

Consulta la [Guida Installazione](INSTALLATION.md) per istruzioni complete *(in sviluppo)*.

---

## 🔄 Differenze vs Cyberpandino

| Aspetto | Cyberpandino (Panda 141) | HyperMusa (Musa 2009) |
|---------|--------------------------|------------------------|
| **CAN-Bus** | Non nativo, sensori analogici | Nativo ISO 15765-4 |
| **Complessità** | Bassa | Media-Alta |
| **OBD2** | K-Line (ISO 9141-2) | CAN (ISO 15765-4) |
| **Interfaccia** | Adattatori custom analogici | Diretta CAN nativa |
| **Body Computer** | Assente | Integrato |
| **PID Disponibili** | Limitati | Estesi (diagnostica avanzata) |

Vedi [Note di Migrazione](docs/migration-notes.md) per dettagli tecnici completi *(in sviluppo)*.

---

## 🏗️ Architettura

Il sistema è basato su:

### Stack Tecnologico
- **Frontend**: React 18 + TypeScript + Three.js
- **Backend**: Node.js + Socket.IO
- **Desktop**: Electron 36
- **Hardware**: Raspberry Pi 4B/5
- **Comunicazione**: CAN-Bus ISO 15765-4

### Struttura Progetto
```
HyperMusa/
├── client/          → Interfaccia React/Three.js
├── server/          → Backend Node.js + CAN-Bus
├── docs/            → Documentazione tecnica
├── hardware/        → Schemi e modelli 3D
└── config/          → Configurazioni CAN-Bus
```

Vedi [Architettura Completa](ARCHITECTURE.md) per dettagli *(in sviluppo)*.

---

## 📝 Stato Sviluppo

### ✅ Fase 1: Setup Iniziale (Completata)
- [x] Inizializzazione repository
- [x] Analisi progetto Cyberpandino
- [x] Struttura directory base
- [x] Documentazione iniziale

### 🚧 Fase 2: Migrazione Core (In corso)
- [ ] Importazione codice base
- [ ] Adattamento CAN-Bus nativo Musa
- [ ] Mappatura PID ISO 15765-4
- [ ] Test integrazione OBD2

### 📋 Fase 3: Testing (Pianificata)
- [ ] Modalità demo funzionante
- [ ] Test lettura CAN-Bus reale
- [ ] Validazione su Lancia Musa 2009

### 🎨 Fase 4: UI/UX (Pianificata)
- [ ] Adattamento interfaccia per Musa
- [ ] Modello 3D Lancia Musa
- [ ] Temi personalizzabili

Vedi [Roadmap Completa](ROADMAP.md) per dettagli *(in sviluppo)*.

---

## 🤝 Contribuire

Ogni contributo è benvenuto! Che si tratti di codice, documentazione, test o suggerimenti.

### Come Contribuire
1. Fork del repository
2. Crea un branch: `git checkout -b feature/nome-feature`
3. Commit: `git commit -m 'feat: descrizione'` ([Conventional Commits](https://www.conventionalcommits.org/))
4. Push: `git push origin feature/nome-feature`
5. Apri una Pull Request

---

## ⚠️ Disclaimer

HyperMusa è un **progetto hobbistico e sperimentale**, nato per curiosità tecnica e passione per l'automotive digitale. Non è un prodotto certificato, non rispetta standard industriali e non è pensato per uso su strada.

**Gli autori non si assumono alcuna responsabilità** in caso di:
- Guasti elettrici o elettronici
- Comportamenti anomali del veicolo
- Danni a persone, cose o animali
- Violazione di normative automotive locali

L'utilizzo di HyperMusa su veicoli in circolazione è **fortemente sconsigliato** e avviene a rischio esclusivo dell'utente.

---

## 📄 Licenza

Questo progetto è rilasciato sotto licenza **GNU General Public License v3.0**.

```
HyperMusa
Copyright (C) 2025  Emanuele Rosato

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
```

Vedi [LICENSE](LICENSE) per il testo completo.

---

## 🙏 Credits

### Progetto Base
HyperMusa è basato su [**Cyberpandino**](https://github.com/cyberpandino/cluster) del team Cyberpandino:
- [Matteo Errera](https://github.com/matteoerrera)
- [Roberto Zaccardi](https://github.com/rzaccardi)
- [Ludovico Verde](https://www.instagram.com/ludovico.verdee/)

Grazie al loro lavoro open-source che ha reso possibile questo progetto!

### Sviluppo HyperMusa
- **Adattamento per Lancia Musa**: [Emanuele Rosato](https://github.com/emanuelerosato)

---

## 📞 Supporto

Per problemi, domande o suggerimenti:
- **Issues**: [GitHub Issues](https://github.com/emanuelerosato/HyperMusa/issues)
- **Discussioni**: [GitHub Discussions](https://github.com/emanuelerosato/HyperMusa/discussions)

---

**Ultimo aggiornamento**: Dicembre 2025
**Veicolo target**: Lancia Musa 2009 (2007-2012)
**Status**: In sviluppo attivo
