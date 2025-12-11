#!/usr/bin/env python3
"""
Simulatore CAN-Bus Lancia Musa 2009
Genera traffico CAN realistico per test HyperMusa senza veicolo

Uso:
    # Crea interfaccia CAN virtuale
    sudo modprobe vcan
    sudo ip link add dev vcan0 type vcan
    sudo ip link set up vcan0

    # Avvia simulatore
    python3 tests/musa-can-simulator.py

    # In altro terminale, monitora traffico
    candump vcan0
"""

import can
import time
import random
import sys

def simulate_musa_can():
    """Simula messaggi CAN tipici di Lancia Musa 2009"""

    try:
        # Configura bus CAN virtuale
        bus = can.interface.Bus(channel='vcan0', bustype='socketcan')
    except Exception as e:
        print(f"❌ Errore: impossibile connettersi a vcan0")
        print(f"   {e}")
        print("\n💡 Suggerimento: Crea interfaccia CAN virtuale con:")
        print("   sudo modprobe vcan")
        print("   sudo ip link add dev vcan0 type vcan")
        print("   sudo ip link set up vcan0")
        sys.exit(1)

    print("🚗 Simulatore CAN Lancia Musa 2009 attivo su vcan0")
    print("   RPM: 800-3000 | Speed: 0-120 km/h | Temp: 80-92°C")
    print("   Premi Ctrl+C per terminare\n")

    iteration = 0

    while True:
        iteration += 1

        # RPM motore (0-6000 rpm) - PID 0x0C
        # Formula: ((A×256)+B)/4
        rpm = random.randint(800, 3000)  # Minimo a medio
        rpm_raw = rpm * 4  # Inverti formula OBD
        msg_rpm = can.Message(
            arbitration_id=0x7E8,  # ID risposta ECU
            data=[0x04, 0x41, 0x0C, (rpm_raw >> 8) & 0xFF, rpm_raw & 0xFF, 0x00, 0x00, 0x00],
            is_extended_id=False
        )
        bus.send(msg_rpm)

        # Velocità (0-200 km/h) - PID 0x0D
        # Formula: A (diretto)
        speed = random.randint(0, 120)
        msg_speed = can.Message(
            arbitration_id=0x7E8,
            data=[0x03, 0x41, 0x0D, speed, 0x00, 0x00, 0x00, 0x00],
            is_extended_id=False
        )
        bus.send(msg_speed)

        # Temperatura motore (60-95°C) - PID 0x05
        # Formula: A-40
        temp_real = random.randint(80, 92)  # Temperatura reale
        temp_obd = temp_real + 40  # Offset +40 per protocollo OBD
        msg_temp = can.Message(
            arbitration_id=0x7E8,
            data=[0x03, 0x41, 0x05, temp_obd, 0x00, 0x00, 0x00, 0x00],
            is_extended_id=False
        )
        bus.send(msg_temp)

        # Livello carburante (20-100%) - PID 0x2F
        # Formula: A*100/255
        fuel_percent = random.randint(30, 90)
        fuel_obd = fuel_percent * 255 // 100
        msg_fuel = can.Message(
            arbitration_id=0x7E8,
            data=[0x03, 0x41, 0x2F, fuel_obd, 0x00, 0x00, 0x00, 0x00],
            is_extended_id=False
        )
        bus.send(msg_fuel)

        # Throttle Position (0-100%) - PID 0x11
        throttle_percent = random.randint(0, 50)
        throttle_obd = throttle_percent * 255 // 100
        msg_throttle = can.Message(
            arbitration_id=0x7E8,
            data=[0x03, 0x41, 0x11, throttle_obd, 0x00, 0x00, 0x00, 0x00],
            is_extended_id=False
        )
        bus.send(msg_throttle)

        # Engine Load (0-100%) - PID 0x04
        load_percent = random.randint(10, 60)
        load_obd = load_percent * 255 // 100
        msg_load = can.Message(
            arbitration_id=0x7E8,
            data=[0x03, 0x41, 0x04, load_obd, 0x00, 0x00, 0x00, 0x00],
            is_extended_id=False
        )
        bus.send(msg_load)

        # Log ogni 100 iterazioni (ogni 10 secondi)
        if iteration % 100 == 0:
            print(f"📊 Sent {iteration} message batches | RPM: {rpm} | Speed: {speed} km/h | Temp: {temp_real}°C | Fuel: {fuel_percent}%")

        time.sleep(0.1)  # 10 Hz update rate

if __name__ == "__main__":
    try:
        simulate_musa_can()
    except KeyboardInterrupt:
        print("\n\n✅ Simulatore terminato")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Errore inatteso: {e}")
        sys.exit(1)
