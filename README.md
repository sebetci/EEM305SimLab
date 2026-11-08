# EEM305SimLab — 8051 Simulation Lab

Prepared by **Sercan Sebetçi** as a simulation tool for the **EEM305 Microprocessors** course taught by Prof. Dr. Şuayb Çağrı Yener at Sakarya University.

An interactive learning environment for the MCS-51 (8051) architecture. Run each instruction step by step and watch how the program counter, stack pointer, registers, internal RAM and flash memory change — or write your own assembly program and simulate it.

## Quick Start

- **Open in your browser:** https://sebetci.github.io/EEM305SimLab/EEM305SimLab.html
- **Download:** save `EEM305SimLab.html` and double-click it. No installation or internet connection is required.

## Features

- **Subroutine Calls:** ACALL / LCALL / RET with PC, SP, stack, flash and RAM shown in micro-steps
- **Code Lab:** syntax-highlighted editor with an in-browser 8051 assembler and emulator
- **Data-Flow Diagram:** animated data packets moving between Flash ↔ CPU (PC, SP) ↔ RAM
- **Timeline:** step-by-step chart of the SP and A registers
- **Instruction Set:** all 111 8051 instructions with opcode, size, cycles and affected flags
- English / Turkish interface, light / dark theme

## Security and Verification

The application **cannot access the network**: a Content Security Policy at the top of the file blocks all network requests at the browser level. See [SECURITY.md](SECURITY.md) for details.

| Check | |
|---|---|
| SHA-256 (`EEM305SimLab.html`) | `c0694fec27c4f6ac0f228ab42924799173675e510fcacba01d99c7c2c437d7f9` |
| VirusTotal report | [View report](https://www.virustotal.com/gui/file/c0694fec27c4f6ac0f228ab42924799173675e510fcacba01d99c7c2c437d7f9/detection) |
| All checksums | [SHA256SUMS.txt](SHA256SUMS.txt) |

To verify the file on Windows (PowerShell):

```powershell
Get-FileHash EEM305SimLab.html -Algorithm SHA256
```

On macOS: `shasum -a 256 EEM305SimLab.html` · On Linux: `sha256sum EEM305SimLab.html`

## Building From Source

Requirements: Node.js 18+ and Python 3.

```bash
cd build
npm ci
npm run build
```

The build embeds the libraries, fonts and icons into `src/EEM305SimLab.src.html` and writes `EEM305SimLab.html` to the repository root. The build is reproducible: the same source always produces the same SHA-256.

## Repository Structure

```
EEM305SimLab.html          Ready-to-use single file (built)
index.html                 Redirect page for GitHub Pages
SHA256SUMS.txt             SHA-256 checksums
SECURITY.md                Security document
THIRD_PARTY_LICENSES.md    Licenses of the embedded libraries
src/EEM305SimLab.src.html  Readable source code
build/                     Build script and pinned dependencies
```

## Third-Party Libraries

CodeMirror 6 (MIT) · Chart.js 4.6.1 (MIT) · GSAP 3.15.1 (GSAP Standard License) · Lucide 1.70.0 (ISC) · Inter and JetBrains Mono (SIL OFL 1.1). License texts: [THIRD_PARTY_LICENSES.md](THIRD_PARTY_LICENSES.md)

## Contact

sercan.sebetci@ogr.sakarya.edu.tr
