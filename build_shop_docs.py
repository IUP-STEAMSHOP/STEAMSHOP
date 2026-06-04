import os
import re
from docx import Document

# ─────────────────────────────────────────────────────────────────────────────
# MACHINE ROUTING TABLE
# Maps every "Quick Reference Guide: <name>" title from the DOCX
# to the exact output path that mkdocs.yml expects.
# Add new machines here — format is:
#   "exact title from docx (lowercase)": "machines/<category>/<filename>.md"
# ─────────────────────────────────────────────────────────────────────────────
MACHINE_ROUTE_MAP = {
    # 3D Printing & Scanning
    "original prusa mini+":                     "machines/3d-printing/prusa-mini.md",
    "original prusa i3 mk3s+":                  "machines/3d-printing/prusa-i3-mk3s.md",
    "bambu lab h2d":                            "machines/3d-printing/bambu-h2d.md",
    "bambu lab p1s":                            "machines/3d-printing/bambu-p1s.md",
    "legacy lulzbot taz 6":                     "machines/3d-printing/lulzbot-taz6.md",
    "formlabs form 3b sla":                     "machines/3d-printing/formlabs-3b.md",
    "ultimaker s3 dual-extrusion":              "machines/3d-printing/ultimaker-s3.md",
    "mole v2.2 3d scanner":                     "machines/3d-printing/mole-scanner.md",
    # CNC & Milling
    "shopbot cnc milling table":                "machines/cnc/shopbot.md",
    "haas minimill":                            "machines/cnc/haas-minimill.md",
    "haas umc-500":                             "machines/cnc/haas-umc500.md",
    "bridgeport series i 2hp mill":             "machines/cnc/bridgeport-mill.md",
    # Laser & Digital Cutting
    "omtech af3555 130w co2":                   "machines/digital-cutting/omtech-laser.md",
    "rabbit laser rl-80-1290":                  "machines/digital-cutting/rabbit-laser.md",
    "roland camm-1 gs-24":                      "machines/digital-cutting/roland-cutter.md",
    "wazer waterjet":                           "machines/digital-cutting/wazer.md",
    # Woodworking
    'sawstop 10" contractor saw':               "machines/woodworking/sawstop.md",
    'dewalt 12" sliding miter saw':             "machines/woodworking/dewalt-miter-saw.md",
    'dewalt 13" planer':                        "machines/woodworking/dewalt-planer.md",
    'grizzly 17" 2 hp bandsaw':                 "machines/woodworking/grizzly-bandsaw.md",
    'wen 16" scroll saw':                       "machines/woodworking/wen-scroll-saw.md",
    'jet 12" drill press':                      "machines/woodworking/jet-drill-press.md",
    "bucktool belt & disc sander":              "machines/woodworking/bucktool-sander.md",
    # Metalworking & Fabrication
    "clausing lathe":                           "machines/metalworking/clausing-lathe.md",
    "powermatic drill press 1150":              "machines/metalworking/powermatic-drill-press.md",
    "baileigh horizontal bandsaw":              "machines/metalworking/baileigh-bandsaw.md",
    "bemato bandsaw kb-36":                     "machines/metalworking/bemato-bandsaw.md",
    "pexto px36-a box & pan brake":             "machines/metalworking/pexto-brake.md",
    "pexto 137-l foot shear":                   "machines/metalworking/pexto-shear.md",
    "atlas mandrel arbor press":                "machines/metalworking/atlas-arbor-press.md",
    "trinco sandblaster 48/bp2":                "machines/metalworking/trinco-sandblaster.md",
    "rockwell/delta machine":                   "machines/metalworking/rockwell-delta.md",
    # Welding
    "hobart iron man 230":                      "machines/welding/hobart-ironman.md",
    "miller welding machine":                   "machines/welding/miller-welder.md",
    # Robotics & Automation
    "universal robots ur5e":                    "machines/robotics/ur5e.md",
    "universal robots ur10e":                   "machines/robotics/ur10e.md",
    # Apparel & Heat Presses
    "geo knight cap heat press":                "machines/apparel/geo-knight-press.md",
    "uscutter digital heat press":              "machines/apparel/uscutter-press.md",
}

def clean_name(text):
    """Removes the 'Quick Reference Guide:' prefix for the page title."""
    return text.replace("Quick Reference Guide:", "").strip()

def normalize_key(text):
    """Normalises a machine title for lookup in MACHINE_ROUTE_MAP."""
    key = text.replace("Quick Reference Guide:", "").strip().lower()
    key = re.sub(r'\s+', ' ', key)
    return key

def save_sop_file(machine_name, content_lines):
    """Writes the SOP .md file to the correct routed path."""
    if not machine_name:
        return

    key = normalize_key(machine_name)
    rel_path = MACHINE_ROUTE_MAP.get(key)

    if rel_path is None:
        # Fallback: slugify into machines/misc/ so nothing is silently lost
        slug = re.sub(r'[^a-z0-9]+', '-', key).strip('-')
        rel_path = f"machines/misc/{slug}.md"
        print(f"   ⚠️  No route found for '{machine_name}' → writing to {rel_path}")

    full_path = os.path.join('docs', rel_path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)

    # Write SOP markdown
    with open(full_path, 'w', encoding='utf-8') as f:
        title = clean_name(machine_name)
        f.write(f"# {title}\n\n")
        f.write(f"!!! info \"Manual\"\n")
        f.write(f"    📄 [Download Official Manufacturer Manual](manual.docx)\n\n")
        f.write("---\n\n")
        f.write('\n'.join(content_lines))
    print(f"   ✅ SOP written: {full_path}")

    # Write manual.docx placeholder alongside the .md file
    manual_path = os.path.join(os.path.dirname(full_path), 'manual.docx')
    if not os.path.exists(manual_path):
        with open(manual_path, 'wb') as f:
            f.write(b'')
        print(f"      ↳ Placeholder: {manual_path}")

def main():
    docx_filename = 'Quick Reference Guide machines.docx'

    if not os.path.exists(docx_filename):
        print(f"❌  Cannot find '{docx_filename}' in this directory.")
        return

    doc = Document(docx_filename)
    current_machine = ""
    current_content = []

    print("🚀  Parsing document and building site structure...\n")

    for paragraph in doc.paragraphs:
        text = paragraph.text.strip()
        if not text:
            continue

        if text.startswith("Quick Reference Guide:"):
            if current_machine:
                save_sop_file(current_machine, current_content)
            current_machine = text
            current_content = []
        else:
            if text.isupper() and len(text) > 3:
                current_content.append(f"\n## {text}\n")
            elif text.endswith(":") and not text.startswith(("*", "-")):
                current_content.append(f"\n### {text}\n")
            elif (paragraph.style.name.startswith('List Bullet')
                  or text.startswith('*')
                  or text.startswith('-')):
                clean_bullet = text.lstrip('*- ')
                current_content.append(f"* {clean_bullet}")
            else:
                current_content.append(f"{text}  ")

    if current_machine:
        save_sop_file(current_machine, current_content)

    print("\n🎉  All SOPs generated and correctly routed!")
    print("    Run: mkdocs serve   to preview")
    print("    Run: mkdocs gh-deploy   to publish\n")

if __name__ == "__main__":
    main()