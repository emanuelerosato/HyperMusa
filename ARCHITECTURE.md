# 🏗️ Architettura Sistema HyperMusa

> **Nota**: Questo documento è in fase di sviluppo e verrà completato durante la Fase 2 (Migrazione Core).

---

## 📋 Overview

HyperMusa è un sistema di quadro strumenti digitale per Lancia Musa 2009 basato su:
- **Frontend**: React 18 + TypeScript + Three.js
- **Backend**: Node.js + CAN-Bus nativo
- **Hardware**: Raspberry Pi 4B/5 + Display touch
- **Comunicazione**: CAN-Bus ISO 15765-4

---

## 🎨 Stack Tecnologico

### Frontend (Client)
```
client/
├── React 18              → Framework UI
├── TypeScript            → Type safety
├── Vite                  → Build tool e dev server
├── Three.js              → Rendering 3D modello Musa
├── Socket.IO Client      → Real-time data dal backend
├── Valtio                → State management
└── SCSS                  → Styling
```

**Caratteristiche**:
- Dashboard 3D interattiva con modello Lancia Musa
- Visualizzazione real-time dati CAN-Bus
- Modalità demo per sviluppo senza hardware
- Responsive design per vari display

---

### Backend (Server)
```
server/
├── Node.js 20 LTS        → Runtime
├── Socket.IO Server      → WebSocket real-time
├── socketcan             → Interfaccia CAN-Bus nativa *(da implementare)*
├── ads1x15               → Sensore carburante (opzionale)
├── w1-temperature        → Sensore temperatura (opzionale)
└── PM2                   → Process manager
```

**Servizi principali** *(da adattare per Musa)*:
- `MusaCANService.js` - Comunicazione CAN-Bus nativo
- `PIDParserService.js` - Parser PID ISO 15765-4
- `WebSocketService.js` - Push dati al frontend
- `MonitoringService.js` - Health check e logging

---

### Desktop Wrapper
```
main.js
└── Electron 36           → Wrapper desktop per kiosk mode
```

**Funzioni**:
- Avvio fullscreen su Raspberry Pi
- Gestione lifecycle applicazione
- Integrazione con sistema operativo

---

## 🔌 Architettura Hardware

### Schema Generale
```
Lancia Musa 2009
    │
    ├─→ OBD2 (pin 16)
    │       │
    │       ├─→ CAN-H (pin 6)  ──┐
    │       └─→ CAN-L (pin 14) ──┤
    │                             │
    │                             ├─→ MCP2515 (Interfaccia CAN)
    │                             │        │
    │                             │        └─→ SPI → Raspberry Pi GPIO
    │
    └─→ 12V Batteria (pin 16)
            │
            ├─→ [FUSIBILE 2A] → DC-DC 12V→5V → Raspberry Pi
            └─→ [FUSIBILE 3A] → Display 12V
```

### Componenti Hardware
- **Raspberry Pi 4B/5** (4GB+ RAM)
- **Interfaccia CAN**: MCP2515 + TJA1050
- **Display**: 7-10" IPS touch (1280×720 o superiore)
- **Alimentazione**: DC-DC converter automotive 12V→5V (3A min)
- **Sensori opzionali**: GPS, temperatura, telecamera

Vedi [HARDWARE.md](HARDWARE.md) per dettagli completi *(in sviluppo)*.

---

## 🔄 Flusso Dati

### 1. Lettura CAN-Bus
```
Lancia Musa CAN-Bus (500 kbps)
    ↓
MCP2515 SPI Interface
    ↓
Raspberry Pi (socketcan0)
    ↓
MusaCANService.js
    ↓
PIDParserService.js (conversione frame → valori)
```

### 2. Elaborazione Backend
```
PIDParserService.js
    ↓
MonitoringService.js (aggregazione dati)
    ↓
WebSocketService.js (push real-time)
```

### 3. Visualizzazione Frontend
```
Socket.IO Client (React)
    ↓
Valtio Store (state management)
    ↓
React Components
    ├─→ Dashboard 2D (gauges, spie)
    └─→ Dashboard 3D (modello Musa Three.js)
    ↓
Electron Window (fullscreen)
    ↓
Display
```

---

## 🛠️ Differenze vs Cyberpandino

| Componente | Cyberpandino (Panda 141) | HyperMusa (Musa 2009) |
|------------|--------------------------|------------------------|
| **Interfaccia OBD** | ELM327 USB (K-Line seriale) | MCP2515 SPI (CAN nativo) |
| **Protocollo** | ISO 9141-2 (38400 bps) | ISO 15765-4 (500 kbps) |
| **Backend Comunicazione** | `serialport` | `socketcan` |
| **GPIO per Spie** | 13× optoaccoppiatori PC817 | Non necessari (spie via CAN) |
| **Sensori Esterni** | DS18B20, ADS1115 (essenziali) | Opzionali (dati già su CAN) |

### Vantaggi Architettura Musa
✅ **CAN nativo**: Latenza inferiore, più dati disponibili
✅ **No GPIO**: Installazione più semplice, meno cablaggio
✅ **Diagnostica avanzata**: DTC (Diagnostic Trouble Codes) via CAN
✅ **Body Computer integrato**: Stato porte, luci, sensori già digitalizzati

### Svantaggi
❌ **Complessità CAN**: Reverse engineering PID custom necessario
❌ **Frame multipli**: Gestione flow control CAN più complessa
❌ **Hardware specifico**: Richiede interfaccia CAN dedicata (MCP2515)

---

## 🔐 Sicurezza e Performance

### Sicurezza
- **Non eseguire come root**: Utente `pi` con gruppo `dialout`
- **Fusibili hardware**: Protezione da cortocircuiti
- **Shutdown controllato**: Script ignition per evitare corruzione SD
- **Rate limiting**: Protezione da flood CAN-Bus

### Performance
- **Latenza target**: <50ms lettura CAN → frontend
- **Frame rate**: 30 FPS modello 3D
- **RAM utilizzata**: ~400-600MB (Raspberry Pi 4B)
- **Boot time**: ~30s (ottimizzabile a ~20s)

---

## 📁 Struttura File Principali

```
HyperMusa/
├── client/                      → Frontend React
│   ├── src/
│   │   ├── components/          → Componenti UI
│   │   ├── routes/
│   │   │   └── Cockpit/         → Dashboard principale
│   │   ├── services/
│   │   │   └── WebSocketService.ts
│   │   ├── store/               → State Valtio
│   │   └── config/
│   │       └── environment.ts   → Configurazione client
│   ├── public/
│   │   └── musa.glb             → Modello 3D Musa *(da creare)*
│   └── package.json
│
├── server/                      → Backend Node.js
│   ├── services/
│   │   ├── MusaCANService.js    → Interfaccia CAN-Bus *(da implementare)*
│   │   ├── PIDParserService.js  → Parser ISO 15765-4 *(da adattare)*
│   │   ├── WebSocketService.js
│   │   └── MonitoringService.js
│   ├── config/
│   │   ├── can-bus.js           → Config CAN-Bus *(da creare)*
│   │   └── musa-pid-mapping.js  → PID Musa *(da mappare)*
│   ├── scripts/
│   │   ├── low-power.sh         → Power-saving
│   │   └── wake.sh              → Risveglio
│   ├── ecosystem.config.js      → PM2 config
│   └── package.json
│
├── docs/                        → Documentazione
│   ├── migration-notes.md
│   ├── musa-specs.md            → *(da creare)*
│   └── can-bus-mapping.md       → *(da creare)*
│
├── hardware/                    → Schemi e modelli
│   ├── schematics/              → Schemi elettrici
│   └── 3d-models/               → Case e supporti
│
├── main.js                      → Electron wrapper
├── package.json                 → Scripts root
├── README.md
├── ROADMAP.md
├── HARDWARE.md                  → *(da completare)*
├── INSTALLATION.md              → *(da creare)*
└── ARCHITECTURE.md              → *(questo file)*
```

---

## 🔮 Prossimi Passi

### Fase 2: Implementazione (In corso)
1. Importare codice Cyberpandino
2. Implementare `MusaCANService.js`
3. Adattare `PIDParserService.js` per ISO 15765-4
4. Creare configurazione CAN-Bus
5. Test modalità demo

Vedi [ROADMAP.md](ROADMAP.md) per timeline completa.

---

**Ultimo aggiornamento**: 11 Dicembre 2025
**Status**: Documento in sviluppo (Fase 1 completata)
**Prossimo aggiornamento**: Durante implementazione Fase 2
