# 🗺️ Roadmap HyperMusa

Questo documento traccia lo stato di avanzamento del progetto HyperMusa e le milestone future.

---

## 📊 Stato Generale

| Fase | Status | Completamento | Note |
|------|--------|---------------|------|
| **Fase 1: Setup** | ✅ Completata | 100% | Repository inizializzato |
| **Fase 2: Migrazione Core** | 🚧 In corso | 10% | Analisi completata |
| **Fase 3: Power Management** | 📋 Pianificata | 0% | Standby mode & batteria |
| **Fase 4: Testing** | 📋 Pianificata | 0% | Dipende da Fase 2-3 |
| **Fase 5: UI/UX** | 📋 Pianificata | 0% | Dipende da Fase 4 |
| **Fase 6: Produzione** | 📋 Pianificata | 0% | Release finale |

---

## ✅ Fase 1: Setup Iniziale (Completata)

**Obiettivo**: Preparare il progetto per lo sviluppo

### Tasks Completati
- [x] Clone e analisi repository Cyberpandino
- [x] Inizializzazione repository Git HyperMusa
- [x] Configurazione remote GitHub
- [x] Creazione struttura directory base
- [x] Documentazione README principale
- [x] Note di migrazione iniziali
- [x] Primo commit e push su GitHub
- [x] Analisi stack tecnologico Cyberpandino

### Deliverable
- ✅ Repository GitHub pubblico
- ✅ Struttura directory organizzata
- ✅ README.md professionale
- ✅ Documentazione migrazione
- ✅ File `project-structure.txt` con analisi Cyberpandino

**Data completamento**: 11 Dicembre 2025

---

## 🚧 Fase 2: Migrazione Core (In corso)

**Obiettivo**: Importare e adattare il codice Cyberpandino per Lancia Musa

### 2.1 Importazione Codice Base
**Status**: 📋 Da iniziare | **Completamento**: 0%

- [ ] Copia selettiva directory `client/` da Cyberpandino
- [ ] Copia selettiva directory `server/` da Cyberpandino
- [ ] Copia `main.js` (Electron wrapper)
- [ ] Copia file configurazione (`package.json`, `tsconfig.json`)
- [ ] Commit separati per ogni modulo importato

**Note**:
- NON copiare `node_modules`
- NON copiare file `.env` o credentials
- Ogni copia deve avere commit atomico dedicato

---

### 2.2 Adattamento Backend CAN-Bus
**Status**: 📋 Da iniziare | **Completamento**: 0%

#### 2.2.1 Implementazione Interfaccia CAN
- [ ] Ricerca e selezione libreria CAN-Bus Node.js
  - Valutare: `socketcan`, `node-can`, `socketcan-native`
  - Test compatibilità Raspberry Pi
- [ ] Implementazione `MusaCANService.js`
  - Connessione CAN-Bus nativo
  - Gestione errori e reconnessione
  - Buffer frame CAN
- [ ] Sostituzione `OBDCommunicationService.js`
  - Mantieni interfaccia per compatibilità
  - Backend completamente CAN nativo

#### 2.2.2 Parser PID ISO 15765-4
- [ ] Implementazione parser PID standard
  - PID Mode 01 (dati real-time)
  - PID Mode 02 (freeze frame)
  - PID Mode 03 (DTC - Diagnostic Trouble Codes)
- [ ] Conversioni unità (hex → valori leggibili)
- [ ] Gestione frame CAN multi-byte (flow control)

#### 2.2.3 Mappatura PID Lancia Musa
- [ ] Acquisizione hardware interfaccia CAN
  - MCP2515 + TJA1050 per Raspberry Pi
  - O ELM327 USB compatibile CAN
- [ ] Sniffing CAN-Bus su Musa 2009
  - Installazione `can-utils` su Raspberry
  - Log frame CAN durante vari stati (idle, accensione, movimento)
- [ ] Identificazione PID custom Fiat/Lancia
  - Mappatura spie cruscotto
  - Sensori non standard
- [ ] Creazione `config/musa-can-mapping.js`
  - PID standard testati
  - PID custom scoperti
  - Documentazione conversioni

#### 2.2.4 Configurazione
- [ ] File `server/config/can-bus.js`
  - Interfaccia CAN (socketcan0)
  - Baudrate (500 kbps standard Fiat)
  - Timeout e retry
- [ ] Aggiornamento `gpio-mapping.js`
  - GPIO opzionali (non più necessari per spie base)
  - Mantenuti per sensori custom

**Commit attesi**:
- `feat(can): implementa interfaccia CAN-Bus nativa`
- `feat(can): aggiunge parser PID ISO 15765-4`
- `feat(config): aggiunge mappatura PID Lancia Musa`
- `refactor(obd): sostituisce seriale con CAN nativo`

---

### 2.3 Testing Backend
**Status**: 📋 Da iniziare | **Completamento**: 0%

- [ ] Unit test `MusaCANService`
- [ ] Unit test parser PID
- [ ] Modalità demo con dati simulati Musa
- [ ] Test integrazione CAN reale su banco
- [ ] Validazione letture sensori

**Deliverable Fase 2**:
- 📦 Codice Cyberpandino importato e organizzato
- 📦 Backend CAN-Bus funzionante
- 📦 Parser PID ISO 15765-4 completo
- 📦 Configurazione Musa testata
- 📦 Modalità demo operativa
- 📦 Almeno 30+ commit di sviluppo

**Data target**: Gennaio 2026

---

## ⚡ Fase 3: Power Management & Standby (Pianificata)

**Obiettivo**: Implementare boot rapido <5s e autonomia batteria 7+ giorni

**Durata**: 2-3 settimane
**Commit target**: 15 commit

### 3.1 Hardware Standby (~5 commit)

#### 3.1.1: Relay Module Installation
- [ ] Acquista relay module 5V 1 canale (~8€)
- [ ] Schema collegamento OBD2 pin 15 → Relay → GPIO 17
- [ ] Montaggio fisico relay vicino Raspberry Pi
- [ ] Test continuità circuito con multimetro
- [ ] Protezione cavi con heat-shrink tubing

**Commit**: `feat(hardware): aggiunge relay module per rilevamento chiave`

#### 3.1.2: GPIO Wake Configuration
- [ ] Config `/boot/firmware/config.txt`: abilita GPIO 17 wake
- [ ] Device tree overlay `gpio-shutdown`
- [ ] Test wake interrupt manuale (GPIO 17 → 3.3V)
- [ ] Verifica `/sys/class/gpio/gpio17/power/wakeup` = enabled

**Commit**: `feat(power): configura GPIO 17 come wake source`

### 3.2 Software Power Daemon (~7 commit)

#### 3.2.1: Kernel S3 Support
- [ ] Verifica `cat /sys/power/state` mostra "mem"
- [ ] Configura `/sys/power/mem_sleep` = "deep"
- [ ] Test suspend manuale: `sudo systemctl suspend`
- [ ] Misura consumo standby con multimetro (<1W target)

**Commit**: `feat(power): abilita Suspend-to-RAM (S3) kernel support`

#### 3.2.2: systemd Service
- [ ] Crea `hypermusa-power.service` unit file
- [ ] Dependencies: after `hypermusa-ui.service`
- [ ] Restart policy: always, 5s delay
- [ ] Logging: journald integration

**Commit**: `feat(power): aggiunge systemd power management service`

#### 3.2.3: Power Daemon Python
- [ ] Implementa `PowerManager` class
- [ ] GPIO monitoring loop (polling 1Hz)
- [ ] Chiave OFF → Suspend logic (60s timeout)
- [ ] GPIO interrupt handler → Wake callback
- [ ] Integrazione con app HyperMusa (stop/start UI)

**Commit**: `feat(power): implementa daemon monitoraggio stato chiave`

#### 3.2.4: Battery Protection
- [ ] Lettura voltaggio batteria da CAN-Bus (PID 0x42)
- [ ] Check periodico ogni 5 minuti
- [ ] Threshold 11.5V → Emergency shutdown
- [ ] Logging eventi batteria

**Commit**: `feat(power): aggiunge protezione batteria bassa`

#### 3.2.5: Integration Testing
- [ ] Test ciclo completo: Active → Standby → Wake
- [ ] Cronometraggio: wake time <5s
- [ ] Stress test: 100 cicli suspend/wake
- [ ] Test autonomia: 48h parcheggio, misura consumo

**Commit**: `test(power): valida cicli suspend/wake completi`

### 3.3 Ottimizzazioni Performance (~3 commit)

#### 3.3.1: Boot Speed Optimization
- [ ] Disabilita servizi non essenziali (bluetooth, cups, avahi)
- [ ] RAM disk per logs: `/var/log` → tmpfs
- [ ] Prelancia app HyperMusa in background
- [ ] Target: cold boot <30s, resume <5s

**Commit**: `perf(power): ottimizza boot speed <30s`

#### 3.3.2: Standby Power Optimization
- [ ] HDMI off pre-suspend: `tvservice -o`
- [ ] USB selective suspend
- [ ] LED Pi disabilitati
- [ ] Target consumo: <0.5W standby

**Commit**: `perf(power): riduce consumo standby <0.5W`

#### 3.3.3: Documentation
- [ ] Aggiorna `docs/power-management.md` con test results
- [ ] Troubleshooting guide
- [ ] Performance benchmarks pubblicati

**Commit**: `docs(power): completa documentazione standby mode`

### 🎯 Milestone Fase 3

**Definition of Done**:
- ✅ Boot/Resume da standby < 5 secondi
- ✅ Consumo standby < 1W (target 0.5W)
- ✅ Autonomia batteria 60Ah > 7 giorni parcheggio
- ✅ 100+ cicli suspend/wake senza errori
- ✅ Protezione batteria <11.5V funzionante
- ✅ Documentazione completa e testata

**Deliverable**:
- 📦 Repository con power management funzionante
- 📦 Video demo: boot 3-5s da chiave AUTO
- 📦 Grafici consumo batteria 7 giorni
- 📦 Tutorial installazione relay module

**Data target**: Marzo 2026

---

## 📋 Fase 4: Testing e Validazione (Pianificata)

**Obiettivo**: Validare il sistema su Lancia Musa 2009 reale

### 4.1 Setup Ambiente Test
- [ ] Installazione Raspberry Pi OS su Pi 4B/5
- [ ] Setup Node.js 20 LTS
- [ ] Configurazione interfaccia CAN hardware
- [ ] Test comunicazione CAN su banco (senza veicolo)

### 4.2 Test su Veicolo (Statico)
- [ ] Installazione temporanea in Musa
- [ ] Connessione OBD2 e CAN-Bus
- [ ] Verifica lettura PID base (RPM, velocità, temperatura)
- [ ] Log dati CAN per analisi offline
- [ ] Identificazione PID mancanti

### 4.3 Test su Veicolo (Dinamico)
- [ ] Test in movimento (passeggero con laptop)
- [ ] Validazione precisione letture
- [ ] Test affidabilità connessione CAN
- [ ] Benchmark latenza e performance

### 4.4 Documentazione Test
- [ ] Creazione `docs/testing-report.md`
- [ ] Documentazione PID scoperti
- [ ] Troubleshooting e soluzioni
- [ ] Video demo funzionamento

**Deliverable Fase 4**:
- 📦 Sistema validato su Musa reale
- 📦 Database PID completo e testato
- 📦 Report testing dettagliato
- 📦 Video demo YouTube

**Data target**: Aprile 2026

---

## 🎨 Fase 5: UI/UX e Frontend (Pianificata)

**Obiettivo**: Adattare interfaccia grafica per Lancia Musa

### 5.1 Adattamento Client React
- [ ] Review configurazione `client/src/config/environment.ts`
- [ ] Aggiornamento URL WebSocket
- [ ] Configurazione parametri Musa
- [ ] Test modalità mock

### 5.2 Modello 3D Musa
- [ ] Creazione/acquisizione modello 3D Lancia Musa
  - Formato `.glb` per Three.js
  - Ottimizzazione poligoni per Raspberry Pi
- [ ] Sostituzione `client/public/panda.glb`
- [ ] Animazioni specifiche Musa (porte, luci)
- [ ] Integrazione con dati CAN

### 5.3 Layout e Responsive
- [ ] Adattamento layout per display target
  - Test 7", 10", 12.6"
  - Responsive 16:9 e 4:1
- [ ] Ottimizzazione leggibilità
- [ ] Temi personalizzabili (scuro/chiaro)
- [ ] Localizzazione italiana

### 5.4 Performance Frontend
- [ ] Ottimizzazione rendering Three.js
- [ ] Riduzione bundle size
- [ ] Lazy loading componenti
- [ ] Test performance su Pi 4B vs Pi 5

**Deliverable Fase 5**:
- 📦 UI completa e ottimizzata
- 📦 Modello 3D Musa integrato
- 📦 Temi personalizzabili
- 📦 Performance fluide su Pi 4B

**Data target**: Maggio 2026

---

## 🚀 Fase 6: Produzione e Release (Pianificata)

**Obiettivo**: Preparare il sistema per installazione definitiva

### 6.1 Installazione Hardware
- [ ] Selezione e acquisto display finale
- [ ] Progettazione supporto/case 3D
- [ ] Stampa 3D componenti
- [ ] Installazione definitiva su Musa

### 6.2 Documentazione Utente
- [ ] Guida installazione completa (`INSTALLATION.md`)
- [ ] Guida hardware completa (`HARDWARE.md`)
- [ ] Architettura sistema (`ARCHITECTURE.md`)
- [ ] Troubleshooting e FAQ
- [ ] Video tutorial installazione

### 6.3 Configurazione PM2
- [ ] Setup PM2 per avvio automatico
- [ ] Script power-saving
- [ ] Log rotation
- [ ] Monitoring e alerting

### 6.4 Release
- [ ] Tag versione 1.0.0
- [ ] Release notes
- [ ] Pacchetto distribuzione
- [ ] Pubblicazione immagine Raspberry Pi (opzionale)

**Deliverable Fase 6**:
- 📦 Sistema installato e funzionante su Musa
- 📦 Documentazione completa
- 📦 Video demo finale
- 📦 Release 1.0.0 su GitHub

**Data target**: Giugno 2026

---

## 🎯 Milestone Future (Wishlist)

### Post 1.0
- [ ] **Telemetria avanzata**: Log viaggi, statistiche consumo
- [ ] **Navigazione GPS**: Integrazione mappe
- [ ] **Retrocamera**: Visualizzazione rear camera
- [ ] **Sensori parcheggio**: Overlay grafico distanze
- [ ] **App mobile companion**: Controllo remoto e statistiche
- [ ] **Aggiornamenti OTA**: Update sistema via WiFi
- [ ] **Dashcam**: Registrazione video su eventi
- [ ] **Multi-veicolo**: Supporto altri modelli Fiat/Lancia

### Community
- [ ] Forum/Discord per utenti
- [ ] Database PID community-driven
- [ ] Template per altri veicoli
- [ ] Marketplace temi e modelli 3D

---

## 📈 Metriche Progetto

### Commit Goal
- Fase 1: ~10 commit ✅ (10/10)
- Fase 2: ~30 commit 🔄 (0/30)
- Fase 3: ~15 commit 📋 (0/15)
- Fase 4: ~20 commit 📋 (0/20)
- Fase 5: ~20 commit 📋 (0/20)
- Fase 6: ~10 commit 📋 (0/10)

**Target totale**: ~105 commit per v1.0

### Documentazione Goal
- [x] README.md
- [x] ROADMAP.md
- [x] docs/migration-notes.md
- [x] HARDWARE.md
- [x] sceltaHARDWARE.md
- [x] docs/power-management.md
- [ ] INSTALLATION.md
- [ ] ARCHITECTURE.md
- [ ] docs/musa-specs.md
- [ ] docs/can-bus-mapping.md
- [ ] docs/testing-report.md

**Target**: 11 documenti principali (6/11 completati)

---

## 🔄 Aggiornamenti

### 11 Dicembre 2025
- ✅ Inizializzazione progetto completata
- ✅ Struttura repository creata
- ✅ Documentazione base scritta
- ✅ Analisi Cyberpandino completata
- 🎯 Prossimo step: Importazione codice base

---

**Nota**: Questa roadmap è un documento vivo e verrà aggiornata regolarmente durante lo sviluppo del progetto.

**Ultimo aggiornamento**: 11 Dicembre 2025
