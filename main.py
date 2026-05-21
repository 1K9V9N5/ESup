import streamlit as st

# 1. App-Konfiguration für das Smartphone
st.set_page_config(
    page_title="ESUB - Premium Health",
    page_icon="🧬",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. Das saubere, vertrauenswürdige Premium-Design
st.markdown("""
    <style>
    /* Basis-Setup: Ruhig, dunkel und edel */
    .stApp {
        background-color: #121417; 
        color: #F8FAFC; 
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    }
    
    /* Perfekte Smartphone-Breite */
    .block-container {
        padding: 2rem 1.2rem !important;
        max-width: 440px !important;
        margin: 0 auto;
    }
    
    /* Überschriften-Design */
    h1 {
        font-size: 1.8rem !important;
        font-weight: 700 !important;
        letter-spacing: -0.5px;
        margin-bottom: 5px !important;
    }
    
    h3 {
        font-size: 1.2rem !important;
        font-weight: 600 !important;
        color: #E2E8F0 !important;
        margin-top: 25px !important;
        margin-bottom: 15px !important;
    }
    
    /* Dynamische App-Kacheln (CSS-Grid) */
    .supp-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 10px;
        margin-bottom: 20px;
    }
    
    .supp-tile {
        background: #1A1D24;
        border: 1px solid #262B35;
        padding: 12px 8px;
        border-radius: 10px;
        text-align: center;
        font-size: 0.85rem;
        font-weight: 500;
        color: #E2E8F0;
        box-shadow: 0 4px 10px rgba(0,0,0,0.15);
    }
    
    /* Hochwertige Ergebnis-Karte */
    .result-card {
        background: #1A1D24;
        border: 1px solid #262B35;
        border-top: 4px solid #84CC16; 
        padding: 16px;
        border-radius: 12px;
        margin-top: 15px;
    }
    
    .result-card h4 {
        color: #FFFFFF !important;
        margin: 0 0 5px 0 !important;
        font-size: 1.1rem;
    }
    
    .result-card p {
        font-size: 0.88rem;
        color: #94A3B8;
        margin: 4px 0 !important;
        line-height: 1.4;
    }
    
    /* Flache Buttons im App-Store-Stil */
    .stButton>button {
        background-color: #84CC16 !important; 
        color: #121417 !important;
        border: none !important;
        border-radius: 10px !important;
        font-weight: 600 !important;
        width: 100% !important;
        padding: 0.6rem !important;
    }
    
    /* Dezent grauer Disclaimer-Text ganz unten */
    .disclaimer-text {
        font-size: 0.8rem;
        color: #64748B;
        line-height: 1.4;
        margin-top: 30px;
        border-top: 1px solid #262B35;
        padding-top: 15px;
    }
    
    /* Sidebar-Verbot */
    [data-testid="collapsedControl"] { display: none !important; }
    section[data-testid="stSidebar"] { display: none !important; }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 3. DIE MASSIVE LEGAL-SUPPLEMENT-DATENBANK (Jetzt mit allen 17 Subs!)
# ==========================================
SUPP_DB = {
    "Kreatin Monohydrat": {
        "icon": "💪",
        "wirkung": "Unterstützt die Energieversorgung der Muskelzellen bei kurzen, intensiven Belastungen (Schnellkraft).",
        "koerper": "Fördert die Bildung von ATP (Zellenergie) und kann die Regeneration begünstigen."
    },
    "Omega-3 Fettsäuren": {
        "icon": "🐟",
        "wirkung": "Liefert essenzielle EPA- und DHA-Fettsäuren für Sportler.",
        "koerper": "Kann entzündungshemmend wirken, unterstützt die Herzfunktion und die Regeneration."
    },
    "Vitamin D3 + K2": {
        "icon": "☀️",
        "wirkung": "Wichtig für das Immunsystem, den Knochenbau und die Muskelfunktion.",
        "koerper": "Reguliert den Calcium-Haushalt; K2 sorgt für die richtige Verteilung im Skelett."
    },
    "Kollagen-Hydrolysat": {
        "icon": "✨",
        "wirkung": "Unterstützt die Elastizität von Haut, Sehnen, Bändern und Gelenkknorpeln.",
        "koerper": "Liefert spezifische Aminosäuren, die für den körpereigenen Strukturaufbau benötigt werden."
    },
    "Molkenprotein (Whey)": {
        "icon": "🥛",
        "wirkung": "Schnell verdauliche Proteinquelle zur Unterstützung des Muskelaufbaus.",
        "koerper": "Liefert essenzielle Aminosäuren (EAAs) zur Aktivierung der Muskelproteinsynthese."
    },
    "Magnesium (Bisglycinat)": {
        "icon": "🔋",
        "wirkung": "Unterstützt die normale Muskelfunktion und das Nervensystem nach dem Sport.",
        "koerper": "Beteiligt an über 300 Enzymreaktionen; fördert die Muskelentspannung."
    },
    "Zink (Picolinat)": {
        "icon": "🛡️",
        "wirkung": "Wichtig für den Kohlenhydrat- und Fettsäurestoffwechsel sowie das Immunsystem.",
        "koerper": "Unterstützt die Zellteilung, Eiweißsynthese und reguliert Regenerationsprozesse."
    },
    "L-Citrullin Malat": {
        "icon": "🚀",
        "wirkung": "Wird im Pre-Workout-Bereich zur Unterstützung die Durchblutung genutzt.",
        "koerper": "Fördert die Stickstoffmonoxid-Produktion (NO) im Blut und weitet funktionell die Gefäße."
    },
    "Beta-Alanin": {
        "icon": "🔥",
        "wirkung": "Wird zur Hinauszögerung der Muskelermüdung bei intensiven Sätzen eingesetzt.",
        "koerper": "Erhöht den Carnosingehalt im Muskel, welcher der Übersäuerung durch Milchsäure entgegenwirkt."
    },
    "Ashwagandha (KSM-66)": {
        "icon": "🌿",
        "wirkung": "Pflanzliches Adaptogen zur Unterstützung der Regeneration.",
        "koerper": "Kann helfen, den Cortisolspiegel (Stresshormon) zu regulieren und den Schlaf zu verbessern."
    },
    "Koffein Anhydrous": {
        "icon": "⚡",
        "wirkung": "Temporäre Erhöhung von Fokus, Wachsamkeit und mentaler Energie.",
        "koerper": "Blockiert die Adenosinrezeptoren im Gehirn und verzögert das Müdigkeitssignal."
    },
    "L-Tyrosin": {
        "icon": "🧠",
        "wirkung": "Sorgt für messerscharfen Fokus und Konzentration in extremen Stresssituationen.",
        "koerper": "Dient als Baustein für die Neurotransmitter Dopamin, Epinephrin und Nordadrenalin im Gehirn."
    },
    "Taurin": {
        "icon": "🌊",
        "wirkung": "Unterstützt den Zell-Flüssigkeitshaushalt und zögert die Muskelerschöpfung hinaus.",
        "koerper": "Wirkt als Antioxidans, stabilisiert Zellmembranen und optimiert die Kalzium-Steuerung im Muskel."
    },
    "Rote Beete Extrakt": {
        "icon": "🩸",
        "wirkung": "Erhöht den Muskelpump und optimiert die Sauerstoffversorgung der Muskeln.",
        "koerper": "Liefert anorganische Nitrate, die im Körper hocheffizient zu Stickstoffmonoxid (NO) umgewandelt werden."
    },
    "EAAs (Aminosäuren)": {
        "icon": "🧱",
        "wirkung": "Verhindert Muskelabbau (Katabolismus) während des Trainings und startet die Regeneration.",
        "koerper": "Liefert die 9 essenziellen Aminosäuren, die der Körper zwingend für die Proteinsynthese benötigt."
    },
    "L-Glutamin": {
        "icon": "🛡️",
        "wirkung": "Unterstützt das Immunsystem und regeneriert die Darmgesundheit nach hartem Sport.",
        "koerper": "Die am häufigsten vorkommende Aminosäure im Muskel; dient Immunzellen als primäre Energiequelle."
    },
    "MSM (Schwefel)": {
        "icon": "🦴",
        "wirkung": "Unterstützt Gelenke, Sehnen und lindert leichten Muskelkater.",
        "koerper": "Liefert organischen Schwefel, der für die Festigkeit von Bindegewebe und Knorpelstrukturen essenziell ist."
    }
}

# --- APP INHALT ---

# Hauptüberschrift
st.markdown('<h1>🧬 ESUB</h1>', unsafe_allow_html=True)

# Englische Markenerklärung
st.markdown('<p translate="no" style="font-size: 1rem; color: #84CC16; font-weight: 600; margin-top: -5px; margin-bottom: 20px;">Easy Supplements</p>', unsafe_allow_html=True)
st.write("Die vertrauenswürdige Orientierungshilfe für deine sportliche Supplementierung.")

# ==========================================
# BEREICH 1: DAS AUSKLAPPBARE LEXIKON (Radikal aufgeräumt!)
# ==========================================
st.subheader("Wissenschaftliches Verzeichnis")

# Der Expander verbirgt die riesige Kachelwand auf dem Smartphone, bis der User klickt
with st.expander("📖 Gesamtes Supplement-Verzeichnis anzeigen"):
    st.markdown('<p style="font-size:0.85rem; color:#94A3B8; margin-bottom:15px;">Tippe unten auf die Suchbox, um Details zu einer bestimmten Substanz zu laden:</p>', unsafe_allow_html=True)
    
    # Das Kachel-Grid wird jetzt nur HIER DRINNEN gerendert
    st.markdown('<div class="supp-grid">', unsafe_allow_html=True)
    for name, info in SUPP_DB.items():
        st.markdown(f'<div class="supp-tile">{info["icon"]} {name}</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Das Auswahlfeld bleibt für die gezielte Suche direkt auf der Hauptseite erreichbar
auswahl = st.selectbox(
    "Substanz suchen & Details anzeigen:", 
    ["Bitte wählen..."] + sorted(list(SUPP_DB.keys()))
)

if auswahl != "Bitte wählen...":
    details = SUPP_DB[auswahl]
    st.markdown(f"""
    <div class="result-card" style="border-top-color: #64748B;">
        <h4>{details['icon']} {auswahl}</h4>
        <p><b>Unterstützende Wirkung:</b> {details['wirkung']}</p>
        <p><b>Funktion im Organismus:</b> {details['koerper']}</p>
    </div>
    """, unsafe_allow_html=True)

# ==========================================
# BEREICH 2: DEIN INDIVIDUELLES PROFIL
# ==========================================
st.subheader("Dein Profil anpassen")

gewicht = st.number_input("Körpergewicht (kg):", min_value=40, max_value=150, value=80, step=1)
sport_tage = st.slider("Wie viele Tage pro Woche treibst du Sport?", 0, 7, 3)

st.markdown("<p style='font-size:0.9rem; font-weight:600; margin-bottom:5px;'>Ernährung & Lebensumstände:</p>", unsafe_allow_html=True)
kein_fisch = st.checkbox("Ich esse keinen Fisch / habe eine Fischallergie")
wenig_sonne = st.checkbox("Ich bin selten im direkten Sonnenlicht")
viel_stress = st.checkbox("Ich habe aktuell viel Stress / Schlafprobleme")

st.markdown(" ")

# Sicherheits-Gatekeeper
arzt_check = st.checkbox("Ich bestätige, dass dies eine unverbindliche Orientierung ist und ich Änderungen mit meinem Hausarzt abspreche.")

if st.button("Unverbindliche Empfehlung berechnen"):
    if not arzt_check:
        st.error("⚠️ Bitte bestätige zuerst den Hinweis zur ärztlichen Absprache.")
    else:
        st.success("Berechnung abgeschlossen. Deine empfohlene Matrix:")
        st.markdown("### 📋 Vorgeschlagene Orientierungswerte")
        
        # 1. Dynamische Kreatin-Berechnung
        if sport_tage >= 3:
            kr_menge = round(gewicht * 0.05, 1)
            st.markdown(f"""
            <div class="result-card">
                <h4>💪 Kreatin Monohydrat</h4>
                <p><b>Möglicher Richtwert:</b> ca. {kr_menge}g täglich nach der Belastung.</p>
                <p style="font-size:0.85rem; color:#94A3B8;">Unterstützt die ATP-Zellenergie bei deiner Trainingsfrequenz von {sport_tage} Tagen pro Woche.</p>
            </div>
            """, unsafe_allow_html=True)

        # 2. Dynamische Kollagen-Berechnung
        kol_kapseln = 3 if sport_tage >= 4 else 2
        st.markdown(f"""
        <div class="result-card">
            <h4>✨ Premium Kollagen</h4>
            <p><b>Allgemeine Orientierung:</b> ca. {kol_kapseln} Kapseln täglich für deine Hautelastizität und Gelenke.</p>
            <p style="font-size:0.85rem; color:#94A3B8;">Berechnet auf Basis deines aktuellen Körpergewichts von {gewicht} kg.</p>
        </div>
        """, unsafe_allow_html=True)

        # 3. Whey Protein an Trainingstagen
        if sport_tage >= 1:
            st.markdown("""
            <div class="result-card">
                <h4>🥛 Molkenprotein (Whey)</h4>
                <p><b>Allgemeine Orientierung:</b> 1-2 Shakes à 30g zur Deckung des sportlich erhöhten Eiweißbedarfs.</p>
                <p style="font-size:0.85rem; color:#94A3B8;">Direkt am Morgen oder unmittelbar nach dem Krafttraining einnehmen.</p>
            </div>
            """, unsafe_allow_html=True)

        # 4. Omega-3 Logik
        if kein_fisch:
            st.markdown("""
            <div class="result-card">
                <h4>🌱 Veganes Algenöl (Omega-3)</h4>
                <p><b>Allgemeine Orientierung:</b> 2 Kapseln täglich zu einer Hauptmahlzeit als fischfreie Alternative.</p>
                <p style="font-size:0.85rem; color:#94A3B8;">Essentiell für Herz, Gehirn und Gelenke, da du auf Fischprodukte verzichtest.</p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="result-card">
                <h4>🐟 Premium Omega-3 (Fischöl)</h4>
                <p><b>Allgemeine Orientierung:</b> 1-2 Kapseln täglich zur Grundversorgung.</p>
                <p style="font-size:0.85rem; color:#94A3B8;">Unterstützt den Entzündungsstatus bei regelmäßiger sportlicher Belastung.</p>
            </div>
            """, unsafe_allow_html=True)

        # 5. Vitamin D3 Logik
        if wenig_sonne:
            st.markdown("""
            <div class="result-card">
                <h4>☀️ Vitamin D3 + K2</h4>
                <p><b>Allgemeine Orientierung:</b> 1 Tropfen/Kapsel jeden zweiten Tag bei geringer Sonnenexposition.</p>
                <p style="font-size:0.85rem; color:#94A3B8;">Wichtig für das Immunsystem und den Knochenbau bei vorwiegenden Indoor-Aktivitäten.</p>
            </div>
            """, unsafe_allow_html=True)

        # 6. Regeneration Basics bei viel Sport (Magnesium, Zink, MSM)
        if sport_tage >= 4:
            st.markdown("""
            <div class="result-card">
                <h4>🔋 Regeneration & Gelenke (Magnesium, Zink, MSM)</h4>
                <p><b>Allgemeine Orientierung:</b> Essenziell bei hoher Gelenkbelastung und Muskelspannung. Magnesium vor dem Schlafen einnehmen.</p>
                <p style="font-size:0.85rem; color:#94A3B8;">Fördert die ZNS-Regeneration und die Regeneration der Sehnenstrukturen.</p>
            </div>
            """, unsafe_allow_html=True)

        # 7. Pre-Workout Booster
        if sport_tage >= 4:
            st.markdown("""
            <div class="result-card">
                <h4>🚀 Fokus & Pump Matrix (Pre-Workout Allrounder)</h4>
                <p><b>Allgemeine Orientierung:</b> Ca. 30–45 Minuten vor harten Einheiten für mentalen Fokus und gesteigerten Blutfluss.</p>
                <p style="font-size:0.85rem; color:#94A3B8;">Enthält Aminosäuren wie L-Citrullin und Coffein für intensive Einheiten.</p>
            </div>
            """, unsafe_allow_html=True)

        # 8. Ashwagandha Logik
        if viel_stress:
            st.markdown("""
            <div class="result-card">
                <h4>🌿 Ashwagandha (KSM-66)</h4>
                <p><b>Allgemeine Orientierung:</b> 1 Kapsel am Abend zur Unterstützung der Cortisolsenkung.</p>
                <p style="font-size:0.85rem; color:#94A3B8;">Unterstützt die Schlafqualität in Phasen erhöhter mentaler oder physischer Belastung.</p>
            </div>
            """, unsafe_allow_html=True)

# ==========================================
# REINER, DEZENTER FOOTER & CREDITS
# ==========================================
st.markdown("---")
st.warning("Medizinischer Hinweis: Alle hier ausgegebenen Werte und Texte dienen ausschließlich der allgemeinen Information und Orientierung. Sie sind keine medizinische Beratung oder Dosierungsempfehlung. Jede Anpassung der Ernährung oder Einnahme von Nahrungsergänzungsmitteln sollte bei Unsicherheiten individuell mit einem Arzt oder Mediziner abgeklärt werden.")

col1, col2 = st.columns(2)
with col2:
    # Reines Weiß und kursiv über die integrierten Streamlit-Farbcodes
    st.caption(":white[*Built by K.K.*]")
