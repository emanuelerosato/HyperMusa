# 🔧 Hardware HyperMusa - Lista Componenti

Guida completa ai componenti hardware necessari per realizzare HyperMusa, il quadro strumenti digitale per Lancia Musa 2009.

> ⚠️ **DISCLAIMER**: Questa lista è fornita a scopo informativo. Acquista e installa hardware solo se hai competenze tecniche adeguate. Vedi [Disclaimer](#️-avvertenze-e-note-legali) per maggiori informazioni.

---

## 📊 Budget Totale Stimato

| Configurazione | Budget | Descrizione |
|----------------|--------|-------------|
| **Base** | ~250€ | Funzionalità minime, display piccolo, Pi 4 |
| **Consigliata** | ~400€ | Performance ottimali, display medio, Pi 5 |
| **Premium** | ~600€ | Massime prestazioni, display bar automotive, accessori |

---

## 🎯 Componenti Principali

### 1. Computer - Raspberry Pi

#### ✅ Opzione A: Raspberry Pi 5 4GB (CONSIGLIATA)

**Descrizione**: CPU Cortex-A76 quad-core 2.4GHz, 2-3x più veloce del Pi 4

**Specifiche**:
- **CPU**: Broadcom BCM2712, Cortex-A76 quad-core 64-bit @ 2.4GHz
- **RAM**: 4GB LPDDR4X-4267 SDRAM
- **GPU**: VideoCore VII, supporto dual 4K @ 60fps
- **Connettività**: Wi-Fi 6 dual-band, Bluetooth 5.0 BLE
- **USB**: 2× USB 3.0, 2× USB 2.0
- **GPIO**: 40 pin compatibili con Pi 4
- **Display**: 2× micro-HDMI (fino a 4K @ 60Hz)
- **Alimentazione**: USB-C 5V 5A (27W raccomandati)

**Vantaggi**:
- ✅ Performance superiori per UI 3D Three.js (rendering fluido)
- ✅ Supporto dual 4K (utile per sviluppo multi-display)
- ✅ PCIe 2.0 nativo (espandibilità futura)
- ✅ Crittografia hardware accelerata

**Svantaggi**:
- ❌ Richiede alimentatore 5A dedicato (più complesso)
- ❌ Scalda di più (necessita ventola attiva)
- ❌ Costo superiore

**Prezzo**: ~75€

**Dove acquistare**:
- [Melopero](https://www.melopero.com/it/shop/boards/pi5/raspberry-pi-5-4gb/) - Distributore ufficiale Italia
- [Amazon.it](https://www.amazon.it/s?k=raspberry+pi+5+4gb) - Disponibilità immediata
- [RS Components](https://it.rs-online.com/) - Fornitore industriale

**Note**: Per Pi 5 serve alimentatore USB-C 5V/5A (27W) - NON riutilizzare alimentatori vecchi!

---

#### Opzione B: Raspberry Pi 4 Model B 4GB (BUDGET)

**Descrizione**: CPU Cortex-A72 quad-core 1.5GHz

**Specifiche**:
- **CPU**: Broadcom BCM2711, Cortex-A72 quad-core 64-bit @ 1.5GHz
- **RAM**: 4GB LPDDR4-3200 SDRAM
- **GPU**: VideoCore VI, supporto dual 4K @ 30fps
- **Connettività**: Wi-Fi 5 dual-band, Bluetooth 5.0
- **USB**: 2× USB 3.0, 2× USB 2.0
- **GPIO**: 40 pin
- **Display**: 2× micro-HDMI (fino a 4K @ 30Hz)
- **Alimentazione**: USB-C 5V 3A (15W)

**Vantaggi**:
- ✅ Prezzo inferiore
- ✅ Alimentazione più semplice (3A)
- ✅ Scalda meno
- ✅ Compatibilità accessori Pi 4

**Svantaggi**:
- ❌ Performance inferiori per UI 3D complesse
- ❌ Rendering Three.js meno fluido

**Prezzo**: ~55€

**Dove acquistare**:
- Amazon.it
- Melopero
- Kubii

**Note**: Sufficiente per HyperMusa ma UI meno fluida con animazioni 3D complesse

---

#### ❌ Da EVITARE: Raspberry Pi 3 e inferiori

**Motivo**: CPU troppo lenta per React + Three.js + Electron
- Raspberry Pi 3B+: ~1.4GHz quad-core (50% più lento del Pi 4)
- RAM limitata (1GB max)
- GPU VideoCore IV obsoleta

**Verdetto**: ❌ **NON COMPRARE** - Performance inaccettabili per HyperMusa

---

### 2. Interfaccia CAN-Bus (OBBLIGATORIA)

#### ✅ MCP2515 + TJA1050 CAN Bus Module (RACCOMANDATO)

**Descrizione**: Controller CAN standalone compatibile con protocollo ISO 15765-4

**Specifiche Tecniche**:
- **Controller**: Microchip MCP2515
  - Implementa protocollo CAN 2.0B
  - Interfaccia SPI (Serial Peripheral Interface)
  - Velocità CAN: 5 kbps - 1 Mbps (Musa usa 500 kbps)
  - Buffer TX: 3 buffer di trasmissione
  - Buffer RX: 2 buffer ricezione con filtri
- **Transceiver**: NXP TJA1050
  - Driver/ricevitore bus CAN
  - Conforme ISO 11898
  - Protezione cortocircuito
  - Modalità standby a basso consumo
- **Alimentazione**: 5V DC
- **Consumo**:
  - Attivo: ~50mA @ 5V
  - Standby: <10µA
- **Temperatura operativa**: -40°C a +85°C (automotive grade)
- **Dimensioni**: ~44mm × 26mm (PCB)

**Connessioni**:
- **CAN-H / CAN-L**: Terminali a vite per collegamento CAN-Bus veicolo
- **GPIO Header**: Pin 2.54mm pitch per Raspberry Pi
- **LED**: Indicatori TX/RX attività CAN

**Prezzo**: ~8-12€

**Dove acquistare**:
- [Battery Atom](https://www.batteryatom.it/prodotto/mcp2515-can-bus-modul-tja1050-transceiver-5v-arduino-raspberry-pi/) - 9.90€
- [AZ-Delivery](https://www.az-delivery.de/it/products/mcp2515-can-bus-modul) - 7.99€
- [Amazon.it](https://www.amazon.it/s?k=MCP2515+Raspberry+Pi) - 10-15€

**Nota importante**: Verifica che il modulo includa **ENTRAMBI** i chip:
- ✅ MCP2515 (controller)
- ✅ TJA1050 (transceiver)

Alcuni moduli economici hanno solo MCP2515 senza transceiver - **non funzionano!**

---

#### Opzione Premium: PiCAN 3 HAT

**Descrizione**: HAT (Hardware Attached on Top) dedicato per Raspberry Pi

**Specifiche**:
- Controller: MCP2515
- Transceiver: MCP2562FD (CAN-FD ready)
- Montaggio: Diretto su GPIO 40 pin
- Connettore: DB9 o terminali a vite
- Oscillatore: 16MHz cristallo esterno
- Protezione: Diodi TVS per protezione ESD

**Vantaggi**:
- ✅ Montaggio professionale diretto su Pi
- ✅ Più stabile (no cavi Dupont volanti)
- ✅ Supporto CAN-FD (futuro)
- ✅ Documentazione ufficiale ottima

**Svantaggi**:
- ❌ Costo 4x superiore
- ❌ Occupa tutti i GPIO (limita espansioni)

**Prezzo**: ~40€

**Dove acquistare**:
- [SK Pang Electronics](https://www.skpang.co.uk/products/pican-3-can-bus-board-for-raspberry-pi) - UK
- [Copperhill Technologies](https://copperhilltech.com/) - USA
- Amazon.de (disponibilità variabile)

**Raccomandazione**: MCP2515 standard è più che sufficiente per proof-of-concept. PiCAN 3 HAT per installazioni definitive.

---

### 3. Display Touch Screen

#### ✅ Opzione A: Display Bar 12.3" 1920×720 (STILE AUTOMOTIVE)

**Descrizione**: Display widescreen panoramico IPS, formato ultra-wide automotive

**Specifiche**:
- **Dimensioni**: 12.3 pollici diagonale
- **Risoluzione**: 1920×720 pixel (aspect ratio 8:3)
- **Tipo pannello**: IPS (In-Plane Switching)
  - Angoli di visione: 178° orizzontali/verticali
  - Contrasto: 1000:1
  - Colori: 16.7M (8-bit)
- **Luminosità**: 400-600 nits (leggibile in pieno sole)
- **Refresh rate**: 60Hz
- **Interfaccia video**:
  - HDMI (più comune)
  - MIPI DSI (alcuni modelli)
- **Touch**:
  - Capacitivo multi-touch (opzionale)
  - Interfaccia USB
- **Alimentazione**: 12V DC (3-5A secondo modello)
- **Dimensioni fisiche**: ~284mm × 75mm × 12mm
- **Temperatura operativa**: 0°C a +60°C

**Vantaggi**:
- ✅ Look professionale automotive (simile BMW/Audi/Tesla)
- ✅ Formato panoramico ideale per cruscotto
- ✅ Si integra perfettamente sopra volante Musa
- ✅ Alta leggibilità (alta luminosità)

**Svantaggi**:
- ❌ Difficile da trovare (principalmente fornitori cinesi)
- ❌ Tempi spedizione lunghi (2-4 settimane da Cina)
- ❌ Richiede adattamento case/supporto custom
- ❌ Verifica dimensioni cruscotto Musa prima di acquistare!

**Prezzo**: ~80-150€ (dipende da fornitore e specifiche)

**Dove acquistare**:
- [AliExpress](https://www.aliexpress.com/) - Cerca: "12.3 inch bar display 1920x720 automotive" o "stretch bar lcd 12.3"
- [Alibaba](https://www.alibaba.com/) - Per ordini all'ingrosso (MOQ 5-10 pezzi)
- eBay - Disponibilità occasionale

**Modelli consigliati**:
- "12.3 inch IPS LCD 1920×720 HDMI" (~100€)
- "Car Dashboard Display 12.3 Bar LCD" (~120€)

**⚠️ IMPORTANTE**: Misura con precisione lo spazio disponibile sul cruscotto Musa prima di ordinare!

**Template dimensioni**:
```
┌────────────────────────────────────┐
│  12.3" Display Bar (284mm × 75mm)  │
└────────────────────────────────────┘
Verifica fit su cruscotto con cartone/carta millimetrata!
```

---

#### Opzione B: Display Touch 10.1" 1920×1200 (EQUILIBRATO)

**Descrizione**: Display IPS standard 16:10, più facile da reperire

**Specifiche**:
- **Dimensioni**: 10.1 pollici
- **Risoluzione**: 1920×1200 pixel (WUXGA)
- **Tipo pannello**: IPS
- **Interfaccia**:
  - Video: HDMI
  - Touch: USB capacitivo 10-point multi-touch
- **Alimentazione**: USB-C (5V 2A) o DC 12V
- **Luminosità**: 300-400 nits
- **Dimensioni fisiche**: ~223mm × 139mm × 8mm

**Vantaggi**:
- ✅ Facile da trovare (Amazon.it)
- ✅ Prezzo accessibile
- ✅ Touch capacitivo multi-point
- ✅ Risoluzione elevata
- ✅ Plug-and-play con Raspberry Pi

**Svantaggi**:
- ❌ Formato meno "automotive"
- ❌ Dimensioni standard (meno integrato)

**Prezzo**: ~60-90€

**Dove acquistare**:
- [Amazon.it](https://www.amazon.it/s?k=display+touch+10+pollici+raspberry) - Cerca: "monitor touch 10.1 pollici HDMI"
- [Beetronics](https://www.beetronics.it/) - Fornitore italiano elettronica
- eBay

**Modelli consigliati**:
- "UPERFECT 10.1 Portable Monitor" (~75€)
- "ELECROW 10.1 Inch Touchscreen" (~65€)
- "Waveshare 10.1inch HDMI LCD" (~80€)

---

#### Opzione C: Display Touch 7" 1024×600 (BUDGET)

**Descrizione**: Display ufficiale Raspberry Pi o compatibile

**Specifiche**:
- **Dimensioni**: 7 pollici
- **Risoluzione**: 1024×600 pixel
- **Interfaccia**:
  - DSI (Display Serial Interface) diretto Pi
  - O HDMI (modelli compatibili)
- **Touch**: Capacitivo
- **Alimentazione**: 5V tramite GPIO
- **Dimensioni fisiche**: ~194mm × 110mm × 20mm

**Vantaggi**:
- ✅ Prezzo economico
- ✅ Integrazione perfetta con Pi (DSI)
- ✅ Documentazione ufficiale
- ✅ Disponibilità immediata

**Svantaggi**:
- ❌ Risoluzione limitata (UI meno dettagliata)
- ❌ Dimensioni ridotte
- ❌ Meno "impressive" per quadro auto

**Prezzo**: ~35-50€

**Dove acquistare**:
- [Amazon.it](https://www.amazon.it/s?k=raspberry+pi+7+display) - Display ufficiale ~50€
- [Melopero](https://www.melopero.com/) - Display ufficiale + compatibili
- [Kubii](https://www.kubii.it/) - Distributore ufficiale

**Raccomandazione**: Solo per budget limitati o proof-of-concept rapidi

---

### 🎯 Raccomandazione Display

| Scenario | Display Consigliato | Motivo |
|----------|-------------------|---------|
| **Installazione Definitiva** | 12.3" Bar 1920×720 | Look professionale automotive |
| **Proof-of-Concept** | 10.1" 1920×1200 | Equilibrio prezzo/prestazioni |
| **Budget Limitato** | 7" 1024×600 | Economico per test |
| **Sviluppo Software** | 10.1" 1920×1200 | Risoluzione adeguata, facile debug |

---

### 4. Connettività Veicolo

#### Cavo Diagnostico OBD2 16 Pin

**Descrizione**: Cavo standard OBD2 maschio per collegamento porta diagnostica Musa

**Specifiche**:
- **Connettore**: J1962 standard 16 pin maschio
- **Cablaggio**:
  - Pin 4, 5: Ground (GND)
  - Pin 6: CAN-H (High)
  - Pin 14: CAN-L (Low)
  - Pin 16: +12V batteria (sempre alimentato)
- **Lunghezza**: 30-50 cm
- **Tipo**: Splitter Y (mantiene porta OBD2 libera per diagnosi)

**Tipologie**:

**A) Cavo OBD2 Splitter Y** (RACCOMANDATO)
- 1 ingresso maschio OBD2 → 2 uscite femmine
- Permette di collegare HyperMusa + scanner diagnostico contemporaneamente
- Prezzo: ~12-18€

**B) Cavo OBD2 con Breakout Board**
- Connettore OBD2 → board con terminali a vite per ogni pin
- Più flessibile per test
- Prezzo: ~15-20€

**Prezzo**: ~8-20€

**Dove acquistare**:
- [Amazon.it](https://www.amazon.it/s?k=cavo+OBD2+splitter) - Cerca: "OBD2 splitter cable" o "OBD2 breakout board"
- eBay - Molte opzioni economiche
- [AliExpress](https://www.aliexpress.com/) - Più economico ma spedizione lenta

**Modelli consigliati**:
- "OBD2 16 Pin Y Splitter Cable" (~12€)
- "OBD2 Breakout Board 16 Pin to Terminal" (~15€)

---

#### Cavi Dupont per MCP2515 → Raspberry Pi

**Descrizione**: Cavi jumper per collegare MCP2515 a GPIO Raspberry Pi

**Specifiche**:
- **Tipo**: Femmina-Femmina (F-F)
- **Lunghezza**: 10-20 cm
- **Sezione**: 22-24 AWG
- **Quantità necessaria**: 7 cavi (VCC, GND, SCK, MOSI, MISO, CS, INT)

**Prezzo**: ~3-5€ (kit 40 pezzi)

**Dove acquistare**:
- [Amazon.it](https://www.amazon.it/s?k=cavi+dupont+femmina) - Kit 40pz ~5€
- [AZ-Delivery](https://www.az-delivery.de/it/) - Kit assortiti
- Qualsiasi negozio elettronica (Futura Elettronica, Robots Italy)

**Raccomandazione**: Compra kit assortito (40-120 pezzi) - utile per debug e test

---

### 5. Alimentazione

#### ✅ Opzione A: Convertitore DC-DC 12V → 5V 5A USB-C (Pi 5)

**Descrizione**: Alimentatore automotive 12V con uscita USB-C Power Delivery 27W

**Specifiche**:
- **Input**:
  - Tensione: 12-24V DC (compatibile 12V auto)
  - Protezione inversione polarità
  - Filtro EMI (anti-interferenze)
- **Output**:
  - Tensione: 5V DC
  - Corrente: 5A continui (max 6A picco)
  - Potenza: 25W nominali, 27-30W picco
  - Connettore: USB-C con Power Delivery
- **Protezioni**:
  - ✅ Sovratensione (OVP)
  - ✅ Sovracorrente (OCP)
  - ✅ Cortocircuito (SCP)
  - ✅ Surriscaldamento (OTP)
  - ✅ Inversione polarità
- **Efficienza**: >85% (tipico ~90%)
- **Temperatura operativa**: -20°C a +60°C
- **Dimensioni**: ~50mm × 30mm × 20mm

**Prezzo**: ~15-25€

**Dove acquistare**:
- [Amazon.it](https://www.amazon.it/s?k=convertitore+12v+5v+5a+usb-c) - Cerca: "12V to 5V 5A USB-C car charger" o "DC-DC converter 5V 5A"
- eBay
- AliExpress (~10€ ma spedizione lenta)

**Modelli consigliati**:
- "DROK Buck Converter 12V to 5V 5A USB-C" (~18€)
- "Cigarette Lighter USB-C 5A PD Car Charger" (~15€)

**⚠️ IMPORTANTE per Pi 5**:
- Raspberry Pi 5 richiede **minimo 5A** a 5V (25W)
- Sotto carico 3D può arrivare a 27W
- NON usare convertitori da 3A (Pi 5 potrebbe riavviarsi)

---

#### Opzione B: Convertitore DC-DC 12V → 5V 3A USB-C (Pi 4)

**Descrizione**: Alimentatore automotive standard per Raspberry Pi 4

**Specifiche**:
- **Input**: 12-24V DC
- **Output**: 5V DC 3A (15W)
- **Connettore**: USB-C
- **Protezioni**: OVP, OCP, SCP

**Prezzo**: ~10-15€

**Dove acquistare**:
- Amazon.it - Cerca: "12V to 5V 3A USB-C"
- Qualsiasi negozio accessori auto

**Nota**: Sufficiente per Raspberry Pi 4 ma NON per Pi 5

---

#### Cablaggio Alimentazione Veicolo

**Come Prelevare 12V dalla Musa**:

**Opzione 1: Porta OBD2 (FACILE)**
- Pin 16 OBD2 = +12V batteria (sempre alimentato)
- Pin 4 o 5 OBD2 = GND
- ✅ Pro: Installazione rapida, nessuna modifica
- ❌ Contro: Occupa porta OBD2 (usare splitter)

**Opzione 2: Scatola Fusibili (PROFESSIONALE)**
- Sotto cofano lato sinistro
- Derivare da fusibile esistente con spinotto Y
- Fusibili consigliati:
  - F15 (10A - Quadro strumenti): Si accende/spegne con chiave
  - F16 (7.5A - Accessori): Sempre alimentato
- ✅ Pro: Installazione pulita, porta OBD2 libera
- ❌ Contro: Richiede smontaggio cofano

**Opzione 3: Batteria Diretta (INSTALLAZIONE DEFINITIVA)**
- Collegamento diretto al polo positivo batteria
- ⚠️ **OBBLIGATORIO**: Fusibile 5A in linea max 10cm dal terminale
- ✅ Pro: Alimentazione stabile, max corrente disponibile
- ❌ Contro: Scarica batteria se non gestito auto-shutdown

**Schema Cablaggio Consigliato**:
```
Batteria 12V Veicolo (o OBD2 pin 16)
    │
    ├─→ [FUSIBILE 3A] → Convertitore DC-DC 12V→5V → Raspberry Pi
    │
    └─→ [FUSIBILE 2A] → Display 12V (se display usa 12V)
```

**⚡ IMPORTANTE**: Usa **SEMPRE** fusibili separati per ogni componente!

---

#### Accessorio: Power Bank Backup (OPZIONALE)

**Descrizione**: Power bank USB-C per shutdown sicuro quando si toglie la chiave

**Specifiche**:
- Capacità: 10.000mAh minimo
- Output: USB-C 3A
- Funzione UPS (passa automaticamente a batteria quando manca alimentazione)

**Prezzo**: ~20-30€

**Dove acquistare**: Amazon.it

**Utilizzo**:
- Collega power bank tra convertitore e Raspberry Pi
- Quando togli chiave, power bank alimenta Pi per ~5-10 minuti
- Script `low-power.sh` esegue shutdown controllato
- Evita corruzione SD card

**Raccomandazione**: Utile per installazioni definitive, non necessario per proof-of-concept

---

### 6. Storage

#### ✅ MicroSD Card 64GB Classe A2 (OBBLIGATORIA)

**Descrizione**: Scheda microSD ad alta velocità per sistema operativo Raspberry Pi OS

**Specifiche Richieste**:
- **Capacità**:
  - Minimo: 32GB
  - Consigliato: 64GB
  - Ideale: 128GB (per log estesi e dashcam futura)
- **Classe Applicazione**: **A2** (Application Performance Class 2)
  - IOPS casuali lettura: ≥4000
  - IOPS casuali scrittura: ≥2000
- **Classe Velocità**:
  - **U3** (UHS Speed Class 3): min 30MB/s scrittura
  - **V30** (Video Speed Class 30): min 30MB/s scrittura continua
- **Bus Interface**: UHS-I (Ultra High Speed)
- **Velocità Reali**:
  - Lettura sequenziale: 90-170 MB/s
  - Scrittura sequenziale: 60-90 MB/s

**Marche Consigliate** (ordine preferenza):
1. **SanDisk Extreme PRO** (migliore)
   - A2, U3, V30, 170MB/s lettura
   - Garanzia lifetime
   - Prezzo 64GB: ~18-22€
2. **Samsung EVO Plus**
   - A2, U3, V30, 130MB/s lettura
   - Garanzia 10 anni
   - Prezzo 64GB: ~12-18€
3. **Kingston Canvas Go! Plus**
   - A2, U3, V30, 170MB/s lettura
   - Garanzia lifetime
   - Prezzo 64GB: ~15-20€

**⚠️ DA EVITARE**:
- ❌ SD card no-brand economiche (<5€)
- ❌ Classe 10 vecchia generazione (senza A2)
- ❌ Capacità <32GB

**Motivo**: SD card scadenti causano:
- Corruzione file system
- Boot lenti (~2-3 minuti invece di 20-30 secondi)
- Crash random applicazione
- Durata ridotta (pochi mesi invece di anni)

**Prezzo**: ~12-22€ (dipende da capacità e marca)

**Dove acquistare**:
- [Amazon.it](https://www.amazon.it/s?k=sandisk+extreme+64gb+a2) - Verifica che sia venduta da Amazon (no marketplace)
- MediaWorld - Negozi fisici
- Unieuro - Negozi fisici
- Saturn - Negozi fisici

**🎯 RACCOMANDAZIONE**: SanDisk Extreme PRO 64GB A2 (~20€) - Best buy qualità/prezzo

---

### 7. Sensori Aggiuntivi (OPZIONALI)

#### GPS Module USB (per Navigazione)

**Descrizione**: Ricevitore GPS USB con chip u-blox per posizionamento satellitare

**Specifiche**:
- **Chipset**: u-blox M8N o superiore
  - 72 canali
  - GPS + GLONASS + Galileo (multi-GNSS)
  - Precisione: ~2.5m CEP
- **Interfaccia**: USB (serial UART)
- **Protocollo**: NMEA 0183
- **Frequenza aggiornamento**: 1-10Hz (configurabile)
- **Alimentazione**: 5V via USB (50-100mA)
- **Antenna**: Integrata o esterna (SMA connector)
- **Time to First Fix**:
  - Cold start: <30s
  - Warm start: <3s
  - Hot start: <1s

**Prezzo**: ~15-35€

**Dove acquistare**:
- [Amazon.it](https://www.amazon.it/s?k=gps+usb+u-blox) - Cerca: "USB GPS receiver u-blox" o "VK-162 GPS"
- [AliExpress](https://www.aliexpress.com/) - Modelli economici ~10€

**Modelli consigliati**:
- **VK-162 u-blox 7** (~15€) - Economico entry-level
- **Beitian BN-880 u-blox M8N** (~25€) - Precision + compass
- **Navilock NL-8012U u-blox M9** (~35€) - High precision

**Utilizzo**: Plug-and-play su Raspberry Pi, device `/dev/ttyUSB0` o `/dev/ttyACM0`

**Funzionalità HyperMusa**:
- Velocità GPS (alternativa a CAN-Bus)
- Navigazione integrata (implementazione futura)
- Trip computer con tracciamento percorsi
- Geofencing

---

#### Sensore Temperatura/Umidità DHT22 (Abitacolo)

**Descrizione**: Sensore digitale temperatura e umidità per monitoraggio clima abitacolo

**Specifiche**:
- **Range Temperatura**: -40°C a +80°C
  - Precisione: ±0.5°C
- **Range Umidità**: 0-100% RH
  - Precisione: ±2-5% RH
- **Interfaccia**: GPIO single-wire
- **Alimentazione**: 3.3-5V DC (1-1.5mA)
- **Sample Rate**: 0.5Hz (1 lettura ogni 2 secondi)

**Prezzo**: ~5-8€

**Dove acquistare**:
- Amazon.it - Cerca: "DHT22 AM2302"
- AZ-Delivery
- Futura Elettronica

**Utilizzo**: Collegamento GPIO Raspberry Pi (1 pin dati + VCC/GND)

**Funzionalità**: Display temperatura/umidità abitacolo su dashboard

---

#### Accelerometro/Giroscopio MPU6050 (G-Force Display)

**Descrizione**: IMU (Inertial Measurement Unit) 6 assi per misurare accelerazioni e rotazioni

**Specifiche**:
- **Accelerometro**: 3 assi (X, Y, Z)
  - Range: ±2g, ±4g, ±8g, ±16g (configurabile)
  - Sensibilità: 16-bit ADC
- **Giroscopio**: 3 assi (pitch, roll, yaw)
  - Range: ±250°/s, ±500°/s, ±1000°/s, ±2000°/s
- **Interfaccia**: I2C (indirizzo 0x68 o 0x69)
- **Alimentazione**: 3-5V DC (3.5mA typical)
- **Frequenza campionamento**: Fino a 1kHz

**Prezzo**: ~5-10€

**Dove acquistare**:
- Amazon.it - Cerca: "MPU6050 GY-521"
- AZ-Delivery
- Banggood

**Utilizzo**: Collegamento I2C Raspberry Pi (SDA/SCL + VCC/GND)

**Funzionalità HyperMusa**:
- **G-Force Display**: Visualizza accelerazioni laterali/longitudinali stile racing
- **Tilt Meter**: Inclinazione veicolo
- **Hard Braking Detection**: Allerta frenate brusche
- **Crash Detection**: Rilevamento impatti (log event)

**Esempio Visualizzazione**:
```
┌─────────────────────┐
│   G-Force Meter     │
│                     │
│       ↑ +0.8g       │
│     ←0.2g  0.5g→    │
│       ↓             │
│                     │
│ Lat: 0.2g  Lon: 0.8g│
└─────────────────────┘
```

---

### 8. Case e Montaggio

#### Case Raspberry Pi 5 con Ventola Attiva (OBBLIGATORIO Pi 5)

**Descrizione**: Case ABS/alluminio con sistema di raffreddamento attivo

**Specifiche**:
- **Materiale**: ABS plastica o alluminio CNC
- **Ventola**:
  - Dimensione: 30mm × 30mm × 7mm
  - Velocità: 5000-7000 RPM
  - Rumorosità: <25 dBA
  - Alimentazione: 5V GPIO
  - Controllo: PWM (modulazione velocità)
- **Dissipatore**:
  - Alluminio con pad termici
  - Contatto CPU + chip memoria
- **Accesso**:
  - Apertura laterale per SD card
  - Fori per GPIO (ribbon cable)
  - Fori HDMI/USB/Ethernet

**Prezzo**: ~12-20€

**Dove acquistare**:
- [Amazon.it](https://www.amazon.it/s?k=raspberry+pi+5+case+fan) - Cerca: "Raspberry Pi 5 case active cooling"
- [Melopero](https://www.melopero.com/) - Case ufficiali e compatibili
- AliExpress - Modelli economici ~8€

**Modelli consigliati**:
- **Argon ONE V3 for Pi 5** (~25€) - Premium alluminio, ultra-silenzioso
- **Geekworm P580 Armor Case** (~18€) - Alluminio CNC, dissipazione passiva+attiva
- **Official Raspberry Pi Case for Pi 5** (~12€) - Basic ma funzionale

**⚠️ IMPORTANTE Pi 5**:
- Raspberry Pi 5 scalda molto (può raggiungere 80-85°C sotto carico)
- Senza ventola attiva, CPU throttla (riduce prestazioni)
- In ambiente chiuso auto, ventola **OBBLIGATORIA**

---

#### Case Raspberry Pi 4 (se usi Pi 4)

**Descrizione**: Case con dissipatori passivi o ventola opzionale

**Prezzo**: ~8-15€

**Modelli consigliati**:
- Case ufficiale Raspberry Pi 4 (~10€)
- Flirc Case (alluminio passivo) (~18€)
- Case con ventola (~8€)

**Nota**: Pi 4 scalda meno, dissipazione passiva spesso sufficiente

---

#### Supporto Montaggio Display

**A) Adesivo Industriale 3M VHB (Tape)**

**Descrizione**: Biadesivo acrilico ad alta resistenza per fissaggio permanente

**Specifiche**:
- **Prodotto**: 3M VHB (Very High Bond) Tape
- **Spessore**: 0.64-1.1mm
- **Resistenza**: Fino a 10kg per 10cm²
- **Temperatura**: -40°C a +90°C
- **UV Resistant**: Sì
- **Rimozione**: Difficile (permanente)

**Prezzo**: ~8-15€ (rotolo 3m)

**Dove acquistare**:
- Amazon.it - Cerca: "3M VHB tape"
- Brico / Leroy Merlin
- Ferramenta

**Applicazione**:
1. Pulisci superficie display + cruscotto con alcool isopropilico
2. Taglia nastro a misura
3. Applica su display
4. Rimuovi pellicola protettiva
5. Posiziona su cruscotto con **PRECISIONE** (non riposizionabile!)
6. Premi forte per 30 secondi
7. Aspetta 24h prima di usare veicolo

**⚠️ ATTENZIONE**: Biadesivo 3M VHB è **PERMANENTE** - testa posizione con nastro normale prima!

---

**B) Velcro Industriale (Riposizionabile)**

**Descrizione**: Strisce velcro adesive per montaggio smontabile

**Specifiche**:
- **Tipo**: Velcro Heavy Duty
- **Resistenza**: ~1.5-2kg per 10cm²
- **Rimozione**: Facile, riposizionabile

**Prezzo**: ~5-10€

**Dove acquistare**: Amazon.it, Brico

**Utilizzo**: Raspberry Pi, sensori, cavi

**Vantaggi**:
- ✅ Smontabile per manutenzione
- ✅ Riposizionabile

**Svantaggi**:
- ❌ Meno resistente (no per display pesanti)
- ❌ Si rovina con tempo/vibrazioni

---

**C) Supporto Custom 3D Printed (Avanzato)**

**Descrizione**: Case/supporto personalizzato stampato in 3D per integrazione perfetta cruscotto

**Servizi**:
- Thingiverse - Modelli gratuiti (cerca "car dashboard mount")
- Etsy - Venditori custom design
- Servizi stampa 3D locali

**Prezzo**: ~20-50€ (dipende da complessità)

**Vantaggi**:
- ✅ Integrazione perfetta su misura
- ✅ Look professionale
- ✅ Rimuovibile

**Svantaggi**:
- ❌ Richiede design CAD
- ❌ Tempi realizzazione lunghi
- ❌ Costo elevato per pezzo singolo

---

### 9. Cablaggio e Accessori

#### Kit Cavi

**A) Cavo HDMI**

**Tipo necessario**: Dipende da display scelto
- Display con HDMI standard: Cavo Micro-HDMI (Pi) → HDMI (~5€)
- Display con HDMI mini: Cavo Micro-HDMI → Mini-HDMI (~7€)

**Lunghezza**: 30-50 cm (cruscotto compatto)

**Prezzo**: ~5-10€

**Dove**: Amazon.it, negozi elettronica

---

**B) Cavo USB (Touch)**

**Tipo**: USB-A (Raspberry Pi) → USB Mini/Micro (Display)

**Lunghezza**: 30-50 cm

**Prezzo**: ~3-5€

---

**C) Fascette Fermacavi**

**Quantità**: Pack 100pz assortite

**Prezzo**: ~5€

**Dove**: Amazon.it, Brico

**Utilizzo**: Organizzazione cavi, fissaggio sotto cruscotto

---

**D) Guaina Spiralata per Cavi**

**Descrizione**: Guaina flessibile per proteggere e organizzare mazzi di cavi

**Diametro**: 10-15mm

**Lunghezza**: 2-3 metri

**Prezzo**: ~5-8€

**Dove**: Amazon.it, negozi elettronica

---

**E) Connettori e Terminali**

- **Capicorda occhiello** (per massa chassis): ~3€
- **Connettori faston** (per derivazioni fusibili): ~5€
- **Guaina termorestringente** (protezione saldature): ~5€
- **Morsetti elettrici rapidi** (Wago): ~8€

**Prezzo totale accessori**: ~20-30€

---

### 10. Protezioni Elettriche (OBBLIGATORIE)

#### Fusibili Automotive

**A) Fusibile per Raspberry Pi**

**Valore**:
- Raspberry Pi 5: **3A** (carico max 2.7A @ 12V)
- Raspberry Pi 4: **2A** (carico max 1.5A @ 12V)

**Tipo**: Fusibile blade automotive mini (ATO/ATC)

**Prezzo**: ~1€ ciascuno

**Quantità**: 3-5 pezzi di ricambio

---

**B) Fusibile per Display**

**Valore**: **3A** (verificare consumo specifico display)

**Nota**: Display 10-12" consuma tipicamente 0.5-1A @ 12V

---

**C) Portafusibili Inline**

**Descrizione**: Portafusibili da inserire in linea sul cavo 12V

**Specifiche**:
- Tipo: Portafusibile blade inline
- Cavo: 14-16 AWG (1.5-2.5mm²)
- Rating: 10A massimo

**Prezzo**: ~2-4€ ciascuno

**Quantità necessaria**: 2 minimo (Raspberry + Display)

**Dove acquistare**: Amazon.it, Brico, negozi ricambi auto

---

**D) Diodi Protezione Inversione Polarità**

**Descrizione**: Diodo per proteggere da inversione accidentale polarità

**Tipo**: 1N5822 Schottky (3A, 40V)

**Prezzo**: ~0.50€ ciascuno

**Quantità**: 2 (uno per linea alimentazione)

**Dove**: Amazon.it (kit diodi), negozi elettronica

---

**⚡ Schema Protezioni Consigliato**:

```
Batteria 12V (o OBD2 pin 16)
    │
    ├─→ [Diodo 1N5822] → [FUSIBILE 3A] → Convertitore DC-DC → Raspberry Pi
    │
    └─→ [Diodo 1N5822] → [FUSIBILE 3A] → Display 12V
```

**Costo totale protezioni**: ~10-15€

**⚠️ NON SALTARE LE PROTEZIONI**: Rischio cortocircuito = incendio auto!

---

### 11. Strumenti (se non posseduti)

#### Multimetro Digitale

**Descrizione**: Strumento essenziale per misurare tensioni CAN-Bus e alimentazione

**Funzioni necessarie**:
- Voltmetro DC (0-30V)
- Continuità (beeper)
- Test diodi

**Prezzo**: ~15-25€

**Dove**: Amazon.it, Brico, Leroy Merlin

**Modelli entry-level**:
- "UNI-T UT33" (~15€)
- "Tacklife DM01M" (~18€)

---

#### Crimpatrice Dupont (Opzionale)

**Descrizione**: Pinza per crimpare connettori Dupont su cavi

**Prezzo**: ~10-15€

**Dove**: Amazon.it

**Nota**: Opzionale, cavi Dupont preassemblati sono sufficienti

---

#### Set Cacciaviti Precisione

**Prezzo**: ~8-12€

**Dove**: Amazon.it, Brico

**Utilizzo**: Smontaggio cruscotto, montaggio case

---

**Costo totale strumenti**: ~25-40€ (se non posseduti)

---

## 🔌 10. Cavetteria Dettagliata e Collegamenti

### Cavo OBD2 → MCP2515 (COMPONENTE CRITICO)

#### Opzione A: Splitter OBD2 a Y (CONSIGLIATA - Non Invasiva)

**Descrizione**: Cavo splitter con 1 ingresso OBD2 maschio + 2 uscite OBD2 femmina

**Vantaggi**:
- ✅ Porta OBD2 rimane accessibile per diagnosi originale
- ✅ Zero modifiche permanenti
- ✅ Totalmente reversibile

**Schema**:
```
Porta OBD2 Musa ──► [Splitter Y] ──┬──► Uscita 1: Diagnosi/Scanner normale
                                    └──► Uscita 2: Cavo breakout → MCP2515
```

**Prezzo**: ~12-18€

**Dove**: Amazon.it (cerca "OBD2 splitter Y cable 16 pin")

**Esempio**: FIXD OBD2 Splitter, Carista Y-Cable

---

#### Opzione B: Cavo OBD2 Breakout con Pin Esposti (DIY)

**Descrizione**: Cavo OBD2 maschio con singoli fili etichettati per ogni pin

**Pin necessari da connettere**:
- **Pin 6** → CAN-H (cavo giallo/arancione) → MCP2515 CANH
- **Pin 14** → CAN-L (cavo verde/blu) → MCP2515 CANL
- **Pin 4 o 5** → GND (cavo nero) → MCP2515 GND
- **Pin 16** → +12V (opzionale, se alimenti da OBD2)

**Vantaggi**: Accesso diretto ai pin, più flessibile

**Svantaggi**: Porta OBD2 occupata (serve splitter aggiuntivo)

**Prezzo**: ~8-12€

**Dove**: Amazon.it (cerca "OBD2 breakout cable" o "OBD2 to wire harness")

---

#### Schema Collegamento OBD2 → MCP2515

```
┌─────────────────────────────────────────────────┐
│      CONNETTORE OBD2 (Vista Frontale)          │
│  ┌─────────────────────────────────────────┐   │
│  │     8  7  6  5  4  3  2  1              │   │
│  │    16 15 14 13 12 11 10  9              │   │
│  └─────────────────────────────────────────┘   │
│                                                 │
│  Pin 4/5: GND ──────────────────┐              │
│  Pin 6: CAN-H ────────┐         │              │
│  Pin 14: CAN-L ──┐    │         │              │
│  Pin 16: +12V    │    │         │              │
└──────────────────┼────┼─────────┼──────────────┘
                   │    │         │
                   │    │         │
          ┌────────▼────▼─────────▼────────┐
          │     MCP2515 CAN Module         │
          │  ┌──────────────────┐          │
          │  │ CANH ← Pin 6     │          │
          │  │ CANL ← Pin 14    │          │
          │  │ GND  ← Pin 4/5   │          │
          │  └──────────────────┘          │
          └────────────────────────────────┘
```

**⚠️ IMPORTANTE**:
- **NON** collegare il pin 16 (+12V) al MCP2515 se alimenti il Raspberry Pi separatamente!
- Il MCP2515 si alimenta dal Raspberry Pi (pin 5V GPIO)
- Verifica con multimetro prima di collegare: CAN-H ~2.5-3.5V, CAN-L ~1.5-2.5V (con chiave su MAR)

---

### Cavi Alimentazione 12V Auto → Raspberry Pi

#### Opzione A: Adattatore Accendisigari USB-C (CONSIGLIATA)

**Descrizione**: Convertitore DC-DC plug & play per accendisigari/12V

**Vantaggi**: Zero modifiche impianto elettrico, installazione 10 secondi

**Specifiche**: Input 12-24V DC, Output 5V 5A USB-C PD

**Prezzo**: ~15-25€ (già inserito in lista principale)

**Dove**: Amazon.it (cerca "adattatore auto USB-C 5A PD")

---

#### Opzione B: Collegamento Diretto Fusibili (Avanzata)

**Descrizione**: Cavo Add-a-Circuit per collegare a scatola fusibili

**Vantaggi**: Installazione pulita, nascosta, si accende con quadro

**Componenti**:
- Add-a-Circuit blade fuse holder: ~8€
- Fusibile 5A aggiuntivo: ~2€
- Convertitore DC-DC 12V→5V 5A isolato: ~12€
- Cavi AWG 18 rosso/nero: ~5€

**Prezzo totale**: ~27€

**Dove**: Amazon.it / Brico

**⚠️ Richiede**: Conoscenza impianti elettrici, multimetro, schema fusibili Musa

**Raccomandazione**: Usa Opzione A per test, Opzione B per installazione definitiva.

---

### Cavi Display

| Tipo Display | Cavi Necessari | Prezzo | Note |
|--------------|----------------|--------|------|
| 7" Raspberry Pi ufficiale | Cavo ribbon DSI (incluso) + USB micro power | 0€ | Plug & play |
| 10.1" HDMI Touch | Mini/Micro HDMI → HDMI (1m) + USB-A to USB-B touch | ~12€ | Verifica tipo HDMI su Pi |
| 12.3" Bar Automotive | HDMI standard (1m) + Controller board USB power | ~15€ | Potrebbe includere cavi |

**Lunghezza raccomandata**: 1-1.5m per passaggio cavi pulito da cruscotto a vano sotto volante.

---

### Kit Gestione Cavi (NECESSARIO!)

| Componente | Quantità | Prezzo | Dove |
|------------|----------|--------|------|
| Guaina spiralata 10mm (nero) | 3 metri | ~8€ | Amazon.it |
| Fascette nylon 15cm | 50 pezzi | ~3€ | Già inserito |
| Clips adesive cavi (Ø6-10mm) | 20 pezzi | ~5€ | Amazon.it / Brico |
| Velcro adesivo industriale 50mm | 1 metro | ~8€ | Già inserito |
| Nastro isolante nero | 1 rotolo | ~3€ | Brico |
| **TOTALE KIT CAVI** | | **~27€** | |

---

### Lista Completa Cavi - Riepilogo

✅ **Cavi da acquistare** (non inclusi nei componenti principali):

- ☑ Splitter OBD2 a Y (12-18€) - **PRIORITÀ ALTA**
- ☑ Cavo Mini/Micro HDMI → HDMI 1m (8€) - secondo display scelto
- ☑ Cavo USB-A to USB per touch screen 1m (5€) - se display touch
- ☑ Guaina spiralata 3m (8€)
- ☑ Clips adesive per cavi 20pz (5€)
- ☑ Nastro isolante (3€)
- ☑ (Opzionale) Add-a-Circuit per fusibili (8€) - installazione permanente

**TOTALE CAVI**: ~49-55€ (da aggiungere al budget configurazione)

---

## 🛡️ 11. Installazione Non Invasiva e Reversibilità

### Filosofia del Progetto HyperMusa

**HyperMusa è progettato per essere 100% REVERSIBILE senza lasciare tracce.**

#### ✅ Cosa NON Faremo MAI

- ❌ Tagliare cavi originali della Musa
- ❌ Forare cruscotto o plastiche
- ❌ Modificare centraline o Body Computer
- ❌ Scrivere dati sul CAN-Bus (solo LETTURA)
- ❌ Bypassare sistemi di sicurezza
- ❌ Sostituire il quadro strumenti originale

#### ✅ Cosa Faremo

- ✅ Collegamento OBD2 con splitter (plug & play)
- ✅ Alimentazione da accendisigari (removibile)
- ✅ Display montato con velcro o biadesivo removibile
- ✅ Solo LETTURA dati CAN-Bus (come scanner diagnosi)
- ✅ Quadro originale rimane completamente funzionante

---

### Funzionamento in Parallelo

```
┌────────────────────────────────────────────────┐
│             LANCIA MUSA 2009                   │
│                                                │
│  ┌──────────────────────────────────────┐     │
│  │    Quadro Strumenti Originale        │     │
│  │      ✅ Funziona al 100%             │     │
│  │      ✅ Sempre prioritario           │     │
│  │      ✅ Mai disattivato              │     │
│  └──────────────────────────────────────┘     │
│                  ▲                             │
│                  │ CAN-Bus                     │
│                  │                             │
│     ┌────────────┴──────────┐                 │
│     │    Body Computer      │                 │
│     │    (ECU Centrale)     │                 │
│     └────────────┬───────────┘                │
│                  │                             │
│                  ├──► Porta OBD2               │
│                  │        │                    │
└──────────────────┼────────┼────────────────────┘
                   │        │
                   │   ┌────▼─────┐
                   │   │ Splitter │
                   │   └────┬─────┘
                   │        │
                   │   ┌────▼──────────────┐
                   │   │    MCP2515        │
                   │   │  (SOLO LETTURA)   │
                   │   └────┬──────────────┘
                   │        │
                   │   ┌────▼──────────────┐
                   │   │  Raspberry Pi     │
                   │   │  + HyperMusa      │
                   │   └────┬──────────────┘
                   │        │
                   │   ┌────▼──────────────┐
                   │   │ Display Digitale  │
                   │   │   (Aggiuntivo)    │
                   │   └───────────────────┘
                   │
                   ✅ Tutto funziona
                   ✅ Auto utilizzabile normalmente
                   ✅ Zero interferenze
```

---

### Modalità Test Sicuro

#### Fase 0: Bench Test (A Casa - Prima di Toccare l'Auto)

**Durata**: 1-2 settimane

**Obiettivo**: Verificare che tutto il sistema funzioni prima di installarlo sulla Musa.

**Checklist**:
- ☑ Assembla Raspberry Pi + MCP2515 su breadboard
- ☑ Installa Raspberry Pi OS e dipendenze
- ☑ Testa MCP2515 in modalità loopback (test interno)
- ☑ Carica interfaccia HyperMusa in modalità demo (dati simulati)
- ☑ Verifica rendering UI, performance, stabilità
- ☑ Lascia acceso per 24h (stress test termico)

**Comando test loopback MCP2515**:
```bash
# Abilita SPI
sudo raspi-config  # Interface Options > SPI > Enable

# Installa can-utils
sudo apt-get install can-utils

# Configura interfaccia CAN in loopback
sudo ip link set can0 type can bitrate 500000 loopback on
sudo ip link set up can0

# Test invio/ricezione
candump can0 &
cansend can0 123#DEADBEEF

# Dovresti vedere il messaggio ricevuto
```

**Risultato atteso**: Sistema stabile, UI fluida, MCP2515 risponde.

---

#### Fase 1: Primo Test su Musa (Auto Ferma, Motore Spento)

**Durata**: 1-2 giorni

**Rischio**: **MINIMO**

**Setup**:
- Auto parcheggiata in garage/posto sicuro
- Chiave su MAR (quadro acceso, motore SPENTO)
- Collegamento temporaneo con tutto smontabile

**Checklist**:
1. ☐ Collega splitter OBD2 alla porta diagnostica Musa
2. ☐ Connetti cavo breakout da splitter a MCP2515
3. ☐ Alimenta Raspberry Pi da powerbank USB-C (NON da auto ancora)
4. ☐ Avvia HyperMusa e monitora

**Test da eseguire**:
- ☐ `candump can0` mostra traffico CAN? (dovresti vedere messaggi)
- ☐ Quadro originale Musa funziona normalmente?
- ☐ HyperMusa riceve dati (velocità=0, RPM=0, temperatura OK)?
- ☐ Nessun warning/errore sul quadro Musa?
- ☐ Lascia acceso 30 minuti, monitora stabilità

**Comandi utili**:
```bash
# Configura CAN a 500kbps (come Musa)
sudo ip link set can0 type can bitrate 500000
sudo ip link set up can0

# Dump tutti i messaggi CAN
candump -c can0 | tee musa-can-dump.log

# Filtra solo RPM (PID 0x0C) se disponibile
candump can0 | grep "0C"
```

**Risultato atteso**: Traffico CAN visibile, zero errori su Musa, HyperMusa legge dati.

**⚠️ Se qualcosa va male**:
1. Spegni chiave Musa
2. Scollega MCP2515 da OBD2
3. Riaccendi Musa e verifica che funzioni normalmente
4. Debug: controlla collegamenti, verifica voltaggio CAN-H/CAN-L con multimetro

---

#### Fase 2: Test con Motore Acceso (Auto Ferma)

**Durata**: 3-7 giorni
**Rischio**: **BASSO**

**Setup**:
- Auto in garage, motore acceso al minimo
- Alimentazione Raspberry Pi ANCORA da powerbank (non da auto)
- Osservazione per 10-30 minuti

**Test**:
- ☐ RPM mostrati da HyperMusa corrispondono a quadro originale?
- ☐ Temperatura motore sale correttamente?
- ☐ Accelerando (pedale gas), RPM si aggiornano in real-time?
- ☐ Quadro originale non mostra errori/spie accese?
- ☐ Sistema stabile per 30+ minuti?

**Logging PID per reverse engineering**:
```bash
# Registra 5 minuti di traffico CAN mentre acceleri
candump -l can0
# Crea file candump-YYYY-MM-DD_HHMMSS.log

# Analizza dopo con SavvyCAN o script Python
```

**Obiettivo**: Mappare i PID specifici Lancia Musa, capire quali dati sono disponibili.

---

#### Fase 3: Test in Movimento (Bassa Velocità)

**Durata**: 1-2 settimane
**Rischio**: **MEDIO** (richiede attenzione)

**Setup**:
- Passeggero presente per monitorare HyperMusa
- Percorso: parcheggio vuoto o strada poco trafficata
- Alimentazione: Ora puoi passare a alimentatore 12V auto (accendisigari)

**Test**:
- ☐ Prima di partire: Velocità HyperMusa = 0?
- ☐ In movimento: Velocità corrisponde a quadro originale e GPS?
- ☐ Cambio marcia: RPM si aggiornano correttamente?
- ☐ Frenata: Velocità scende in sync con quadro originale?
- ☐ Test 10-20 km, varie velocità (30-90 km/h)

**🚨 REGOLE SICUREZZA**:
- **TU GUIDI**, non guardare mai HyperMusa mentre sei in movimento
- **PASSEGGERO** monitora display e annota anomalie
- Se qualsiasi cosa sembra strana, **FERMA** e disabilita HyperMusa
- Quadro originale è **SEMPRE** la fonte di verità

**Risultato atteso**: Dati accurati, zero interferenze con auto, sistema stabile.

---

#### Fase 4: Test Esteso (Uso Quotidiano)

**Durata**: 1-2 mesi
**Rischio**: **BASSO** (se Fase 1-3 ok)

**Setup**:
- Installazione semi-permanente: display con velcro, cavi nascosti con guaine
- Raspberry Pi fissato sotto sedile/in vano portaoggetti
- Uso quotidiano normale della Musa

**Obiettivi**:
- ☐ Sistema acceso ad ogni utilizzo auto (2-4 settimane)
- ☐ Nessun errore/warning sul quadro Musa
- ☐ HyperMusa stabile in tutte le condizioni (caldo/freddo, pioggia)
- ☐ Batteria auto non si scarica (verifica con multimetro dopo 2-3 giorni fermo)
- ☐ Zero problemi durante revisione (se prevista)

**Monitoraggio**:
- Log errori HyperMusa: `/var/log/hypermusa/errors.log`
- Check tensione batteria: prima/dopo uso HyperMusa
- Feedback: eventuali anomalie comportamento Musa?

**Se tutto ok per 2 mesi** → Installazione definitiva (ma sempre reversibile!)

---

### Guida Rimozione Rapida (Emergenza)

**Tempo richiesto**: 5-10 minuti

**Scenario**: Devi portare la Musa in officina/revisione e vuoi rimuovere HyperMusa.

**Procedura**:
1. ☐ Spegni Raspberry Pi (shutdown corretto, non staccare alimentazione!)
2. ☐ Scollega splitter OBD2 (10 secondi)
3. ☐ Scollega alimentatore 12V da accendisigari (5 secondi)
4. ☐ Rimuovi display (se velcro: 30 sec, se biadesivo: 2 min con alcool isopropilico)
5. ☐ Rimuovi Raspberry Pi e nascondi cavi sotto sedile
6. ☐ Accendi Musa e verifica funzionamento normale

**Checklist verifica**:
- ☐ Quadro strumenti funziona?
- ☐ Nessuna spia accesa anomala?
- ☐ Porta OBD2 libera?
- ☐ Zero segni visibili di modifica?

**Tempo totale**: <10 minuti
**Reversibilità**: 100%

---

### Installazione Permanente (Opzionale)

**⚠️ Esegui SOLO dopo 2+ mesi di test senza problemi!**

**Upgrade da temporanea a permanente**:

**1. Alimentazione**:
- Sostituisci accendisigari con Add-a-Circuit su scatola fusibili
- Collega a fusibile "accessori" che si attiva con quadro (es. radio)
- Nascondi cavo alimentazione sotto plancia

**2. Display**:
- Sostituisci velcro con biadesivo 3M VHB (permanente ma removibile)
- Valuta supporto custom stampato 3D per integrazione pulita
- Passa cavi HDMI/USB dentro plancia (richiede smontaggio)

**3. Raspberry Pi**:
- Case custom 3D per montaggio sotto cruscotto
- Ventola sempre attiva (temperatura auto alta in estate!)
- Fissaggio con viti a plancia (verifica punti di montaggio sicuri)

**4. Cavi**:
- Tutti i cavi in guaina nera nascosta
- Fissaggio con clips lungo percorso cavi originali
- Etichettatura professionale per manutenzione futura

**⚠️ Anche con "installazione permanente", rimane 100% reversibile!**
Tempo rimozione sale a 30-60 minuti ma è possibile.

---

## 🧪 12. Modalità Demo e Test Senza Auto

### Simulatore CAN-Bus Virtuale

Per sviluppare HyperMusa senza accesso continuo alla Musa, implementa modalità demo:

#### Virtual CAN Interface (vcan)

```bash
# Crea interfaccia CAN virtuale su Raspberry Pi
sudo modprobe vcan
sudo ip link add dev vcan0 type vcan
sudo ip link set up vcan0

# Simula traffico CAN Lancia Musa
# Script Python per generare PID realistici
```

---

### Script Simulatore Python

Crea file `tests/musa-can-simulator.py`:

```python
#!/usr/bin/env python3
"""
Simulatore CAN-Bus Lancia Musa 2009
Genera traffico CAN realistico per test HyperMusa senza veicolo
"""

import can
import time
import random

# Configura bus CAN virtuale
bus = can.interface.Bus(channel='vcan0', bustype='socketcan')

def simulate_musa_can():
    """Simula messaggi CAN tipici di Lancia Musa"""

    while True:
        # RPM motore (0-6000 rpm) - PID 0x0C
        rpm = random.randint(800, 3000)  # Minimo a medio
        msg_rpm = can.Message(
            arbitration_id=0x7E8,  # ID risposta ECU
            data=[0x04, 0x41, 0x0C, rpm >> 8, rpm & 0xFF],
            is_extended_id=False
        )
        bus.send(msg_rpm)

        # Velocità (0-200 km/h) - PID 0x0D
        speed = random.randint(0, 120)
        msg_speed = can.Message(
            arbitration_id=0x7E8,
            data=[0x03, 0x41, 0x0D, speed],
            is_extended_id=False
        )
        bus.send(msg_speed)

        # Temperatura motore (60-95°C) - PID 0x05
        temp = random.randint(80, 92) + 40  # Offset +40 per protocollo OBD
        msg_temp = can.Message(
            arbitration_id=0x7E8,
            data=[0x03, 0x41, 0x05, temp],
            is_extended_id=False
        )
        bus.send(msg_temp)

        # Livello carburante (20-100%) - PID 0x2F
        fuel = random.randint(30, 90) * 255 // 100
        msg_fuel = can.Message(
            arbitration_id=0x7E8,
            data=[0x03, 0x41, 0x2F, fuel],
            is_extended_id=False
        )
        bus.send(msg_fuel)

        time.sleep(0.1)  # 10 Hz update rate

if __name__ == "__main__":
    print("🚗 Simulatore CAN Lancia Musa attivo su vcan0")
    print("   RPM: 800-3000 | Speed: 0-120 km/h | Temp: 80-92°C")
    try:
        simulate_musa_can()
    except KeyboardInterrupt:
        print("\n✅ Simulatore terminato")
```

**Uso**:
```bash
# Avvia simulatore in background
python3 tests/musa-can-simulator.py &

# Verifica messaggi
candump vcan0

# Testa HyperMusa con dati simulati
./hypermusa --can-interface vcan0
```

---

## ✅ 13. Checklist Compatibilità Finale

### Hardware

- ☑ **Raspberry Pi 5 4GB**: ✅ Compatibile con MCP2515 via SPI
- ☑ **MCP2515 + TJA1050**: ✅ Supporta ISO 15765-4 CAN a 500 kbps
- ☑ **Lancia Musa 2009**: ✅ CAN-Bus nativo, porta OBD2 standard J1962
- ☑ **Display 10.1"-12.3"**: ✅ Connessione HDMI standard Raspberry Pi
- ☑ **Alimentazione 12V→5V 5A**: ✅ Compatibile con impianto elettrico Musa 12V
- ☑ **Cavi e connettori**: ✅ Standard automotive, disponibili su Amazon.it

---

### Software

- ☑ **Raspberry Pi OS**: ✅ Supporto nativo MCP2515 (driver mcp251x kernel)
- ☑ **can-utils**: ✅ Tool standard Linux per CAN-Bus
- ☑ **Socket CAN**: ✅ Interfaccia Linux per applicazioni CAN
- ☑ **Node.js + React**: ✅ Stack Cyberpandino compatibile con Pi 5

---

### Sicurezza e Normative

- ☑ **OBD2 Read-Only**: ✅ Solo lettura, nessuna scrittura su CAN-Bus
- ☑ **Quadro Originale Intatto**: ✅ Funziona in parallelo, mai disabilitato
- ☑ **Reversibilità**: ✅ Rimozione completa in <10 minuti senza tracce
- ☑ **Fusibile Protezione**: ✅ Fusibile inline 5A su alimentazione (raccomandato)
- ☑ **Isolamento Elettrico**: ✅ MCP2515 con transceiver TJA1050 isolato
- ☑ **Temperatura Operativa**: ✅ -40°C a +85°C (componenti automotive-grade)

---

### Garanzia e Assicurazione

- ☑ **Garanzia Musa**: ⚠️ Verifica con concessionario (auto 2009 probabilmente fuori garanzia)
- ☑ **Assicurazione**: ⚠️ Informa assicurazione se installazione permanente
- ☑ **Revisione**: ✅ Display aggiuntivo non interferisce con sistemi sicurezza (OK per revisione)

---

## 🎯 Riepilogo Budget Aggiornato

### Configurazione Consigliata (AGGIORNATA con cavetteria)

| Categoria | Costo | Note |
|-----------|-------|------|
| **Hardware base** (già definito) | 298€ | Pi 5, MCP2515, display 10.1", etc. |
| **Cavetteria aggiuntiva** | +55€ | Splitter OBD2, HDMI, clips, guaine |
| **TOTALE REALE** | **~353€** | Budget finale realistico |

---

### Budget Corretto per Fasce

- **Base**: 169€ + 40€ cavi = **~210€**
- **Consigliata**: 298€ + 55€ cavi = **~350€** ✅
- **Premium**: 505€ + 60€ cavi = **~565€**

---

## 🛒 LISTA DELLA SPESA COMPLETA

### ⚙️ Configurazione Base (~250€)

**Target**: Proof-of-concept funzionante, sviluppo software

| # | Componente | Modello/Specifiche | Prezzo | Link Suggerito |
|---|------------|-------------------|--------|----------------|
| 1 | Computer | Raspberry Pi 4B 4GB | 55€ | [Amazon.it](https://www.amazon.it/s?k=raspberry+pi+4+4gb) |
| 2 | CAN Interface | MCP2515 + TJA1050 | 10€ | [Battery Atom](https://www.batteryatom.it/prodotto/mcp2515-can-bus-modul-tja1050-transceiver-5v-arduino-raspberry-pi/) |
| 3 | Display | 7" Touch 1024×600 | 40€ | [Amazon.it](https://www.amazon.it/s?k=raspberry+pi+7+display) |
| 4 | Alimentazione | DC-DC 12V→5V 3A USB-C | 12€ | [Amazon.it](https://www.amazon.it/s?k=12v+5v+3a+usb-c) |
| 5 | Storage | MicroSD 64GB Samsung EVO Plus A2 | 15€ | [Amazon.it](https://www.amazon.it/s?k=microsd+64gb+a2) |
| 6 | Connettività OBD | Cavo OBD2 splitter + Dupont kit | 12€ | [Amazon.it](https://www.amazon.it/s?k=obd2+splitter) |
| 7 | Case | Case Pi 4 con ventola | 10€ | [Amazon.it](https://www.amazon.it/s?k=raspberry+pi+4+case) |
| 8 | Protezioni | Fusibili 3A + portafusibili inline (×2) | 8€ | Amazon.it / Brico |
| 9 | Cablaggio | HDMI + USB + accessori | 15€ | Amazon.it |
| 10 | Montaggio | Velcro heavy duty + fascette | 8€ | Amazon.it / Brico |
| 11 | **Cavetteria** | Splitter OBD2 + cavi HDMI/USB + guaine | **40€** | Amazon.it |
| | **TOTALE BASE** | | **~210€** | |

**+ Opzionale Strumenti** (se non posseduti):
- Multimetro digitale: ~18€
- Cacciaviti set: ~10€
- **Subtotale con strumenti**: ~240€

---

### 🚀 Configurazione Consigliata (~400€)

**Target**: Performance ottimali, installazione semi-definitiva

| # | Componente | Modello/Specifiche | Prezzo | Link Suggerito |
|---|------------|-------------------|--------|----------------|
| 1 | Computer | **Raspberry Pi 5 4GB** | 75€ | [Melopero](https://www.melopero.com/it/shop/boards/pi5/raspberry-pi-5-4gb/) |
| 2 | CAN Interface | MCP2515 + TJA1050 | 10€ | [Battery Atom](https://www.batteryatom.it/prodotto/mcp2515-can-bus-modul-tja1050-transceiver-5v-arduino-raspberry-pi/) |
| 3 | Display | **10.1" Touch 1920×1200 IPS** | 75€ | [Amazon.it](https://www.amazon.it/s?k=10.1+touch+1920x1200) |
| 4 | Alimentazione | **DC-DC 12V→5V 5A USB-C PD** | 20€ | [Amazon.it](https://www.amazon.it/s?k=12v+5v+5a+usb-c) |
| 5 | Storage | **MicroSD 64GB SanDisk Extreme PRO A2** | 20€ | [Amazon.it](https://www.amazon.it/s?k=sandisk+extreme+pro+64gb) |
| 6 | Connettività OBD | Cavo OBD2 premium breakout + Dupont | 15€ | [Amazon.it](https://www.amazon.it/s?k=obd2+breakout) |
| 7 | Case | **Case Pi 5 con ventola attiva PWM** | 18€ | [Melopero](https://www.melopero.com/) / Amazon.it |
| 8 | GPS | **VK-162 USB GPS u-blox** | 18€ | [Amazon.it](https://www.amazon.it/s?k=vk-162+gps) |
| 9 | Sensori | MPU6050 accelerometro | 7€ | [Amazon.it](https://www.amazon.it/s?k=mpu6050) |
| 10 | Protezioni | Fusibili + portafusibili + diodi | 10€ | Amazon.it / Brico |
| 11 | Montaggio | Biadesivo 3M VHB + velcro | 12€ | Amazon.it / Brico |
| 12 | **Cavetteria** | Splitter OBD2 + HDMI + USB + guaine + clips | **55€** | Amazon.it |
| | **TOTALE CONSIGLIATO** | | **~353€** | |

**+ Opzionale Strumenti**:
- Multimetro + cacciaviti: ~28€
- **Subtotale con strumenti**: ~380€

**+ Opzionale Power Bank** (shutdown sicuro):
- Power Bank 10000mAh USB-C: ~25€
- **Totale con UPS**: ~353€

---

### 💎 Configurazione Premium (~600€)

**Target**: Installazione definitiva look automotive professionale

| # | Componente | Modello/Specifiche | Prezzo | Link Suggerito |
|---|------------|-------------------|--------|----------------|
| 1 | Computer | **Raspberry Pi 5 8GB** | 95€ | [Melopero](https://www.melopero.com/) |
| 2 | CAN Interface | **PiCAN 3 HAT** | 42€ | [SK Pang Electronics](https://www.skpang.co.uk/) |
| 3 | Display | **12.3" Bar Touch 1920×720 IPS** | 130€ | [AliExpress](https://www.aliexpress.com/) "stretch bar lcd automotive" |
| 4 | Alimentazione | DC-DC 5A + **Power Bank 10Ah UPS** | 40€ | Amazon.it |
| 5 | Storage | **MicroSD 128GB SanDisk Extreme PRO A2** | 28€ | [Amazon.it](https://www.amazon.it/s?k=sandisk+extreme+pro+128gb) |
| 6 | Connettività OBD | Cavo OBD2 professionale breakout | 18€ | Amazon.it / eBay |
| 7 | Case | **Argon ONE V3 alluminio CNC Pi 5** | 28€ | [Amazon.it](https://www.amazon.it/s?k=argon+one+v3) |
| 8 | GPS | **Beitian BN-880 u-blox M8N + compass** | 28€ | Amazon.it / AliExpress |
| 9 | Sensori | MPU6050 + DHT22 + accessori | 18€ | Amazon.it |
| 10 | Protezioni | Kit protezioni completo (fusibili, diodi, relay) | 15€ | Amazon.it |
| 11 | Montaggio | **Supporto custom 3D printed** + 3M VHB | 40€ | Etsy / Servizi stampa 3D |
| 12 | **Cavetteria** | Splitter OBD2 + Kit cavi professionale guainato | **60€** | Amazon.it |
| 13 | Strumenti | Multimetro + set cacciaviti + crimpatrice | 40€ | Amazon.it |
| | **TOTALE PREMIUM** | | **~565€** | |

**+ Opzionale Dashcam** (integrazione futura):
- USB Webcam HD: ~30€
- **Totale con dashcam**: ~595€

---

## 🎯 Raccomandazioni Finali per Budget

### Budget ~210€ (Minimo Assoluto)
- Pi 4B 4GB + Display 7" + MSD 32GB + MCP2515 + cavetteria base
- ⚠️ Funziona ma UI limitata, solo per POC rapidi

### Budget ~353€ (Sweet Spot) ✅ **RACCOMANDATO**
- Pi 5 4GB + Display 10.1" + MSD 64GB + GPS + sensori + cavetteria completa
- ✅ Performance ottime, espandibile, installazione semi-definitiva

### Budget ~565€ (Enthusiast)
- Pi 5 8GB + Display bar 12.3" + tutti accessori + supporto custom + cavetteria premium
- ✅ Massime performance, look professionale automotive

---

## 📐 Dimensioni Cruscotto Lancia Musa

**⚠️ IMPORTANTE**: Prima di ordinare il display, **misura accuratamente** lo spazio disponibile sul cruscotto!

### Aree Disponibili

**A) Sopra Volante (Posizione Principale)**
- Larghezza utile: ~26-30 cm
- Altezza disponibile: ~7-10 cm
- Profondità: ~5-7 cm
- **Ideale per**: Display bar 12.3" (28.4cm × 7.5cm)

**B) Centrale Console (Alternativa)**
- Area radio/clima: ~18-20 cm larghezza
- **Ideale per**: Display 7-10"

### Tool Necessari per Misurazioni

- **Metro a nastro** flessibile
- **Calibro digitale** (per precisione)
- **Carta millimetrata** (template dimensioni)
- **Cartone** (mockup display per test posizionamento)

### Procedura

1. **Misura spazio cruscotto** con metro
2. **Crea template** cartaceo dimensioni display
3. **Testa posizionamento** con cartone (mockup)
4. **Verifica visibilità** da posizione guida
5. **Controlla non ostruisca** spie/volante
6. **Solo dopo**: ordina display

**Template Download**:
- Display 12.3" bar: 284mm × 75mm (scala 1:1 stampabile)
- Display 10.1": 223mm × 139mm (scala 1:1)

---

## 🔌 Pin Mapping e Collegamenti

### MCP2515 → Raspberry Pi GPIO

| MCP2515 Pin | Nome Segnale | Raspberry Pi GPIO | Pin Fisico | Note |
|-------------|--------------|-------------------|------------|------|
| VCC | Alimentazione 5V | 5V Power | Pin 2 o 4 | Alimentazione |
| GND | Ground | Ground | Pin 6, 9, 14, 20, 25, 30, 34, 39 | Massa |
| SCK | SPI Clock | GPIO 11 (SCLK) | Pin 23 | Clock SPI |
| SI (MOSI) | Master Out Slave In | GPIO 10 (MOSI) | Pin 19 | Dati TX |
| SO (MISO) | Master In Slave Out | GPIO 9 (MISO) | Pin 21 | Dati RX |
| CS | Chip Select | GPIO 8 (CE0) | Pin 24 | Selezione device |
| INT | Interrupt | GPIO 25 | Pin 22 | Segnale interrupt |

**Cablaggio Fisico**:
```
MCP2515 Module          Raspberry Pi GPIO Header
┌──────────────┐        ┌────────────────────────┐
│              │        │  1 [3.3V]    2 [5V]   │◄── VCC
│  VCC      ●──┼────────┤                        │
│  GND      ●──┼────────┤  6 [GND]              │
│  CS       ●──┼────────┤ 24 [GPIO 8]           │
│  SO(MISO) ●──┼────────┤ 21 [GPIO 9]           │
│  SI(MOSI) ●──┼────────┤ 19 [GPIO 10]          │
│  SCK      ●──┼────────┤ 23 [GPIO 11]          │
│  INT      ●──┼────────┤ 22 [GPIO 25]          │
│              │        │                        │
│  CAN_H    ●  │        └────────────────────────┘
│  CAN_L    ●  │             Raspberry Pi
│              │
└──────────────┘
       │
       ↓ To OBD2
```

**⚠️ ATTENZIONE**:
- MCP2515 VCC = **5V** (NON 3.3V!)
- Raspberry Pi GPIO sono **3.3V** ma MCP2515 ha level shifters integrati
- Usa cavi Dupont corti (<20cm) per ridurre interferenze

---

### OBD2 Connector → MCP2515

| OBD2 Pin | Funzione | Colore Cavo Standard | MCP2515 Terminale |
|----------|----------|----------------------|-------------------|
| Pin 4 | Ground Chassis | Nero | - |
| Pin 5 | Ground Segnale | Nero/Marrone | GND (comune con Pi) |
| Pin 6 | **CAN-H** (High) | Verde/Bianco | **CAN_H** |
| Pin 14 | **CAN-L** (Low) | Verde | **CAN_L** |
| Pin 16 | +12V Batteria | Rosso | (per alimentazione, NON a MCP2515) |

**Schema Connessione**:
```
        Lancia Musa OBD2 Port (J1962)
        ┌───────────────────────┐
        │  1  2  3  4  5  6  7  8 │
        │  9 10 11 12 13 14 15 16 │
        └───────────────────────┘
              │  │     │      │  │
              │  │     │      │  └─► Pin 16: +12V ──► Convertitore DC-DC
              │  │     │      │
              │  │     │      └─────► Pin 14: CAN-L ──┐
              │  │     │                                │
              │  │     └────────────► Pin 6: CAN-H ────┤
              │  │                                      │
              │  └──────────────────► Pin 5: GND       │
              │                                         │
              └─────────────────────► Pin 4: GND       │
                                                        │
                                                        ▼
                                                MCP2515 Module
                                                ┌──────────────┐
                                                │  CAN_H    ●  │
                                                │  CAN_L    ●  │
                                                │  GND      ●  │
                                                └──────────────┘
```

**⚠️ IMPORTANTE CAN-Bus**:
- CAN-Bus usa comunicazione **differenziale**: CAN-H e CAN-L devono essere collegati entrambi
- **NON invertire** CAN-H e CAN-L (CAN-Bus non funzionerà)
- Resistenza terminazione 120Ω già presente nel veicolo (non aggiungerne)

---

### Tensioni CAN-Bus (per debug con multimetro)

| Stato | CAN-H Voltage | CAN-L Voltage | Differenziale (H-L) |
|-------|---------------|---------------|---------------------|
| **Idle (Recessivo)** | ~2.5V | ~2.5V | 0V |
| **Dominant (0)** | ~3.5V | ~1.5V | ~2V |
| **Dominant (1)** | ~1.5V | ~3.5V | ~-2V |

**Test con Multimetro**:
1. Motore acceso, quadro ON
2. Misura tensione CAN-H rispetto GND: deve oscillare 1.5V - 3.5V
3. Misura tensione CAN-L rispetto GND: deve oscillare 1.5V - 3.5V
4. Se entrambe ferme a 2.5V: nessun traffico CAN o CAN non attivo

---

## 🚗 Specifiche CAN-Bus Lancia Musa 2009

### Protocollo

- **Standard**: ISO 15765-4 (Diagnostic Communication over CAN)
  - Basato su ISO 11898 (CAN 2.0B)
- **Velocità**: 500 kbps (500 kbit/s)
- **Frame Type**: Standard (11-bit identifier) e Extended (29-bit)
- **Tensione**: Differenziale CAN-H / CAN-L
  - Idle: 2.5V / 2.5V
  - Dominant: 3.5V / 1.5V
- **Terminazione**: 120Ω resistenza su CAN-H/CAN-L (già nel veicolo)

### PID OBD2 Standard Supportati

Questi PID sono definiti dallo standard ISO 15765-4 e dovrebbero essere disponibili su Musa 2009:

#### Mode 01: Current Data (Real-time)

| PID | Nome | Unità | Formula Conversione | Descrizione |
|-----|------|-------|---------------------|-------------|
| **0x0C** | Engine RPM | rpm | `((A×256)+B)/4` | Giri motore |
| **0x0D** | Vehicle Speed | km/h | `A` | Velocità veicolo |
| **0x05** | Engine Coolant Temp | °C | `A-40` | Temperatura liquido raffreddamento |
| **0x0F** | Intake Air Temp | °C | `A-40` | Temperatura aria aspirata |
| **0x11** | Throttle Position | % | `A*100/255` | Posizione farfalla |
| **0x2F** | Fuel Tank Level | % | `A*100/255` | Livello carburante |
| **0x46** | Ambient Air Temp | °C | `A-40` | Temperatura esterna |
| **0x5C** | Engine Oil Temp | °C | `A-40` | Temperatura olio motore |
| **0x42** | Control Module Voltage | V | `((A×256)+B)/1000` | Tensione batteria |
| **0x0B** | Intake Manifold Pressure | kPa | `A` | Pressione collettore aspirazione |
| **0x04** | Calculated Engine Load | % | `A*100/255` | Carico motore |
| **0x0E** | Timing Advance | ° | `(A-128)/2` | Anticipo accensione |
| **0x1F** | Run Time Since Start | s | `(A×256)+B` | Tempo motore acceso |
| **0x21** | Distance with MIL On | km | `(A×256)+B` | Distanza con spia avaria |
| **0x31** | Distance Since Codes Cleared | km | `(A×256)+B` | Distanza da reset errori |

#### Mode 03: Diagnostic Trouble Codes (DTC)

- Legge codici errore salvati (es. P0420, P0171, etc.)
- Formato: 2 byte per codice
- Esempio: `0x0420` = P0420 (Catalyst System Efficiency Below Threshold)

### PID Custom Fiat/Lancia (Da Verificare)

Questi PID **potrebbero** essere proprietari Fiat e richiedono sniffing CAN su veicolo reale:

| PID Possibile | Descrizione | Probabilità | Note |
|---------------|-------------|-------------|------|
| 0x65 o custom | Stato spie cruscotto | Media | Body Computer |
| Custom frames | Stato porte (aperte/chiuse) | Alta | Su CAN Comfort |
| Custom frames | Luci attive (abbaglianti, frecce, etc.) | Alta | Body Computer |
| Custom frames | Trip computer (km residui, media) | Media | Può essere calcolato |
| Custom frames | Sensori parcheggio | Bassa | Solo Musa con PDC |

**⚠️ IMPORTANTE**: La maggior parte delle funzioni "avanzate" (spie, porte, luci) sono gestite dal Body Computer Fiat su frame CAN proprietari. Serve reverse engineering con sniffing CAN-Bus reale.

### Strumenti per Sniffing CAN

1. **can-utils** (Linux):
   ```bash
   # Installa su Raspberry Pi
   sudo apt install can-utils

   # Attiva interfaccia CAN
   sudo ip link set can0 type can bitrate 500000
   sudo ip link set can0 up

   # Dumpa tutto il traffico CAN
   candump can0 -l

   # Filtra per ID specifico
   candump can0,7E8:7FF  # Range ID diagnostica
   ```

2. **SavvyCAN** (GUI grafico): Analisi e reverse engineering

3. **Wireshark** + plugin SocketCAN: Analisi protocolli alto livello

### Esempio Frame CAN ISO 15765-4

**Request PID 0x0C (Engine RPM)**:
```
CAN ID: 0x7DF (broadcast) o 0x7E0 (ECU engine)
Data: [02 01 0C 00 00 00 00 00]
      │  │  │  └─ Padding
      │  │  └─ PID 0x0C
      │  └─ Service 01 (Current Data)
      └─ Length (2 bytes)
```

**Response**:
```
CAN ID: 0x7E8 (ECU engine response)
Data: [04 41 0C 1A F8 00 00 00]
      │  │  │  │  └─ Byte B (LSB)
      │  │  │  └─ Byte A (MSB)
      │  │  └─ PID 0x0C
      │  └─ Service 41 (response to 01)
      └─ Length (4 bytes)

RPM = ((0x1A × 256) + 0xF8) / 4
    = (26 × 256 + 248) / 4
    = 6912 / 4
    = 1728 rpm
```

---

## ⚡ Consumo Energetico Totale

### Analisi Consumi per Componente

| Componente | Tensione | Corrente | Potenza | Note |
|------------|----------|----------|---------|------|
| **Raspberry Pi 5** | 5V | 2.5-5A | 12-27W | Max sotto carico 3D |
| **Raspberry Pi 4** | 5V | 1.5-3A | 7-15W | Max sotto carico |
| **Display 10.1" LED** | 5V o 12V | 0.5-1.5A | 6-12W | Dipende da luminosità |
| **Display 12.3" LED** | 12V | 0.8-1.2A | 10-15W | Consuma di più |
| **MCP2515** | 5V | 50mA | 0.25W | Trascurabile |
| **GPS USB** | 5V | 100mA | 0.5W | Trascurabile |
| **Sensori (MPU6050, DHT22)** | 3-5V | 5-10mA | <0.1W | Trascurabile |

### Consumo Totale per Configurazione

#### Base (Pi 4 + Display 7")
- **Idle**: ~10W (0.8A @ 12V)
- **Carico normale**: ~15W (1.25A @ 12V)
- **Carico massimo**: ~20W (1.7A @ 12V)

#### Consigliata (Pi 5 + Display 10.1")
- **Idle**: ~15W (1.25A @ 12V)
- **Carico normale**: ~23W (1.9A @ 12V)
- **Carico massimo**: ~30W (2.5A @ 12V)

#### Premium (Pi 5 + Display 12.3")
- **Idle**: ~18W (1.5A @ 12V)
- **Carico normale**: ~28W (2.3A @ 12V)
- **Carico massimo**: ~35W (2.9A @ 12V)

### Impatto Batteria Auto

**Batteria Musa**: ~60Ah (tipica batteria auto)

| Scenario | Consumo | Durata Batteria (motore spento) |
|----------|---------|----------------------------------|
| Sistema idle | 1.5A | ~40 ore |
| Sistema carico normale | 2.3A | ~26 ore |
| Sistema carico massimo | 2.9A | ~20 ore |

**⚠️ Raccomandazioni**:
1. **Implementa auto-shutdown**: Spegni Raspberry dopo 10-15 min senza chiave
2. **Power bank UPS**: 10.000mAh garantisce shutdown sicuro (~2-3 ore autonomia)
3. **Monitor tensione batteria**: Alert se batteria < 11.8V
4. **Evita uso prolungato** a motore spento (max 30 min)

### Ottimizzazioni Risparmio Energetico

**Software**:
- Riduci luminosità display (50% risparmia ~20-30%)
- Disabilita Wi-Fi/Bluetooth se non necessari
- Undervolt GPU Raspberry Pi (`gpu_mem=64` in `/boot/config.txt`)
- Governor CPU "powersave" quando idle

**Hardware**:
- Display con auto-dimming (sensore luce ambientale)
- Relay controllo alimentazione display (spegni quando non in uso)
- Power bank con UPS automatico

---

## ⚠️ Avvertenze e Note Legali

### Sicurezza

1. **Distrazioni alla Guida**
   - ❌ Il display NON deve distrarre dalla guida
   - ❌ Non interagire con touch screen durante la guida
   - ✅ Posiziona display in area non invasiva campo visivo
   - ✅ Testa posizionamento a veicolo fermo

2. **Sicurezza Elettrica**
   - ⚡ **SEMPRE** usa fusibili su tutte le linee 12V
   - ⚡ Verifica polarità con multimetro prima di collegare
   - ⚡ Isola connessioni con guaina termorestringente
   - ⚡ Non toccare circuiti con motore acceso
   - ⚡ Scollega batteria per installazioni definitive

3. **Incendio / Cortocircuito**
   - 🔥 Fusibili OBBLIGATORI (no eccezioni)
   - 🔥 Cavi dimensionati correttamente (vedi tabelle)
   - 🔥 No cavi volanti sotto cruscotto
   - 🔥 Verifica cablaggio ogni 6 mesi
   - 🔥 Tieni estintore in auto

### Normativa e Omologazione

1. **Codice della Strada (Italia)**
   - ⚠️ Modifiche impianto elettrico possono violare CdS
   - ⚠️ Display non devono coprire campo visivo obbligatorio
   - ⚠️ Possibile sanzione in revisione se display troppo invasivo

2. **Garanzia Veicolo**
   - ❌ Modifiche elettriche invalidano garanzia costruttore
   - ❌ Eventuali danni impianto elettrico non coperti
   - ✅ Installazione removibile minimizza rischi

3. **Assicurazione**
   - ⚠️ Alcune polizze escludono danni da modifiche
   - ✅ Verifica con la tua assicurazione prima di installare
   - ✅ Documenta installazione con foto (prova removibilità)

4. **Omologazione**
   - ❌ Sistema HyperMusa NON omologato per uso stradale EU
   - ❌ Non è dispositivo certificato automotive
   - ⚠️ Uso a proprio rischio e responsabilità

### Disclaimer Legale

**Il progetto HyperMusa è fornito "AS IS", senza garanzie di alcun tipo.**

Gli autori e contributori NON si assumono responsabilità per:
- ❌ Danni a persone, cose, animali
- ❌ Incidenti stradali causati da distrazioni
- ❌ Guasti elettrici/elettronici al veicolo
- ❌ Incendi, cortocircuiti, malfunzionamenti
- ❌ Violazioni codice della strada
- ❌ Invalidazione garanzie o assicurazioni
- ❌ Problemi durante revisione veicolo

**L'installazione di HyperMusa è:**
- ✅ A scopo educativo e hobbistico
- ✅ Sotto esclusiva responsabilità dell'utente
- ✅ Da eseguire solo con competenze elettriche/elettroniche adeguate
- ✅ Vietata su veicoli in circolazione pubblica (consiglio)

**Se non sei sicuro delle tue competenze**: rivolgiti a elettrauto professionista.

---

## 📝 Checklist Pre-Acquisto

Prima di ordinare i componenti, verifica:

### Misurazioni Veicolo
- [ ] Ho misurato lo spazio disponibile su cruscotto Musa
- [ ] Ho verificato la posizione porta OBD2 (sotto volante lato guida)
- [ ] Ho creato template cartaceo dimensioni display
- [ ] Ho testato posizionamento mockup display (cartone)
- [ ] Ho verificato che display non ostruisca spie/volante
- [ ] Ho verificato visibilità display da posizione guida

### Budget e Configurazione
- [ ] Ho deciso quale configurazione (Base / Consigliata / Premium)
- [ ] Ho definito budget totale (250€ / 400€ / 600€)
- [ ] Ho verificato disponibilità prodotti su Amazon.it
- [ ] Ho letto specifiche tecniche di ogni componente

### Competenze e Strumenti
- [ ] Ho competenze elettriche base (uso multimetro)
- [ ] Ho strumenti necessari (cacciaviti, multimetro)
- [ ] Ho letto schema collegamenti GPIO e OBD2
- [ ] Ho compreso rischi elettrici (cortocircuito, incendio)

### Normativa e Sicurezza
- [ ] Ho letto avvertenze sicurezza
- [ ] Ho verificato con assicurazione (modifiche veicolo)
- [ ] Ho compreso che sistema non è omologato
- [ ] Accetto responsabilità installazione

---

## 🎯 Prossimi Step Dopo Acquisto

### 1. Test Banco (Senza Veicolo)

**Obiettivo**: Verificare funzionamento hardware prima di installare in auto

**Setup**:
1. Collega Raspberry Pi + Display su tavolo
2. Installa Raspberry Pi OS
3. Configura MCP2515 in loopback mode (test senza CAN)
4. Testa interfaccia grafica HyperMusa in modalità demo

**Durata**: 2-4 ore

---

### 2. Primo Test CAN su Veicolo

**Obiettivo**: Verificare lettura CAN-Bus reale Lancia Musa

**Setup**:
1. Collega sistema temporaneamente (cavi volanti OK)
2. Alimentazione da porta OBD2 pin 16
3. CAN-H/CAN-L da OBD2 a MCP2515
4. Avvia Raspberry Pi e sniffa traffico CAN

**Comandi**:
```bash
# Attiva CAN interface
sudo ip link set can0 type can bitrate 500000
sudo ip link set can0 up

# Dumpa traffico CAN
candump can0 -l

# Test lettura PID 0x0C (RPM)
cansend can0 7DF#020100
```

**Durata**: 1-2 ore

---

### 3. Mappatura PID

**Obiettivo**: Identificare PID disponibili su Musa 2009

**Procedura**:
1. Leggi tutti PID standard (0x00-0xFF)
2. Documenta PID che rispondono
3. Verifica valori corrispondono a realtà (RPM, velocità, etc.)
4. Salva mapping in `docs/musa-can-pids.md`

**Durata**: 2-3 ore

---

### 4. Installazione Definitiva

**Obiettivo**: Montaggio permanente sistema su Musa

**Procedura**:
1. Installa supporto display (biadesivo 3M VHB)
2. Fissa Raspberry Pi con velcro sotto cruscotto
3. Cabla alimentazione con fusibili dedicati
4. Organizza cavi con fascette e guaine
5. Test finale completo

**Durata**: 4-6 ore

---

## 📚 Risorse e Link Utili

### Fornitori Italiani

- **[Melopero](https://www.melopero.com/)** - Raspberry Pi ufficiale, HAT, accessori
- **[Battery Atom](https://www.batteryatom.it/)** - Moduli elettronici, sensori
- **[Beetronics](https://www.beetronics.it/)** - Display automotive
- **[Futura Elettronica](https://www.futurashop.it/)** - Componenti elettronici
- **[RS Components](https://it.rs-online.com/)** - Fornitore industriale
- **[Conrad](https://www.conrad.it/)** - Elettronica generale

### Fornitori Internazionali

- **[AliExpress](https://www.aliexpress.com/)** - Display bar economici (spedizione 2-4 settimane)
- **[Amazon.de](https://www.amazon.de/)** - Alternative se non disponibile su .it
- **[Digi-Key](https://www.digikey.it/)** - Componenti elettronici professionali
- **[Mouser](https://www.mouser.it/)** - Componenti elettronici professionali
- **[SK Pang Electronics](https://www.skpang.co.uk/)** - PiCAN HAT ufficiali

### Community e Forum

- **[Raspberry Pi Forum](https://forums.raspberrypi.com/)** - Supporto tecnico ufficiale
- **[Fiat500owners.com](https://www.fiat500owners.com/)** - Community Fiat (include Musa)
- **[Automotive CAN Wiki](https://en.wikipedia.org/wiki/CAN_bus)** - Info protocollo CAN
- **[OpenDBC Database](https://github.com/commaai/opendbc)** - Database PID veicoli

### Documentazione Tecnica

- **[ISO 15765-4](https://www.iso.org/)** - Standard diagnostica CAN (a pagamento)
- **[Raspberry Pi Docs](https://www.raspberrypi.com/documentation/)** - Docs ufficiali Pi
- **[MCP2515 Datasheet](https://www.microchip.com/en-us/product/MCP2515)** - Specs controller CAN
- **[SocketCAN Kernel Docs](https://www.kernel.org/doc/html/latest/networking/can.html)** - Linux CAN interface

### Software e Tool

- **[can-utils](https://github.com/linux-can/can-utils)** - Suite tool CAN Linux
- **[SavvyCAN](https://www.savvycan.com/)** - Analizzatore CAN grafico open-source
- **[Wireshark](https://www.wireshark.org/)** - Protocol analyzer (plugin SocketCAN)
- **[python-can](https://python-can.readthedocs.io/)** - Libreria Python CAN-Bus

---

## 🏁 Conclusione

Hai ora tutte le informazioni per acquistare l'hardware necessario a realizzare HyperMusa!

### Recap Configurazioni

| Budget | Configurazione | Performance | Descrizione |
|--------|----------------|-------------|-------------|
| ~185€ | **Base** | ⭐⭐⭐ | Proof-of-concept funzionante |
| ~300€ | **Consigliata** | ⭐⭐⭐⭐⭐ | Performance ottime, espandibile |
| ~557€ | **Premium** | ⭐⭐⭐⭐⭐ | Look professionale automotive |

### 🎯 Il Nostro Consiglio

**Configurazione Consigliata (~300€)** è il miglior compromesso:
- ✅ Raspberry Pi 5 4GB: performance eccellenti
- ✅ Display 10.1" 1920×1200: risoluzione ottima, facile da trovare
- ✅ GPS + Sensori: funzionalità complete
- ✅ Protezioni complete: sicurezza garantita
- ✅ Espandibile: aggiungi componenti in futuro

### 📧 Supporto

Hai dubbi su componenti specifici o compatibilità?
- **GitHub Issues**: [HyperMusa Issues](https://github.com/emanuelerosato/HyperMusa/issues)
- **GitHub Discussions**: [HyperMusa Discussions](https://github.com/emanuelerosato/HyperMusa/discussions)

---

**Buon acquisto e buon hacking automotive! 🚗⚡**

**Ultimo aggiornamento**: 11 Dicembre 2025
**Versione**: 1.0
**Testato su**: Lancia Musa 2009 (in sviluppo)
