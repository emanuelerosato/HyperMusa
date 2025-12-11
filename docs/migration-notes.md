# Note di Migrazione da Cyberpandino a HyperMusa

## 📋 Overview

Questo documento traccia le differenze tecniche tra il progetto Cyberpandino (Fiat Panda 141) e HyperMusa (Lancia Musa 2009), e le modifiche necessarie per l'adattamento.

---

## 🚗 Differenze Veicolo

### Fiat Panda 141 (Cyberpandino)
- **Anni**: 1980-2003
- **CAN-Bus**: Non nativo, sensori analogici
- **Protocollo OBD**: ISO 9141-2 (K-Line) e ISO 14230-4 (KWP2000)
- **Centralina**: Magneti Marelli IAW 4AF
- **Baudrate**: 38400 bps
- **Porta seriale**: `/dev/ttyUSB0` (ELM327 USB)
- **Spie**: Rilevate tramite optoaccoppiatori PC817 su GPIO
- **Complessità**: Bassa
- **Sensori**: Analogici esterni (DS18B20, ADS1115)

### Lancia Musa (HyperMusa)
- **Anni**: 2007-2012 (target: 2009)
- **CAN-Bus**: Nativo ISO 15765-4 (CAN 2.0B)
- **Protocollo OBD**: ISO 15765-4 (CAN-Bus)
- **Body Computer**: Integrato Fiat/Lancia
- **Baudrate CAN**: 500 kbps (standard Fiat/Lancia)
- **Connettore**: OBD2 standard 16 pin
- **Spie**: Disponibili via CAN-Bus (no GPIO necessari)
- **Complessità**: Media-Alta
- **Sensori**: Digitali su CAN-Bus

---

## 🔧 Adattamenti Necessari

### 1. Interfaccia CAN-Bus

#### Cyberpandino
- **Hardware**: Adattatore ELM327 USB per protocollo K-Line
- **Comunicazione**: Seriale USB (`/dev/ttyUSB0`)
- **Libreria**: `serialport` (Node.js)
- **Sensori**: Lettura GPIO per spie + sensori esterni analogici

#### HyperMusa
- **Hardware**: Interfaccia CAN nativa (MCP2515 o ELM327 compatibile CAN)
- **Comunicazione**: CAN-Bus nativo ISO 15765-4
- **Libreria**: `socketcan` o `node-can` (Node.js)
- **Sensori**: Lettura diretta da CAN-Bus (PID standard + custom Fiat/Lancia)

**Modifiche richieste**:
- Sostituire `OBDCommunicationService.js` con comunicazione CAN nativa
- Implementare parser PID ISO 15765-4
- Mappare PID specifici Lancia Musa 2009

---

### 2. PID OBD2

#### PID Standard Supportati (ISO 15765-4)

| Parametro | PID | Descrizione |
|-----------|-----|-------------|
| Velocità | `0x0D` | Velocità veicolo (km/h) |
| RPM | `0x0C` | Giri motore (rpm) |
| Temperatura motore | `0x05` | Temperatura liquido raffreddamento (°C) |
| Pressione turbo | `0x0B` | MAP Sensor (kPa) |
| Posizione acceleratore | `0x11` | Throttle position (%) |
| Livello carburante | `0x2F` | Livello serbatoio (%) |
| Tensione batteria | `0x42` | Tensione modulo controllo (V) |
| Distanza percorsa | `0x31` | Distanza da reset MIL (km) |
| Tempo motore acceso | `0x1F` | Tempo dall'avvio motore (s) |

#### PID Custom Fiat/Lancia (da verificare su Musa 2009)

Questi PID potrebbero essere specifici del Body Computer Fiat/Lancia e richiedono test su veicolo reale:

| Parametro | PID Possibile | Note |
|-----------|---------------|------|
| Spie cruscotto | `0x65` o custom | Da verificare con tool diagnostici |
| Stato porte | Custom | Richiede reverse engineering CAN |
| Luci attive | Custom | Richiede reverse engineering CAN |
| Trip computer | Custom | Potrebbe essere su CAN separato |

**Azioni richieste**:
1. Sniffing CAN-Bus su Musa 2009 con tool diagnostici
2. Identificare frame CAN per spie e sensori
3. Mappare PID custom Fiat/Lancia
4. Testare disponibilità servizi su CAN

---

### 3. Architettura Software

#### Moduli da Modificare

**Priorità Alta**:
- `server/services/OBDCommunicationService.js`
  - Sostituire comunicazione seriale con CAN-Bus
  - Implementare parser ISO 15765-4
  - Aggiungere gestione frame CAN multi-byte

- `server/services/PIDParserService.js`
  - Aggiungere PID ISO 15765-4
  - Implementare conversioni unità CAN
  - Gestire PID custom Fiat/Lancia

- `server/config/gpio-mapping.js`
  - Rimuovere o rendere opzionali i GPIO per spie (disponibili via CAN)
  - Mantenere GPIO solo per sensori esterni (se necessari)

**Priorità Media**:
- `server/services/GPIOService.js`
  - Rendere opzionale (GPIO non più necessari per spie base)
  - Mantenere per sensori custom esterni

- `server/services/IgnitionService.js`
  - Adattare per rilevare accensione da CAN-Bus invece che GPIO

- `client/src/config/environment.ts`
  - Aggiungere configurazione CAN-Bus
  - Parametri specifici Musa

**Priorità Bassa**:
- `client/src/components/*` - UI generalmente compatibile
- `client/public/panda.glb` - Sostituire con modello 3D Musa
- Display layout - Adattare dimensioni se necessario

---

### 4. Dimensioni Display

#### Cyberpandino
- **Display**: 12.6" ultra-wide
- **Risoluzione**: 1920×480 (4:1 aspect ratio)
- **Montaggio**: Sostituzione quadro Panda 141

#### HyperMusa
- **Opzioni**:
  - 7-10" standard (più facile da montare in Musa)
  - 12.6" ultra-wide (richiede modifica cruscotto)
- **Risoluzione**: 1280×720 o 1920×1080 (16:9 più comune)
- **Montaggio**: Da valutare spazio disponibile cruscotto Musa

**Modifiche UI**:
- Adattare layout per aspect ratio 16:9 se necessario
- Responsive design per varie risoluzioni
- Testare leggibilità su display più piccoli

---

### 5. Alimentazione

#### Cyberpandino
- Convertitore DC-DC 12V → 5V (3A per Pi 4B)
- Fusibili separati per Pi, Display, GPIO

#### HyperMusa
- Identico (sistema elettrico 12V standard Fiat)
- Eventuale integrazione con Body Computer per power management
- Possibile alimentazione diretta da OBD2 (pin 16: 12V battery)

**Vantaggio**: Musa ha gestione energetica più avanzata, possibile sfruttarla per auto-shutdown.

---

## 🔍 Stack Tecnologico Cyberpandino (da adattare)

### Frontend
- **Framework**: React 18
- **Linguaggio**: TypeScript
- **Build**: Vite
- **3D**: Three.js (modello Panda interattivo)
- **State**: Valtio
- **Socket**: Socket.IO Client
- **Styling**: SCSS

### Backend
- **Runtime**: Node.js 18+
- **Socket**: Socket.IO Server
- **Seriale**: `serialport` (per ELM327)
- **GPIO**: `onoff` (per optoaccoppiatori)
- **Sensori**: `ads1x15`, `w1-temperature`
- **Process Manager**: PM2

### Desktop
- **Wrapper**: Electron 36
- **Target**: Raspberry Pi OS

### Hardware
- **SBC**: Raspberry Pi 4B/5
- **Display**: 12.6" IPS 1920×480
- **OBD**: ELM327 USB
- **Optoaccoppiatori**: PC817 × 13
- **Sensori**: DS18B20, ADS1115

---

## 📝 Modifiche Codice Previste

### Fase 1: Setup ✅
- [x] Analisi struttura Cyberpandino
- [x] Inizializzazione repository HyperMusa
- [x] Documentazione base

### Fase 2: Backend CAN-Bus 🔄
- [ ] Implementare `MusaCANService.js` (sostituzione OBDCommunicationService)
- [ ] Implementare parser PID ISO 15765-4
- [ ] Mappare PID Lancia Musa
- [ ] Test comunicazione CAN-Bus reale
- [ ] Gestione errori e reconnessione CAN

### Fase 3: Testing
- [ ] Modalità demo con dati simulati Musa
- [ ] Test su veicolo reale (sniffing CAN)
- [ ] Validazione PID custom
- [ ] Benchmark performance

### Fase 4: UI/UX
- [ ] Modello 3D Lancia Musa
- [ ] Adattamento layout per display target
- [ ] Animazioni specifiche Musa
- [ ] Temi personalizzabili

---

## 🛠️ Tool Necessari per Sviluppo

### Software
- **CAN Sniffer**: `can-utils` per Linux/Raspberry
- **OBD Scanner**: Torque Pro, OBD Fusion (per reverse engineering PID)
- **Logic Analyzer**: PulseView + Saleae (per debug CAN)

### Hardware
- **Interfaccia CAN**: MCP2515 + TJA1050 (per Raspberry Pi)
- **OBD2 Cable**: Cavo diagnostico con breakout CAN-H/CAN-L
- **Multimetro**: Per misurazioni tensione CAN-Bus

---

## 🚨 Rischi e Criticità

### Rischi Tecnici
1. **PID custom non documentati**: Potrebbe servire reverse engineering estensivo
2. **CAN-Bus multipli**: Musa potrebbe avere CAN comfort/powertrain separati
3. **Crittografia CAN**: Alcuni frame potrebbero essere protetti
4. **Incompatibilità hardware**: Possibili varianti Musa con CAN diversi

### Mitigazioni
- Test estensivi su veicolo reale prima dello sviluppo completo
- Modalità demo sempre funzionante per sviluppo offline
- Documentazione accurata di ogni PID scoperto
- Community Fiat/Lancia per condivisione conoscenze

---

## 📚 Risorse Utili

### Documentazione Tecnica
- ISO 15765-4: Diagnostica via CAN (acquisto standard)
- Manuale officina Lancia Musa: Schemi elettrici
- Forum Fiat/Lancia: Reverse engineering CAN

### Tool Open-Source
- `can-utils`: Suite tool CAN per Linux
- `python-can`: Libreria Python per CAN-Bus
- `socketcan`: Kernel Linux CAN interface

### Community
- OBD2 Wiki: Database PID veicoli
- Forum Raspberry Pi: Progetti automotive
- GitHub: Progetti CAN-Bus open-source

---

## ✅ Checklist Migrazione

### Pre-Sviluppo
- [x] Analisi Cyberpandino completata
- [x] Documentazione differenze veicoli
- [ ] Acquisizione interfaccia CAN hardware
- [ ] Setup ambiente sviluppo CAN

### Sviluppo
- [ ] Implementazione backend CAN
- [ ] Test unitari servizi CAN
- [ ] Modalità demo funzionante
- [ ] Test integrazione completa

### Testing
- [ ] Sniffing CAN su Musa reale
- [ ] Mappatura PID completa
- [ ] Validazione letture sensori
- [ ] Test stress e affidabilità

### Produzione
- [ ] Installazione su Raspberry Pi
- [ ] Test su veicolo (statico)
- [ ] Test su veicolo (in movimento)
- [ ] Documentazione finale utente

---

**Ultimo aggiornamento**: 11 Dicembre 2025
**Status**: Documento in aggiornamento continuo durante sviluppo
