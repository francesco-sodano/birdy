# Architecture

# Edge logical Architecture

The SmartBox is based on a Raspberry Pi architecture running Raspberry Pi OS (Debian 11 - Bullseye).
On top of the OS, we have the IoT Edge Runtime: The IoT Edge service provides and maintains security standards on the IoT Edge device. The service starts on every boot and bootstraps the device by starting the rest of the IoT Edge runtime.

Azure IoT Edge relies on an OCI-compatible container runtime. Birdy is using Moby Engine for maximize support and compatibility: The Moby engine is the only container engine officially supported with IoT Edge.

The Birdy software are running as custom modules on the Azure Iot Edge service. there are three different custom modules running on the device:

- Controller
- Watcher
- Sender

## Controller

## Watcher

## Sender



# Back-End logical Architecture

## The Trained AI

## Data Layer
